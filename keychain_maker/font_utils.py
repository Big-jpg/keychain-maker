# keychain_maker/font_utils.py

from pathlib import Path
from typing import Optional
import struct

def extract_font_name(font_path: str) -> Optional[str]:
    """
    Extract the font family name from a TTF/OTF file.
    
    This reads the 'name' table from the font file to get the actual font family name
    that OpenSCAD will recognize.
    
    Args:
        font_path: Path to the TTF or OTF font file
        
    Returns:
        Font family name if found, None otherwise
    """
    try:
        with open(font_path, 'rb') as f:
            # Read the font file header
            data = f.read()
            
            # TTF/OTF files have different magic numbers
            if data[:4] not in [b'\x00\x01\x00\x00', b'OTTO', b'true', b'typ1']:
                return None
            
            # Find the 'name' table
            if data[:4] == b'OTTO':  # CFF-based OpenType
                num_tables = struct.unpack('>H', data[4:6])[0]
            else:  # TrueType
                num_tables = struct.unpack('>H', data[4:6])[0]
            
            # Search for 'name' table in the table directory
            name_table_offset = None
            for i in range(num_tables):
                offset = 12 + i * 16
                tag = data[offset:offset+4]
                if tag == b'name':
                    name_table_offset = struct.unpack('>I', data[offset+8:offset+12])[0]
                    break
            
            if name_table_offset is None:
                return None
            
            # Read the name table
            f.seek(name_table_offset)
            format_selector = struct.unpack('>H', f.read(2))[0]
            count = struct.unpack('>H', f.read(2))[0]
            string_offset = struct.unpack('>H', f.read(2))[0]
            
            # Look for name ID 1 (Font Family) or name ID 4 (Full Font Name)
            font_family_name = None
            full_font_name = None
            
            for i in range(count):
                platform_id = struct.unpack('>H', f.read(2))[0]
                encoding_id = struct.unpack('>H', f.read(2))[0]
                language_id = struct.unpack('>H', f.read(2))[0]
                name_id = struct.unpack('>H', f.read(2))[0]
                length = struct.unpack('>H', f.read(2))[0]
                offset = struct.unpack('>H', f.read(2))[0]
                
                # We want English names (language_id 0x0409 for Windows, 0 for Mac)
                if name_id == 1 and (language_id == 0x0409 or language_id == 0):
                    # Font Family name
                    current_pos = f.tell()
                    f.seek(name_table_offset + string_offset + offset)
                    name_data = f.read(length)
                    f.seek(current_pos)
                    
                    # Decode based on platform
                    if platform_id == 3:  # Windows
                        try:
                            font_family_name = name_data.decode('utf-16-be')
                        except:
                            try:
                                font_family_name = name_data.decode('utf-8')
                            except:
                                pass
                    elif platform_id == 1:  # Mac
                        try:
                            font_family_name = name_data.decode('mac-roman')
                        except:
                            try:
                                font_family_name = name_data.decode('utf-8')
                            except:
                                pass
                
                elif name_id == 4 and (language_id == 0x0409 or language_id == 0):
                    # Full Font Name (fallback)
                    current_pos = f.tell()
                    f.seek(name_table_offset + string_offset + offset)
                    name_data = f.read(length)
                    f.seek(current_pos)
                    
                    if platform_id == 3:  # Windows
                        try:
                            full_font_name = name_data.decode('utf-16-be')
                        except:
                            pass
                    elif platform_id == 1:  # Mac
                        try:
                            full_font_name = name_data.decode('mac-roman')
                        except:
                            pass
            
            # Return font family name, or full name as fallback
            return font_family_name or full_font_name
            
    except Exception as e:
        # If we can't read the font, return None
        return None


def suggest_font_name(font_path: str) -> str:
    """
    Suggest an OpenSCAD-compatible font name for the given font file.
    
    Tries to extract the actual font name from the file, falls back to filename-based guess.
    
    Args:
        font_path: Path to the TTF or OTF font file
        
    Returns:
        Suggested font name string for OpenSCAD
    """
    # Try to extract the actual font name
    extracted_name = extract_font_name(font_path)
    
    if extracted_name:
        # Clean up the name and add style if not present
        if ':style=' not in extracted_name:
            return f"{extracted_name}:style=Regular"
        return extracted_name
    
    # Fallback: use filename without extension
    filename = Path(font_path).stem
    
    # Clean up common patterns in filenames
    # Remove version numbers, hyphens, underscores
    clean_name = filename.replace('-', ' ').replace('_', ' ')
    
    # Remove common suffixes
    for suffix in [' Regular', ' Bold', ' Italic', ' Light', ' Medium']:
        if clean_name.endswith(suffix):
            style = suffix.strip()
            clean_name = clean_name[:-len(suffix)]
            return f"{clean_name}:style={style}"
    
    # Default to Regular style
    return f"{clean_name}:style=Regular"
