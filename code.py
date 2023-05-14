print("Starting")

import board
from kmk.modules.layers import Layers
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.stringy_keymaps import StringyKeymaps
rollover_cols_every_rows = 4


keyboard = KMKKeyboard()
keyboard.extensions.append(StringyKeymaps())
keyboard.modules.append(Layers())
keyboard.col_pins = (
    board.GP28,board.GP27,board.GP26,
    board.GP22,board.GP7,board.GP6,
    board.GP8,board.GP9,board.GP15,board.GP10
    )
keyboard.row_pins = (
    board.GP3,board.GP2,board.GP1,board.GP0
    )
keyboard.diode_orientation = DiodeOrientation.COL2ROW
______ = 'NO'
MOLYR = KC.MO(1)
keyboard.keymap = [
    [
        "Q",'W','E','R','T','Y','U','I','O','P',
        'A','S','D','F','G','H','J','K','L','ENT',
        'Z','X','C','V','B','N','M','COMMA','DOT','QUOTE',
        MOLYR,'RCTL','LGUI','LSFT','SPC',______,'BSLASH','SCOLON','MINUS','BSPC' 
    ],
    [
        "F1",'F2','F3','F4','F5','F6','F7','F8','F9','TAB',
        "N1",'N2','N3','N4','N5','N6','N7','N8','N9','N0',
        'F10','F11','F12','SCOLON','GRAVE','SLASH','EQL','LBRC','RBRC','ESC',
        MOLYR,'RCTL','LGUI','RSFT','SPC',______,'LEFT','DOWN','UP','RIGHT' 
    ],

]

if __name__ == '__main__':
    keyboard.go()
