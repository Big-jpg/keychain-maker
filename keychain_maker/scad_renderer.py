# keychain_maker/scad_renderer.py

import subprocess
import shutil
import os
import platform
from pathlib import Path
from typing import Optional
from .models import KeychainRequest

def get_openscad_path() -> Optional[str]:
    """
    Find OpenSCAD executable across different platforms and installation methods.
    
    Checks in order:
    1. OPENSCAD_PATH environment variable
    2. System PATH
    3. Common installation directories for each platform
    
    Returns:
        Path to OpenSCAD executable if found, None otherwise
    """
    # 1. Check environment variable
    env_path = os.environ.get('OPENSCAD_PATH')
    if env_path and Path(env_path).exists():
        return env_path
    
    # 2. Check system PATH
    path_executable = shutil.which("openscad")
    if path_executable:
        return path_executable
    
    # 3. Check common installation directories by platform
    system = platform.system()
    common_paths = []
    
    if system == "Windows":
        # Windows common installation paths
        program_files = os.environ.get('ProgramFiles', 'C:\\Program Files')
        program_files_x86 = os.environ.get('ProgramFiles(x86)', 'C:\\Program Files (x86)')
        
        common_paths = [
            Path(program_files) / "OpenSCAD" / "openscad.exe",
            Path(program_files_x86) / "OpenSCAD" / "openscad.exe",
            Path(program_files) / "OpenSCAD" / "openscad.com",
            Path(program_files_x86) / "OpenSCAD" / "openscad.com",
            # Check user's local AppData
            Path.home() / "AppData" / "Local" / "Programs" / "OpenSCAD" / "openscad.exe",
        ]
    elif system == "Darwin":  # macOS
        common_paths = [
            Path("/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD"),
            Path.home() / "Applications" / "OpenSCAD.app" / "Contents" / "MacOS" / "OpenSCAD",
            Path("/usr/local/bin/openscad"),
            Path("/opt/homebrew/bin/openscad"),
        ]
    else:  # Linux and others
        common_paths = [
            Path("/usr/bin/openscad"),
            Path("/usr/local/bin/openscad"),
            Path("/snap/bin/openscad"),
            Path("/opt/openscad/bin/openscad"),
            Path.home() / ".local" / "bin" / "openscad",
        ]
    
    # Check each common path
    for path in common_paths:
        if path.exists() and path.is_file():
            return str(path)
    
    return None

def check_openscad_installed() -> bool:
    """
    Check if OpenSCAD CLI is installed and available.
    
    Returns:
        True if OpenSCAD is available, False otherwise
    """
    return get_openscad_path() is not None

def get_openscad_version(openscad_path: str) -> Optional[str]:
    """
    Get OpenSCAD version string.
    
    Args:
        openscad_path: Path to OpenSCAD executable
        
    Returns:
        Version string if available, None otherwise
    """
    try:
        result = subprocess.run(
            [openscad_path, "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        # Extract version from output
        output = result.stdout + result.stderr
        for line in output.split('\n'):
            if 'OpenSCAD' in line:
                return line.strip()
        return "OpenSCAD (version unknown)"
    except Exception:
        return None

def render_stl(scad_file_path: str, stl_file_path: str, openscad_path: Optional[str] = None) -> None:
    """
    Run OpenSCAD CLI to generate an STL from a SCAD file.
    
    Args:
        scad_file_path: Path to input SCAD file
        stl_file_path: Path to output STL file
        openscad_path: Optional custom path to OpenSCAD executable
        
    Raises:
        FileNotFoundError: If OpenSCAD is not installed
        subprocess.CalledProcessError: If OpenSCAD rendering fails
    """
    # Use provided path or auto-detect
    if openscad_path is None:
        openscad_path = get_openscad_path()
    
    if openscad_path is None:
        raise FileNotFoundError(
            "OpenSCAD CLI not found. Please install OpenSCAD or set the OPENSCAD_PATH environment variable."
        )
    
    cmd = [
        openscad_path,
        "-o",
        str(stl_file_path),
        str(scad_file_path),
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        error_msg = result.stderr or result.stdout or "Unknown error"
        raise subprocess.CalledProcessError(
            result.returncode,
            cmd,
            output=result.stdout,
            stderr=error_msg
        )
