from matplotlib.pyplot import *
from fuzzylab import *

# Plot HRC
x = np.linspace(10, 70, 1000)
soft = trapmf(x, [10, 10, 20, 30])
medium = trapmf(x, [20, 30, 50, 60])
hard = trapmf(x, [50, 60, 70, 70])
plot(x, soft, label='soft')
plot(x, medium, label='medium')
plot(x, hard, label='hard')
legend(loc='best')
xlabel('HRC')
savefig('img/hardness.png')
show()

# Plot thickness
x = np.linspace(1, 50, 1000)
thin = trapmf(x, [1, 1, 3, 5])
medium = trapmf(x, [3, 5, 10, 20])
thick = trapmf(x, [10, 20, 50, 50])
plot(x, thin, label='thin')
plot(x, medium, label='medium')
plot(x, thick, label='thick')
legend(loc='best')
xlabel('mm')
savefig('img/thickness.png')
show()

# Cutting force
x = np.linspace(0, 15000000, 1000)
weak = trapmf(x, [0, 0, 4e6, 5e6])
medium = trapmf(x, [4e6, 5e6, 10e6, 11e6])
strong = trapmf(x, [10e6, 11e6, 15e6, 15e6])
plot(x, weak, label='weak')
plot(x, medium, label='medium')
plot(x, strong, label='strong')
legend(loc='best')
xlabel('N')
savefig('img/force.png')
show()
