
import csv
import argparse
import inspect
import heapq


CSV_PATH = './map.csv'


def get_parser(name):
    """
    :param name:
    :rtype: object
    :return: 引数解析用のオブジェクト
    """
    file_path = inspect.currentframe().f_back.f_code.co_filename
    desc = u'{0} [Args] [Options]\nDetailed '.format(file_path)
    parser = argparse.ArgumentParser(prog=name, description=desc)
    parser.add_argument('-s', '--start', metavar='String', action='store', 
                        type=str, required=True, help='Start')
    parser.add_argument('-e', '--end', metavar='String', action='store', 
                        type=str, required=True, help='End')
    return parser


def get_map(csv_path):
    """
    map.csvから距離を取得するメソッド
    :param csv_path:
    :rtype:string
    :return: 各拠点からの距離
    """
    with open(csv_path, "r", encoding="utf-8") as map_file:
        reader = csv.DictReader(map_file)
        dict_1 = {}
        for row in reader:
            dict_1[row[""]] = {
                k: int(v) for k, v in row.items() if k != '' and v != '0'
            }
       
    return dict_1


def dijkstra(graph, start, end):
    """
    map.csvから距離を取得するメソッド
    :param csv_path:
    :rtype:string
    :return: 各拠点からの距離
    """
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
                
    path = []
    while end:
        path.append(end)
        end = previous_nodes[end]
    path.reverse() 

    return distances, path


if __name__ == '__main__':
    parser = get_parser('test')
    args = parser.parse_args()
    graph = get_map(CSV_PATH)
    distances, path = dijkstra(graph, args.start, args.end)
    print("[最短経路] :", " → ".join(path))
    print("[距離]    :", distances[args.end])
