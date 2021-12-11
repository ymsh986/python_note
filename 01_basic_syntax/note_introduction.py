# coding: utf-8

def note_string_embedded():
    """文字列への変数埋め込み
    """
    print("Hi, {}".format("hello world"))
    Name = "Bob"
    text = f"My name is {Name}."
    print(text)
    s = "A:{2}, B:{0}, C:{1}"
    A = 1
    B = 10
    C = 100
    print(s.format(B, C, A))


def note_string_sample():
    """文字列操作
    """
    s = 'hello world'
    print(s.title())
    print(s.capitalize())
    print(s.find("l"))
    print(s.find("x"))
    print(s.rfind("l"))
    print(s.replace("l", "x"))
    print(s.strip(" "))


def note_for_else_break():
    """for文のelseブロック
    """
    numlist = [3, 4.2, 10, "x", 1, 9]  # 文字列が含まれているlist
    sum = 0

    for num in numlist:
        # numが数値ではないときは処理をブレイクする
        if not isinstance(num, (int, float)):
            print(num, "数値ではない値が含まれていました。")
            break  # ブレイクする
        sum += num
    else:
        # breakされなかったときは合計する
        print("合計", sum)


def note_try_expect_finally():
    """try-expect-finaly文例
    """
    num = 0
    try:
        value = 120 / num
        print(value)
    except Exception as error:
        print("エラーになりました。")
        print(error)
    finally:
        print("計算終わり。")


def note_try_expect_as():
    """try-expect-as文例
    """
    sum = 7600
    while True:
        num = input("何人ですか？（qで終了）")
        if num == "q":
            print("終了しました。")
            break

        try:
            price = round(sum / int(num))
        except Exception as error:
            print("エラーになりました。")
            print(error)
        else:
            if price < 0:
                # マイナスの場合は無視
                continue
            print("１人当たりの金額", price)


def note_for_enumerate():
    """enumereateを用いたfor文
    """
    names = ["鈴木", "田中", "栗林", "山岡"]
    for i, who in enumerate(names, 1):
        print(f"{i}：{who}さん")


def note_for_zip():
    """for文で2つのリストを同時にまわす
    """
    name1 = ["鈴木", "田中", "赤尾", "佐々木", "高田"]
    name2 = ["星奈", "優美", "恵子", "薫花", "幸恵"]
    longname = []

    # name1とname2を連結したリストを作る
    for n1, n2 in zip(name1, name2):
        longname.append(n1 + n2)
    print(longname)


def note_list_comprehension():
    """listの内包表記
    """
    numbers = [2.1, 4, "", 2.2, 'x', "12", 3]
    numbers = [num for num in numbers if isinstance(num, (int, float))]
    print(numbers)


def note_route(start, end, *args):
    """任意の数の引数を受け取る

    Args:
        start (str): start place
        end (str): end place
        *args: waypoint
    """
    route_list = [start]
    route_list += list(args)
    route_list += [end]

    route_str = "->".join(route_list)
    print(route_str)


def note_route_args():
    """route()を試す
    """
    start = "東京"
    end = "宮崎"
    note_route(start, end, "神戸", "長崎", "熊本")


def note_entry(name, gender, **kwargs):
    """任意の数の引数を受け取る

    Args:
        name (str): name
        gender (str): gender
    """
    data = {"name": name, "gender": gender}  # 必須の引数の辞書
    data.update(kwargs)  # 必須の辞書とオプションの辞書を１つに合わせる
    print(data)


def note_route_kwargs():
    """entry()を試す
    """
    note_entry(name="大山坂道", gender="男性", age=27, course="E")


def note_size(item):
    """指定文字列の順序を定義して順序を返す

    Args:
        item (str): 文字列を割り振られたindexにして返す

    Returns:
        int: 文字列のindexリスト
    """
    sizelist = ["XS", "S", "M", "L"]  # この順に並び替える
    pos = sizelist.index(item)  # itemのインデックス番号を値として返す
    return pos


def note_sort_size():
    """note_size関数を用いてdataをサイズ順に並べる
    """
    data = ["S", "M", "XS", "L", "M", "M", "XS", "S", "M", "L", "M"]
    data.sort(key=note_size)
    print(data)


def note_sort_size_lambda():
    """note_sort_sizeと同様処理をlambda式で行う
    """
    sizelist = ["XS", "S", "M", "L"]   # この順に並び替える
    data = ["S", "M", "XS", "L", "M", "M", "XS", "S", "M", "L", "M"]
    data.sort(key=lambda item: sizelist.index(item))  # dataをサイズ順に並べる
    print(data)


def note_map_double():
    """map関数を使ってリストの数値を２倍する
    """
    def double(x):
        return x * 2
    nums = [4, 3, 7, 6, 2, 1]
    nums2 = list(map(double, nums))
    print(nums2)


def note_filter():
    """note_map_doubleと同様処理をlambda式で行う
    """
    nums = [4, -3, 9, 1, -2, -4, 5]
    nums = list(filter(lambda x: x > 0, nums))
    print(nums)


def note_unpack_list():
    """アンパックの仕組みを利用
        変数が足りない場合、*付きの変数に割り当てられていない値がまとめられる
    """
    list_x = [1, 'a', -1, [3, 4], False]
    a, b, c, d, e = list_x
    print(a, b, c, d, e)
    # -> 1 a -1 [3, 4] False

    f, *g, h = list_x
    print(f, g, h)
    # -> 1 ['a', -1, [3, 4]] False


def note_type_hints() -> int:
    """型ヒントを使った書き方
        型ヒントと異なる型が入ってきたとしても、エラーにはならない。
        あくまで注釈（ヒント）。

    Returns:
        int: 税込み計算
    """
    from typing import List, Dict
    x: int = 100
    y: float = 1.1
    list_x: List[int] = [1, 2, 3, 4]
    dict_x: Dict[str, str] = {'name': 'yama'}

    print(list_x)
    print(dict_x)

    return int(x * y)


if __name__ == "__main__":
    print(note_type_hints())
