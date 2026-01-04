# 第一周快速入门：线性代数基础

## 欢迎开始ML数学之旅！

第一周的目标很简单：**理解向量和矩阵的几何意义**，掌握基本运算。

记住：重点是**直觉理解**，不是记公式！

---

## 开始前的准备（30分钟）

### 第0天：环境搭建

**今天就完成这些：**

1. **安装Python和必要库（15分钟）**
   ```bash
   # 如果已有Python，安装这些库
   pip install numpy matplotlib jupyter
   ```
   - NumPy：矩阵运算
   - Matplotlib：可视化
   - Jupyter：交互式编程

2. **下载学习资料（10分钟）**
   - [ ] 下载MML Book PDF：https://mml-book.github.io/book/mml-book.pdf
   - [ ] 订阅3Blue1Brown YouTube频道
   - [ ] 准备笔记本（纸质或电子）

3. **创建学习文件夹（5分钟）**
   ```bash
   mkdir ml-math-learning
   cd ml-math-learning
   mkdir week1 week2 week3 ...
   ```

4. **测试环境**
   ```python
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
   ```

**环境搭建完成！✓**

---

## Day 1：向量是什么？（1.5小时）

### 目标
理解向量的**几何直觉** - 向量就是空间中的箭头！

### 学习计划

**1. 观看视频（20分钟）**
- [ ] 3Blue1Brown - "Vectors, what even are they?"
  - 链接：https://www.youtube.com/watch?v=fNk_zzaMoSs
  - 重点：向量的物理学视角 vs 计算机科学视角

**2. 阅读教材（30分钟）**
- [ ] MML Book Chapter 2.1-2.2（向量定义和运算）
- 重点理解：
  - 向量 = 有方向和大小的量
  - 向量加法的几何意义（首尾相连）
  - 数乘的几何意义（伸缩）

**3. 动手实践（30分钟）**

创建文件：`week1/day1_vectors.py`

```python
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
plt.savefig('week1/day1_vectors.png')
plt.show()
```

**4. 练习题（10分钟）**
- Khan Academy - Vectors练习（3-5道题）
- 或者手动计算：
  - v = [2, 3], w = [1, -1]，求 v + w, v - w, 3v

**今日检查：**
- [ ] 理解向量的几何意义
- [ ] 能用NumPy创建向量
- [ ] 能可视化向量
- [ ] 保存了今天的代码

**今日笔记：**
用自己的话解释：什么是向量？为什么向量加法要"首尾相连"？

---

## Day 2：向量的大小和方向（1.5小时）

### 目标
理解向量的**长度（范数）**和**点积**

### 学习计划

**1. 观看视频（15分钟）**
- [ ] 3Blue1Brown - 继续昨天的视频，或搜索"dot product intuition"

**2. 阅读+理解（30分钟）**
- [ ] 复习MML Book Ch2.1-2.2
- 学习新概念：
  - 向量长度（范数）：||v|| = √(v₁² + v₂²)
  - 点积：v · w = v₁w₁ + v₂w₂
  - 点积的几何意义：v · w = ||v|| ||w|| cos(θ)

**3. 动手实践（40分钟）**

创建文件：`week1/day2_dot_product.py`

