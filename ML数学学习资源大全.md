# ML数学学习资源大全

这里汇总了学习机器学习数学的所有推荐资源，分类整理，方便查找。

---

## 📚 核心教材

### 1. Mathematics for Machine Learning (MML Book) ⭐⭐⭐⭐⭐
- **作者**: Marc Peter Deisenroth, A. Aldo Faisal, Cheng Soon Ong
- **免费PDF**: https://mml-book.github.io/book/mml-book.pdf
- **官网**: https://mml-book.github.io/
- **优点**:
  - 专为ML设计，不讲无关的数学
  - 从基础到应用，循序渐进
  - 配有Python练习
- **适合**: 初学者到中级
- **使用建议**: 作为主教材，配合视频学习

### 2. Deep Learning Book
- **作者**: Ian Goodfellow, Yoshua Bengio, Aaron Courville
- **免费在线**: https://www.deeplearningbook.org/
- **重点章节**:
  - Ch2: Linear Algebra
  - Ch3: Probability
  - Ch4: Numerical Computation
- **适合**: 有一定基础后深入学习
- **使用建议**: 第二遍学习时参考

---

## 🎥 视频课程（最重要！）

### 线性代数

#### 3Blue1Brown - Essence of Linear Algebra ⭐⭐⭐⭐⭐
- **YouTube播放列表**: https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
- **时长**: 约3小时（15个视频）
- **特点**:
  - 最好的数学可视化
  - 直觉理解优先
  - 动画精美，解释清晰
- **必看集数**:
  1. Vectors, what even are they?
  2. Linear combinations, span, and basis
  3. Matrix multiplication as composition
  4. The determinant
  5. Inverse matrices, column space and null space
  6. Eigenvectors and eigenvalues ⭐最重要！
- **学习建议**: 每集看2-3遍，第一遍理解，第二遍做笔记

#### MIT 18.06 Linear Algebra by Gilbert Strang
- **YouTube**: https://www.youtube.com/playlist?list=PL49CF3715CB9EF31D
- **课程网站**: https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/
- **时长**: 完整学期课程（~35讲）
- **特点**: 经典课程，深入系统
- **适合**: 想要深入理解线性代数
- **使用建议**: 作为进阶参考，不必全看

#### Khan Academy - Linear Algebra
- **网站**: https://www.khanacademy.org/math/linear-algebra
- **特点**: 交互式练习，适合打基础
- **适合**: 完全零基础
- **使用建议**: 用来做练习题

---

### 微积分

#### 3Blue1Brown - Essence of Calculus ⭐⭐⭐⭐⭐
- **YouTube播放列表**: https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr
- **时长**: 约3小时（12个视频）
- **必看集数**:
  1. The essence of calculus
  2. The paradox of the derivative
  3. Derivative formulas through geometry
  4. Chain rule and product rule ⭐关键！
  5. Implicit differentiation
- **学习建议**: 理解导数的直觉，链式法则是重点

#### Khan Academy - Calculus
- **网站**: https://www.khanacademy.org/math/calculus-1
- **适合**: 练习基本求导技巧

---

### 概率与统计

#### StatQuest with Josh Starmer ⭐⭐⭐⭐⭐
- **YouTube频道**: https://www.youtube.com/c/joshstarmer
- **特点**:
  - 解释清晰，幽默风趣
  - 适合完全零基础
  - 每个视频5-15分钟，碎片化学习
- **必看视频**:
  1. Probability vs Likelihood
  2. Bayes' Theorem
  3. Covariance and Correlation
  4. The Central Limit Theorem
  5. Bias and Variance
  6. Gradient Descent
  7. Stochastic Gradient Descent
- **学习建议**: 当作休闲学习，很轻松

#### Khan Academy - Statistics and Probability
- **网站**: https://www.khanacademy.org/math/statistics-probability
- **适合**: 系统学习概率统计基础

---

### 综合课程

#### Andrew Ng - Machine Learning (Coursera)
- **链接**: https://www.coursera.org/learn/machine-learning
- **特点**:
  - 会复习必要的数学（线性代数、微积分基础）
  - 结合ML应用讲解数学
  - 编程作业巩固理解
- **适合**: 边学数学边学ML
- **使用建议**: Week 1-3重点看数学部分

#### Andrew Ng - Deep Learning Specialization
- **链接**: https://www.coursera.org/specializations/deep-learning
- **第一门课**: Neural Networks and Deep Learning
  - Week 2: 神经网络基础（矩阵运算、梯度下降）
  - Week 3: 浅层神经网络（反向传播推导）
- **适合**: 学完基础数学后，看如何应用

---

## 📖 在线资源和博客

### 可视化和交互式学习

#### Immersive Math ⭐⭐⭐⭐
- **网站**: http://immersivemath.com/ila/index.html
- **特点**: 交互式线性代数教材，可以拖动图形
- **内容**: 线性代数全覆盖
- **使用建议**: 理解几何直觉的好工具

#### Distill.pub
- **网站**: https://distill.pub/
- **特点**: 高质量机器学习文章，可视化优秀
- **推荐文章**:
  - "Attention and Augmented Recurrent Neural Networks"
  - "Feature Visualization"
