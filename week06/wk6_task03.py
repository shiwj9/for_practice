import pandas as pd

# （1）探索2012欧洲杯数据(导入“data.csv”文件)
# （2）将数据集命名为euro12
euro12 = pd.read_csv('data.csv')

# （3）只选取并输出 Goals 这一列
print(euro12['Goals'])

# （4）有多少球队参与了2012欧洲杯？
print(f"有多少球队参与了2012欧洲杯？{len(euro12['Team'].unique())}")

# （5）该数据集中一共有多少列(columns)?
print(f"数据集中一共有{len(euro12.columns)}列")

# （6）将数据集中的列Team, Yellow Cards和Red Cards单独存为一个名叫discipline的数据框
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]

# （7）对数据框discipline按照先Red Cards再Yellow Cards进行排序
discipline_sorted = discipline.sort_values(by=['Red Cards', 'Yellow Cards'])
print(discipline_sorted)

# （8）计算每个球队拿到的黄牌数的平均值
yellow_cards_avg = euro12['Yellow Cards'].mean()
print(f"每个球队拿到的黄牌数的平均值:{yellow_cards_avg}")

# （9）找到进球数Goals超过6的球队数据
goals_over_6 = euro12[euro12['Goals'] > 6]
print("进球数Goals超过6的球队数据:")
print(goals_over_6)

# （10）选取以字母G开头的球队数据
teams_starting_with_G = euro12[euro12['Team'].str.startswith('G')]
print("以字母G开头的球队数据:")
print(teams_starting_with_G)

# （11）选取前7列
first_7_columns = euro12.iloc[:, :7]
print("前7列:")
print(first_7_columns)

# （12）选取除了最后3列之外的全部列
except_last_3_columns = euro12.iloc[:, :-3]
print("除了最后3列之外的全部列:")
print(except_last_3_columns)

# （13）找到英格兰(England)、意大利(Italy)和俄罗斯(Russia)的射正率(Shooting Accuracy)
shooting_accuracy = euro12[euro12['Team'].isin(['England', 'Italy', 'Russia'])][['Team', 'Shooting Accuracy']]
print("英格兰(England)、意大利(Italy)和俄罗斯(Russia)的射正率(Shooting Accuracy):")
print(shooting_accuracy)
