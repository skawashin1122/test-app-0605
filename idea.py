import random

# 問題リスト（用語, 正解, 選択肢, 解説）
questions = [
    {
        "question": "コンピュータの基本的な構成要素で、演算や制御を行う装置はどれ？",
        "answer": "CPU",
        "choices": ["CPU", "RAM", "ROM", "HDD"],
        "explanation": "CPU（中央処理装置）は演算や制御を担当します。"
    },
    {
        "question": "データを一時的に記憶する主記憶装置はどれ？",
        "answer": "RAM",
        "choices": ["RAM", "ROM", "SSD", "DVD"],
        "explanation": "RAMは電源を切ると消える一時的な記憶装置です。"
    },
    {
        "question": "プログラムやデータを永続的に保存する装置はどれ？",
        "answer": "HDD",
        "choices": ["HDD", "RAM", "CPU", "キャッシュメモリ"],
        "explanation": "HDDは電源を切ってもデータが残る補助記憶装置です。"
    },
    {
        "question": "ソフトウェアの著作権を守るための仕組みはどれ？",
        "answer": "ライセンス",
        "choices": ["ライセンス", "プロトコル", "ファイアウォール", "データベース"],
        "explanation": "ライセンスはソフトウェアの利用条件を定めるものです。"
    },
    {
        "question": "ネットワーク上でデータの送受信手順を定めたものは？",
        "answer": "プロトコル",
        "choices": ["プロトコル", "ルータ", "サーバ", "ファイアウォール"],
        "explanation": "プロトコルは通信のルールです。"
    },
    {
        "question": "インターネットでWebページを閲覧するためのソフトは？",
        "answer": "ブラウザ",
        "choices": ["ブラウザ", "エディタ", "サーバ", "データベース"],
        "explanation": "ブラウザはWebページを表示するソフトです。"
    },
    {
        "question": "データベースでデータを一意に識別するための項目は？",
        "answer": "主キー",
        "choices": ["主キー", "外部キー", "インデックス", "レコード"],
        "explanation": "主キーは重複しない値でデータを識別します。"
    },
    {
        "question": "LANの中で各機器を接続する中心となる装置は？",
        "answer": "ハブ",
        "choices": ["ハブ", "ルータ", "スイッチ", "モデム"],
        "explanation": "ハブは複数の機器を接続する装置です。"
    },
    {
        "question": "プログラムの誤りを発見・修正する作業は？",
        "answer": "デバッグ",
        "choices": ["デバッグ", "コンパイル", "テスト", "コーディング"],
        "explanation": "デバッグはバグ（誤り）を見つけて直す作業です。"
    },
    {
        "question": "情報セキュリティの3要素でないものは？",
        "answer": "効率性",
        "choices": ["効率性", "機密性", "完全性", "可用性"],
        "explanation": "情報セキュリティの3要素は機密性・完全性・可用性です。"
    },
    {
        "question": "1バイトは何ビット？",
        "answer": "8",
        "choices": ["8", "4", "16", "32"],
        "explanation": "1バイトは8ビットです。"
    },
    {
        "question": "コンピュータウイルスの感染を防ぐソフトは？",
        "answer": "ウイルス対策ソフト",
        "choices": ["ウイルス対策ソフト", "表計算ソフト", "ワープロソフト", "画像編集ソフト"],
        "explanation": "ウイルス対策ソフトはウイルスの検出・駆除を行います。"
    },
    {
        "question": "ネットワークで他のネットワークと接続する装置は？",
        "answer": "ルータ",
        "choices": ["ルータ", "ハブ", "スイッチ", "モデム"],
        "explanation": "ルータは異なるネットワークを接続します。"
    },
    {
        "question": "プログラムを機械語に翻訳するソフトは？",
        "answer": "コンパイラ",
        "choices": ["コンパイラ", "エディタ", "デバッガ", "ブラウザ"],
        "explanation": "コンパイラは高水準言語を機械語に翻訳します。"
    },
    {
        "question": "パスワードなどを盗み取る攻撃は？",
        "answer": "フィッシング",
        "choices": ["フィッシング", "スパム", "クラッキング", "マルウェア"],
        "explanation": "フィッシングは偽サイトなどで情報を盗む攻撃です。"
    },
    {
        "question": "情報を暗号化して送信する技術は？",
        "answer": "SSL",
        "choices": ["SSL", "HTML", "FTP", "SMTP"],
        "explanation": "SSLは通信を暗号化する技術です。"
    },
    {
        "question": "複数の処理を同時に行うことを何という？",
        "answer": "マルチタスク",
        "choices": ["マルチタスク", "シングルタスク", "マルチメディア", "マルチユーザ"],
        "explanation": "マルチタスクは複数の処理を同時に実行します。"
    },
    {
        "question": "データベースでデータの重複を防ぐ設計手法は？",
        "answer": "正規化",
        "choices": ["正規化", "暗号化", "圧縮", "分散"],
        "explanation": "正規化はデータの重複や矛盾を防ぐ設計手法です。"
    },
    {
        "question": "インターネットで使われる住所のような番号は？",
        "answer": "IPアドレス",
        "choices": ["IPアドレス", "MACアドレス", "URL", "DNS"],
        "explanation": "IPアドレスはネットワーク上の住所です。"
    },
    {
        "question": "プログラムの処理手順を図で表したものは？",
        "answer": "フローチャート",
        "choices": ["フローチャート", "ER図", "UML", "ネットワーク図"],
        "explanation": "フローチャートは処理の流れを図で表します。"
    },
    {
        "question": "データのバックアップを取る主な目的は？",
        "answer": "データの消失防止",
        "choices": ["データの消失防止", "速度向上", "容量削減", "セキュリティ強化"],
        "explanation": "バックアップはデータ消失時の復旧のために行います。"
    }
]

def main():
    print("全国商業高等学校 情報処理検定1級 用語学習クイズ")
    print("4択から選んでください。全20問です。\n")

    random.shuffle(questions)
    score = 0

    for idx, q in enumerate(questions[:20], 1):
        print(f"Q{idx}: {q['question']}")
        choices = q["choices"].copy()
        random.shuffle(choices)
        for i, choice in enumerate(choices, 1):
            print(f"  {i}. {choice}")
        ans = input("番号で選択してください: ")
        try:
            ans_idx = int(ans) - 1
            if choices[ans_idx] == q["answer"]:
                print("正解！", end=" ")
                score += 1
            else:
                print(f"不正解。正解は「{q['answer']}」です。", end=" ")
        except:
            print(f"入力が不正です。不正解。正解は「{q['answer']}」です。", end=" ")
        print(f"【解説】{q['explanation']}\n")

    rate = score / 20 * 100
    print(f"あなたの正解数: {score} / 20（正解率 {rate:.1f}%）")
    if rate == 100:
        print("素晴らしい！満点です！あなたは情報処理検定1級合格間違いなし！")
    elif rate >= 80:
        print("とても良い成績です！この調子で頑張りましょう！")
    elif rate >= 60:
        print("合格圏内です！あと少し頑張ろう！")
    else:
        print("まだまだ伸びしろがあります！繰り返し学習して力をつけましょう！")

if __name__ == "__main__":
    main()