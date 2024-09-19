import pandas as pd

# 读取CSV文件
df = pd.read_csv('E:/dj_sora_challenge/more_video/all/meta_time_cut_videos_all_flow.csv')

# 筛选'flow'列大于5.0的数据
filtered_df = df[df['flow'] > 5.0]

# 将筛选后的数据保存到新的CSV文件
filtered_df.to_csv('E:/dj_sora_challenge/more_video/all/meta_time_cut_videos_all_flow_5.0.csv', index=False)
print('Done!')