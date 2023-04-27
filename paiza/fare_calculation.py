n, m = map(int, input().split())
costs = [list(map(int, input().split())) for _ in range(n)]
x = int(input())
route = [tuple(map(int, input().split())) for _ in range(x)]

current_line = 0  # 現在の路線は1番目の路線
current_station = 0  # 現在地は1番目の駅
total_cost = 0  # 現在までの合計運賃

for r, s in route:
    # 次の駅までの運賃を計算する
    next_line = r - 1  # 目的地の路
    next_station = s - 1  # 目的地の駅
    
    if current_line == next_line:
        # 同じ路線内での移動の場合、差分を計算する
        fare = abs(costs[current_line][next_station] - costs[current_line][current_station])
    else:
        # 異なる路線への移動の場合、差分を計算する
        fare = abs(costs[next_line][next_station] - costs[next_line][current_station])
    total_cost += fare
    
    # 次の目的地に移動する
    current_line = next_line
    current_station = next_station

print(total_cost)