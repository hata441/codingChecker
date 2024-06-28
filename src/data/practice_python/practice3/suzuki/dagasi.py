import itertools

def dagasi_list():
    """
    商品一覧を作成

    :rtype: object
    :return: 商品一覧
    """
    dagasi_list = [
    ('うまい棒', 12, 10),
    ('カントリーマアム', 278, 350),
    ('チロルチョコ', 23, 29),
    ('オレオ', 234, 275),
    ('きのこの山', 168, 150),
    ('たけのこの里', 168, 200)
    ]
    dagasi = sorted(dagasi_list, key=lambda x: x[2])
    return dagasi


def shopping(product):
    """
    購入する商品一覧、価格、幸福度を計算する

    :param list product_list: 商品一覧
    :rtype: object
    :return: 購入商品情報
    """
    price = 0
    happy = 0
    result = []
    name = []
    for i in range(1, len(product)+1):
        for j in itertools.combinations(product, i):
            for row in j:
                price += row[1]
                if price <= 500:
                    name.append(row[0])
                    happy += row[2]
                    result = name, price, happy
                else:
                    pass
    return result


if __name__ == '__main__':
    shopping_list = shopping(dagasi_list())
    print("[おすすめ商品組合せ]\t:", shopping_list[0])
    print("[合計金額]\t:", shopping_list[1])
    print("[幸福度]\t:", shopping_list[2])
