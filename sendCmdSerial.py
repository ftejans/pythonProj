import serial

# Define the serial port and baud rate.
port = 'com10'
baud_rate = 9600    #match this with your device baud rate


try:
        if serial.is_open:
                print(f"Serial port {port} is open. Sending command...")

                #Example cmmand to send
                command = b'LED_ON\r\n'     #Example command to turn on an LED


                #Send the command
                serial.write(command)
                print(f"Commmand sent: {command.decode('utf-8').rstrip()}")

except Exception as e:
        print(f"Error: {str(e)}")

finally:
        #Close the serial connection
        if serial.is_open:
                serial.close()
                print("Serial port closed.")