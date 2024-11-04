import numpy as np
import matplotlib.pyplot as plt


F = 2000
L = 1

E = 200000000000
d = 0.10 #10cm de diametre
Igz = np.pi * d*d*d*d/64

c3 = -F*L*L/2
c4 = F*L*L*L/6

les_x1 = np.linspace(0,1,100)
les_x2 = np.linspace(1,2,100)
les_y1 = F*les_x1*les_x1*(les_x1-3*L)/6
les_y2 = c3*les_x2+c4



les_x = np.concatenate((les_x1,les_x2))
les_y = np.concatenate((les_y1,les_y2))

plt.plot(les_x,les_y/E/Igz*1000)
plt.plot(les_x1,les_y1/E/Igz*1000)
plt.show()