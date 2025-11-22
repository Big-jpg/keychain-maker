# 🎨 Multi-Color 3D Printing Guide

This guide explains how to create and print two-layer keychains with different colors for the base and text layers.

## 🎯 Overview

The keychain design has two distinct layers:
- **Base Layer**: 2.5mm height (bottom) - Color 1
- **Text Layer**: 1.5mm height (top) - Color 2
- **Total Height**: 4.0mm

Both layers are exported as a **single STL mesh**, allowing your slicer to assign different colors at specific Z-heights.

## 📐 How It Works

### Layer Structure

```
┌─────────────────────┐  ← 4.0mm (top)
│   Text Layer        │  
│   (1.5mm high)      │  ← Color 2 (e.g., White)
│   Z: 2.5 to 4.0mm   │
├─────────────────────┤  ← 2.5mm (color change here!)
│   Base Layer        │
│   (2.5mm high)      │  ← Color 1 (e.g., Pink)
│   Z: 0 to 2.5mm     │
└─────────────────────┘  ← 0mm (build plate)
```

### Single Mesh Design

The template uses OpenSCAD's `union()` to combine both layers into one continuous mesh. This is crucial because:
- ✅ Single STL file = easier to handle
- ✅ Layers are perfectly aligned
- ✅ No gaps between layers
- ✅ Compatible with all slicers

## 🛠️ Template Options

### Option 1: Fixed Heights Template

**File**: `barbie_keychain_multicolor.scad`

Pre-configured with:
- Base layer: 2.5mm
- Text layer: 1.5mm
- Total: 4.0mm

Perfect for consistent results!

### Option 2: Configurable Template

**File**: `keychain_configurable.scad`

Allows customization:
- `Base_Layer_Height`: 1.0 to 5.0mm (default: 2.5mm)
- `Text_Layer_Height`: 0.5 to 3.0mm (default: 1.5mm)
- `Text_Size`: 10 to 50 (default: 15)

Great for experimentation!

## 🎨 Setting Up Multi-Color Printing

### Step 1: Generate STL

1. Open the Keychain Maker app
2. Upload template: `barbie_keychain_multicolor.scad`
3. Upload your font file
4. Enter text (e.g., "Ayla")
5. Check "Generate STL file"
6. Click "Generate Keychain"
7. Download the `.stl` file

### Step 2: Configure Your Slicer

#### PrusaSlicer / SuperSlicer

1. **Import STL**:
   - File → Import → Select your `.stl` file

2. **Add Color Change**:
   - Method A: Right-click on layer slider → "Add color change"
   - Method B: Click the "+" icon on the layer slider
   - Set height: **2.5mm** (or your Base_Layer_Height)

3. **Assign Filaments**:
   - Layers 0-2.5mm: Filament 1 (e.g., Pink)
   - Layers 2.5-4.0mm: Filament 2 (e.g., White)

4. **Slice and Export**:
   - Click "Slice now"
   - Review the preview (use color mode)
   - Export G-code

#### Cura

1. **Import STL**:
   - File → Open File → Select your `.stl` file

2. **Install Post-Processing Plugin** (if not installed):
   - Extensions → Post Processing → Modify G-Code
   - Add Script → "Filament Change"

3. **Add Filament Change**:
   - Extensions → Post Processing → Modify G-Code
   - Add Script → "Filament Change"
   - Layer: Calculate based on your layer height
     - For 0.2mm layers: Layer 13 (2.5mm ÷ 0.2mm = 12.5, round up)
     - For 0.15mm layers: Layer 17 (2.5mm ÷ 0.15mm = 16.67, round up)

4. **Slice and Export**:
   - Click "Slice"
   - Save to file

#### Bambu Studio

1. **Import STL**:
   - Add plate → Import → Select your `.stl` file

2. **Add Color Change**:
   - Click on the layer slider (right side)
   - Find layer at 2.5mm height
   - Click "+" to add filament change
   - Or right-click → "Add pause/filament change"

3. **Assign Filaments**:
   - Select different filaments for each section
   - Preview in color mode

4. **Slice and Send**:
   - Click "Slice plate"
   - Send to printer or save

#### OrcaSlicer

1. **Import STL**:
   - Add → Import → Select your `.stl` file

2. **Add Filament Change**:
   - Use layer slider on right
   - Click at 2.5mm height
   - Add color change marker

3. **Configure Multi-Material**:
   - Assign different filaments to each layer range
   - Preview to verify

4. **Slice and Export**

## 📏 Calculating Layer Numbers

To find which layer number corresponds to 2.5mm:

**Formula**: `Layer Number = Height ÷ Layer Height`

**Examples**:

| Layer Height | Calculation | Layer Number |
|--------------|-------------|--------------|
| 0.10mm | 2.5 ÷ 0.10 = 25 | Layer 25 |
| 0.12mm | 2.5 ÷ 0.12 = 20.83 | Layer 21 |
| 0.15mm | 2.5 ÷ 0.15 = 16.67 | Layer 17 |
| 0.20mm | 2.5 ÷ 0.20 = 12.5 | Layer 13 |
| 0.25mm | 2.5 ÷ 0.25 = 10 | Layer 10 |
| 0.30mm | 2.5 ÷ 0.30 = 8.33 | Layer 9 |

