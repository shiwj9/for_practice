import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
from seaborn import load_dataset
import pandas as pd

# 设置字体为 SimHei 显示中文标签，(Windows 系统)
rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# (1) 绘制简单图形（箱线图）  # 加载 iris 数据集(由于无法连接，已直接通过GitHub下载到本地)
iris = load_dataset('iris')

# 绘制箱线图，以种类为x轴，花萼长度为y轴（这里需要稍微调整代码）
plt.figure(figsize=(10, 6))
sns.boxplot(x='sepal_length', data=iris, color='lightblue')
plt.title('花萼长度箱线图示例')
plt.xlabel('鸢尾花种类')
plt.ylabel('花萼长度（cm）')
plt.savefig('boxplot_seaborn.png')
plt.show()

# (2) 绘制复杂图形（热力图）
print(iris.dtypes)
numeric_cols = iris.columns[:-1]  # 选择除了最后一列之外的所有列
# 计算数值列的相关性矩阵
corr_matrix = iris[numeric_cols].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Iris 数据集特征相关性热力图')
plt.savefig('complex_plot_seaborn.png')
plt.show()

# (3) 鸢尾花数据分析
# 绘制条形图展示不同鸢尾花种类的花萼长度分布情况
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 假设 iris 是一个已经加载好的包含鸢尾花数据的 Pandas DataFrame
# iris = sns.load_dataset('iris')  # 如果您还没有加载数据

# 离散化花萼长度数据
bins = [0, 4, 5, 6, 7, 8]  # 定义区间边界
iris['sepal_length_bin'] = pd.cut(iris['sepal_length'], bins=bins, labels=False)

# 计算每个种类和长度区间的数量
count_df = iris.groupby(['species', 'sepal_length_bin']).size().unstack(fill_value=0)

# 绘制条形图
count_df.plot(kind='bar', stacked=False, width=0.8, alpha=0.7)  # stacked=False 表示不堆叠
plt.title('不同鸢尾花种类的花萼长度分布情况（近似）')
plt.xlabel('鸢尾花种类')
plt.ylabel('数量')
plt.xticks(rotation=0)  # 旋转x轴标签以便更清晰地显示
plt.legend(title='花萼长度区间')
plt.tight_layout()  # 自动调整子图参数, 使之填充整个图像区域
plt.savefig('barplot_seaborn.png')
plt.show()

# 绘制散点图展示sepal_length和petal_length之间的相关性，并区分不同的鸢尾花种类
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=iris, palette='viridis')
plt.title('Sepal Length vs Petal Length 散点图')
plt.xlabel('花萼长度（cm）')
plt.ylabel('花瓣长度（cm）')
plt.legend(title='鸢尾花种类')
plt.savefig('scatter_seaborn.png')
plt.show()
