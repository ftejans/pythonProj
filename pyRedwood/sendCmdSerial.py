import time
import serial
from serial import SerialException

# Define the serial port and baud rate.
serialPortName  = 'COM10'
baudRate    = 115200
byteSize    = 8
parityBit   = 'N'
stopBit     = 1


def portIsUsable(portName):
    try:
       ser = serial.Serial(port=portName)
       return True
    except:
       return False
    

try:
        if portIsUsable(serialPortName):
                ser=serial.Serial(serialPortName, baudRate, byteSize, parityBit, stopBit)
                print(f"Serial port {serialPortName} is open. Sending command...")

                #Set MODULATION ON
                cmd='CONF:SETUP:MODULATION ON\n' 
                ser.write(cmd.encode())
                print(f"Mod ON Command sent: {cmd.encode('utf-8').rstrip()}")
                time.sleep(1)

                #Set RF ON
                cmd='CONF:SETUP:RF ON\n' 
                ser.write(cmd.encode())            
                print(f"RF ON Command sent: {cmd.encode('utf-8').rstrip()}")
                time.sleep(5)

                #Set MODULATION OFF
                cmd='CONF:SETUP:MODULATION OFF\n'    
                ser.write(cmd.encode())            
                print(f"Mod OFF Command sent: {cmd.encode('utf-8').rstrip()}")
                time.sleep(1)

                #Set RF OFF
                cmd='CONF:SETUP:RF OFF\n' 
                ser.write(cmd.encode())            
                print(f"RF OFF Command sent: {cmd.encode('utf-8').rstrip()}")
                time.sleep(5)
        

except Exception as e:
        print(f"Error: {str(e)}")

finally:
        #Close the serial connection
        if ser.is_open:
                ser.close()
                print("Serial port closed.")