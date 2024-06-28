import argparse
import inspect
import random
import time

ALGORITHMS = [
    'chiikawa',
    'hachiware',
    'usagi',
    'shimajiro',
    'momonga'
]


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
        '-n', '--number', action='store', default=1000, type=int
    )
    parser.add_argument(
        '-a', '--algorithm', action='store', choices=ALGORITHMS,
        default=ALGORITHMS[0], type=str
    )

    return parser


def chiikawa_sort(req_list):
    """左から一個ずつ並べ替えていくメソッド(おそい)
    """
    sort_list = req_list.copy()
    for i in range(1, len(sort_list)):
        if sort_list[i] < sort_list[i-1]:
            j = i
            while j > 0:
                if sort_list[j] >= sort_list[j-1]:
                    break
                sort_list[j], sort_list[j -
                                        1] = sort_list[j-1], sort_list[j]
                j -= 1
    return sort_list


def hachiware_sort(req_list):
    """最小値を持ってきて並べ替えていくメソッド(ちいかわよりちょっと早い)
    """
    sort_list = req_list.copy()
    max_length = len(sort_list)
    for i in range(max_length):
        min_index = i
        for j in range(i, max_length):
            if sort_list[j] < sort_list[min_index]:
                min_index = j
        sort_list[i], sort_list[min_index] = sort_list[min_index], sort_list[i]
    return sort_list


def usagi_sort(req_list):
    """2分割を繰り返すメソッド(はやい)
    """
    nest = [req_list]
    i = 0
    while i < len(req_list):
        if len(nest[i]) == 1:
            i += 1
        else:
            for j in range(len(nest[i])):
                smallers = []
                largers = []
                base = nest[i][j]
                for k in nest[i]:
                    if k < base:
                        smallers.append(k)
                    else:
                        largers.append(k)
                if len(smallers) != 0 and len(largers) != 0:
                    nest[i] = smallers
                    nest.insert(i+1, largers)
                    break
            else:
                pop = nest.pop(i)
                for k in range(i, i+len(pop)):
                    nest.insert(k, [pop[0]])
                i += len(pop)
    return [item[0] for item in nest]


def shimajiro_sort(req_list):
    """ヒープソート（ヒップではない）
    """
    sort_list = req_list.copy()

    def heap(arr, top):
        max_length = len(arr)
        parent, child1, child2 = top, 2*top+1, 2*top+2
        if child2 < max_length and arr[child1] > arr[parent]:
            parent = child1
        if child2 < max_length and arr[child2] > arr[parent]:
            parent = child2
        if parent != top:
            arr[top], arr[parent] = arr[parent], arr[top]
            heap(arr, parent)

    # 最初の全体ソート
    for i in range(len(sort_list)//2-1, -1, -1):
        heap(sort_list, i)
    result_list = [sort_list.pop(0)]

    # 繰り返しソート
    for _ in range(len(sort_list)):
        sort_list.insert(0, sort_list.pop())
        heap(sort_list, 0)
        result_list.insert(0, sort_list.pop(0))

    return result_list


def momonga_sort(req_list):
    """python標準のソート（ずるい めちゃはやい）
    """
    sort_list = req_list.copy()
    return sorted(sort_list)


if __name__ == "__main__":
    args = parse_args('sort').parse_args()
    if args.number < 2:
        print("2以上の長さを指定してください")
    else:
        random_list = [random.randint(1, args.number*10)
                       for _ in range(args.number)]
        start = time.perf_counter()
        if args.algorithm == "chiikawa":
            sorted_list = chiikawa_sort(random_list)
        elif args.algorithm == "hachiware":
            sorted_list = hachiware_sort(random_list)
        elif args.algorithm == "usagi":
            sorted_list = usagi_sort(random_list)
        elif args.algorithm == "shimajiro":
            sorted_list = shimajiro_sort(random_list)
        elif args.algorithm == "momonga":
            sorted_list = momonga_sort(random_list)
        else:
            sotrd_list = []
        end = time.perf_counter()
        print(
            f"[実行前]: \n{random_list}\n[実行後]: \n{sorted_list}\n"
            + f"[処理時間]: {end-start} s")
