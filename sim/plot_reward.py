import matplotlib.pyplot as plt
import numpy as np

LOG_PATH = './results/log_test'

epochs = []
mean_rewards = []

with open(LOG_PATH, 'r') as f:
  lines = f.readlines()
  for line in lines:
    data = line.split()
    # add epoch as int and mean reward as float
    epochs.append(int(data[0]))
    mean_rewards.append(float(data[3]))


def moving_average(input_list, window_size):
    if len(input_list) < window_size:
        return []

    moving_averages = []
    window_sum = sum(input_list[:window_size])
    moving_averages.append(window_sum / window_size)

    for i in range(window_size, len(input_list)):
        window_sum = window_sum - input_list[i - window_size] + input_list[i]
        moving_averages.append(window_sum / window_size)

    return moving_averages

window_size = 100
mean_rewards = moving_average(mean_rewards, window_size)

plt.plot(epochs[:-window_size+1], mean_rewards)
plt.xlabel('Epochs')
plt.ylabel('Mean Reward')
plt.title('Mean Reward vs Epochs')
plt.savefig('./mean_reward.png')
