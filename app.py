# app.py

import streamlit as st
from pathlib import Path
import tempfile
import shutil
from keychain_maker.models import KeychainRequest
from keychain_maker.templates import render_template, write_scad_and_font
from keychain_maker.scad_renderer import render_stl, check_openscad_installed

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
    if check_openscad_installed():
        st.success("✅ OpenSCAD CLI detected")
    else:
        st.warning("⚠️ OpenSCAD CLI not found. STL rendering will be disabled.")
        st.markdown("[Install OpenSCAD](https://openscad.org/downloads.html)")

# Main form
st.header("Generate Keychain")

# File uploads
template_file = st.file_uploader(
    "Upload OpenSCAD Template (.scad)",
    type=["scad"],
    help="Upload a .scad file with {{TEXT}}, {{FONT_NAME}}, and {{TTF_FILE}} placeholders"
)

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
                                
                                import subprocess
                                cmd = [
                                    "openscad",
                                    "-o",
                                    str(stl_output_path),
                                    str(scad_output_path),
                                ]
                                result = subprocess.run(cmd, check=True, capture_output=True, text=True)
                                
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

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.9em;'>
    Made with ❤️ using Streamlit | 
    <a href='https://github.com/yourusername/keychain-maker' target='_blank'>View on GitHub</a>
</div>
""", unsafe_allow_html=True)
