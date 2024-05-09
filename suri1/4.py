import numpy as np
import time

# 物の個数
n = 20
# 要領
capacity = 55
# 物の重さ、価値
weight= [3, 6, 5, 4, 8, 5, 3, 4, 3, 5, 6, 4, 8, 7, 11, 8, 14, 6, 12, 4]
price = [7, 12, 9, 7, 13, 8, 4, 5, 3, 10, 7, 5, 6, 14, 5, 9, 6, 12, 5, 9]

# 最高の重さと価格と最適な組み合わせを記録する
max_weight = -1
max_price = -1
combination = []

# 実行時間計測開始
start_time = time.time()

# iには2**nまでの値が入る。
for i in range(2 ** n):
    # 変数の初期化
    tmp_weight = 0
    tmp_price = 0
    tmp_combination = []
    over_flag = False
    for j in range(n):
        # 2進数で計算。シフトして１ビットずつ判断。
        is_put = i >> (n - j - 1) & 1
        # 値を入力
        tmp_combination.append(is_put)
        tmp_weight += is_put * weight[j]
        tmp_price += is_put * price[j]
        # capa を越えたらフラグを立てて break
        if tmp_weight > capacity:
            over_flag = True
            break
    # over flag が立ってない かつ 暫定 max price より高いときに更新
    if (not over_flag) and tmp_price > max_price:
        max_price = tmp_price
        max_weight = tmp_weight
        combination = tmp_combination

# 実行時間計測終了
end_time = time.time()

print("合計が最大になる組み合わせ")
print(combination)
print("合計価格: ", max_price)
print("合計サイズ: ", max_weight)

# 総当たりの数
total_combinations = 2 ** n
print("総当たりの数:", total_combinations)

# 計算時間
execution_time = end_time - start_time
print("計算時間: {:.6f}秒".format(execution_time))