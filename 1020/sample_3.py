import random  # 乱数用モジュール
marks = ('S', 'H', 'C', 'D')  # 4種類のマーク
cards = []                  # デッキ用リスト

for i in range(4):
    for j in range(1, 14):
        cards.append((marks[i], j))

print('-'*10)
print(cards)
print('-'*10)

# 1枚選択
r = random.randrange(52)  # 0〜51の乱数生成
print(f'選んだカードは{cards[r]}です')
