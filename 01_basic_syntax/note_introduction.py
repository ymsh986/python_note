# coding: utf-8

def string_embedded():
    """fstring
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


if __name__ == "__main__":
    string_embedded()
