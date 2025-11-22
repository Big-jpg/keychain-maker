// Multi-color two-layer keychain template
// Base layer: 2.5mm height (Color 1)
// Text layer: 1.5mm height (Color 2)
// Total height: 4.0mm
// For multi-color printing: Set color change at Z = 2.5mm in your slicer

use <{{TTF_FILE}}>

Text="{{TEXT}}";
Text_Size=15; // [15,20,25,30]

// Layer heights for multi-color printing
base_layer_height = 2.5;  // Height of base layer (first color)
text_layer_height = 1.5;  // Height of text layer (second color)
total_height = base_layer_height + text_layer_height;  // Total: 4.0mm

// DO NOT MODIFY PROGRAM BEYOND THIS LINE!

// Create the complete keychain as a single mesh
union() {
    // Base layer (0 to 2.5mm) - First color
    translate([0, 0, 0])
    linear_extrude(height=base_layer_height)
    offset(r=round(((Text_Size+10)/5)/2))
        text(Text, size=Text_Size, halign="left", valign="center", $fn=32, font=Font);
    
    // Text layer (2.5mm to 4.0mm) - Second color
    translate([0, 0, base_layer_height])
    linear_extrude(height=text_layer_height)
        text(Text, size=Text_Size, halign="left", valign="center", $fn=32, font=Font);
    
    // Keyring hole (goes through entire height)
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
