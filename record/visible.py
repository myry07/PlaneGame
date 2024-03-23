import numpy as np
from matplotlib import pyplot as plt

path = "/Users/myry/Documents/MyPythonProject/Games/PlaneGame/record/scores.txt"
scores = np.loadtxt(path, delimiter=" ", dtype=int)
x = range(len(scores))
dimension = 2
x_ = x
x_label = ["{}".format(i) for i in x_]


plt.title("Score for PlaneGame")
plt.xticks(x_[::dimension], x_[::dimension], rotation=45)
plt.plot(x, scores, label="score")
plt.legend()
plt.grid()
plt.show()