# keychain_maker/scad_renderer.py

import subprocess
import shutil
from pathlib import Path
from .models import KeychainRequest

def check_openscad_installed() -> bool:
    """
    Check if OpenSCAD CLI is installed and available on PATH.
    
    Returns:
        True if OpenSCAD is available, False otherwise
    """
    return shutil.which("openscad") is not None

def render_stl(req: KeychainRequest) -> None:
    """
    Run OpenSCAD CLI to generate an STL from the generated SCAD file.
    Requires `openscad` to be on PATH.
    
    Args:
        req: KeychainRequest containing input/output paths
        
    Raises:
        FileNotFoundError: If OpenSCAD is not installed
        subprocess.CalledProcessError: If OpenSCAD rendering fails
    """
    if not check_openscad_installed():
        raise FileNotFoundError(
            "OpenSCAD CLI not found. Please install OpenSCAD and ensure it's on your PATH."
        )
    
    cmd = [
        "openscad",
        "-o",
        str(req.output_stl),
        str(req.output_scad),
    ]
    subprocess.run(cmd, check=True, capture_output=True, text=True)
