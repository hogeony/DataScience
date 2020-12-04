# reference => https://www.statstodo.com/CombineMeansSDs_Pgm.php
import numpy as np

# n, mean, std of each dataset
n_mean_std = [[10, 11.8, 2.4],
              [20, 15.3, 3.2],
              [15, 8.4, 4.1]]

n_mean_std = np.array(n_mean_std)

n_sum = n_mean_std[:, 0].sum()
x_sum = (n_mean_std[:, 0] * n_mean_std[:, 1]).sum()
x_squared_sum = ((n_mean_std[:, 2] ** 2) * (n_mean_std[:, 0] - 1) + (n_mean_std[:, 0] * n_mean_std[:, 1]) ** 2 / n_mean_std[:, 0]).sum()

n_total = n_sum
mean_total = x_sum / n_total
std_total = np.sqrt((x_squared_sum - (x_sum ** 2) / n_sum) / (n_sum - 1))
print(n_mean_std)
print(n_total, mean_total, std_total)

# [[10.  11.8  2.4]
#  [20.  15.3  3.2]
#  [15.   8.4  4.1]]
# 45.0 12.222222222222221 4.502821786436149
