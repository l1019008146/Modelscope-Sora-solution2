import pandas as pd


# 读取CSV文件
df = pd.read_csv('E:\dj_sora_challenge\more_video\/all\/test-aes-processed_flow.csv')

# 假设'flow'列是我们要分析的列
scores = df['flow']

# 计算统计数据
min_score = scores.min()
max_score = scores.max()
average_score = scores.mean()
percentile_1 = scores.quantile(0.75)
median_score = scores.median()
percentile_3 = scores.quantile(0.85)
desc_stats = scores.describe()
# 打印统计数据
print(f"最小值: {min_score}")
print(f"最大值: {max_score}")
print(f"平均分: {average_score}")
print(f"75%分位数: {percentile_1}")
print(f"中位数: {median_score}")
print(f"85%分位数: {percentile_3}")
print("描述性统计信息:")
print(desc_stats)