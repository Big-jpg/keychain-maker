# 🔑 OpenSCAD Keychain Maker

A Streamlit web application that generates customized OpenSCAD keychain files from templates. Upload your template and font, enter your text, and download the generated SCAD and STL files ready for 3D printing.

## 📋 Overview

This tool allows you to:

- Pick a base OpenSCAD template (`.scad` file) for a keychain
- Pick a font file (`.ttf` / `.otf`)
- Type the text for the keychain
- Get back:
  - A generated `.scad` file with the text & font wired in
  - Optionally, an STL rendered via the OpenSCAD CLI

The tool works with any OpenSCAD template that follows a simple placeholder convention.

## 🚀 Prerequisites

### Required

- **Python 3.10+**
- **pip** (Python package installer)

### Optional (for STL rendering)

- **OpenSCAD CLI** - Download from [openscad.org](https://openscad.org/downloads.html)
  - The app automatically detects OpenSCAD in common installation locations
  - No PATH configuration required on most systems!
  - See [OPENSCAD_SETUP.md](OPENSCAD_SETUP.md) for detailed setup instructions
  - Without OpenSCAD, you can still generate `.scad` files

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/keychain-maker.git
cd keychain-maker
```

2. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

3. **Verify OpenSCAD installation (optional):**

```bash
openscad --version
```

## 🎯 Usage

### Running the Streamlit App

Start the application with:

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`.

### Using the Web Interface

1. **Upload Template**: Choose an OpenSCAD template file (`.scad`) with placeholders
2. **Upload Font**: Select a font file (`.ttf` or `.otf`)
3. **Enter Text**: Type the text you want on your keychain
4. **Specify Font Name**: Enter the OpenSCAD font identifier (e.g., `GG:style=Bartex-Regular`)
5. **Set Output Name**: Choose a base name for your generated files
6. **Generate**: Click the "Generate Keychain" button
7. **Download**: Download your generated SCAD and/or STL files

## 📝 Template Requirements

Your OpenSCAD template must include these placeholders:

- **`{{TEXT}}`** - Where the keychain text will be inserted
- **`{{FONT_NAME}}`** - The OpenSCAD font identifier string
- **`{{TTF_FILE}}`** - The font file name used in the `use <...>` statement

### Example Template

```openscad
// keychain template with placeholders

use <{{TTF_FILE}}>

Text="{{TEXT}}";
Text_Size=15;

color("pink")
translate([0,0,-1])
linear_extrude (base_thickness)
offset(r=round(((Text_Size+10)/5)/2))
    text(Text, size=Text_Size, halign="left", valign="center", $fn=32, font=Font);

Font="{{FONT_NAME}}";
base_thickness=2.5;
```

A complete example template is provided in `examples/barbie_keychain.scad`.

## 📂 Project Structure

```
keychain-maker/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── app.py                    # Main Streamlit application
├── keychain_maker/           # Core package
│   ├── __init__.py
│   ├── models.py            # Data models
│   ├── templates.py         # Template processing
│   └── scad_renderer.py     # STL rendering
├── examples/                 # Example templates and fonts
│   └── barbie_keychain.scad
└── dist/                     # Generated files (gitignored)
```

## 🔧 Extending the Tool

### Adding Custom Parameters

You can extend templates with additional placeholders for customization:

- `{{TEXT_SIZE}}` - Font size
- `{{BASE_THICKNESS}}` - Base thickness
- `{{COLOR}}` - Color specification

Update the `templates.py` file to handle new placeholders:

```python
def render_template(req: KeychainRequest) -> str:
    scad_text = Path(req.template_scad).read_text(encoding="utf-8")
    
    return (
        scad_text
        .replace(PLACE_TEXT, req.text)
        .replace(PLACE_FONT_NAME, req.font_name)
        .replace(PLACE_TTF, font_filename_only)
        .replace("{{TEXT_SIZE}}", str(req.text_size))  # New parameter
    )
```

### Creating New Templates

To create a new template:

1. Design your keychain in OpenSCAD
2. Replace hardcoded values with placeholders:
   - Text → `{{TEXT}}`
   - Font name → `{{FONT_NAME}}`
   - Font file → `{{TTF_FILE}}`
3. Save the template in the `examples/` directory
4. Test it using the Streamlit app

## 🐛 Troubleshooting

### OpenSCAD Not Found

**Error**: "OpenSCAD CLI not found"

**Solution**: 
- Install OpenSCAD from [openscad.org](https://openscad.org/downloads.html)
- Ensure the `openscad` command is available in your PATH
- On Windows, you may need to add the OpenSCAD installation directory to your system PATH

### Font Not Rendering Correctly

**Error**: Text appears in wrong font in STL

**Solution**:
- Verify the font name matches the font file
- Use OpenSCAD's font list to find the correct identifier: `Help > Font List`
- Common format: `FontFamily:style=StyleName` (e.g., `Arial:style=Bold`)

### Template Placeholders Not Replaced

**Error**: Generated SCAD still contains `{{TEXT}}` or other placeholders

**Solution**:
- Ensure placeholders are exactly `{{TEXT}}`, `{{FONT_NAME}}`, and `{{TTF_FILE}}`
- Check for extra spaces or typos in the template
- Verify the template file encoding is UTF-8

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

Made with ❤️ using Streamlit and OpenSCAD
