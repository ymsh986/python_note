# coding: utf-8

from datetime import datetime

class Car:
    """車情報を保持するクラス
    """
    # クラス変数
    maker = "PEACE"  # 自動車メーカー
    count = 0  # 台数

    # クラスメソッド
    @classmethod
    def countup(cls):
        cls.count += 1
        print(f"出荷台数：{cls.count}")

    # 初期化メソッド
    def __init__(self, color="white"):
        Car.countup()  # カウントアップする
        self.mynumber = Car.count  # 自分の番号
        self.color = color  # 引数で受け取った値を代入
        self.mileage = 0  # 0からスタート

    # インスタンスメソッド
    def drive(self, km):
        self.mileage += km
        msg = f"{km}kmドライブしました。総距離は{self.mileage}kmです。"
        print(msg)


def note_class_car():
    """Carクラスの試行
    """
    car1 = Car()
    car2 = Car('red')
    car3 = Car('blue')
    print(car1.mynumber)
    print(car2.mynumber)
    print(car3.mynumber)
    car1.drive(100)
    print(car1.mileage)
    print(car2.color)
    print(car3.mileage)


class Datalog:
    """スーパークラスサンプル
    """
    # 初期化メソッド
    def __init__(self):
        self.loglist = []

    # インスタンスメソッド
    def log(self, data):
        now = datetime.now()  # 現在の日時データ
        item = (now, data)  # タプルを作る
        self.loglist.append(item)  # loglistリストに追加する


class Mydata(Datalog):
    """Datalogクラスを継承したMydataクラス

    Args:
        Datalog (class): スーパークラス
    """

    def printlog(self):
        # スーパークラスのインスタンス変数の値を取り出す
        for date, data in self.loglist:
            print(date, data)


def note_datalog():
    """サブクラスであるMydataの試行
    """
    obj = Mydata()
    obj.log("あいう")  # スーパークラスのインスタンスメソッドを実行
    obj.log("abc")
    obj.log(123)
    obj.printlog()  # サブクラスのインスタンスメソッドを実行


class Greet():
    """スーパークラス
    """
    def hello(self):
        print("やあ！")

    def bye(self):
        print("さよなら")


class Greet2(Greet):
    """Greetクラスを継承したGreet2クラス

    Args:
        Greet (class): スーパークラス
    """

    # スーパークラスのメソッドをオーバーライドする
    def hello(self, name=None):
        if name:
            print(name + "さん、こんにちは！")
        else:
            super().hello()    # スーパークラスのhello()をそのまま使う


def note_override():
    obj = Greet2()
    obj.hello('Yamamoto')
    obj.hello()


class Person():
    """スーパークラスのサンプル
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Player(Person):
    """Personクラスを継承したPlayerクラス

    Args:
        Person (class): スーパークラス
    """
    def __init__(self, name, age, number, position):
        super().__init__(name, age)  # スーパークラスの初期化メソッドを呼び出す
        self.number = number
        self.position = position


def note_subclass_init():
    player1 = Player('Yamamoto', 10, 20, 'MF')
    print(player1.name)
    print(player1.age)
    print(player1.number)
    print(player1.position)


class Person2():
    """非公開のインスタンス変数を設定するクラス
    """
    def __init__(self, name):
        self.__name = name    # 非公開のインスタンス変数

    def who(self):
        print(self.__name + "です。")


def note_person_sample():
    """非公開のインスタンス変数が設定されていることを確認する関数
    """
    man = Person2('Yamamoto')
    man.who()
    print(man.__name)  # 'Person' object has no attribute '__name' とエラーになる
