########################### Remote Programming Guide ############################
## ● Set Serial                                                                ##
## ● Set up Baud Rate, Parity Bit (None), Data Bit (8 bit), Stop Bit (1 bit).  ##
## ● Open port.                                                                ##     
## ● Send RS232C command through serial port.                                  ##
## ● Check command execution results on the RWC2010C screen.                   ##
## ● Send the next command after successful execution of the previous command. ##
#################################################################################
##Inital release: July 08, 2024
## Added by Filjun Tejano (UIDR8208)


############## Basic Command for RWC2010C Digital Radio Tester ##################
## [Command]                            [<value>]           [Description]
## CONF:SETUP:RF <value>                OFF, ON             RF On/Off
## CONF:SETUP:MODULATION <value>        OFF, ON             RF On/Off
## CONF:SETUP:FREQUENCY <value>         0.15 ~ 30 MHz       LF/MF/HF Band
## ..............................       47 ~ 68 MHz         Band I
## ..............................       87 ~ 108 MHz        Band II
## ..............................       174 ~ 250 MHz       Band III
## CONF:SETUP:TESTER_MODE <value>       FM, AM, DAB,        -
## ..............................       DRM, ETI, MDI,      -
## ..............................       DRM_IQ              -
## CONF:DAB:ENSEMBLE:CHANNEL <val_1>    EU_5A ~ EU_13F      EUROPE ensemble                
## CONF:DAB:ENSEMBLE:CH_TYPE <val_1>    EUROPE, KOREA       -                              
## EXEC:REBOOT                                              Reboot Tester
## 
## 
## 
## 
##################################################################################

############################## Tips for programming ##############################
##  ● A colon is used between commands
##  ● A space is only used between parameter values and commands
##  ● All commands should be finished by LF (Line Feed, char(10))
##################################################################################



import serial

# Set Parameters base from Redwood(Serial Port,  Baud Rate, Parity Bit (None), Data Bit (8 bit), Stop Bit (1 bit))
serialPort  = 'COM10'
baudRate    = 115200
byteSize    = 8
parityBit   = 'N'
stopBit     = 1

#Configure data
cfgData=serial.Serial(serialPort, baudRate, byteSize, parityBit, stopBit)

#Send command to serial port via user input
while True:
    cmd=input('Please enter your command: ')
    cmd=cmd+'\r'
    cfgData.write(cmd.encode())




