import time

N = 20  # 荷物の数
C = 55  # ナップサックの許容量
w = [3, 6, 5, 4, 8, 5, 3, 4, 3, 5, 6, 4, 8, 7, 11, 8, 14, 6, 12, 4] # 荷物それぞれの重さの配列
p = [7, 12, 9, 7, 13, 8, 4, 5, 3, 10, 7, 5, 6, 14, 5, 9, 6, 12, 5, 9] # 荷物それぞれの価値の配列

# 次使用する配列に今回の結果を残すので+1している
dp = [[0]*(C+1) for i in range(N+1)] # DPの配列作成

# 実行時間計測開始
start_time = time.time()

for i in range(N):
    for j in range(C+1):
        if j < w[i]: # この時点では許容量を超えていないので選択しない
            dp[i+1][j] = dp[i][j] # ただ選択はしていないが、今回の情報をそのままi+1の方へ移す
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]]+p[i])

# 実行時間計測終了
end_time = time.time()

print("合計価格:", dp[N][C])

# 最適な組み合わせのサイズを求める
total_size = 0
current_weight = C
for i in range(N-1, -1, -1):
    if dp[i+1][current_weight] != dp[i][current_weight]:
        total_size += w[i]
        current_weight -= w[i]

print("合計サイズ:", total_size)

# 計算時間
execution_time = end_time - start_time
print("計算時間: {:.6f}秒".format(execution_time))
