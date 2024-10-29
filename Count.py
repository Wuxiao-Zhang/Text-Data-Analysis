import re
import csv
from collections import Counter


# 统计汉字出现次数的函数
def count_chinese_characters(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        chinese_characters = re.findall(r'[\u4e00-\u9fff]', text)
        character_counts = Counter(chinese_characters)
    return character_counts


# 将结果写入CSV文件的函数
def save_to_csv(character_counts, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name', 'num'])  # 写入表头
        for character, count in character_counts.items():
            writer.writerow([character, count])  # 写入每行的汉字和出现次数


# 文件路径
input_file_path = 'test.txt'      # 请替换为你的文件路径
output_file_path = 'resultOfCount.csv'  # 输出文件路径
counts = count_chinese_characters(input_file_path)
save_to_csv(counts, output_file_path)

print("统计结果已保存到", output_file_path)