- **适合**: 进阶学习

#### The Matrix Cookbook
- **PDF**: https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf
- **特点**: 矩阵运算速查手册
- **使用建议**: 当字典用，需要时查

---

### 优质博客

#### Colah's Blog ⭐⭐⭐⭐
- **网站**: https://colah.github.io/
- **推荐文章**:
  - "Understanding LSTM Networks"
  - "Neural Networks, Manifolds, and Topology"
  - "Visualizing Representations"
- **特点**: 深度好文，可视化出色

#### Jay Alammar's Blog ⭐⭐⭐⭐
- **网站**: https://jalammar.github.io/
- **推荐文章**:
  - "The Illustrated Transformer"
  - "The Illustrated Word2vec"
  - "A Visual Intro to NumPy"
- **特点**: 图解清晰，适合视觉学习者

#### Better Explained
- **网站**: https://betterexplained.com/
- **推荐文章**:
  - "An Intuitive Guide to Linear Algebra"
  - "Vector Calculus: Understanding the Dot Product"
  - "Intuitive Understanding of Euler's Formula"
- **特点**: 用类比解释数学概念

---

## 💻 编程工具和实践

### Python库

#### NumPy ⭐⭐⭐⭐⭐
- **官网**: https://numpy.org/
- **文档**: https://numpy.org/doc/stable/
- **教程**:
  - 官方快速入门: https://numpy.org/doc/stable/user/quickstart.html
  - NumPy for MATLAB users: https://numpy.org/doc/stable/user/numpy-for-matlab-users.html
- **重点掌握**:
  - 数组创建和索引
  - 线性代数操作 (np.linalg)
  - 广播(broadcasting)
  - 数值计算

#### SciPy
- **官网**: https://scipy.org/
- **用途**: 科学计算（优化、积分、统计）
- **线性代数**: scipy.linalg（比NumPy功能更多）

#### Matplotlib ⭐⭐⭐⭐
- **官网**: https://matplotlib.org/
- **教程**: https://matplotlib.org/stable/tutorials/index.html
- **用途**: 可视化数学概念
- **重点**:
  - 基本绘图（plot, scatter）
  - 向量绘制（arrow, quiver）
  - 3D绘图（mplot3d）

#### SymPy
- **官网**: https://www.sympy.org/
- **用途**: 符号数学（自动求导、积分）
- **适合**: 验证手动推导

---

### 在线编程平台

#### Google Colab ⭐⭐⭐⭐⭐
- **网站**: https://colab.research.google.com/
- **特点**:
  - 免费GPU/TPU
  - 预装ML库
  - 云端运行，无需配置
- **使用建议**: 做练习和项目的首选

#### Kaggle Notebooks
- **网站**: https://www.kaggle.com/code
- **特点**: 免费GPU，数据集丰富
- **适合**: 实践项目

#### Jupyter Notebook
- **安装**: `pip install jupyter`
- **优点**: 本地运行，交互式编程
- **使用建议**: 本地学习首选

---

## 📝 练习平台

### Khan Academy ⭐⭐⭐⭐
- **网站**: https://www.khanacademy.org/
- **科目**: 线性代数、微积分、统计
- **特点**:
  - 交互式练习
  - 即时反馈
  - 进度跟踪
- **使用建议**: 每天做10道题巩固

### MIT OpenCourseWare
- **网站**: https://ocw.mit.edu/
- **课程**:
  - 18.06 Linear Algebra (有习题和解答)
  - 18.01 Single Variable Calculus
- **特点**: MIT原版习题
- **使用建议**: 想要挑战可以做MIT习题

### Coursera课程作业
- **Andrew Ng课程**: 自带编程作业
- **特点**: 结合ML应用的数学练习
- **使用建议**: 必做！

---

## 📱 移动App

### Wolfram Alpha
- **网站**: https://www.wolframalpha.com/
- **App**: iOS/Android都有
- **用途**:
  - 计算矩阵运算
  - 求解方程
  - 绘制函数图像
  - 验证答案
- **示例查询**:
  - "eigenvalues of {{1,2},{3,4}}"
  - "derivative of x^2 * sin(x)"
  - "plot y = x^2"

### Desmos Graphing Calculator
- **网站**: https://www.desmos.com/calculator
- **App**: iOS/Android都有
- **用途**: 函数可视化
- **特点**:
  - 交互式绘图
  - 可以拖动参数
  - 分享图表
- **使用建议**: 可视化函数和导数

### Photomath
- **App**: iOS/Android
- **用途**: 拍照解题，显示步骤
- **适合**: 检查手算答案

---

## 📚 补充书籍

### 线性代数

#### "Linear Algebra Done Right" - Sheldon Axler
- **级别**: 中级
- **特点**: 概念优先，少计算
- **适合**: 想深入理解线性代数

#### "Introduction to Linear Algebra" - Gilbert Strang
- **配套**: MIT 18.06课程
- **特点**: 应用导向，讲解清晰
- **适合**: 系统学习

#### "Coding the Matrix" - Philip Klein
- **特点**: 用Python学线性代数
- **适合**: 程序员背景

