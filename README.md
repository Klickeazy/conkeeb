# Conkeeb - Split Keyboard

## Design and Fabrication
- Modified layout from ErgoDox on [KLE](http://www.keyboard-layout-editor.com/#/)
- Switch-plate template generated on [SwillKB](http://builder.swillkb.com/)
- CAD done on OnShape
- Printed on a modified Ender3Pro using a 0.6mm nozzle in PLA

## Bill of Materials
- 2 x Adafruit [NeoKey 5x6 Ortho Snap-Apart Mechanical Key Switches w/ NeoPixel - For MX Compatible Switches](https://www.adafruit.com/product/5157)
- 60 x MX socket compatible switches : Using [Gateron KS-9 RGB](https://a.co/d/2FaNAoF) for LEDs
- 50 x 1u keycaps compatible to switch stems : [Pudding Style XDA](https://a.co/d/bYV5bW5) for LEDs
- 2 x Joystick with breakout board [WMYCONGCONG Game Joystick](https://a.co/d/7XcAHXY)
- 2 x Display units [Hosyond 0.96 Inch OLED](https://a.co/d/dcp77Un)
- 2 x [USB-A breakout](https://a.co/d/6CouvCj) + 1 [USB-A Male to Male cable](https://a.co/d/9nUPYLn) : to connect the two halves of the keyboard - need 4 lines for UART, could look at alternate TRRS or USB-C connector choices
- 2 x [RPi-Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) for each of the halves - there are some spare GPIO pins - could add more hardware like an encoder or use a smaller one by sacrificing the joystick or display unit

- Fasteners **per KB half**
    - 4-6 x M3 6mm(H)x5mm(OD) heat-set inserts and 6mm socket-heads for the case and switch plate - holes dimensioned to allow for socket heads to sink into the base
    - 2 x M3 4mm (H)x5mm(OD) heat-set inserts and 4mm socket-heads for the USB-A breakout board
    - 2 x M2 4mm(H)x3.5mm(OD) heat-set inserts and 6mm screws for the Pico
    - 4 x M2 4mm socket-heads and nuts for the display unit - these screw heads are visible - pick whatever you think looks the best
    - optional :  3 x 2mm(H)x6mm(D) magnets for the foot and base

- [3D Printed parts](stl)
    - 1 each of switchplate and base L & R
    - optional foot L & R
    - Approximately 100g per base, 40g per switchplate and foot - tested with 0.6mm nozzle, 0.32mm layer height 25% adaptive cubic infill
