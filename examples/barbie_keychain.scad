// keychain template with placeholders

use <{{TTF_FILE}}>

Text="{{TEXT}}";
Text_Size=15; // [15,20,25,30]

// DO NOT MODIFY PROGRAM BEYOND THIS LINE!
    
color("pink")
translate([0,0,-1])
linear_extrude (base_thickness)
offset(r=round(((Text_Size+10)/5)/2))
    text(Text, size=Text_Size, halign="left", valign="center", $fn=32, font=Font);

translate([0,0,0.5])
color("white")
linear_extrude (base_thickness)
    text(Text, size=Text_Size, halign="left", valign="center", $fn=32, font=Font);

// Draw hole for key ring adjusting the position if the first letter is either J, T, or 7
color("pink")
if (Text[0] == "J" || Text[0] == "j" || Text[0] == "7") 
    translate([((((Text_Size-10)/5)-3)*2)+2,0,-1]) draw_ringhole();
else if (Text[0] == "T" || Text[0] == "t" )
    translate([((Text_Size-10)/5)-1,0,-1]) draw_ringhole();
else translate([-3,0,-1]) draw_ringhole();
    
module __Customizer_Limit__ () {}

Font="{{FONT_NAME}}";
cyl_segments=50;
base_thickness=2.5;

module draw_ringhole(){
    difference() {
        color("black")
            cylinder($fn=cyl_segments,h=base_thickness,d=8);

        translate([0,0,-.5]) cylinder($fn=cyl_segments,h=base_thickness+1,d=3.5);
    }    
}
