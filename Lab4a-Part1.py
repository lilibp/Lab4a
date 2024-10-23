from machine import Pin
import time

# define GPIO pins for shift register control
DS = Pin(20, Pin.OUT)
SHCP = Pin(18, Pin.OUT)
STCP = Pin(19, Pin.OUT)
OE = Pin(21, Pin.OUT)

# LED configurations for each light
off = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
east_car = [[1,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
west_green = [[0,1,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
west_yellow = [[0,0,1,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
west_red = [[0,0,0,1], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
north_car = [[0,0,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]
south_green = [[0,0,0,0], [0,1,0,0], [0,0,0,0], [0,0,0,0]]
south_yellow = [[0,0,0,0], [0,0,1,0], [0,0,0,0], [0,0,0,0]]
south_red = [[0,0,0,0], [0,0,0,1], [0,0,0,0], [0,0,0,0]]
west_car = [[0,0,0,0], [0,0,0,0], [1,0,0,0], [0,0,0,0]]
east_green = [[0,0,0,0], [0,0,0,0], [0,1,0,0], [0,0,0,0]]
east_yellow = [[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,0]]
east_red = [[0,0,0,0], [0,0,0,0], [0,0,0,1], [0,0,0,0]]
south_car = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [1,0,0,0]]
north_green = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,1,0,0]]
north_yellow = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,1,0]]
north_red = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,1]]


def shift_register_output(light_settings):
    # Shift out 16 bits to the shift register
    for direction in light_settings:
        for bit in direction :
            # shift in all of the traffic light control bit values
            DS.value(bit)
            # Clock line
            SHCP.value(1) 
            SHCP.value(0) 
    STCP.value(1)   # latch the 16 bit value (stored into memory)
    STCP.value(0)
    OE.off()

shift_register_output(east_car)
print("East white light is on\n")
time.sleep(1)
shift_register_output(west_green)
print("West green light is on\n")
time.sleep(1)
shift_register_output(west_yellow)
print("West yellow light is on\n")
time.sleep(1)
shift_register_output(west_red)
print("West red light is on\n")
time.sleep(1)

shift_register_output(north_car)
print("North white light is on\n")
time.sleep(1)
shift_register_output(south_green)
print("South green light is on\n")
time.sleep(1)
shift_register_output(south_yellow)
print("South yellow light is on\n")
time.sleep(1)
shift_register_output(south_red)
print("South red light is on\n")
time.sleep(1)

shift_register_output(west_car)
print("West white light is on\n")
time.sleep(1)
shift_register_output(east_green)
print("East green light is on\n")
time.sleep(1)
shift_register_output(east_yellow)
print("East yellow light is on\n")
time.sleep(1)
shift_register_output(east_red)
print("East red light is on\n")
time.sleep(1)

shift_register_output(south_car)
print("South white light is on\n")
time.sleep(1)
shift_register_output(north_green)
print("North green light is on\n")
time.sleep(1)
shift_register_output(north_yellow)
print("North yellow light is on\n")
time.sleep(1)
shift_register_output(north_red)
print("North red light is on\n")
time.sleep(1)

shift_register_output(off)


