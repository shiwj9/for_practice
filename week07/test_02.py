import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2)

ax[0, 0].plot([1, 2, 3, 4])
ax[0, 1].scatter([1, 2, 3], [4, 5, 6])

plt.show()
