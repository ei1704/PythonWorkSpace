import random
# 初期化
marks = ('S','H','C','D') # 4 種類のマーク
cards = [] # デッキ用リスト
for m in marks:
 for n in range(1,14):
  t = (m,n) # タプルでカード生成
  cards.append(t) # リストに追加

# 5 枚選択
f_cards = [random.choice(cards) for i in range(5)]
# 並び替え
f_cards.sort(key=lambda x:x[1],reverse=True)
# 出力
print(f_cards)