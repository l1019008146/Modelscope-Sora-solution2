import csv
import json
import os

def process_csv_to_jsonl(input_csv, output_jsonl):
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_jsonl), exist_ok=True)

    with open(input_csv, 'r', encoding='utf-8') as csv_file, \
         open(output_jsonl, 'w', encoding='utf-8') as jsonl_file:
        
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            # 构建输出数据结构
            output_data = {
                "videos": [row['path']],
                "text": f"<__dj__video> {row['text']} <|__dj__eoc|>"
            }
            
            # 将数据写入JSONL文件
            json.dump(output_data, jsonl_file, ensure_ascii=False)
            jsonl_file.write('\n')

    print(f"处理完成。输出文件：{output_jsonl}")

# 使用示例
input_csv = "E:\dj_sora_challenge\more_video\merged_captions_scene_flow_1.0.csv"
output_jsonl = "E:\dj_sora_challenge\more_video\jsonl\merged_captions_scene_flow_1.0.jsonl"

process_csv_to_jsonl(input_csv, output_jsonl)