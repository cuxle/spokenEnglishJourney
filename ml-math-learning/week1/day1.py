import numpy as np
import matplotlib.pyplot as plt

# 1. 创建向量
v = np.array([3, 2])
w = np.array([1, 3])

print(f"向量v: {v}")
print(f"向量w: {w}")

# 2. 向量加法
v_plus_w = v + w
print(f"v + w = {v_plus_w}")

# 3. 数乘
scaled_v = 2 * v
print(f"2 * v = {scaled_v}")

# 4. 可视化
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# 图1：两个向量
ax[0].arrow(0, 0, v[0], v[1], head_width=0.2, color='blue', label='v')
ax[0].arrow(0, 0, w[0], w[1], head_width=0.2, color='red', label='w')
ax[0].grid()
ax[0].legend()
ax[0].set_title('向量 v 和 w')
ax[0].set_xlim(-1, 5)
ax[0].set_ylim(-1, 5)

# 图2：向量加法
ax[1].arrow(0, 0, v[0], v[1], head_width=0.2, color='blue', alpha=0.5)
ax[1].arrow(v[0], v[1], w[0], w[1], head_width=0.2, color='red', alpha=0.5)
ax[1].arrow(0, 0, v_plus_w[0], v_plus_w[1], head_width=0.2, color='green', linewidth=2, label='v+w')
ax[1].grid()
ax[1].legend()
ax[1].set_title('向量加法：v + w')
ax[1].set_xlim(-1, 6)
ax[1].set_ylim(-1, 6)

# 图3：数乘
ax[2].arrow(0, 0, v[0], v[1], head_width=0.2, color='blue', alpha=0.5, label='v')
ax[2].arrow(0, 0, scaled_v[0], scaled_v[1], head_width=0.2, color='purple', linewidth=2, label='2*v')
ax[2].grid()
ax[2].legend()
ax[2].set_title('数乘：2 * v')
ax[2].set_xlim(-1, 8)
ax[2].set_ylim(-1, 8)

plt.tight_layout()
plt.savefig('day1_vectors.png')
plt.show()