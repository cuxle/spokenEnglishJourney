import numpy as np
import matplotlib.pyplot as plt

# 创建一个简单向量
v = np.array([3, 2])
print(f"向量v: {v}")
print(f"向量长度: {np.linalg.norm(v)}")

# 绘制向量
plt.arrow(0, 0, v[0], v[1], head_width=0.3, color='blue')
plt.grid()
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.show()