```python
import numpy as np
import matplotlib.pyplot as plt

# 1. 向量长度
v = np.array([3, 4])
length_v = np.linalg.norm(v)
print(f"向量v: {v}")
print(f"长度: {length_v}")  # 应该是5（3-4-5直角三角形）

# 手动计算验证
manual_length = np.sqrt(v[0]**2 + v[1]**2)
print(f"手动计算长度: {manual_length}")

# 2. 单位向量（长度为1的向量）
unit_v = v / length_v
print(f"单位向量: {unit_v}")
print(f"单位向量长度: {np.linalg.norm(unit_v)}")

# 3. 点积
w = np.array([2, 1])
dot_product = np.dot(v, w)
print(f"v · w = {dot_product}")

# 手动计算
manual_dot = v[0]*w[0] + v[1]*w[1]
print(f"手动计算点积: {manual_dot}")

# 4. 计算夹角
cos_theta = dot_product / (np.linalg.norm(v) * np.linalg.norm(w))
theta_rad = np.arccos(cos_theta)
theta_deg = np.degrees(theta_rad)
print(f"夹角: {theta_deg:.2f}度")

# 5. 可视化
plt.figure(figsize=(10, 5))

# 左图：向量长度
plt.subplot(1, 2, 1)
plt.arrow(0, 0, v[0], v[1], head_width=0.3, color='blue', linewidth=2)
# 画出长度（斜边）
plt.plot([0, v[0]], [0, 0], 'r--', label='水平分量')
plt.plot([v[0], v[0]], [0, v[1]], 'g--', label='垂直分量')
plt.plot([0, v[0]], [0, v[1]], 'purple', linewidth=3, label=f'长度={length_v:.1f}')
plt.grid()
plt.legend()
plt.title('向量长度')
plt.xlim(-1, 5)
plt.ylim(-1, 5)

# 右图：点积和夹角
plt.subplot(1, 2, 2)
plt.arrow(0, 0, v[0], v[1], head_width=0.3, color='blue', linewidth=2, label='v')
plt.arrow(0, 0, w[0], w[1], head_width=0.3, color='red', linewidth=2, label='w')
plt.text(1.5, 2.5, f'v · w = {dot_product}', fontsize=12)
plt.text(1.5, 2, f'夹角 = {theta_deg:.1f}°', fontsize=12)
plt.grid()
plt.legend()
plt.title('点积和夹角')
plt.xlim(-1, 5)
plt.ylim(-1, 5)

plt.tight_layout()
plt.savefig('week1/day2_dot_product.png')
plt.show()
```

**4. 练习（5分钟）**
手动计算：
- v = [1, 0], w = [0, 1]，求点积和夹角（应该是90度）
- v = [1, 1], w = [1, 1]，求点积和夹角（应该是0度）

**今日检查：**
- [ ] 理解向量长度的计算
- [ ] 理解点积的几何意义
- [ ] 知道点积为0意味着垂直

**今日笔记：**
点积的物理意义是什么？为什么垂直时点积为0？

---

## Day 3：矩阵基础（1.5小时）

### 目标
理解矩阵 = **向量的集合** = **线性变换的编码**

### 学习计划

**1. 观看视频（15分钟）**
- [ ] 3Blue1Brown - "Linear combinations, span, and basis vectors"
  - https://www.youtube.com/watch?v=k7RM-ot2NWY

**2. 阅读（30分钟）**
- [ ] MML Book Ch2.3（矩阵定义）
- 理解：
  - 矩阵 = 数字的矩形数组
  - 矩阵的维度：m×n（m行n列）
  - 矩阵转置

**3. 动手实践（40分钟）**

创建文件：`week1/day3_matrices.py`

```python
import numpy as np

# 1. 创建矩阵
A = np.array([
    [1, 2],
    [3, 4]
])
print("矩阵A:")
print(A)
print(f"形状: {A.shape}")  # (2, 2)

# 2. 创建不同形状的矩阵
B = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("\n矩阵B (2x3):")
print(B)

# 3. 矩阵加法
C = np.array([
    [5, 6],
    [7, 8]
])
A_plus_C = A + C
print("\nA + C:")
print(A_plus_C)

# 4. 数乘
scaled_A = 2 * A
print("\n2 * A:")
print(scaled_A)

# 5. 矩阵转置
A_T = A.T
print("\nA的转置:")
print(A_T)

# 6. 特殊矩阵
# 零矩阵
zeros = np.zeros((3, 3))
print("\n零矩阵:")
print(zeros)

# 单位矩阵（对角线为1）
I = np.eye(3)
print("\n单位矩阵:")
print(I)

# 7. 理解矩阵的列向量
print("\nA的列向量:")
col1 = A[:, 0]  # 第一列
col2 = A[:, 1]  # 第二列
print(f"第一列: {col1}")
print(f"第二列: {col2}")

# 可视化列向量
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.arrow(0, 0, col1[0], col1[1], head_width=0.2, color='blue', linewidth=2, label='列1')
plt.arrow(0, 0, col2[0], col2[1], head_width=0.2, color='red', linewidth=2, label='列2')
plt.grid()
plt.legend()
plt.title('矩阵A的列向量')
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('week1/day3_matrix_columns.png')
plt.show()
```

