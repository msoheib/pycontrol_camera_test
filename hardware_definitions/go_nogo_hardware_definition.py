# This hardware definition specifies that 3 pokes are plugged into ports 1-3 and a speaker into
# port 4 of breakout board version 1.2.  The houselight is plugged into the center pokes solenoid socket.

from devices import *
from devices.rotary_encoder import Rotary_encoder

board = Breakout_1_2()

# Instantiate Devices.
#lick   = Poke(board.port_1, name='running_wheel', sampling_rate=100)


#port_1
lick   = Digital_input(board.port_1.DIO_A, rising_event = 'lick_port1', debounce=5)

#port_2
horizontal = Digital_output(board.port_2.DIO_A)

#port_3
vertical = Digital_output(board.port_3.DIO_A)

#port 4
photodetector_port_4 = Digital_input(board.port_4.DIO_A, rising_event = 'photodetector_port_4', debounce=5)

#enable for the base
#bnc1   = Digital_output(board.BNC_1)

# Instantiate analog input on BNC connector BNC_1.
bnc_1_speed = Analog_input(pin=board.BNC_1, name='Speed', sampling_rate=1000)

# Instantiate analog input on BNC connector BNC_2.
bnc_2_dir = Analog_input(pin=board.BNC_2, name='Direction', sampling_rate=1000)


#bnc1   = Digital_output(board.BNC_1)

dac_1_reward = Digital_output(board.DAC_1)

dac_2_trigger_PV = Digital_output(board.DAC_2)


#lick = Digital_input('X17', rising_event='lick', pull='up') # pyboard usr button.
LED    = Digital_output('B4') 
