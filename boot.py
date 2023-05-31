import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid

from code import keyboard
from kmk.scanners import DiodeOrientation


# If this key is held during boot, don't run the code which hides the storage and disables serial
# This will use the first row/col pin. Feel free to change it if you want it to be another pin
col = digitalio.DigitalInOut(board.GP28)
row = digitalio.DigitalInOut(board.GP3)

if keyboard.diode_orientation == DiodeOrientation.COLUMNS:
    col.switch_to_output(value=True)
    row.switch_to_input(pull=digitalio.Pull.DOWN)
else:
    col.switch_to_input(pull=digitalio.Pull.DOWN)
    row.switch_to_output(value=True)

if not row.value:
    storage.disable_usb_drive()
    # Equivalent to usb_cdc.enable(console=False, data=False)
    usb_cdc.disable()
    usb_hid.enable(boot_device=1)

row.deinit()
col.deinit()


# import board

# from kmk.bootcfg import bootcfg

# bootcfg(
#     sense=board.GP28,  # column
#     source=board.GP2, # row
#     boot_device = 1,
#     midi=False,
#     mouse=False,
#     storage=False,
#     usb_id=('CoffeeSippingBastard', 'Shorty40'),
# )