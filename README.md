# The Shorty40
An ortholinear 39key keyboard with a 2U spacebar and KMK support using a Raspberry Pi Pico


## Bill of Materials

### Cost Saving Open Build
* Printed circuit board
* Raspberry Pi Pico or clones with same dimensions and GPIO Layouts with male headers attached 
* 39 1N4148 Diodes - through hole version
* 39 CherryMX Compatible plate mount switches
* 38 1U Keycaps and 1 2U Keycaps
* 1 2U plate mount stabilizer
* 1 3D Printed key plate
* 1 Laser Cut bottom plate
* 4 M2 Stand-Offs with  minimum 20mm clearance
* 8 5mm M2 screws
* 4 adhesive silicone/rubber foot - recommended but not required

### Close Case Build
* Printed circuit board
* Raspberry Pi Pico or clones with same dimensions and GPIO Layouts 
* 2 20 Pin male headers for the Pi Pico
* 2 20 Pin male to female headers for PCB
* 39 1N4148 Diodes - through hole version
* Hot Swap Sockets - tested with Millmax 0305 Socket
* 39 CherryMX Compatible plate mount switches
* 38 1U Keycaps and 1 2U Keycaps
* 1 2U plate mount stabilizer
* 1 3D Printed key plate
* 1 3D Printed Case - testing in process
* 8 5mm M2 screws
* 4 adhesive silicone/rubber foot

## Software Setup
1. Install [circuit python](https://circuitpython.org/)
2. Get [KMK](https://github.com/KMKfw/kmk_firmware/archive/refs/heads/master.zip) and unzip the files on to the circuit-python/pi-pico drive
3. Replace the code.py and boot.py files on the Pi-Pico drive with the ones provided on this repository
