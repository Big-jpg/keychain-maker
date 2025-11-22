# ⚡ Quick Start Guide

Get up and running with OpenSCAD Keychain Maker in 5 minutes!

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Big-jpg/keychain-maker.git
cd keychain-maker
```

### Step 2: Set Up Python Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Run the App

```bash
streamlit run app.py
```

Or use the convenience script:

```bash
./run.sh
```

The app will open automatically in your browser at `http://localhost:8501`

## 🎯 First Keychain

### Using the Web Interface

1. **Upload Template**: Use the example `examples/barbie_keychain.scad`
2. **Upload Font**: Any `.ttf` or `.otf` font file from your system
3. **Enter Text**: Type your name or any text (e.g., "ROSS")
4. **Font Name**: Use the default or specify your font (e.g., "Arial:style=Bold")
5. **Click Generate**: Download your `.scad` file!

### Optional: Render STL

To generate 3D-printable STL files:

1. **Install OpenSCAD**: Download from [openscad.org](https://openscad.org/downloads.html)
2. **Verify Installation**:
   ```bash
   openscad --version
   ```
3. **Check the "Generate STL" box** in the app
4. **Generate**: You'll get both `.scad` and `.stl` files!

## 📝 Example Template

The included `examples/barbie_keychain.scad` is a complete working template. It includes:

- Text customization
- Font support
- Keyring hole
- Pink and white layers
- Special positioning for letters J, T, and 7

## 🔧 Customization

### Create Your Own Template

1. Design your keychain in OpenSCAD
2. Replace hardcoded values with placeholders:
   - `{{TEXT}}` - Your custom text
   - `{{FONT_NAME}}` - Font identifier
   - `{{TTF_FILE}}` - Font file reference

3. Save as `.scad` file
4. Upload to the app!

### Example Template Structure

```openscad
use <{{TTF_FILE}}>

Text="{{TEXT}}";
Font="{{FONT_NAME}}";

// Your OpenSCAD design here
text(Text, font=Font);
```

## 🎨 Finding Font Names

To find the correct font name for OpenSCAD:

1. Open OpenSCAD
2. Go to **Help** → **Font List**
3. Find your font (format: `FontFamily:style=StyleName`)
4. Use that exact string in the app

Common examples:
- `Arial:style=Regular`
- `Arial:style=Bold`
- `Times New Roman:style=Regular`
- `Comic Sans MS:style=Regular`

## 📦 What You Get

After generation, you'll receive:

- **`.scad` file**: Editable OpenSCAD source with your text
- **`.stl` file** (optional): Ready for 3D printing!

## 🐛 Troubleshooting

### "OpenSCAD CLI not found"

**Solution**: Install OpenSCAD and ensure it's in your system PATH

```bash
# Ubuntu/Debian
sudo apt install openscad

# macOS
brew install openscad

# Windows
# Download installer from openscad.org
```

### Font Not Working

**Solution**: 
- Check the font name format: `FontFamily:style=StyleName`
- Verify the font file is valid `.ttf` or `.otf`
- Try a system font like Arial first

### Port Already in Use

**Solution**:
```bash
# Kill process on port 8501
lsof -ti:8501 | xargs kill -9

# Or use a different port
streamlit run app.py --server.port=8502
```

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [DEPLOYMENT.md](DEPLOYMENT.md) for cloud deployment options
- Explore the code in `keychain_maker/` to understand how it works
- Create your own custom templates!

## 🤝 Need Help?

- Open an issue on [GitHub](https://github.com/Big-jpg/keychain-maker/issues)
- Check existing issues for solutions
- Contribute improvements via Pull Requests!

---

Happy keychain making! 🔑✨
