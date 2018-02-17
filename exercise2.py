import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5.,5.,500)
fig, ax = plt.subplots()
ax.plot(x,np.sqrt(np.abs(x))*np.sin(x*x))
plt.show()