**4. 练习**
手动写出下列矩阵：
- 3×3单位矩阵
- 2×3零矩阵
- 矩阵[[1,2],[3,4]]的转置

**今日检查：**
- [ ] 理解矩阵的定义
- [ ] 能用NumPy创建各种矩阵
- [ ] 理解矩阵的列可以看作向量

**今日笔记：**
矩阵和向量有什么关系？

---

## Day 4-5：矩阵乘法（最重要！）（每天1.5小时）

### Day 4目标
理解矩阵乘法的**计算方法**

### 学习计划

**1. 观看视频（20分钟）**
- [ ] 3Blue1Brown - "Matrix multiplication as composition"
  - https://www.youtube.com/watch?v=XkY2DOUCWMU
  - **这个视频超级重要！** 看2遍！

**2. 阅读（40分钟）**
- [ ] MML Book Ch2.4（矩阵乘法）
- 理解：
  - 矩阵乘法 ≠ 逐元素相乘
  - (A × B)ᵢⱼ = A的第i行 · B的第j列
  - 乘法顺序很重要：AB ≠ BA

**3. 手动计算（30分钟）**

拿出纸笔，手算这个：
```
A = [1  2]    B = [5  6]
    [3  4]        [7  8]

计算 A × B = ?
```

步骤：
1. 结果的第(1,1)元素 = A的第1行 · B的第1列 = 1×5 + 2×7 = 19
2. 结果的第(1,2)元素 = A的第1行 · B的第2列 = 1×6 + 2×8 = 22
3. ... 继续算完4个元素

**4. 用NumPy验证**

创建文件：`week1/day4_matrix_mult.py`

```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# 矩阵乘法
C = A @ B  # 或 np.dot(A, B)
print("A × B =")
print(C)

# 验证：AB ≠ BA
C_reverse = B @ A
print("\nB × A =")
print(C_reverse)

print("\nAB 是否等于 BA?", np.array_equal(C, C_reverse))

# 验证手动计算
print("\n手动验证:")
print(f"C[0,0] = 1×5 + 2×7 = {1*5 + 2*7}")
print(f"C[0,1] = 1×6 + 2×8 = {1*6 + 2*8}")
# ... 等等
```

**今日检查：**
- [ ] 能手算2×2矩阵乘法
- [ ] 理解AB ≠ BA
- [ ] 能用NumPy做矩阵乘法

---

### Day 5目标
理解矩阵乘法的**几何意义** - 线性变换！

**1. 重看视频（30分钟）**
- [ ] 再看一遍3Blue1Brown的矩阵乘法视频
- 重点：矩阵乘法 = 依次施加线性变换

**2. 动手实践（1小时）**

创建文件：`week1/day5_transform.py`

```python
import numpy as np
import matplotlib.pyplot as plt

# 1. 原始向量
v = np.array([1, 0])
w = np.array([0, 1])

# 2. 变换矩阵（旋转90度）
A = np.array([[0, -1],
              [1,  0]])

# 3. 应用变换
v_transformed = A @ v
w_transformed = A @ w

print(f"原始v: {v} -> 变换后: {v_transformed}")
print(f"原始w: {w} -> 变换后: {w_transformed}")

# 4. 可视化
plt.figure(figsize=(10, 5))

# 左图：原始
plt.subplot(1, 2, 1)
plt.arrow(0, 0, v[0], v[1], head_width=0.1, color='blue', linewidth=2, label='v')
plt.arrow(0, 0, w[0], w[1], head_width=0.1, color='red', linewidth=2, label='w')
plt.grid()
plt.legend()
plt.title('原始向量')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

# 右图：变换后
plt.subplot(1, 2, 2)
plt.arrow(0, 0, v_transformed[0], v_transformed[1], head_width=0.1, color='blue', linewidth=2, label='A*v', linestyle='--')
plt.arrow(0, 0, w_transformed[0], w_transformed[1], head_width=0.1, color='red', linewidth=2, label='A*w', linestyle='--')
plt.grid()
plt.legend()
plt.title('旋转90度后')
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

plt.tight_layout()
plt.savefig('week1/day5_rotation.png')
plt.show()
```

