# 🔧 OpenSCAD Setup Guide

This guide helps you set up OpenSCAD for STL rendering in the Keychain Maker app.

## 📥 Installation

### Windows

1. **Download OpenSCAD**:
   - Visit [openscad.org/downloads.html](https://openscad.org/downloads.html)
   - Download the Windows installer (`.exe`)

2. **Install**:
   - Run the installer
   - Follow the installation wizard
   - Default location: `C:\Program Files\OpenSCAD\`

3. **Verify Installation**:
   - The app will automatically detect OpenSCAD in common locations
   - No PATH configuration needed!

**Common Installation Paths** (auto-detected):
- `C:\Program Files\OpenSCAD\openscad.exe`
- `C:\Program Files (x86)\OpenSCAD\openscad.exe`
- `%LOCALAPPDATA%\Programs\OpenSCAD\openscad.exe`

### macOS

1. **Download OpenSCAD**:
   - Visit [openscad.org/downloads.html](https://openscad.org/downloads.html)
   - Download the macOS `.dmg` file

2. **Install**:
   - Open the `.dmg` file
   - Drag OpenSCAD to Applications folder

3. **Verify Installation**:
   - The app will automatically detect OpenSCAD
   - No additional configuration needed!

**Common Installation Paths** (auto-detected):
- `/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD`
- `~/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD`

**Alternative: Homebrew**
```bash
brew install openscad
```

### Linux

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install openscad
```

**Fedora:**
```bash
sudo dnf install openscad
```

**Arch Linux:**
```bash
sudo pacman -S openscad
```

**Snap (any Linux):**
```bash
sudo snap install openscad
```

**Common Installation Paths** (auto-detected):
- `/usr/bin/openscad`
- `/usr/local/bin/openscad`
- `/snap/bin/openscad`
- `~/.local/bin/openscad`

## ✅ Verification

After installation, the Keychain Maker app will automatically detect OpenSCAD. You'll see:

```
✅ OpenSCAD CLI detected
📍 OpenSCAD version 2021.01
C:\Program Files\OpenSCAD\openscad.exe
```

If detected, the "Generate STL file" checkbox will be enabled!

## 🔧 Manual Configuration

If OpenSCAD is installed but **not detected**, you can manually specify the path:

### Option 1: Environment Variable (Recommended)

**Windows PowerShell:**
```powershell
$env:OPENSCAD_PATH="C:\Program Files\OpenSCAD\openscad.exe"
streamlit run app.py
```

**Windows CMD:**
```cmd
set OPENSCAD_PATH=C:\Program Files\OpenSCAD\openscad.exe
streamlit run app.py
```

**macOS/Linux:**
```bash
export OPENSCAD_PATH="/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD"
streamlit run app.py
```

**Permanent Setup (Linux/macOS):**

Add to your `~/.bashrc` or `~/.zshrc`:
```bash
export OPENSCAD_PATH="/path/to/openscad"
```

Then reload:
```bash
source ~/.bashrc  # or source ~/.zshrc
```

### Option 2: Add to System PATH

**Windows:**
1. Search for "Environment Variables" in Start Menu
2. Click "Edit the system environment variables"
3. Click "Environment Variables" button
4. Under "System variables", find "Path"
5. Click "Edit"
6. Click "New"
7. Add: `C:\Program Files\OpenSCAD`
8. Click "OK" on all dialogs
9. Restart your terminal/command prompt

**macOS/Linux:**

Add to `~/.bashrc` or `~/.zshrc`:
```bash
export PATH="/Applications/OpenSCAD.app/Contents/MacOS:$PATH"
```

## 🐛 Troubleshooting

### "OpenSCAD CLI not found"

**Check if OpenSCAD is installed:**

**Windows:**
```cmd
where openscad
```

**macOS/Linux:**
```bash
which openscad
```

If nothing is returned, OpenSCAD is not in your PATH.

**Find OpenSCAD manually:**

**Windows:**
- Check `C:\Program Files\OpenSCAD\`
- Check `C:\Program Files (x86)\OpenSCAD\`

**macOS:**
- Check `/Applications/OpenSCAD.app/Contents/MacOS/`

**Linux:**
- Check `/usr/bin/openscad`
- Check `/usr/local/bin/openscad`

### "Permission Denied" (Linux/macOS)

Make sure OpenSCAD is executable:
```bash
chmod +x /path/to/openscad
```

### "OpenSCAD detected but STL rendering fails"

1. **Check OpenSCAD version:**
   ```bash
   openscad --version
   ```
   Minimum recommended: 2019.05 or newer

2. **Test OpenSCAD manually:**
   ```bash
   openscad -o test.stl test.scad
   ```

3. **Check error messages** in the Streamlit app - they will show specific OpenSCAD errors

## 📝 Without OpenSCAD

The app works perfectly **without OpenSCAD** installed! You can:

✅ Upload templates and fonts  
✅ Generate customized `.scad` files  
✅ Download `.scad` files  

You just won't be able to:
❌ Generate `.stl` files directly in the app

**Workaround:** Download the `.scad` file and open it in OpenSCAD desktop app to manually export STL.

## 🎯 Quick Test

To verify OpenSCAD is working:

1. Run the Keychain Maker app
2. Check the sidebar - it should show:
   - ✅ OpenSCAD CLI detected
   - Version information
   - Installation path

3. Upload a template and font
4. Check the "Generate STL file" checkbox
5. Click "Generate Keychain"
6. You should get both `.scad` and `.stl` files!

## 🔗 Useful Links

- **OpenSCAD Official Site**: https://openscad.org
- **OpenSCAD Downloads**: https://openscad.org/downloads.html
- **OpenSCAD Documentation**: https://openscad.org/documentation.html
- **OpenSCAD Cheatsheet**: https://openscad.org/cheatsheet/

---

Need more help? Open an issue on [GitHub](https://github.com/Big-jpg/keychain-maker/issues)!