**Tip**: Always round UP to ensure the color change happens after the base layer is complete.

## 🎨 Color Combination Ideas

### Classic Combinations
- **Pink base + White text** (Barbie style)
- **Black base + Gold text** (Elegant)
- **Blue base + White text** (Clean)
- **Red base + White text** (Bold)

### Fun Combinations
- **Purple base + Yellow text** (Vibrant)
- **Green base + Orange text** (Playful)
- **Navy base + Pink text** (Modern)
- **Gray base + Neon text** (Eye-catching)

### Professional
- **Dark gray base + Silver text**
- **Black base + White text**
- **White base + Black text**

## 🔧 Customizing Layer Heights

If you want different heights, edit the template:

```openscad
base_layer_height = 3.0;  // Change to your desired base height
text_layer_height = 2.0;  // Change to your desired text height
```

**Recommendations**:
- **Minimum base height**: 1.5mm (for strength)
- **Minimum text height**: 0.8mm (for visibility)
- **Maximum total height**: 8mm (for keychain practicality)

## 🖨️ Printing Tips

### Before Printing

1. **Check STL in viewer**:
   - Verify it's a single mesh
   - Check for errors (use Meshmixer or 3D Builder)

2. **Test with single color first**:
   - Print one keychain in single color
   - Verify dimensions and quality

### During Color Change

**Manual Filament Change**:
1. Printer will pause at specified layer
2. Remove old filament
3. Load new filament
4. Purge until new color flows cleanly
5. Resume print

**Multi-Material Printer** (e.g., Bambu AMS, Prusa MMU):
- Automatic color changes
- Ensure purge tower is enabled
- Check filament transitions

### Print Settings

**Recommended**:
- **Layer height**: 0.15mm or 0.20mm (for smooth finish)
- **Infill**: 100% (for solid keychain)
- **Perimeters**: 3-4 (for strength)
- **Top/bottom layers**: 5+ (for solid surfaces)
- **Print speed**: 40-60mm/s (for quality)
- **Temperature**: Per filament specifications

**For Best Results**:
- Enable "Detect thin walls"
- Use "Arachne" perimeter generator (if available)
- Disable supports (not needed)
- Enable brim if adhesion is an issue

## 🐛 Troubleshooting

### Colors Bleeding Together

**Cause**: Insufficient purging during color change

**Solution**:
- Increase purge amount (50-100mm of filament)
- Manually purge until color is pure
- Use purge tower/wipe tower

### Gap Between Layers

**Cause**: Template issue or slicer problem

**Solution**:
- Verify template uses `union()` correctly
- Check STL has no gaps (use repair tool)
- Ensure no "pause" between layers, only color change

### Text Layer Not Adhering

**Cause**: Poor layer adhesion

**Solution**:
- Increase bed temperature for second color
- Ensure first layer of text is well-squished
- Clean nozzle before color change

### Wrong Color Change Height

**Cause**: Incorrect layer calculation

**Solution**:
- Recalculate: `2.5mm ÷ your_layer_height`
- Round UP to next whole layer
- Preview in slicer before printing

## 📊 Quality Checklist

Before printing, verify:

- [ ] STL is a single mesh (not two separate objects)
- [ ] Color change is set at exactly 2.5mm (or your base height)
- [ ] Layer height divides evenly into total height
- [ ] Filament colors are loaded and ready
- [ ] Purge settings are configured
- [ ] Preview shows correct color layers
- [ ] Print time is reasonable
- [ ] Bed adhesion is enabled (brim/raft if needed)

## 🎓 Advanced Techniques

### Three-Color Printing

Add a third layer for more complexity:

```openscad
base_layer_height = 2.0;   // Color 1
middle_layer_height = 1.5; // Color 2  
top_layer_height = 0.5;    // Color 3
```

Set two color changes:
- First change at 2.0mm
- Second change at 3.5mm

### Gradient Effect

Use multiple thin layers with gradual color transitions:
- Layer 1: Dark pink (0-1mm)
- Layer 2: Medium pink (1-2mm)
- Layer 3: Light pink (2-3mm)
- Layer 4: White (3-4mm)

### Transparent + Opaque

- Base: Transparent/translucent filament
- Text: Opaque colored filament
- Creates interesting light effects!

## 📚 Additional Resources

- **OpenSCAD Manual**: https://openscad.org/documentation.html
- **PrusaSlicer Color Print**: https://help.prusa3d.com/article/color-print_1687
- **Multi-Material Printing Guide**: https://all3dp.com/2/multi-material-3d-printing/

## 🎉 Example Workflow

1. ✅ Generate STL with `barbie_keychain_multicolor.scad`
2. ✅ Import into PrusaSlicer
3. ✅ Add color change at 2.5mm
4. ✅ Assign Pink (0-2.5mm) and White (2.5-4.0mm)
5. ✅ Slice with 0.2mm layer height
6. ✅ Export G-code
7. ✅ Load Pink filament
8. ✅ Start print
9. ✅ At pause (layer 13), change to White filament
10. ✅ Resume and complete print
11. ✅ Enjoy your two-color keychain! 🎨

---

**Need help?** Open an issue on [GitHub](https://github.com/Big-jpg/keychain-maker/issues)!
