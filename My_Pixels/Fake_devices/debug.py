
# import subprocess
# subprocess.call("test.sh")

import os
# os.system('adb shell am broadcast -a com.yama.fake.ADBCom --es id "S1123555ABABABBB55" --es lat "50.08593724592065" --es lng "36.21560508169411"')
os.system('adb shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings')
os.system('adb shell input tap 800 100')
os.system('adb shell input keyevent 4')
os.system('')
os.system('')