import subprocess

def run():
    path=f'C:\\Program Files (x86)\\teraterm\\ttermpro.exe'
    comport=18
    Baudrate=115200
    process=subprocess.Popen(f'{path} /C={comport} /BAUD={Baudrate}',stdout=subprocess.PIPE, text=True)

run()