---

### 微积分

#### "Calculus Made Easy" - Silvanus Thompson
- **特点**: 通俗易懂，入门经典
- **免费**: 公共领域，可免费下载
- **适合**: 完全零基础

#### "The Calculus Lifesaver" - Adrian Banner
- **特点**: 学生视角，详细讲解
- **适合**: 自学微积分

---

### 概率统计

#### "All of Statistics" - Larry Wasserman
- **特点**: 简洁，覆盖ML需要的统计
- **级别**: 中级
- **适合**: 快速掌握统计概念

#### "Introduction to Probability" - Dimitri Bertsekas, John Tsitsiklis
- **配套**: MIT 6.041课程
- **特点**: 严谨但可读
- **适合**: 系统学习概率

---

## 🎓 大学课程（OCW）

### MIT OpenCourseWare ⭐⭐⭐⭐⭐
- **18.06 Linear Algebra**: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- **18.01 Calculus**: https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/
- **6.041 Probability**: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/

### Stanford Online
- **CS229 Machine Learning**: http://cs229.stanford.edu/
  - 附有数学复习材料
- **CS231n CNN**: http://cs231n.stanford.edu/
  - 有很好的数学推导

---

## 🛠️ 实用工具

### 数学工具

#### LaTeX数学公式
- **在线编辑器**: https://www.overleaf.com/
- **学习**: https://www.overleaf.com/learn/latex/Mathematical_expressions
- **使用建议**: 写笔记时用LaTeX记公式

#### GeoGebra
- **网站**: https://www.geogebra.org/
- **用途**: 几何和代数可视化
- **特点**: 交互式图形计算器

#### MATLAB/Octave
- **Octave**: https://www.gnu.org/software/octave/
- **特点**: MATLAB开源替代品
- **适合**: 数值计算和可视化

---

## 🌟 学习路径推荐

### 快速路径（6-8周）
1. **Week 1-2**: 3Blue1Brown线性代数 + MML Ch2
2. **Week 3-4**: 3Blue1Brown微积分 + MML Ch5
3. **Week 5-6**: StatQuest概率 + MML Ch6
4. **Week 7-8**: 实战项目（从零实现LR, LogR, PCA）

### 系统路径（10-12周）
按照《ML数学基础学习计划.md》的10周计划，配合：
- MML Book作为主教材
- 3Blue1Brown/StatQuest作为视频讲解
- Khan Academy作为练习平台
- Google Colab作为编程平台

### 深入路径（3-6个月）
1. MIT 18.06完整课程（线性代数）
2. Stanford CS229数学部分
3. Deep Learning Book Ch2-4
4. 实现经典ML算法并理解数学原理

---

## 🔍 如何查找资源

### YouTube搜索技巧
- "linear algebra intuition"
- "matrix multiplication visualization"
- "gradient descent explained"
- "backpropagation derivation"

### Google搜索技巧
- "understanding [概念] intuitively"
- "[概念] geometric interpretation"
- "visualizing [概念]"
- "[概念] for machine learning"

### Reddit社区
- r/learnmachinelearning
- r/MachineLearning
- r/math
- r/learnmath

---

## 💡 学习建议

### 资源使用策略
1. **主教材**: MML Book（系统学习）
2. **直觉理解**: 3Blue1Brown（可视化）
3. **快速参考**: StatQuest（概念速记）
4. **动手练习**: Google Colab（编程实践）
5. **习题**: Khan Academy（巩固基础）

### 不要陷入的坑
- ❌ 囤积资源不学习
- ❌ 看完所有视频才动手
- ❌ 追求数学证明的完美理解
- ❌ 只看不练
- ✅ 选1-2个主要资源，坚持学完
- ✅ 边学边练，边学边用
- ✅ 重视直觉理解
- ✅ 每天1-2小时，持续10周

---

## 📌 快速链接汇总

### 必看视频（按优先级）
1. 3Blue1Brown - Essence of Linear Algebra
2. 3Blue1Brown - Essence of Calculus
3. StatQuest - Machine Learning/Statistics系列

### 必读教材
1. Mathematics for Machine Learning (MML Book)
2. Deep Learning Book (Ch2-4)

### 必备工具
1. Google Colab / Jupyter Notebook
2. NumPy + Matplotlib
3. Wolfram Alpha

### 必做练习
1. Khan Academy每日练习
2. MML Book习题
3. Andrew Ng课程作业

---

## 🎯 按主题快速查找

### 我想学...

**线性代数几何直觉**
→ 3Blue1Brown线性代数系列

**如何用Python做矩阵运算**
→ NumPy官方教程 + Jay Alammar的NumPy可视化

**贝叶斯定理的直觉理解**
→ 3Blue1Brown贝叶斯定理视频 + Better Explained博客

**梯度下降的原理**
→ StatQuest梯度下降系列 + Andrew Ng课程Week 1

**反向传播的数学推导**
→ Andrew Ng DL专项课程 + CS231n讲义

**概率分布的可视化**
→ StatQuest + Seeing Theory网站(https://seeing-theory.brown.edu/)

---

**祝你学习顺利！记得收藏这个资源列表！** 🚀
