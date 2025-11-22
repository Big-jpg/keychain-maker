// Configurable two-layer keychain template
// Supports custom layer heights for multi-color 3D printing

use <{{TTF_FILE}}>

// Customizable parameters
Text="{{TEXT}}";
Text_Size=15; // [10:1:50]
Base_Layer_Height=2.5; // [1.0:0.5:5.0] Height of base layer (first color)
Text_Layer_Height=1.5; // [0.5:0.5:3.0] Height of text layer (second color)

// Calculated values
total_height = Base_Layer_Height + Text_Layer_Height;
offset_radius = round(((Text_Size+10)/5)/2);

// DO NOT MODIFY PROGRAM BEYOND THIS LINE!

// Create single mesh for multi-color printing
// Set color change at Z = Base_Layer_Height in your slicer
union() {
    // Layer 1: Base (0 to Base_Layer_Height) - First color
    translate([0, 0, 0])
    linear_extrude(height=Base_Layer_Height)
    offset(r=offset_radius)
        text(Text, size=Text_Size, halign="left", valign="center", $fn=32, font=Font);
    
    // Layer 2: Text (Base_Layer_Height to total_height) - Second color
    translate([0, 0, Base_Layer_Height])
    linear_extrude(height=Text_Layer_Height)
        text(Text, size=Text_Size, halign="left", valign="center", $fn=32, font=Font);
    
    // Keyring hole (through entire height)
    translate([0, 0, 0])
    if (Text[0] == "J" || Text[0] == "j" || Text[0] == "7") 
        translate([((((Text_Size-10)/5)-3)*2)+2, 0, 0]) draw_ringhole();
    else if (Text[0] == "T" || Text[0] == "t")
        translate([((Text_Size-10)/5)-1, 0, 0]) draw_ringhole();
    else 
        translate([-3, 0, 0]) draw_ringhole();
}

module __Customizer_Limit__ () {}

Font="{{FONT_NAME}}";
cyl_segments=50;

module draw_ringhole(){
    difference() {
        cylinder($fn=cyl_segments, h=total_height, d=8);
        translate([0, 0, -0.5]) 
            cylinder($fn=cyl_segments, h=total_height+1, d=3.5);
    }    
}

// Multi-color printing instructions:
// 1. Export this file as STL
// 2. Import STL into your slicer (PrusaSlicer, Cura, etc.)
// 3. Add a color/filament change at layer height = Base_Layer_Height
//    - For Base_Layer_Height=2.5mm with 0.2mm layer height: Change at layer 13
//    - For Base_Layer_Height=2.5mm with 0.15mm layer height: Change at layer 17
// 4. Assign Color 1 to layers 0 to Base_Layer_Height
// 5. Assign Color 2 to layers Base_Layer_Height to total_height
