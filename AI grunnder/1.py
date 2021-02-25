import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
from collections import Counter
style.use("fivethirtyeight")

# def eucdist(goalplot, plot):
#     euc = sqrt((plot[0]-goalplot[0])**2 + (plot[1]-goalplot[1])**2)
#     print(euc)
#     plt.scatter(plot[0], plot[1], s=100)


# plot = [1, 3]
# goalplot = [2, 5]
# plt.scatter(goalplot[0], goalplot[1], s=150)
# eucdist(goalplot, plot)
# plot2 = [4, 7]
# eucdist(goalplot, plot2)

# eucdist(goalplot, goalplot)
# plt.show()

dataset = {"k": [[2, 5], [4, 1], [6, 5]], "g": [
    [3, 2], [6, 3], [4, 5]], "r": [[5, 5], [7, 7], [8, 6]]}

dataset = {
    "Hus": [[35, 35], [37, 37], [42, 32], [60, 34], [63, 36], [61, 35], [65, 22], [76, 16]],
    "Hyresrätt": [[23, 12], [26, 33], [28, 20], [19, 6], [97, 9]],
    "BostadsRätt": [[57, 45], [24, 28], [26, 30]],
    "Radhus": [[37, 21], [45, 47], [32, 42], [55, 24], [61, 25]]
}

new_feature = [42, 23]


def knearest(data, predict, k=4):
    if len(data) >= k:
        warnings.warn("k is set to lower than total known number of groups")
    distance = []

    for group in data:
        for feature in data[group]:
            euclidianDistance = np.linalg.norm(
                np.array(feature) - np.array(predict))
            distance.append([euclidianDistance, group])

    votes = [i[1] for i in sorted(distance)[:k]]
    print(Counter(votes).most_common(1))
    voteResult = Counter(votes).most_common(1)[0][0]
    return voteResult


result = knearest(dataset, new_feature, k=4)

print(result)

colors = {"Hus": "r", "Hyresrätt": "b", "BostadsRätt": "g", "Radhus": "k"}
[[plt.scatter(ii[0], ii[1], color=colors[i])
  for ii in dataset[i]] for i in dataset]
plt.scatter(new_feature[0], new_feature[1], s=100)
plt.ylabel("Inkomst")
plt.xlabel("Ålder")

plt.show()
