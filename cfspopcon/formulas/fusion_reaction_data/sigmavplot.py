import reaction_rate_coefficients as rrc

temperature =25 # keV

DHE3 = rrc.sigmav_DHe3(temperature)
DD = rrc.sigmav_DD(temperature) 
DT = rrc.sigmav_DT(temperature)
print("DD: ", DD)
print("DT: ", DT)
print("DHe3: ", DHE3)

"""
#plot the function for a range of temperatures
import numpy as np
import matplotlib.pyplot as plt
temperatures = np.linspace(1, 100, 10)
for temperature in temperatures:
    DHE3 = rrc.sigmav_DHe3(temperature)
    DD = rrc.sigmav_DD(temperature) 
    DT = rrc.sigmav_DT(temperature)
    plt.plot(temperature, DD[0], 'ro')
    plt.plot(temperature, DT, 'bo')
    plt.plot(temperature, DHE3, 'go')
    plt.xlabel('Temperature (keV)')
    plt.ylabel('Reaction rate coefficient')
    plt.yscale('log')
    plt.xticks(np.arange(0, 100, 5))
    plt.title('Reaction rate coefficient vs temperature')
    plt.grid(True)
    plt.legend(['DD', 'DT', 'DHe3'])
plt.show()
"""