**3. 实验不同的变换矩阵**

试试这些矩阵，看看它们做了什么变换：
```python
# 缩放2倍
scale = np.array([[2, 0],
                  [0, 2]])

# 只在x方向缩放
scale_x = np.array([[2, 0],
                    [0, 1]])

# 剪切变换
shear = np.array([[1, 1],
                  [0, 1]])
```

**今日检查：**
- [ ] 理解矩阵乘法 = 线性变换
- [ ] 能可视化变换效果
- [ ] 理解为什么AB ≠ BA（变换顺序不同）

---

## Day 6：巩固练习（1.5小时）

### 目标
通过编程练习巩固本周所学

### 综合练习项目

创建文件：`week1/day6_practice.py`

```python
import numpy as np
import matplotlib.pyplot as plt

"""
练习1：向量运算
"""
def practice_vectors():
    v = np.array([3, 4])
    w = np.array([1, 2])

    # TODO: 计算
    # 1. v + w
    # 2. v - w
    # 3. 2*v + 3*w
    # 4. ||v||（长度）
    # 5. v · w（点积）
    # 6. v和w的夹角

    # 可视化结果
    pass

"""
练习2：矩阵运算
"""
def practice_matrices():
    A = np.array([[1, 2],
                  [3, 4]])
    B = np.array([[2, 0],
                  [1, 3]])

    # TODO: 计算
    # 1. A + B
    # 2. A × B
    # 3. B × A
    # 4. A²（A × A）
    # 5. A的转置

    pass

"""
练习3：线性变换
"""
def visualize_transformation(matrix, title):
    """可视化矩阵变换效果"""
    # 创建网格点
    x = np.linspace(-2, 2, 10)
    y = np.linspace(-2, 2, 10)
    X, Y = np.meshgrid(x, y)

    # 原始点
    points = np.vstack([X.ravel(), Y.ravel()])

    # 变换后的点
    transformed = matrix @ points

    # 绘图
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(points[0], points[1], alpha=0.5)
    plt.title('原始')
    plt.grid()
    plt.axis('equal')

    plt.subplot(1, 2, 2)
    plt.scatter(transformed[0], transformed[1], alpha=0.5)
    plt.title(f'变换后: {title}')
    plt.grid()
    plt.axis('equal')

    plt.show()

# 测试不同的变换
rotation_90 = np.array([[0, -1],
                        [1,  0]])
visualize_transformation(rotation_90, '旋转90度')

# 自己定义更多变换矩阵并测试！
```

**挑战题：**
1. 写一个函数，输入角度θ，输出旋转θ度的变换矩阵
   提示：旋转矩阵 = [[cos θ, -sin θ], [sin θ, cos θ]]

2. 验证：(AB)ᵀ = BᵀAᵀ（转置的性质）

**今日检查：**
- [ ] 完成所有练习
- [ ] 能独立写出矩阵运算代码
- [ ] 理解每个运算的几何意义

---

## Day 7：周总结和回顾（2小时）

### 目标
系统回顾第一周，准备第二周

### 活动清单

**1. 重看3Blue1Brown系列（40分钟）**
- [ ] 快速复习本周看过的所有视频
- 这次应该理解得更深了！

**2. 整理笔记（40分钟）**
创建文件：`week1/week1_summary.md`

写下：
- 向量的3个要点
- 矩阵乘法的几何意义
- 本周最难理解的概念（以及你怎么理解的）
- 3个关键公式
- 给未来的自己：下周要记住的事

**3. 创建思维导图（30分钟）**
用纸笔或工具（如XMind）画出：
```
向量和矩阵
  ├── 向量
  │   ├── 几何意义：箭头
  │   ├── 运算：加法、数乘
  │   ├── 长度（范数）
  │   └── 点积
  ├── 矩阵
  │   ├── 定义：数字数组
  │   ├── 特殊矩阵：零矩阵、单位矩阵
  │   └── 转置
  └── 矩阵乘法
      ├── 计算方法
      ├── 几何意义：线性变换
      └── 性质：AB ≠ BA
```

