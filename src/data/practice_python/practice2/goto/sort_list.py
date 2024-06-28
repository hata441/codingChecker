import random
import argparse
import inspect
import time


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
        '-n', '--number', action='store', required=True, type=int
    )
    parser.add_argument(
        '-a', '--algorithm', action='store', required=True, type=str
    )
    return parser


def result_list(r_list):
    """
    リストをカンマ区切りで表示させるメソッドである
    :params list ran: ランダムなリスト（ソート前）
    :params list sort: ソートされたリスト
    :rtype: list
    :return: リストをカンマ区切りした値
    """
    r_list_1 = ','.join([str(r) for r in r_list])
    return r_list_1


def create_random_list(num):
    """
    引数からランダムな配列を作成するメソッドである
    :param int num: 引数
    :rtype: list
    :return: ランダムな順序で並んでいる配列
    """
    random_list = random.sample(range(num), k=num)
    return random_list


def bubble_sort_list(ran_b):
    """
    ランダムな順序で並ぶ配列を昇順でソートするメソッドである(バブルソート)
    :param list ran: ランダムなリスト
    :rtype: list
    :rtype: float
    :return: ソートしたリスト
    :return: 開始時間、終了時間
    """
    # 計測開始
    start = time.time()

    for i in range(len(ran_b) - 1):
        a = 0
        b = 1
        while b < len(ran_b):
            if ran_b[a] > ran_b[b]:
                ran_b[a], ran_b[b] = ran_b[b], ran_b[a]
            a += 1
            b += 1
    # 計測終了
    end = time.time()
    return ran_b, start, end


def insertion_sort_list(ran_i):
    """
    ランダムな順序で並ぶ配列を昇順でソートするメソッドである(挿入ソート)
    :param list ran: ランダムなリスト
    :rtype: list
    :rtype: float
    :return: ソートしたリスト
    :return: 開始時間、終了時間
    """
    # 計測開始
    start = time.time()

    for i in range(len(ran_i) - 1):
        # ran_i[i]の一つ右の要素: a[j]をソート対象に定める
        j = i + 1

        # ran_i[j]がソート済みの位置に収まるまで繰り返す
        while i >= 0:
            # ran_i[j]を一つ左の要素と比較し、ran_i[j]の方が小さければ交換する
            if ran_i[j] < ran_i[i]:
                ran_i[i], ran_i[j] = ran_i[j], ran_i[i]
                # 比較対象が左に移動しているので、indexを1ずつ減らす
                i -= 1
                j -= 1
            else:
                break
    # 計測終了
    end = time.time()
    return ran_i, start, end


if __name__ == '__main__':
    args = parse_args('search_list').parse_args()
    # ランダムなリスト作成
    ran_list = create_random_list(args.number)
    print("[実行前]:", result_list(ran_list))

    # ソートしたリスト作成
    if args.algorithm == 'bubble':
        sort_list, s_tme, e_time = bubble_sort_list(ran_list)
    elif args.algorithm == 'insertion':
        sort_list, s_tme, e_time = insertion_sort_list(ran_list)
    
    print("[実行後]:", result_list(sort_list))
    print("[処理時間]:", '{:.9f}'.format((e_time-s_tme)/60))