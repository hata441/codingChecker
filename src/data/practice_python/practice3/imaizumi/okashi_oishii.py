"""お菓子の組み合わせを出すプログラム
"""
import itertools

DEFAULT_OKASHI = [
    ('うまい棒', 12, 10),
    ('カントリーマアム', 278, 350),
    ('チロルチョコ', 23, 29),
    ('オレオ', 234, 275),
    ('きのこの山', 168, 150),
    ('たけのこの里', 168, 200)
]

# 満足度が最大になるお菓子の組み合わせ、そのときの合計の満足度、合計金額を出す関数
# ([名前]、満足度,金額)


def okashi_kumiawase():
  # 全ての組み合わせで、満足度を求めたい。
  # 1. 組み合わせを出す。
  # list(itertools.combinations(l, 2))⇒lのリストで、2つ選ぶ時の組み合わせを出してくれる。
  result_list = []
  for nanko in range(1, len(DEFAULT_OKASHI) + 1):
    kumiawases = list(itertools.combinations(DEFAULT_OKASHI, nanko))
    # 2. 組み合わせの通りに、タプルの要素を足す。これをすべての組み合わせでやる
    for kumiawase in kumiawases:
      # 名前⇒[うまい、オレオ], 12+278, 10+350
      okashi_names = []
      total_price = 0
      total_manzoku = 0
      for okashi_tuple in kumiawase:
        name, price, manzoku = okashi_tuple
        okashi_names.append(name)
        total_price += price
        total_manzoku += manzoku
      # 3. 予算がオーバーしたものを排除
      if total_price > 500:
        continue
      result_list.append((okashi_names, total_price, total_manzoku))

  # 4 満足度が一番高いものを抜きだす
  result_sorted_list = sorted(result_list, key=lambda x: x[2])
  return result_sorted_list[-1]


if __name__ == "__main__":
  manzoku_kumiawase = okashi_kumiawase()
  print(manzoku_kumiawase)
