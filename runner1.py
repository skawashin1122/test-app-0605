import random

# ダミーの女性選手名リスト（日本人風の名前を20人分用意）
names = [
    "佐藤 美咲", "鈴木 彩花", "高橋 由美", "田中 さくら", "伊藤 美穂", "渡辺 真由", "山本 愛", "中村 友美", "小林 優子", "加藤 美紀",
    "吉田 亜美", "山田 里奈", "佐々木 綾", "山口 美和", "松本 佳奈", "井上 由佳", "木村 朋美", "林 由里", "斎藤 美香", "清水 亜紀"
]

# 9.56～12.99の間でランダムなタイムを生成（20人分）
times = [round(random.uniform(9.56, 12.99), 2) for _ in range(20)]

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