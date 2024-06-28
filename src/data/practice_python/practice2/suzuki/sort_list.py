import time
import inspect
import argparse
import random


def parse_args(name, add_help=True):
    """
    引数解析用のメソッドである。

    :param str name: ヘルプ表示する名前
    :param str version: バージョン
    :param bool add_help: 子オプションを作成する場合は偽
    :rtype: object
    :return: 引数解析用のオブジェクト
    """
    # 実行中のメソッド名を取得する=sort_list.py
    file_path = inspect.currentframe().f_back.f_code.co_filename
    # f=フォーマット済み文字列リテラル
    desc = f'{file_path} [Options]'
    # プログラム実行時にコマンドラインで引数を受ける処理を定義
    parser = argparse.ArgumentParser(
        prog=name, add_help=add_help, description=desc)
    parser.add_argument(
        '-n', '--number', required=True, type=int
    )
    return parser


def sort(sort_list):
    """
    配列の中から最小値探して挿入する

    :param list sort_list: ソート前リスト
    :rtype: object
    :return: ソート後リスト
    """
    for i in range(len(sort_list)):
        # 配列の最小値を探す
        target = i
        for j in range(i+1, len(sort_list)):
            if sort_list[j] < sort_list[target]:
                target = j
        # 最小値の挿入
        sort_list[i], sort_list[target] = sort_list[target], sort_list[i]
    return sort_list


def time_measurement(args):
    """
    処理時間を計測するメソッド

    :param int args: コマンド引数で入力された数値
    """
    start = time.time()
    max_number = args.number + 1
    lst = list(range(0, max_number))
    start_list = random.sample(lst, len(lst))
    print("[実行前]:", start_list)
    sort_list = sort(start_list)
    print("[実行後]:", sort_list)
    end = time.time()
    time_diff = end - start
    print("[処理時間]:", time_diff)


if __name__ == '__main__':
    args = parse_args('sort list').parse_args()
    time_measurement(args)
