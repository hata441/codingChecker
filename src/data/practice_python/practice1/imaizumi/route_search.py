import csv
import os
import heapq
import argparse

MAP_CSV_PATH = os.path.join(os.path.dirname(__file__), "map.csv")


def search_path_by_dijkstra(map, start, end):
    """Dijkstra法で最短経路を求める

    Args:
        map (list[list[str]]): map.csvの二次元配列
        start (int): 開始地点番号(A:1, B:2, ..)
        end (int): 終了地点番号

    Returns:
        int, list[int]: 移動コスト、経路のリスト
    """
    # 移動コスト、基準点、経路(最小値を取りたいのでheapqを使用)
    # 始点の移動コストを0とする
    queue = [(0, start, [])]
    # 最小コストが確定した地点の集合
    seen = set()
    # 最小コスト保存用
    min_cost = {start: 0}

    # 1. 未確定の地点の中から、距離が最も小さい地点を選んで、 その距離を「その地点までの最短距離」として確定します。
    # 2. 直近で確定した地点から「直接つながっている」かつ 「未確定である」地点に対して、 直近で確定した場所を経由した場合の距離を
    #    計算し、今までの距離よりも小さければ更新します。
    # 3. 全ての地点が確定すれば終了です。そうでなければ1へ。
    # 参考：https://nw.tsuda.ac.jp/lec/dijkstra
    while queue:
        # 移動コストが最も小さいレコードをpopして確定する
        (cost, node, path) = heapq.heappop(queue)
        if node not in seen:
            # 地点の確定
            seen.add(node)
            # ここまでの経路を記録しておく
            path = path + [node]
            if node == end:
                # 終了地点まで来たらreturn
                return path, cost

            # 直近で確定した地点からの移動コストを走査
            for next_node in range(1, len(map[node])):
                # 「直接つながっている」かつ 「未確定である」地点のみ参照
                if int(map[node][next_node]) != 0 and next_node not in seen:
                    # 移動コストの計算
                    next_cost = cost + int(map[node][next_node])
                    # 移動コストが小さければ最小コスト更新
                    if next_node not in min_cost or next_cost < min_cost[next_node]:
                        # 更新情報をキューに保存
                        heapq.heappush(queue, (next_cost, next_node, path))
                        min_cost[next_node] = next_cost

    return None, None


def search_path_by_bellman_ford(map, start, end):
    """Bellman_Ford法で最短経路を求める

    Args:
        map (list[list[str]]): map.csvの二次元配列
        start (int): 開始地点番号(A:1, B:2, ..)
        end (int): 終了地点番号

    Returns:
        int, list[int]: 移動コスト、経路のリスト
    """
    # 1. 全ての辺に対し、その辺を通った頂点のコストが小さければ値を更新する。
    # 2. 1のプロセスを（頂点の数-1）回行います。
    dist = [(float('inf'), [])] * (len(map))
    dist[start] = (0, [start])

    for _ in range(len(map)-2):
        for node1 in range(1, len(map)):
            for node2 in range(1, len(map)):
                if int(map[node1][node2]) == 0:
                    continue
                newlen = dist[node1][0]+int(map[node1][node2])
                if newlen < dist[node2][0]:
                    dist[node2] = (newlen, dist[node1][1] + [node2])

    return dist[end]


if __name__ == "__main__":
    # 引数設定
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", type=str, required=True)
    parser.add_argument("-e", "--end", type=str, required=True)
    args = parser.parse_args()

    try:
        start = ord(args.start.upper())-64
        end = ord(args.end.upper())-64

        with open(MAP_CSV_PATH) as f:
            reader = list(csv.reader(f))

        if start > 0 and end > 0 and start < len(reader) and end < len(reader):
            result_d = search_path_by_dijkstra(reader, start, end)
            result_b = search_path_by_bellman_ford(reader, start, end)
            if result_d[0] is not None:
                path_str_d = " -> ".join([chr(node+64)
                                         for node in result_d[0]])
                path_str_b = " -> ".join([chr(node+64)
                                         for node in result_b[1]])
                print(
                    f"ダイクストラ法\n[最短経路] : {path_str_d}\n[距離] : {result_d[1]}\n")
                print(
                    f"ベルマン・フォード法\n[最短経路] : {path_str_b}\n[距離] : {result_b[0]}")
            else:
                print("経路が見つかりませんでした")
        else:
            print("マップにある地点を指定してください")
    except TypeError as e:
        print(e)
        print("半角英字を指定してください")
