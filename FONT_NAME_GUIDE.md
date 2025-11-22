# 🔤 Font Name Guide for OpenSCAD

## Understanding Font Names in OpenSCAD

OpenSCAD requires the **actual font family name** from the font file, not the filename. The app now **auto-detects** this for you!

## How It Works

### Automatic Detection

When you upload a font file, the app:

1. ✅ Reads the font's internal metadata
2. ✅ Extracts the font family name
3. ✅ Suggests the correct OpenSCAD format
4. ✅ Pre-fills the "Font Name" field

**Example:**
- **File**: `Crossing-80Vm2.ttf`
- **Detected**: `Crossing 80:style=Regular`
- **Auto-filled**: Ready to use!

### Font Name Format

OpenSCAD uses this format:
```
FontFamily:style=StyleName
```

**Examples:**
- `Arial:style=Regular`
- `Arial:style=Bold`
- `Times New Roman:style=Italic`
- `Comic Sans MS:style=Bold Italic`

## Common Issues & Solutions

### Issue 1: Font Not Rendering Correctly

**Symptom**: Text appears in default font, not your custom font

**Cause**: Incorrect font name

**Solution**: 
1. The app auto-detects the name - use the suggested value
2. If detection fails, find the font name manually (see below)

### Issue 2: Font Name Contains Special Characters

**Symptom**: OpenSCAD errors or wrong font

**Cause**: Font name has spaces, hyphens, or special characters

**Solution**:
- ✅ Use the exact name from the font file (app handles this)
- ✅ Keep the `:style=` part
- ❌ Don't use the filename

### Issue 3: Multiple Font Styles

**Symptom**: Want to use Bold, Italic, etc.

**Solution**: Change the style part:
- `YourFont:style=Regular` → Normal
- `YourFont:style=Bold` → Bold
- `YourFont:style=Italic` → Italic
- `YourFont:style=Bold Italic` → Bold Italic

## Manual Font Name Detection

If auto-detection doesn't work, you can find the font name manually:

### Windows

1. **Right-click** the font file
2. Select **Properties**
3. Go to **Details** tab
4. Look for **Title** or **Font name**
5. Use format: `FontName:style=Regular`

**OR**

1. Double-click the font file (opens Font Viewer)
2. Look at the top - that's the font family name
3. Use format: `FontName:style=Regular`

### macOS

1. **Double-click** the font file (opens Font Book)
2. Look at the **PostScript name** or **Family**
3. Use format: `FontName:style=Regular`

**OR**

1. Open **Font Book** app
2. Find your font
3. Right-click → **Show in Finder**
4. Get Info → look for font name
5. Use format: `FontName:style=Regular`

### Linux

Use `fc-query` command:
```bash
fc-query -f '%{family}\n' your-font.ttf
```

Output will be the font family name.

Use format: `FontName:style=Regular`

## Testing Your Font Name

### Method 1: OpenSCAD Preview

1. Open OpenSCAD
2. Create a test file:
```openscad
use <your-font.ttf>
text("Test", font="YourFontName:style=Regular");
```
3. If text appears in your font → correct name!
4. If text appears in default font → wrong name

### Method 2: OpenSCAD Font List

1. Open OpenSCAD
2. Go to **Help** → **Font List**
3. Search for your font
4. Copy the exact name shown

## Common Font Examples

| Font File | Correct Font Name |
|-----------|-------------------|
| `arial.ttf` | `Arial:style=Regular` |
| `arialbd.ttf` | `Arial:style=Bold` |
| `comic.ttf` | `Comic Sans MS:style=Regular` |
| `times.ttf` | `Times New Roman:style=Regular` |
| `Roboto-Regular.ttf` | `Roboto:style=Regular` |
| `Roboto-Bold.ttf` | `Roboto:style=Bold` |
| `OpenSans-Regular.ttf` | `Open Sans:style=Regular` |

## Font Styles Reference

Common style values:
- `Regular` - Normal weight, upright
- `Bold` - Bold weight
- `Italic` - Italic/slanted
- `Bold Italic` - Bold and italic
- `Light` - Lighter weight
- `Medium` - Medium weight
- `SemiBold` - Semi-bold weight
- `Black` - Heaviest weight
- `Thin` - Thinnest weight

## Troubleshooting

### "Font not found" Error

**Cause**: Font name doesn't match the font file

**Fix**:
1. Check the auto-detected name
2. Try without `:style=` part: just `FontName`
3. Use OpenSCAD's Font List to verify

### Default Font Appears

**Cause**: OpenSCAD can't find the font with that name

**Fix**:
1. Ensure font file is in the same directory as .scad file (app does this automatically)
2. Verify the font name is correct
3. Try opening the .scad file in OpenSCAD directly to test

### Special Characters in Font Name

**Cause**: Font name has unusual characters

**Fix**:
- Use the exact name from the font file
- Don't try to "clean" or simplify it
- The app handles this automatically

## Best Practices

1. ✅ **Use auto-detection** - Let the app find the name
2. ✅ **Keep font and .scad together** - App does this automatically
3. ✅ **Test in OpenSCAD** - Open the generated .scad to verify
4. ✅ **Use common fonts** - Arial, Times, etc. are easier
5. ✅ **Check Font List** - OpenSCAD → Help → Font List

## App Features

### Auto-Detection
- Reads TTF/OTF metadata
- Extracts font family name
- Suggests correct format
- Pre-fills the field

### Manual Override
- You can edit the detected name
- Useful for specific styles
- Change `Regular` to `Bold`, etc.

### Validation
- Font file is copied to output directory
- .scad file references the font correctly
- Everything stays together

## Example Workflow

1. **Upload font**: `MyCustomFont.ttf`
2. **App detects**: `My Custom Font:style=Regular`
3. **Auto-fills**: Font Name field
4. **You can edit**: Change to `My Custom Font:style=Bold` if needed
5. **Generate**: SCAD and STL files use correct font
6. **Success**: Your custom font renders perfectly!

## Need Help?

If auto-detection doesn't work:

1. Check the font file is valid (open it in your OS)
2. Try the manual methods above
3. Test in OpenSCAD directly
4. Open an issue on [GitHub](https://github.com/Big-jpg/keychain-maker/issues)

---

**Pro Tip**: The app now handles all of this automatically! Just upload your font and use the suggested name. 🎉
