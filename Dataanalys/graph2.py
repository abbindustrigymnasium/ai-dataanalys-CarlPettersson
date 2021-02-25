# Mathias, Carl, Linus (190s)

import matplotlib.pyplot as plt
import json


while True:
    filename = str(input('Vilken fil vill du öppna? '))
    try:
        with open(filename + ".csv", "r") as f:
            data = f.read()
            dataSplit = data.split('\n')
        break
    except:
        print(filename +' existerar inte.')
del dataSplit[-1]

x = []
y = []
xDiff = []
yDiff = []
ti = 0
time = []
average = []

for values in dataSplit:
    value = values.split(',')
    x.append(int(value[0]))
    y.append(int(value[1]))

for q in range(0, len(x)-1):
    Xdifference = x[q]-x[q+1]
    # if Xdifference < 0:
    #     Xdifference = Xdifference *-1
    xDiff.append(Xdifference)

for w in range(0, len(y)-1):
    Ydifference = y[w]-y[w+1]
    # if Ydifference < 0:
    #     Ydifference = Ydifference *-1
    yDiff.append(Ydifference)

for z in range(0, len(x)-1):
    ti += 10
    time.append(ti)

# for a in range(4, len(x) - 5):
#     smoothing_number = (y[a-5] + y[a-4] + y[a-3] + y[a-2] + y[a-1] + y[a] + y[a+1] + y[a+2] + y[a+3] + y[a+4] + y[a+5])/11
#     average.append(float(smoothing_number))
#     time.append(x[a])

# for x in range(4, len(average) - 5):
#     smoothing_number = (average[x-5] + average[x-4] + average[x-3] + average[x-2] + average[x-1] + average[x] + average[x+1] + average[x+2] + average[x+3] + average[x+4] + average[x+5])/11
#     average2.append(float(smoothing_number))
#     time2.append(i[x])

plt.plot(x, y)
plt.ylabel('hastighet')
plt.xlabel('time')
plt.show()