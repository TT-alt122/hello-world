import numpy as np
import matplotlib.pyplot as plt

# 绘制连续的余弦信号
t_continuous = np.linspace(0, 10, 1000)
y_continuous = np.cos(t_continuous)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t_continuous, y_continuous)
plt.title('连续余弦信号')
plt.xlabel('时间')
plt.ylabel('幅值')

# 绘制离散的阶跃信号
t_discrete = np.arange(0, 10)
y_discrete = np.heaviside(t_discrete - 5, 1)

plt.subplot(1, 2, 2)
plt.stem(t_discrete, y_discrete)
plt.title('离散阶跃信号')
plt.xlabel('时间')
plt.ylabel('幅值')

plt.tight_layout()
plt.show()
    