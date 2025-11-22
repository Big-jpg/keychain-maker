# app.py

import streamlit as st
from pathlib import Path
import tempfile
import shutil
import subprocess
from keychain_maker.models import KeychainRequest
from keychain_maker.templates import render_template, write_scad_and_font
from keychain_maker.scad_renderer import render_stl, check_openscad_installed, get_openscad_path, get_openscad_version
from keychain_maker.font_utils import suggest_font_name

# Page configuration
st.set_page_config(
    page_title="OpenSCAD Keychain Maker",
    page_icon="🔑",
    layout="centered"
)

# Title and description
st.title("🔑 OpenSCAD Keychain Maker")
st.markdown("""
Generate customized keychain files from OpenSCAD templates. Upload your template and font, 
enter your text, and download the generated SCAD and STL files.
""")

# Sidebar for information
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This tool generates customized OpenSCAD keychain files by:
    1. Taking a template SCAD file with placeholders
    2. Replacing placeholders with your custom text and font
    3. Optionally rendering an STL file for 3D printing
    
    **Template Requirements:**
    - Use `{{TEXT}}` for text placeholder
    - Use `{{FONT_NAME}}` for font name placeholder
    - Use `{{TTF_FILE}}` for font file placeholder
    """)
    
    # Check OpenSCAD installation
    openscad_path = get_openscad_path()
    
    if openscad_path:
        st.success("✅ OpenSCAD CLI detected")
        version = get_openscad_version(openscad_path)
        if version:
            st.info(f"📍 {version}")
        st.code(openscad_path, language="text")
    else:
        st.warning("⚠️ OpenSCAD CLI not found")
        st.markdown("[Install OpenSCAD](https://openscad.org/downloads.html)")
        
        # Allow manual path configuration
        with st.expander("🔧 Configure OpenSCAD Path"):
            st.markdown("""
            If OpenSCAD is installed but not detected, you can:
            
            **Option 1:** Set environment variable before running:
            ```bash
            export OPENSCAD_PATH="/path/to/openscad"
            streamlit run app.py
            ```
            
            **Option 2:** Add OpenSCAD to your system PATH
            
            **Common Windows paths:**
            - `C:\\Program Files\\OpenSCAD\\openscad.exe`
            - `C:\\Program Files (x86)\\OpenSCAD\\openscad.exe`
            
            **Common macOS paths:**
            - `/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD`
            
            **Common Linux paths:**
            - `/usr/bin/openscad`
            - `/usr/local/bin/openscad`
            """)

# Main form
st.header("Generate Keychain")

# Template selection or upload
st.subheader("📄 Template")

template_option = st.radio(
    "Choose template source:",
    ["Use Example Template", "Upload Custom Template"],
    horizontal=True
)

template_file = None
template_description = ""

if template_option == "Use Example Template":
    example_templates = {
        "Basic (Original)": {
            "file": "examples/barbie_keychain.scad",
            "description": "Original template with pink base and white text overlay. Single color or basic multi-color."
        },
        "Multi-Color (2 layers)": {
            "file": "examples/barbie_keychain_multicolor.scad",
            "description": "**Optimized for multi-color printing!** Base: 2.5mm (Color 1), Text: 1.5mm (Color 2). Set color change at Z=2.5mm in your slicer."
        },
        "Configurable Heights": {
            "file": "examples/keychain_configurable.scad",
            "description": "Advanced template with customizable layer heights. Edit the .scad file to adjust Base_Layer_Height and Text_Layer_Height."
        }
    }
    
    selected_template = st.selectbox(
        "Select example template:",
        list(example_templates.keys())
    )
    
    template_info = example_templates[selected_template]
    st.info(f"ℹ️ {template_info['description']}")
    
    # Read the example template file
    from pathlib import Path
    template_path = Path(template_info['file'])
    if template_path.exists():
        template_content = template_path.read_bytes()
        # Create a file-like object
        import io
        template_file = io.BytesIO(template_content)
        template_file.name = template_path.name
    
    if selected_template == "Multi-Color (2 layers)":
        st.success("🎨 **Multi-color printing ready!** See the Multi-Color Printing Guide below for slicer setup instructions.")
else:
    template_file = st.file_uploader(
        "Upload OpenSCAD Template (.scad)",
        type=["scad"],
        help="Upload a .scad file with {{TEXT}}, {{FONT_NAME}}, and {{TTF_FILE}} placeholders"
    )

st.subheader("🎨 Font")

font_file = st.file_uploader(
    "Upload Font File (.ttf or .otf)",
    type=["ttf", "otf"],
    help="Upload the font file you want to use for the keychain text"
)

# Text inputs
col1, col2 = st.columns(2)

with col1:
    keychain_text = st.text_input(
        "Keychain Text",
        value="",
        max_chars=50,
        help="Enter the text to appear on your keychain"
    )

with col2:
    font_name = st.text_input(
        "Font Name",
        value="GG:style=Bartex-Regular",
        help="OpenSCAD font identifier (e.g., 'GG:style=Bartex-Regular')"
    )

output_basename = st.text_input(
    "Output File Name",
    value="keychain",
    help="Base name for generated files (without extension)"
)

# Render options
render_stl_option = st.checkbox(
    "Generate STL file",
    value=check_openscad_installed(),
    disabled=not check_openscad_installed(),
    help="Render an STL file using OpenSCAD CLI (requires OpenSCAD to be installed)"
)

# Generate button
if st.button("🚀 Generate Keychain", type="primary", use_container_width=True):
    # Validation
    if not template_file:
        st.error("❌ Please upload a template SCAD file")
    elif not font_file:
        st.error("❌ Please upload a font file")
    elif not keychain_text:
        st.error("❌ Please enter text for the keychain")
    elif not output_basename:
        st.error("❌ Please enter an output file name")
    else:
        try:
            with st.spinner("Generating files..."):
                # Create temporary directory for processing
                with tempfile.TemporaryDirectory() as tmpdir:
                    tmpdir_path = Path(tmpdir)
                    
                    # Save uploaded files to temp directory
                    template_path = tmpdir_path / template_file.name
                    font_path = tmpdir_path / font_file.name
                    
                    # Reset file pointers in case they were read before
                    template_file.seek(0)
                    font_file.seek(0)
                    
                    template_path.write_bytes(template_file.read())
                    font_path.write_bytes(font_file.read())
                    
                    # Create output directory
                    output_dir = tmpdir_path / "dist"
                    output_dir.mkdir(exist_ok=True)
                    
                    # Create request object
                    req = KeychainRequest(
                        template_scad=template_path,
                        font_file=font_path,
                        text=keychain_text,
                        font_name=font_name,
                        output_basename=output_basename
                    )
                    
                    # Render template
                    rendered = render_template(req)
                    
                    # Define output paths in temp directory
                    scad_output_path = output_dir / f"{output_basename}.scad"
                    scad_output_path.write_text(rendered, encoding="utf-8")
                    
                    # Copy font file to output directory
                    dest_font_path = output_dir / font_path.name
                    shutil.copy2(font_path, dest_font_path)
                    
                    st.success("✅ SCAD file generated successfully!")
                    
                    # Render STL if requested
                    stl_output_path = None
                    if render_stl_option:
                        try:
                            with st.spinner("Rendering STL file..."):
                                # Define STL output path
                                stl_output_path = output_dir / f"{output_basename}.stl"
                                
                                # Render STL using detected OpenSCAD path
                                render_stl(
                                    scad_file_path=str(scad_output_path),
                                    stl_file_path=str(stl_output_path),
                                    openscad_path=openscad_path
                                )
                                
                                st.success("✅ STL file rendered successfully!")
                        except subprocess.CalledProcessError as e:
                            st.error(f"❌ STL rendering failed: {e.stderr}")
                        except Exception as e:
                            st.error(f"❌ STL rendering error: {str(e)}")
                    
                    # Download section
                    st.header("📥 Download Files")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        # Download SCAD file
                        with open(scad_output_path, "rb") as f:
                            st.download_button(
                                label="⬇️ Download SCAD",
                                data=f.read(),
                                file_name=f"{output_basename}.scad",
                                mime="text/plain",
                                use_container_width=True
                            )
                    
                    with col2:
                        # Download STL file if it exists
                        if stl_output_path and stl_output_path.exists():
                            with open(stl_output_path, "rb") as f:
                                st.download_button(
                                    label="⬇️ Download STL",
                                    data=f.read(),
                                    file_name=f"{output_basename}.stl",
                                    mime="application/octet-stream",
                                    use_container_width=True
                                )
                    
                    # Preview SCAD content
                    with st.expander("👁️ Preview Generated SCAD"):
                        st.code(rendered, language="openscad")
                        
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.exception(e)

# Multi-color printing guide
st.markdown("---")
st.header("🎨 Multi-Color 3D Printing Guide")

with st.expander("📚 Click to view multi-color printing instructions", expanded=False):
    st.markdown("""
    ### How to Print with Two Colors
    
    The **Multi-Color (2 layers)** template creates a single STL with two distinct height layers:
    
    - **Base Layer**: 0 to 2.5mm (Color 1, e.g., Pink)
    - **Text Layer**: 2.5mm to 4.0mm (Color 2, e.g., White)
    
    #### Step-by-Step Instructions:
    
    1. **Generate STL** using the "Multi-Color (2 layers)" template
    2. **Import STL** into your slicer (PrusaSlicer, Cura, Bambu Studio, etc.)
    3. **Add color change** at height = **2.5mm**
       - PrusaSlicer: Right-click layer slider → "Add color change" at 2.5mm
       - Cura: Extensions → Post Processing → "Filament Change" at layer 13 (for 0.2mm layers)
       - Bambu Studio: Click "+" on layer slider at 2.5mm
    4. **Assign colors**:
       - Layers 0-2.5mm: Color 1 (base)
       - Layers 2.5-4.0mm: Color 2 (text)
    5. **Slice and print!**
    
    #### Layer Number Calculator:
    
    If your slicer requires layer numbers instead of height:
    
    | Layer Height | Layer Number for 2.5mm |
    |--------------|------------------------|
    | 0.10mm | Layer 25 |
    | 0.15mm | Layer 17 |
    | 0.20mm | Layer 13 |
    | 0.25mm | Layer 10 |
    | 0.30mm | Layer 9 |
    
    **Formula**: `Layer Number = 2.5mm ÷ Your Layer Height` (round up)
    
    #### Tips for Best Results:
    
    - ✅ Use 100% infill for solid keychains
    - ✅ Enable purge tower/wipe tower for clean color transitions
    - ✅ Purge 50-100mm of filament when changing colors manually
    - ✅ Preview in your slicer's color mode before printing
    - ✅ First layer of each color should be well-squished for adhesion
    
    #### Color Combination Ideas:
    
    - Pink base + White text (Classic Barbie)
    - Black base + Gold text (Elegant)
    - Blue base + White text (Clean)
    - Purple base + Yellow text (Vibrant)
    - Any combination you like!
    
    For detailed instructions, see [MULTICOLOR_PRINTING.md](https://github.com/Big-jpg/keychain-maker/blob/main/MULTICOLOR_PRINTING.md)
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.9em;'>
    Made with ❤️ using Streamlit | 
    <a href='https://github.com/Big-jpg/keychain-maker' target='_blank'>View on GitHub</a>
</div>
""", unsafe_allow_html=True)
