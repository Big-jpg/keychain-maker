# keychain_maker/templates.py

from pathlib import Path
import shutil
from .models import KeychainRequest

# Placeholder constants
PLACE_TEXT = "{{TEXT}}"
PLACE_FONT_NAME = "{{FONT_NAME}}"
PLACE_TTF = "{{TTF_FILE}}"

def render_template(req: KeychainRequest) -> str:
    """
    Load the SCAD template and replace placeholders with actual values.
    
    Args:
        req: KeychainRequest containing template path and replacement values
        
    Returns:
        Rendered SCAD content as string
    """
    scad_text = Path(req.template_scad).read_text(encoding="utf-8")
    
    # Derive the font file name as seen by OpenSCAD
    # For v1 assume font file will live beside generated .scad
    font_filename_only = Path(req.font_file).name
    
    return (
        scad_text
        .replace(PLACE_TEXT, req.text)
        .replace(PLACE_FONT_NAME, req.font_name)
        .replace(PLACE_TTF, font_filename_only)
    )

def write_scad_and_font(req: KeychainRequest, rendered_scad: str) -> None:
    """
    Write the rendered SCAD file and copy the font file to the output directory.
    
    Args:
        req: KeychainRequest containing output paths
        rendered_scad: Rendered SCAD content to write
    """
    out_scad_path = req.output_scad
    out_scad_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write the SCAD file
    out_scad_path.write_text(rendered_scad, encoding="utf-8")
    
    # Copy font file into the same directory as the .scad
    dest_font_path = out_scad_path.parent / Path(req.font_file).name
    if dest_font_path.resolve() != Path(req.font_file).resolve():
        shutil.copy2(req.font_file, dest_font_path)
