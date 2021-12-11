# coding: utf-8

def note_num_generator():
    """数列の値を作るジェネレータ

    Yields:
       int: 数値
    """
    n = 0
    while True:
        num = n * n + 2 * n + 3    # 数列式
        num = yield num
        n += 1


def main_generator():
    """ジェネレータが返す値を使って処理を行う
    """
    def do_something(num):
        return (num % 2, num % 3)

    gen = note_num_generator()  # ジェネレータを作る
    for i in range(1, 10):
        num = next(gen)  # ジェネレータから次の値を取り出す
        result = do_something(num)
        print(i, result)


def note_main_gen(n):
    """main generator

    Args:
        n (int): sample number

    Yields:
        multi: yield multiple genre
    """
    yield "start"
    yield from range(n, 0, -1)  # サブイテレータから値を作る
    yield from "abc"            # サブイテレータから値を作る
    yield from [10, 20, 30]     # サブイテレータから値を作る
    yield from note_sub_gen()   # サブジェネレータから値を作る
    yield "end"


def note_sub_gen():
    """sub genereator

    Yields:
        str: sample string
    """
    yield "X"
    yield "Y"
    yield "Z"


def note_subgenerator():
    """サブジェネレータを持つジェネレータを実行する
    """
    gen = note_main_gen(3)
    print(list(gen))
