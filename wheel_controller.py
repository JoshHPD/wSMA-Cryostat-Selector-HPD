##
# Selector Wheel Control Client for wSMA
# 11/27/23
# Josh Hirsh
# Formfactor Inc.
##

# imports
from pymodbus.client import ModbusTcpClient

default_IP = "10.104.88.103"

setpoint_addr = 1000

print("Welcome to the selector wheel control client\
\n\nPlease enter one of th following commands:\
\n\"connect\" -> to connect to the controller (run once after power up)\
\n\"pos1\" -> for position 1\
\n\"pos2\" -> for position 2\
\n\"pos3\" -> for position 3\
\n\"pos4\" -> for position 4\
\n\"home\" -> for home sequeance\
\n\"off\" -> power off the motor\
\n\"on\" -> power on the motor")

while True:
    cmd = str(input("command:"))
    match cmd:
        case "connect" :
            client = ModbusTcpClient(default_IP)
            print("connected")
        case "pos1" :
            client.write_registers(setpoint_addr, 1)
        case "pos2" :
            client.write_registers(setpoint_addr, 2)
        case "pos3" :
            client.write_registers(setpoint_addr, 3)
        case "pos4" :
            client.write_registers(setpoint_addr, 4)
        case "home" :
            client.write_registers(setpoint_addr, 5)
        case "off" :
            client.write_registers(setpoint_addr, 6)
        case "on"  :
            client.write_registers(setpoint_addr, 7)
        case _ :
            print("invalide command")



