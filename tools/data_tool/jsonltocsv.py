import json
import csv
"""
将jsonl文件转换成csv文件
"""

# 要转换的JSONL文件路径 jsonl_file_path = 'E:\dj_sora_challenge\processed_data_flow_20240709_after.jsonl' jsonl_file_path =
# 'E:/dj_sora_challenge/evalurate_data/filtered_data.jsonl' jsonl_file_path =
# 'E:\dj_sora_challenge\input\data_17628.jsonl' jsonl_file_path =
# 'E:\dj_sora_challenge/evalurate_data/filtered_data_novideo.jsonl' jsonl_file_path = '../data/best_more_0719.jsonl'
# jsonl_file_path = '../data/filtered_data_for_training_better.jsonl' jsonl_file_path = '../data/need_more.jsonl'
# jsonl_file_path = 'E:\dj_sora_challenge\output\processed_data\orange_729.jsonl' jsonl_file_path =
# 'E:\dj_sora_challenge\output\processed_data\merged_orange_tie_bird.jsonl' jsonl_file_path =
# 'E:/dj_sora_challenge/evalurate_data/data/bear_graffe_bird_frisbee.jsonl' jsonl_file_path =
# 'E:/dj_sora_challenge/test/mergedall_data_all731.jsonl' jsonl_file_path =
# 'E:\dj_sora_challenge\more_video\end81_1.jsonl' jsonl_file_path =
# 'E:/dj_sora_challenge/more_video/jsonl/AAAAAA_FLOW1_object.jsonl' sonl_file_path =
# 'E:/dj_sora_challenge/more_video/aes5_object_AAAAAA_FLOW_top5_similar_results_per_query_score_above_0.5.jsonl'
#jsonl_file_path = 'E:/dj_sora_challenge/more_video/aes5_aes55_object_AAAAAA_FLOW5_top5_similar_results_per_query_score_above_0.5.jsonl'
#jsonl_file_path = 'E:/dj_sora_challenge/more_video/jsonl/merged_captions_scene.jsonl'
#jsonl_file_path = 'E:/dj_sora_challenge/more_video/jsonl/2merged_captions_5scene_flow5_similar_results_per_query_score_above_0.5.jsonl'
jsonl_file_path = 'E:/dj_sora_challenge/more_video/jsonl/2merged_captions_5object_flow5_similar_results_per_query_score_above_0.5.jsonl'

# 输出的CSV文件路径
csv_file_path = 'E:/dj_sora_challenge/more_video/2merged_captions_5object_flow5_similar_results_per_query_score_above_0.5.csv'

# 确保使用双反斜杠或原始字符串防止转义字符问题
csv_file_path = csv_file_path.replace('\\', '\\\\')

# 读取JSONL文件，转换数据格式，然后写入CSV文件
with open(jsonl_file_path, 'r', encoding='utf-8') as jsonl_file, \
        open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    # 创建CSV写入器，并指定列标题
    csv_writer = csv.DictWriter(csv_file, fieldnames=['path', 'text'])
    csv_writer.writeheader()  # 写入列标题行

    # 读取JSONL文件中的每一行
    for line in jsonl_file:
        # 解析JSON对象
        json_obj = json.loads(line)

        # 假设json_obj中包含'videos'键，其值是一个列表，列表中包含文件路径
        videos_list = json_obj.get('videos', [])
        if videos_list:  # 确保列表不为空
            file_path = videos_list[0].strip()  # 获取列表中的第一个元素
        else:
            file_path = ''  # 如果列表为空，设置默认为空字符串

        # 假设json_obj中包含'text'键，其值是文本描述
        description = json_obj.get('text', '')
        # 清理文本描述，去除不需要的标记
        cleaned_description = description.replace('<__dj__video>', '').replace('<|__dj__eoc|>', '').strip()

        # 写入转换后的数据到CSV
        csv_writer.writerow({'path': file_path, 'text': cleaned_description})

print("转换完成，结果已保存到", csv_file_path)
