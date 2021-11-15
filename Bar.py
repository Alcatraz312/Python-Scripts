import matplotlib.pyplot as plt
import numpy as np 
x = [[1,2,3,4],[5,4,6,7],[8,7,5,6]]
s = np.arange(1,15,4)
plt.bar(s , x[0], color = "r")
plt.bar(s + 1 , x[1] , color = "g")
plt.bar(s+2 , x[2], color = "b")
plt.title("Bars")
plt.xlim(-2,18)
plt.show()