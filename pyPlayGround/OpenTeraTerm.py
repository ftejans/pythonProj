import os
from pywinauto import application


############ Change path to Teraterm root folder #################################

out=os.getcwd()
print("Current working directory is:", out)
path = os.chdir('C:/Program Files (x86)/teraterm')
out=os.getcwd()
print("Current working directory is:", out)

############ Start Teraterm ###########################
app = application.Application()
app.start("ttermpro.exe")
a=app.windows()[0]

################### Autostart Macro to allow user to select DSC dump script #######################

app.VTWin32.draw_outline()
app.VTWin32.menu_select("Control -> Macro")