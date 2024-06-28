import csv
from operator import mul


class KnapsackPractice:
  """Python課題3 ナップザック問題を解くプログラムの作成
  """

  def __init__(self, file_path, weight_limit):
    """コンストラクタ
    クラス変数の初期化を実施

    Args:
        file_path (string): 商品一覧のファイルパス
        weight_limit (int): 重量限界
    """
    self.items = {
        "names": [],
        "weights": [],
        "scores": []
    }
    self.weight_limit = weight_limit
    # CSVファイルの読み込みを実施
    self._read_items_file(file_path)

  def _read_items_file(self, file_path):
    """商品一覧を読み込む

    Args:
        file_path (string): 商品一覧のファイルパス
    """
    with open(file_path, "r") as f:
      csv_contents = csv.reader(f, delimiter=',')

      # ヘッダーはスキップ
      next(csv_contents)

      for line in csv_contents:
        # 行の値が3種でないものは何かしら異常
        if len(line) != 3:
          continue
        else:
          # リスト形式が後に使いやすいので格納
          self.items["names"].append(line[0])
          self.items["weights"].append(float(line[1]))
          self.items["scores"].append(float(line[2]))

  def _calc_by_all_check(self):
    """全探索での走査

    Returns:
        float: 最大満足度の値
        list: 最大満足度の時の組み合わせ(商品名)
    """
    max_score = 0
    max_score_list = None

    # 最悪こういう形式で書けば解けます
    for i_0 in range(2):
      for i_1 in range(2):
        for i_2 in range(2):
          for i_3 in range(2):
            for i_4 in range(2):
              for i_5 in range(2):
                current_list = [i_0, i_1, i_2, i_3, i_4, i_5]
                current_weight = sum(map(mul, current_list, self.items["weights"]))
                current_score = sum(map(mul, current_list, self.items["scores"]))

                # 重量が限界値を超えてなく、かつ満足度が最大になった場合値を保持する
                if current_weight <= self.weight_limit and current_score > max_score:
                  max_score, max_score_list = current_score, current_list

    # 組み合わせリストを名称に書き換える
    max_score_list = [i for index, i in enumerate(self.items["names"]) if max_score_list[index] == 1]

    return max_score, max_score_list

  def calcSatisFaction(self):
    """メインで呼び出される関数
    """
    max_score, max_score_list = self._calc_by_all_check()
    print(f"[最大満足度]:{max_score}")
    print(f"[組み合わせ]:{max_score_list}")


if __name__ == "__main__":
  # 固定値の定義
  FILE_PATH = "./items.csv"
  LIMIT = 500

  # クラスの呼び出し
  kp = KnapsackPractice(FILE_PATH, LIMIT)
  kp.calcSatisFaction()
