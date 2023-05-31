print("Starting")

import board
from kmk.modules.layers import Layers
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.stringy_keymaps import StringyKeymaps
from kmk.modules.modtap import ModTap
from kmk.modules.string_substitution import StringSubstitution



rollover_cols_every_rows = 4


keyboard = KMKKeyboard()
keyboard.extensions.append(StringyKeymaps())
keyboard.modules.append(Layers())

modtap = ModTap()
keyboard.modules.append(modtap)

translations = {
    ':data':"""import pandas as np
import numpy as np""",


    ':viz':"""from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure

fig=figure()
""",


    ':email':"""from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
import smtplib
from email.mime.application import MIMEApplication

send_from = 'placeholder@domain.com'
send_to = 'placeholder@domain.com'

msg = MIMEMultipart()
msg["From"] = send_from
msg["To"] = send_to
msg["Subject"] = '{{{placeholder}}}'

message = '{{{placeholder}}}'
message = MIMEText(message, "plain")
msg.attach(message)

s = smtplib.SMTP()
s.connect(host="smtp.domain.com")
s.sendmail(send_from, send_to.split(","), msg.as_string())
s.close()

""",


    ':sign':"""Thank You,
John Doe""",


    ':mysql':"""import mysql.connector
from sqlalchemy import create_engine
import urllib


host='{{{placeholder}}}'
user='{{{placeholder}}}'
password='{{{placeholder}}}'
database = '{{{placeholder}}}'
sql = '{{{placeholder}}}'

engine = create_engine('mysql+pymysql://{user}:{psw}@{host}/{db}'.format(user=user,host=host,db=database,psw=urllib.parse.quote(password)))
data = pd.read_sql(sql, engine)

engine.dispose()
""",


    ':redshift':"""import redshift_connector
import urllib


host='{{{placeholder}}}'
user='{{{placeholder}}}'
password='{{{placeholder}}}'
database = '{{{placeholder}}}'
port = '{{{placeholder}}}'
sql = '{{{placeholder}}}'

conn = redshift_connector.connect(host= host,port= port,database= database,user= user,password= password)
data = pd.read_sql(sql, conn)

conn.dispose()
"""
}

string_substitution = StringSubstitution(dictionary = translations)

keyboard.modules.append(string_substitution)

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

switchwinmod = KC.MT(KC.LGUI(KC.TAB),MOLYR)
bswitchwinclt = KC.MT(KC.LGUI(KC.LSFT(KC.TAB)),KC.LCTL)

switchtabgui = KC.MT(KC.LCTL(KC.TAB),KC.LGUI)
bswitchtabsft = KC.MT(KC.LCTL(KC.LSFT(KC.TAB)),KC.LSFT)
altesc = KC.MT( KC.ESC, KC.LALT)
keyboard.keymap = [
    [
        "Q",'W','E','R','T','Y','U','I','O','P',
        'A','S','D','F','G','H','J','K','L','ENT',
        'Z','X','C','V','B','N','M','COMMA','DOT','QUOTE',
        switchwinmod,bswitchwinclt,switchtabgui,bswitchtabsft,'SPC',______,altesc,'SCOLON','MINUS','BSPC' 
    ],
    [
        "F1",'F2','F3','F4','F5','F6','F7','F8','F9','TAB',
        "N1",'N2','N3','N4','N5','N6','N7','N8','N9','N0',
        'F10','F11','F12','BSLASH','GRAVE','SLASH','EQL','LBRC','RBRC','ESC',
        MOLYR,'RCTL','LGUI','RSFT','SPC',______,'LEFT','DOWN','UP','RIGHT' 
    ],

]

if __name__ == '__main__':
    keyboard.go()
