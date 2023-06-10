# Import modules
from pyControl.utility import *
import hardware_definition as hw
from pyControl.utility import *
from devices import *

import time


# Define states
states = ['pretrial',
          'stimuli_horizontal',
          'stimuli_vertical',
          'go_response_window',
          'nogo_response_window',
          'reward', 
          'punishment'] 

# Define initial state
initial_state = 'pretrial'

# Define events
events = ['lick_port1', 
          'horizontal', 
          'vertical',
          'dac_1_reward',
          'dac_2_trigger_PV',
          'photodetector_port_4',
          'reward_dispensed_dac2'
          ]

# Define variables

variables = {'trial_number': 0,
             'trials_to_run': 100, # 100 trials
             'go_stimulus': 0, 
             'n_reward': 10, 
             'punishment_duration': 5, 
             'session_duration': 3600} 

# api variable
v.api_class = 'go_nogo_learning'
#v.api_class = 'Blinker'

# State behaviour

#the pretrial event randomly selects the stimuli to be presented
def pretrial(event):
    hori_or_vert = ["stimuli_horizontal", "stimuli_vertical"]
    select = choice(hori_or_vert) 
    timed_goto_state(select, 5*second) 

#the stimuli_horizontal event presents a horizontal stimulus
def stimuli_horizontal(event):
    if event == "entry":
        hw.horizontal.on()
        time.sleep(0.005)
        hw.horizontal.off()
        publish_event('horizontal')
        timed_goto_state('go_response_window', 5*second) # Go to the

    elif event == "exit":
        hw.horizontal.off()

#the stimuli_vertical event presents a vertical stimulus
def stimuli_vertical(event):
    if event == "entry":
        hw.vertical.on()
        time.sleep(0.005)
        hw.vertical.off()
        publish_event('vertical')
        timed_goto_state('nogo_response_window', 5*second) # Go to the

    elif event == "exit":
        hw.vertical.off()

#the go_response_window event is the response window for the go stimulus
def go_response_window(event):
    if event == "lick_port1":
        goto_state('reward')
    timed_goto_state('punishment', 5*second)

#the nogo_response_window event is the response window for the nogo stimulus
def nogo_response_window(event):
    if event == "lick_port1":
        goto_state('punishment')
    timed_goto_state('reward', 5*second)

#the reward event delivers a rewardx
def reward(event):
    if event == "entry":
        hw.LED.toggle()
        #first pulse to start
        time.sleep(0.005)
        hw.dac_1_reward.on()
        time.sleep(0.005)
        hw.dac_1_reward.off()
        #second pulse to stop
        time.sleep(0.5)
        hw.dac_1_reward.on()
        time.sleep(0.005)
        hw.dac_1_reward.off()
    elif event == "exit":
        hw.LED.toggle()
    timed_goto_state('pretrial', 5*second)

#the punishment event delivers a punishment
def punishment(event):
    timed_goto_state('pretrial', 20*second)

