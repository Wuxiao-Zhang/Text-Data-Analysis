import jieba
from collections import Counter
import csv

# 读取文件内容
file_path = '全唐诗.txt'  # 替换为你的txt文件路径
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# 使用 jieba 分词并过滤出汉字或中文短语
words = [word for word in jieba.cut(text) if all('\u4e00' <= char <= '\u9fff' for char in word)]

# 统计出现次数
word_counts = Counter(words)

# 获取出现次数前1000的词汇
top_1000 = word_counts.most_common(1000)

# 将结果写入CSV文件
csv_file_path = 'top_1000_words.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['name', 'num'])  # 写入表头
    writer.writerows(top_1000)  # 写入数据

print(f"结果已保存到 {csv_file_path}")
