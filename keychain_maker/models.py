# keychain_maker/models.py

from pydantic import BaseModel, FilePath
from pathlib import Path
from typing import Optional

class KeychainRequest(BaseModel):
    """Data model for keychain generation request."""
    
    template_scad: Path
    font_file: Path
    text: str
    font_name: str  # e.g. "GG:style=Bartex-Regular"
    output_basename: str  # for naming out files without extension
    
    class Config:
        arbitrary_types_allowed = True
    
    @property
    def output_scad(self) -> Path:
        """Path to the generated SCAD file."""
        return Path("dist") / f"{self.output_basename}.scad"
    
    @property
    def output_stl(self) -> Path:
        """Path to the generated STL file."""
        return Path("dist") / f"{self.output_basename}.stl"
