def shuffle_cards(n, m, k):
    cards = list(range(1, n+1))  # 1からNまでの整数が書かれたカードのリスト
    for _ in range(k):
        # M枚ごとのセットに分ける
        sets = []
        for i in range(0, n, m): # range(start, stop, step)
            sets.append(cards[i:i+m]) # 配列の追加　cardsのi番目の要素からi+m-1番目の要素までをスライスして取得する
        # セットごとに並び替える
        sets.reverse()
        # 並び替えたカードをリストに戻す
        # 各セットsの中のカードcを一つずつ取り出して、新しいリストcardsに追加する
        cards = [c for s in sets for c in s]
    return cards

n, m, k = map(int, input().split())
result = shuffle_cards(n, m, k)
for c in result:
    print(c)