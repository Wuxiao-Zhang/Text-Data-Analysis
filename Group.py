import pandas as pd

# 读取原始 CSV 文件
df = pd.read_csv('top_1000_words.csv')

# 定义分组字典，每个分组对应的字词列表
groups = {
    "自然": ["山", "水", "草", "月", "云", "风", "雨", "花", "柳", "雪", "春风", "白云", "明月", "天", "鸟", "秋风", "树", "青山", "白日", "霜"],
    "情感": ["悲", "思", "喜", "愁", "怨", "笑", "爱", "恨", "惆怅", "惊", "相思", "寂寞", "哭", "急", "乐", "叹", "寂寥", "忧", "茫茫", "伤"],
    "地点及方位": ["长安", "洛阳", "都", "西", "东", "南", "蜀", "城", "家", "门", "上", "下", "中", "里", "后", "前", "外", "山中", "楼", "天涯"],
    "人物": ["人", "君", "王", "妾", "子", "客", "谁", "我", "白居易", "杜甫", "李白", "故人", "刘禹锡", "齐己", "使君", "少年", "孟郊", "元稹", "韩愈", "陆龟蒙"],
    "时间": ["日", "夜", "时", "年", "朝", "久", "月", "春", "秋", "今日", "暮", "岁", "今", "旧", "宿", "早", "春日", "今朝", "从此", "此时"],
    "形容": ["更", "新", "长", "老", "深", "旧", "高", "空", "清", "难", "满", "寒", "闲", "久", "白", "红", "晚", "香", "绿", "碧"],
    "物品与建筑": ["书", "钱", "寺", "门", "棹", "阙", "黄金", "弦", "玉", "城", "楼", "郊庙", "剑", "舟", "船", "帐", "草堂", "辇", "郭", "樽"],
    "思念": ["人", "月", "谁", "欲", "相思", "别", "梦", "故人", "闻", "辞", "旧", "柳", "杨柳", "忆", "独", "思", "回首", "别离", "情", "乡"],
    "战争": ["还", "人", "无", "归", "将", "酒", "空", "行", "和", "回", "生", "死", "无人", "阙", "骑", "将军", "城", "乱", "君王", "剑"],
    "动作": ["去", "归", "送", "见", "来", "寄", "到", "看", "听", "赠", "坐", "飞", "望", "回", "醉", "问", "歌", "梦", "游", "说"]
}

# 遍历每个分组
for group_name, words in groups.items():
    # 过滤出当前组的字词
    group_df = df[df['name'].isin(words)]

    # 如果分组有匹配的字词，保存到对应的 CSV 文件
    if not group_df.empty:
        group_df.to_csv(f'{group_name}.csv', index=False, encoding='utf-8-sig')
        print(f"{group_name} 分组的字词统计已保存到 {group_name}.csv 文件中。")
