import random

# ダミーの選手名リスト（日本人風の名前を50人分用意）
names = [
    "佐藤 大輔", "鈴木 一郎", "高橋 健太", "田中 直樹", "伊藤 翔", "渡辺 剛", "山本 亮", "中村 優", "小林 拓也", "加藤 祐樹",
    "吉田 直人", "山田 智也", "佐々木 亮介", "山口 大地", "松本 俊介", "井上 慎吾", "木村 直樹", "林 健", "斎藤 亮", "清水 大樹",
    "山崎 亮太", "森本 直人", "池田 祐介", "橋本 健太", "阿部 亮", "石井 直樹", "村上 大輔", "藤田 祐樹", "青木 亮", "三浦 健太",
    "福田 直人", "西村 亮介", "太田 大地", "岡田 俊介", "中島 慎吾", "小川 健", "後藤 亮", "長谷川 大樹", "近藤 亮太", "石田 祐介",
    "坂本 健太", "遠藤 亮", "藤井 直樹", "岡本 大輔", "村田 祐樹", "竹内 亮", "金子 健", "和田 亮介", "中野 大地", "原田 俊介"
]

# 9.56～12.99の間でランダムなタイムを生成
times = [round(random.uniform(9.56, 12.99), 2) for _ in range(50)]

# 選手データを作成
runners = [{"name": name, "time": time} for name, time in zip(names, times)]

# バブルソートでタイムが良い順（昇順）に並べ替え
def bubble_sort(runners):
    n = len(runners)
    for i in range(n):
        for j in range(0, n-i-1):
            if runners[j]["time"] > runners[j+1]["time"]:
                print(f'入れ替え: {runners[j]["name"]}({runners[j]["time"]}) ↔ {runners[j+1]["name"]}({runners[j+1]["time"]})')
                runners[j], runners[j+1] = runners[j+1], runners[j]
    return runners

print("=== 並び替え開始 ===")
sorted_runners = bubble_sort(runners)
print("=== 並び替え終了 ===\n")

print("上位5名:")
for i in range(5):
    print(f'{i+1}位: {sorted_runners[i]["name"]} - {sorted_runners[i]["time"]}秒')