**4. 完成检查清单**
在《ML数学学习记录.md》中：
- [ ] 填写第1周的所有复选框
- [ ] 记录学习时长
- [ ] 写下本周反思

**5. 预习第2周（10分钟）**
快速浏览：
- MML Book Ch2.5-2.6（线性变换）
- 3Blue1Brown下一集视频标题

---

## 第一周检查清单

### 知识点掌握
- [ ] 理解向量的几何意义（箭头）
- [ ] 能手算向量加法、数乘、点积
- [ ] 理解矩阵 = 向量的集合
- [ ] 能手算2×2矩阵乘法
- [ ] **关键**：理解矩阵乘法 = 线性变换
- [ ] 理解为什么AB ≠ BA

### 编程技能
- [ ] 能用NumPy创建向量和矩阵
- [ ] 能用NumPy进行各种矩阵运算
- [ ] 能用Matplotlib可视化向量
- [ ] 能可视化线性变换的效果

### 学习习惯
- [ ] 每天坚持学习1-1.5小时
- [ ] 做了笔记
- [ ] 保存了所有代码
- [ ] 在学习记录表打卡

---

## 常见问题

### Q: 第一周感觉好难，跟不上怎么办？
**A:** 很正常！不要急：
1. 重点是理解**直觉**，不是记公式
2. 多看几遍3Blue1Brown视频
3. Day 1-3慢慢来，确保理解了再继续
4. 可以延长到2周完成第一周内容

### Q: 矩阵乘法的几何意义还是不懂？
**A:**
1. 把3Blue1Brown的视频看3遍
2. 动手画图：画出变换前后的向量
3. 用代码可视化不同的变换矩阵
4. 记住：矩阵 = 一种变换，矩阵乘法 = 连续变换

### Q: 为什么要学这些？和ML有什么关系？
**A:**
- 神经网络 = 一堆矩阵乘法！
- 数据 = 向量/矩阵
- 训练模型 = 优化矩阵参数
- 第10周你会看到所有联系！

### Q: NumPy代码不会写怎么办？
**A:**
- NumPy官方教程：https://numpy.org/doc/stable/user/quickstart.html
- 多运行示例代码，改改参数看效果
- Google: "numpy how to [你想做的事]"

---

## 激励自己

### 第一周感言

**你已经完成了最重要的一步 - 开始！**

线性代数是ML数学的核心，理解向量和矩阵的几何意义，后面的学习会容易很多。

**记住：**
- 不要追求完美，理解80%就很好了
- 几何直觉比公式推导重要
- 动手实践比看视频重要
- 坚持10周，你会蜕变！

**本周最重要的领悟：**
> 矩阵不是抽象的数字表格，而是空间变换的编码！

---

## 下周预告

**第2周：线性变换和行列式**

你将学会：
- 深入理解线性变换
- 行列式的几何意义（超酷！）
- 逆矩阵和求解线性方程组

剧透：行列式 = 变换后面积的缩放因子！

---

## 快速参考

### 常用NumPy命令
```python
# 创建
v = np.array([1, 2, 3])
A = np.array([[1, 2], [3, 4]])

# 运算
v + w              # 向量加法
2 * v              # 数乘
np.dot(v, w)       # 点积
A @ B              # 矩阵乘法
A.T                # 转置

# 属性
np.linalg.norm(v)  # 向量长度
A.shape            # 矩阵形状

# 特殊矩阵
np.zeros((3, 3))   # 零矩阵
np.eye(3)          # 单位矩阵
```

### 公式速查
- 向量长度：||v|| = √(v₁² + v₂² + ...)
- 点积：v · w = Σ vᵢwᵢ = ||v|| ||w|| cos θ
- 矩阵乘法：(AB)ᵢⱼ = Σₖ AᵢₖBₖⱼ

---

**开始第一周的学习吧！🚀**

Remember: "Understanding beats memorization!"
