"""お菓子の組み合わせを計算するプログラム
"""
import argparse
import inspect
import random
import itertools
import data as d


def parse_args(name, version='1.0.0', add_help=True):
  """
  引数解析用のメソッドである。

  :param str name: ヘルプ表示する名前
  :param str version: バージョン
  :param bool add_help: 子オプションを作成する場合は偽
  :rtype: object
  :return: 引数解析用のオブジェクト
  """
  file_path = inspect.currentframe().f_back.f_code.co_filename
  desc = f'{file_path} [Args] [Options]\nDetailed '
  parser = argparse.ArgumentParser(
      prog=name, add_help=add_help, description=desc)
  parser.add_argument(
      '-v', '--version', action='version', version=f'Version {version}'
  )
  parser.add_argument(
      '-n', '--number', action='store', type=int
  )
  parser.add_argument(
      '-b', '--budget', action='store', default=500, type=int
  )
  parser.add_argument(
      '-a', '--algorithm', action='store', choices=d.ALGORITHMS,
      default=d.ALGORITHMS[1], type=str
  )

  return parser


def osusume(budget, algo, kashi_list):
  """コンソールにおすすめ組み合わせを出力する関数

  :param int number: 数
  :param int budget: 予算
  """
  if algo == d.ALGORITHMS[0]:
    satisfaction_que = calc_satisfaction_chiikawa(kashi_list, budget)
  elif algo == d.ALGORITHMS[1]:
    satisfaction_que = calc_satisfaction_hachiware(kashi_list, budget)
  print('☆☆おすすめ組み合わせ☆☆\n')
  for i in range(d.RANK_LENGTH):
    if len(satisfaction_que) < 1:
      if i == 0:
        print("おすすめできる組み合わせがありません(´・ω:;.:...")
      break
    sat, pri, prs = satisfaction_que.pop(-1)
    pro_str = ""

    def price(data, key):
      return str(next(
          (item[1] for item in data if item[0] == key), None))
    for pro in prs:
      pro_str += "・" + pro + " " + price(kashi_list, pro) + "円\n"
    print(f'☆おすすめ{i+1}\n{pro_str}合計：{pri}円\n満足度：{sat}点\n')


def make_kashi_list(list_length):
  """
  適当なお菓子のリストを生成する関数

  :param int list_length (int): リスト長
  :rtype: List[Tuple[str, int, int]]
  :return: お菓子のリスト (名称, 価格, 満足度)
  """
  i = 0
  kashi_list, index_list = [], []
  len1, len2, len3, len4, len5 = len(d.OKASHI_NAMES['MAKER']), \
      len(d.OKASHI_NAMES['PRE_NAME']), len(d.OKASHI_NAMES['CONNECTION']), \
      len(d.OKASHI_NAMES['NAME']), len(d.OKASHI_NAMES['FLAVOR'])
  max_length = len1 * len2 * len3 * len4 * len5
  if max_length < list_length:
    list_length = max_length
  while i < list_length:
    name_index = (
        random.randint(0, len1 - 1),
        random.randint(0, len2 - 1),
        random.randint(0, len3 - 1),
        random.randint(0, len4 - 1),
        random.randint(0, len5 - 1)
    )
    if name_index in index_list:
      continue
    index_list.append(name_index)
    okashi_name = d.OKASHI_NAMES['MAKER'][name_index[0]] + ' ' + \
        d.OKASHI_NAMES['PRE_NAME'][name_index[1]] + \
        d.OKASHI_NAMES['CONNECTION'][name_index[2]] + \
        d.OKASHI_NAMES['NAME'][name_index[3]] + \
        (f"（{d.OKASHI_NAMES['FLAVOR'][name_index[4]]}）"
         if d.OKASHI_NAMES['FLAVOR'][name_index[4]] else '')
    price = random.randint(d.MIN_PRICE, d.MAX_PRICE)
    satisfaction = random.randint(d.MIN_SATISFACTION, d.MAX_SATISFACTION)
    kashi_list.append((okashi_name, price, satisfaction))
    i += 1
  return kashi_list


def calc_satisfaction_chiikawa(kashi_list, budget):
  """
  満足度を計算する関数その1: 全通り力技(PCこわれる)
  :param List[Tuple[str, int, int]] kashi_list:
  :param int budget: 予算
  :return List[Tuple[int, int, Lit[str]]]: 合計のリスト 
  """
  combs = []
  lis = [i for i in range(len(kashi_list))]
  for i in range(1, len(kashi_list) + 1):
    combs += [list(conb)
              for conb in itertools.combinations(lis, i)]
  result_list, sorted_list = [], []
  for comb in combs:
    products = []
    total_satisfuction = 0
    total_price = 0
    for index in comb:
      pro, pri, sat = kashi_list[index]
      products.append(pro)
      total_price += pri
      total_satisfuction += sat
      if total_price > budget:
        break
    else:
      result_list.append((total_satisfuction, total_price, products))
      sorted_list = sorted(result_list, key=lambda x: x[0])

  return sorted_list


def calc_satisfaction_hachiware(kashi_list, budget):
  """
  満足度を計算する関数その2: 動的計画法
  :param List[Tuple[str, int, int]] kashi_list:
  :param int budget: 予算
  :return List[Tuple[int, int, Lit[str]]]: 合計のリスト
  """
  # 情報を保存する二次元配列を作成
  # 縦軸：お菓子の種類数(リスト長)、横軸：合計金額
  dp = [[(0, 0, []) for _ in range(budget + 1)]
        for _ in range(len(kashi_list))]
  for i, t in enumerate(kashi_list):
    pro, pri, sat = t
    for j in range(budget + 1):
      dp[i][j] = dp[i - 1][j]
      if j >= pri:
        if dp[i - 1][j - pri][0] + sat > dp[i][j][0]:
          psat, ppri, ppros = dp[i - 1][j - pri]
          dp[i][j] = (psat + sat, ppri + pri, ppros + [pro])
  return [dp[len(kashi_list) - 1][budget]]


if __name__ == "__main__":
  args = parse_args('おかしえらび').parse_args()
  if args.number and args.number > 0:
    okashi_data = make_kashi_list(args.number)
  else:
    okashi_data = d.DEFAULT_OKASHI
  osusume(args.budget, args.algorithm, okashi_data)
