import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd
import numpy as np
import random
import serial

#initialize serial port
#ser = serial.Serial()
#ser.port = '/dev/cu.usbmodem1441301' #Arduino serial port
#ser.baudrate = 115200
#ser.timeout = 10 #specify timeout when using readline()
#ser.open()
#if ser.is_open==True:
#	print("\nAll right, serial port now open. Configuration:\n")
#	print(ser, "\n") #print serial parameters

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#xs = [] #store trials here (n)
#ys = [] #store relative frequency here
#rs = [] #for theoretical probability
#chan1 = []
#chan2 = []
#chan3 = []
#chan4 = []
#chan5 = []

# This function is called periodically from FuncAnimation
#def animate(i, xs, ys):
def animate(i):

    #Aquire and parse data from serial port
  #  line=ser.readline()      #ascii
    
    #readchan=ser.readline()
    
    
  #  line_as_list = line.split(b',')
  #  i = int(line_as_list[0])
  #  relProb = line_as_list[1]
  #  relProb_as_list = relProb.split(b'\n')
  #  relProb_float = float(relProb_as_list[0])
	
	# Add x and y to lists
  #  xs.append(i)
  #  ys.append(relProb_float)
  #  rs.append(0.5)
    
    #chan1.append(float(readchan))
    
    #readchan=ser.readline()
    #chan2.append(float(readchan))
    #readchan=ser.readline()
    #chan3.append(float(readchan))
    #readchan=ser.readline()
    #chan4.append(float(readchan))
    #readchan=ser.readline()
    #chan5.append(float(readchan))

    # Limit x and y lists to 20 items
    #xs = xs[-20:]
    #ys = ys[-20:]
    
    data = pd.read_csv('data.csv')
    x = data['x_value']
    chan1 = data['total_1']
    chan2 = data['total_2']

    # Draw x and y lists
    ax.clear()
    ax.plot(x, chan1, label="Experimental Probability")
    ax.plot(x, chan2, label="Other Channel")
  #  ax.plot(xs, rs, label="Theoretical Probability")

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('This is how I roll...')
    plt.ylabel('Relative frequency')
    plt.legend()
    plt.axis([1, None, 0, 2000]) #Use for arbitrary number of trials
    #plt.axis([1, 100, 0, 1.1]) #Use for 100 trial demo

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()