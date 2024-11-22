# -*- coding: utf-8 -*-
"""matplotlib.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k_hlU7lJhrEFsRm4mwECNkpwaRL2LrIz
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 6])
y = np.array([0, 250])

plt.plot(x, y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,6,8])
y = np.array([3,8,1,10])

plt.plot(x, y)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Function to create a single heartbeat
def generate_heartbeat(t):
    heartbeat = (
        0.2 * np.sin(2 * np.pi * (t - 0.1)) * (t > 0.1) * (t <= 0.2) +  # P wave
        -0.15 * np.sin(2 * np.pi * 8 * (t - 0.2)) * (t > 0.2) * (t <= 0.25) +  # Q wave
        1.0 * np.sin(2 * np.pi * 30 * (t - 0.3)) * (t > 0.25) * (t <= 0.35) +  # R wave
        -0.25 * np.sin(2 * np.pi * 8 * (t - 0.4)) * (t > 0.35) * (t <= 0.45) +  # S wave
        0.2 * np.sin(2 * np.pi * (t - 0.5)) * (t > 0.45) * (t <= 0.6)  # T wave
    )
    return heartbeat

# Simulation parameters
time = np.linspace(0, 1, 1000)
heart_rate = 60  # Beats per minute
beats_per_second = heart_rate / 60

# Generate the heart rate graph
ecg_signal = np.tile(generate_heartbeat(time), int(beats_per_second * time.size))

# Plot the heart rate graph
plt.figure(figsize=(12, 4))
plt.plot(time, ecg_signal[:time.size], label='Heartbeat')
plt.title('Human Heart Rate Graph')
plt.xlabel('Time (seconds)')
plt.ylabel('ECG Signal')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

y = np.array([3,8,1,10])

plt.plot(y, 'o:r')
plt.show()

import matplotlib.pyplot as plt

import numpy as np

x1 = np.array([0,1,2,3])

y1 = np.array([3,8,1,10])

x2 = np.array([0,1,2,3])

y2 = np.array([6,2,7,11])

plt.plot(x1,y1,x2,y2)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.piecewise(x, [x < 2, (x >= 2) & (x < 4), x >= 4],
                 [lambda x: 0,
                  lambda x: 1 - (x - 2),
                  lambda x: 0])

plt.plot(x, y, color='red')
plt.title("Tiriklik ko'rsatkichi")
plt.xlabel("Vaqt")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()

import matplotlib.pyplot as plt
import numpy as np
y = np.array([3,8,1,10])
plt.plot(y, marker= 'o', ms= 20,
mec='r')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,1,2,3,4,5])
y = np.array([0,8,12,20,26,38])
plt.scatter(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,1,2,3,4,5])
y = np.array([0,2,8,1,14,7])
plt.scatter(x,y,color='red')
x = np.array([12,6,8,11,8,3])
y = np.array([5,6,3,7,17,19])
plt.scatter(x,y,color='green')
plt.show()

# -*- coding: utf-8 -*-
"""matplotlib.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jCXDhGZ7aXcu-lsW5ZBba1myIHofCbpk
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 6])
y = np.array([0, 250])

plt.plot(x, y)
plt.show()

x = np.array([1, 2, 6, 8])
y = np.array([3, 8, 1, 10])

plt.plot(x, y)
plt.show()

y = np.array([3, 8, 1, 10])

plt.plot(y, marker = 'X')
plt.show()

y = np.array([3, 8, 1, 10])

plt.plot(y, 'X:r')
plt.show()

y = np.array([3, 8, 1, 10])

plt.plot(y, marker = 'X', ms = 20)
plt.show()

x = np.array([45, 20, 20, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(x, labels = mylabels, startangle = 90)
plt.show()

y = np.array([2, 6, 1, 8])

plt.plot(y, marker = 'X', ms = 20, mec = 'r')
plt.show()

x1 = np.array([0, 1, 2, 3])
y1 = np.array([2, 6, 1, 8])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([5, 2, 7, 10])

plt.plot(x1, y1, x2, y2)
plt.show()

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 7, 11, 19, 25, 37])

plt.scatter(x, y)
plt.show()

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 8, 1, 14, 7])
plt.scatter(x, y, color = 'r')

x = np.array([12, 6, 8, 11, 8, 3])
y = np.array([5, 6, 3, 7, 17, 19])
plt.scatter(x, y, color = 'g')
plt.show()

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 8, 1, 13, 7])

mycolor = ['r', 'g', 'b', 'c', 'm', 'y']

plt.scatter(x, y, color = mycolor)
plt.show()

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 8, 1, 13, 7])

mycolor = ['r', 'g', 'b', 'c', 'm', 'y']
size = [10, 60, 120, 80, 20, 190]

plt.scatter(x, y, color = mycolor)
plt.show()

x = np.array(['A', 'B', 'C', 'D'])
y = np.array([2, 6, 3, 8])

plt.bar(x, y)
plt.show()

x = np.array(['A', 'B', 'C', 'D'])
y = np.array([2, 6, 3, 8])

plt.barh(x, y)
plt.show()

x = np.array([45, 20, 20, 15])

plt.pie(x)
plt.show()

x = np.array([45, 20, 20, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(x, labels = mylabels)
plt.show()

x = np.array([45, 20, 20, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(x, labels = mylabels, startangle = 90)
plt.show()

x = np.array([45, 20, 20, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.5, 0, 0, 0]

plt.pie(x, labels = mylabels, startangle = 90, explode = myexplode)
plt.show()

x = np.array([45, 20, 20, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.5, 0, 0, 0]

plt.pie(x, labels = mylabels, startangle = 90, explode = myexplode, shadow = True)
plt.show()

x = np.array([45, 20, 20, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.5, 0, 0, 0]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(x, labels = mylabels, startangle = 90, explode = myexplode, colors = mycolors)
plt.show()

x = np.array([45, 20, 20, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(x, labels = mylabels,)
plt.legend()
plt.show()

x = np.array([45, 20, 20, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(x, labels = mylabels,)
plt.legend(title = 'Four fruits:')
plt.show()