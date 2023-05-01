def shuffle_cards(n, m, k):
    cards = list(range(1, n+1))  # 1からNまでの整数が書かれたカードのリスト
    for _ in range(k):
        # M枚ごとのセットに分ける
        sets = []
        for i in range(0, n, m):
            sets.append(cards[i:i+m])
        # セットごとに並び替える
        sets.reverse()
        # 並び替えたカードをリストに戻す
        cards = [c for s in sets for c in s]
    return cards

n, m, k = map(int, input().split())
result = shuffle_cards(n, m, k)
for c in result:
    print(c)