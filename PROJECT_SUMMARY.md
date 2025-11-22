# 📋 Project Summary: OpenSCAD Keychain Maker

## 🎯 Project Overview

**OpenSCAD Keychain Maker** is a standalone Streamlit web application that generates customized OpenSCAD keychain files from templates. Users can upload templates and fonts, enter custom text, and download generated `.scad` and `.stl` files ready for 3D printing.

## 🔗 Repository

**GitHub**: [https://github.com/Big-jpg/keychain-maker](https://github.com/Big-jpg/keychain-maker)

## ✨ Key Features

- **Web-based Interface**: User-friendly Streamlit UI, no command-line required
- **Template System**: Works with any OpenSCAD template using placeholder conventions
- **Font Support**: Upload custom `.ttf` or `.otf` fonts
- **SCAD Generation**: Creates customized OpenSCAD files with text and font integrated
- **STL Rendering**: Optional 3D-printable STL generation via OpenSCAD CLI
- **Local & Cloud Ready**: Run locally or deploy to cloud platforms
- **Example Template**: Includes working Barbie keychain template
- **No External Dependencies**: Self-contained application (except optional OpenSCAD CLI)

## 🏗️ Architecture

### Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python 3.11+
- **Dependencies**: 
  - `streamlit>=1.28.0` - Web interface
  - `pydantic>=2.0.0` - Data validation
- **Optional**: OpenSCAD CLI for STL rendering

### Project Structure

```
keychain-maker/
├── app.py                      # Main Streamlit application
├── keychain_maker/             # Core package
│   ├── __init__.py            # Package initialization
│   ├── models.py              # Data models (Pydantic)
│   ├── templates.py           # Template processing logic
│   └── scad_renderer.py       # STL rendering via OpenSCAD
├── examples/                   # Example templates
│   └── barbie_keychain.scad   # Sample template
├── dist/                       # Generated files (gitignored)
├── requirements.txt            # Python dependencies
├── run.sh                      # Convenience launch script
├── README.md                   # Main documentation
├── QUICKSTART.md              # Quick start guide
├── DEPLOYMENT.md              # Deployment instructions
├── LICENSE                     # MIT License
└── .gitignore                 # Git ignore rules
```

## 🔄 How It Works

### Template Placeholder System

Templates use three placeholders:

1. **`{{TEXT}}`** - User's custom text
2. **`{{FONT_NAME}}`** - OpenSCAD font identifier (e.g., "Arial:style=Bold")
3. **`{{TTF_FILE}}`** - Font file reference for `use <...>` statement

### Processing Flow

1. **Upload**: User uploads template `.scad` and font file
2. **Input**: User enters text and font name
3. **Render**: App replaces placeholders in template
4. **Generate**: Creates customized `.scad` file
5. **Optional**: Renders `.stl` via OpenSCAD CLI
6. **Download**: User downloads generated files

### Code Architecture

```python
# Data Model (models.py)
KeychainRequest
  - template_scad: Path
  - font_file: Path
  - text: str
  - font_name: str
  - output_basename: str

# Template Processing (templates.py)
render_template(req) -> str
  - Loads template
  - Replaces placeholders
  - Returns rendered content

write_scad_and_font(req, rendered)
  - Writes .scad file
  - Copies font to output directory

# STL Rendering (scad_renderer.py)
check_openscad_installed() -> bool
render_stl(req)
  - Calls OpenSCAD CLI
  - Generates .stl file
```

## 🚀 Deployment Options

### Local Deployment
- Clone repository
- Install dependencies: `pip install -r requirements.txt`
- Run: `streamlit run app.py` or `./run.sh`
- Access: `http://localhost:8501`

### Cloud Deployment

1. **Streamlit Community Cloud** (Recommended)
   - Free hosting for Streamlit apps
   - Direct GitHub integration
   - Automatic deployment

2. **Docker**
   - Containerized deployment
   - Includes OpenSCAD CLI
   - Portable across platforms

3. **Heroku**
   - PaaS deployment
   - Easy scaling
   - Custom domain support

4. **AWS EC2 / VPS**
   - Full control
   - Custom configuration
   - Systemd service setup

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## 📦 Dependencies

### Required
- Python 3.10+
- streamlit>=1.28.0
- pydantic>=2.0.0

### Optional
- OpenSCAD CLI (for STL rendering)

## 🎨 Example Template

The included `barbie_keychain.scad` demonstrates:

- Multi-layer design (pink base, white text)
- Dynamic keyring hole positioning
- Special handling for specific letters (J, T, 7)
- Customizable text size
- Professional OpenSCAD structure

## 🔧 Customization & Extension

### Adding New Templates

1. Create OpenSCAD design
2. Add placeholders: `{{TEXT}}`, `{{FONT_NAME}}`, `{{TTF_FILE}}`
3. Save as `.scad` file
4. Upload via web interface

### Adding New Parameters

Extend `KeychainRequest` model:

```python
class KeychainRequest(BaseModel):
    # Existing fields...
    text_size: int = 15
    base_thickness: float = 2.5
    color: str = "pink"
```

Update template processing to handle new placeholders.

### Custom Styling

Modify `.streamlit/config.toml` for theme customization:

```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
font = "sans serif"
```

## 🧪 Testing

Basic functionality test included:

```bash
python test_basic.py
```

Tests verify:
- Template loading
- Placeholder replacement
- File generation
- Font handling

## 📝 Documentation

- **README.md**: Comprehensive project documentation
- **QUICKSTART.md**: 5-minute setup guide
- **DEPLOYMENT.md**: Cloud deployment instructions
- **PROJECT_SUMMARY.md**: This file - project overview

## 🔒 Security & Best Practices

- Input validation via Pydantic
- Temporary file handling
- No persistent storage of user data
- Safe subprocess execution
- HTTPS recommended for production

## 🐛 Known Limitations

1. **OpenSCAD Dependency**: STL rendering requires OpenSCAD CLI
2. **File Size**: Large/complex templates may take time to render
3. **Font Compatibility**: Some fonts may not work with OpenSCAD
4. **Cloud Limitations**: Streamlit Cloud may not support OpenSCAD CLI

## 🔮 Future Enhancements

Potential improvements:

- [ ] Template gallery with pre-made designs
- [ ] Preview rendering (2D/3D visualization)
- [ ] Batch processing for multiple keychains
- [ ] Advanced customization (colors, sizes, shapes)
- [ ] User accounts and saved templates
- [ ] Direct 3D printer integration
- [ ] Mobile-responsive design improvements
- [ ] Multi-language support

## 📊 Project Stats

- **Lines of Code**: ~965
- **Files**: 12 source files
- **Dependencies**: 2 Python packages (+ transitive)
- **License**: MIT
- **Language**: Python 3.11

## 🤝 Contributing

Contributions welcome! Areas for contribution:

1. New template examples
2. UI/UX improvements
3. Additional file format support
4. Documentation improvements
5. Bug fixes and optimizations

## 📧 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/Big-jpg/keychain-maker/issues)
- **Discussions**: GitHub Discussions
- **Pull Requests**: Welcome!

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit**: For the excellent web framework
- **OpenSCAD**: For the powerful 3D modeling tool
- **Pydantic**: For robust data validation
- **Community**: For feedback and contributions

---

**Built with ❤️ using Streamlit and OpenSCAD**

Last Updated: November 2025
