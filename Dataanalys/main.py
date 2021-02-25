# Mathias, Carl, Linus (190s)

import matplotlib.pyplot as plt

f = open("data.csv", "r")
data = f.read()
dataSplit = data.split('\n')

i = []
x = []
y = []
z = []

average = []
time = []
average2 = []
time2 = []

for values in dataSplit:
    value = values.split(',')
    i.append(float(value[0]) - 1567068324355)
    x.append(float(value[1]))
    y.append(float(value[2]))
    z.append(float(value[3]))

for x in range(4, len(i) - 5):
    smoothing_number = (y[x-5] + y[x-4] + y[x-3] + y[x-2] + y[x-1] + y[x] + y[x+1] + y[x+2] + y[x+3] + y[x+4] + y[x+5])/11
    average.append(float(smoothing_number))
    time.append(i[x])

for x in range(4, len(average) - 5):
    smoothing_number = (average[x-5] + average[x-4] + average[x-3] + average[x-2] + average[x-1] + average[x] + average[x+1] + average[x+2] + average[x+3] + average[x+4] + average[x+5])/11
    average2.append(float(smoothing_number))
    time2.append(i[x])

plt.plot(i, y)
plt.plot(time2, average2)
plt.ylabel('acceleration')
plt.xlabel('time')
plt.show()