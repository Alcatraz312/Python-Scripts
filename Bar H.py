import matplotlib.pyplot as plt 
import numpy as np 
v = [[1,2,3,4],[5,3,10,8],[8,9,11,13]]
x = np.arange(1,15,4)
plt.barh(x ,v[0]  , color = "b")
plt.barh(x +1 , v[1]  , color = "g")
plt.barh(x +2, v[2]  , color = "r")
plt.show()

