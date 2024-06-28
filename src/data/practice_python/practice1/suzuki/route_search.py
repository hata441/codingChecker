import csv
import math

def get_tizu_date():
    """
    CSVから地図情報を取得するメソッド
    引数:なし
    return:地図データ
    """
    '''
    tizu_data = []
    filename = 'map.csv'
    csvfile = open(filename, 'r', encoding='utf-8-sig')
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        tizu_data.append(row)
    csvfile.close()
    '''
    tizu_data = {
    "A": {"B":1},
    "B": {"C":5,"F":4},
    "C": {"B":5,"D":2},
    "D": {"C":2,"E":3},
    "E": {"E":3,"H":1},
    "F": {"B":4,"G":3,"I":5},
    "G": {"F":3,"H":3,"J":4},
    "H": {"G":3,"K":4},
    "I": {"F":5,"J":4},
    "J": {"G":4,"I":4,"K":4},
    "K": {"H":4,"J":4}
    }    
    return tizu_data
 
def route_search(data, start, goal):
    """
    最短経路を出すメソッド
    引数:地図情報
    return:最小経路、距離
    """
    #開始点に0、それ以外の頂点は∞
    undetermined = data
    node_distances = dict()
    pre_nodes = dict()
    for nodes in undetermined:
        node_distances[nodes] = math.inf
    node_distances[start] = 0

    #for文に変更する必要あり
    while undetermined:
        mininum_node = None
        #未確定のノードの中で最小値のノードを選び、最短距離として確定
        for node in undetermined:
            if mininum_node is None:
                mininum_node = node
            elif node_distances[node] < node_distances[mininum_node]:
                mininum_node = node

        #確定ノードに隣接する未確定ノードに対し、開始からの最短距離を更新
        for node, distance in undetermined[mininum_node].items():
            if distance + node_distances[mininum_node] < node_distances[node]:
                node_distances[node] = distance + node_distances[mininum_node]
                pre_nodes[node] = mininum_node
        undetermined.pop(mininum_node)
    return node_distances

if __name__ == '__main__':
    start = "A"
    goal = "H"
    tizu_data = get_tizu_date()
    min_route = route_search(tizu_data, start, goal)
    print(min_route[goal])