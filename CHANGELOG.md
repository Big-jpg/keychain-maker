# Changelog

All notable changes to the OpenSCAD Keychain Maker project will be documented in this file.

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
