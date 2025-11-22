# Changelog

All notable changes to the OpenSCAD Keychain Maker project will be documented in this file.

## [1.3.0] - 2025-11-22

### Added
- **Automatic Font Name Detection**: App now extracts the actual font family name from TTF/OTF files
  - Reads font metadata to get the correct OpenSCAD font identifier
  - Auto-fills the "Font Name" field with the detected name
  - Shows success message with detected font info
  - Fallback to filename-based suggestion if extraction fails
- **Font Utilities Module** (`font_utils.py`): 
  - `extract_font_name()`: Reads TTF/OTF 'name' table
  - `suggest_font_name()`: Provides OpenSCAD-compatible font names
- **FONT_NAME_GUIDE.md**: Comprehensive guide for understanding font names
  - Auto-detection explanation
  - Manual detection methods for Windows/macOS/Linux
  - Troubleshooting common font issues
  - Font style reference

### Fixed
- **Font Rendering Issue**: Fonts now render correctly in generated SCAD/STL files
  - Previously used hardcoded default "GG:style=Bartex-Regular"
  - Now uses actual font name from uploaded file
  - Proper format: `FontFamily:style=StyleName`

### Improved
- **User Experience**: No more guessing font names!
- **File Handling**: Added seek(0) to reset file pointers after reading
- **Error Prevention**: Automatic detection reduces user errors

## [1.2.0] - 2025-11-22

### Added
- **Multi-Color 3D Printing Support**: New templates optimized for two-color printing
  - `barbie_keychain_multicolor.scad`: Fixed heights (2.5mm base + 1.5mm text)
  - `keychain_configurable.scad`: Customizable layer heights
- **Template Selection UI**: Choose from example templates or upload custom ones
- **MULTICOLOR_PRINTING.md**: Comprehensive guide for multi-color 3D printing
  - Slicer setup instructions (PrusaSlicer, Cura, Bambu Studio, OrcaSlicer)
  - Layer calculation formulas and tables
  - Color combination ideas
  - Troubleshooting tips
- **In-App Guide**: Expandable multi-color printing instructions in the UI
- **Single Mesh Design**: Both layers combined into one STL for easy slicing

### Improved
- **Template Architecture**: Two-layer design with distinct heights for color changes
- **User Experience**: Clear template descriptions and multi-color printing indicators
- **Documentation**: Added multi-color printing section to README

### Technical Details
- Templates use OpenSCAD `union()` to create single mesh
- Base layer: 0-2.5mm (Color 1)
- Text layer: 2.5-4.0mm (Color 2)
- Color change point: Z=2.5mm
- Compatible with all major slicers

## [1.1.0] - 2025-11-22

### Added
- **Smart OpenSCAD Detection**: Automatically finds OpenSCAD in common installation locations
  - Windows: Program Files, Program Files (x86), AppData\Local
  - macOS: /Applications, ~/Applications, Homebrew paths
  - Linux: /usr/bin, /usr/local/bin, /snap/bin, ~/.local/bin
- **Version Display**: Shows OpenSCAD version and installation path in sidebar
- **Environment Variable Support**: `OPENSCAD_PATH` for custom installations
- **Configuration Guide**: Expandable help section for manual path setup
- **OPENSCAD_SETUP.md**: Comprehensive setup guide for all platforms

### Improved
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux without PATH configuration
- **Better Error Messages**: Specific guidance for OpenSCAD installation and configuration
- **User Experience**: Clear visual feedback about OpenSCAD status

### Changed
- `scad_renderer.py`: Complete rewrite with platform-aware detection
- `app.py`: Enhanced sidebar with version info and configuration help

## [1.0.1] - 2025-11-22

### Fixed
- **Critical Bug**: Fixed `AttributeError: property 'output_scad' of 'KeychainRequest' object has no setter`
  - Removed invalid lambda function assignments to Pydantic model properties
  - Simplified file path handling in `app.py` to directly use Path objects
  - The app now correctly generates SCAD files without property setter errors

### Technical Details
- **Issue**: Lines 134-135 in `app.py` attempted to override `@property` decorated methods with lambda functions
- **Solution**: Removed property overrides and directly used local Path variables for file operations
- **Impact**: Users can now successfully generate keychain files without encountering AttributeError

## [1.0.0] - 2025-11-22

### Added
- Initial release of OpenSCAD Keychain Maker
- Streamlit web interface for keychain generation
- Template system with placeholder support (`{{TEXT}}`, `{{FONT_NAME}}`, `{{TTF_FILE}}`)
- Custom font upload (.ttf/.otf)
- SCAD file generation
- Optional STL rendering via OpenSCAD CLI
- Example Barbie keychain template
- Comprehensive documentation (README, QUICKSTART, DEPLOYMENT guides)
- MIT License

### Features
- Web-based UI with file upload
- Real-time preview of generated SCAD code
- Download functionality for generated files
- OpenSCAD CLI detection and status display
- Error handling and user-friendly error messages
- Temporary file management for security

### Documentation
- README.md - Complete project documentation
- QUICKSTART.md - 5-minute setup guide
- DEPLOYMENT.md - Cloud deployment instructions
- PROJECT_SUMMARY.md - Architecture overview
- LICENSE - MIT License
