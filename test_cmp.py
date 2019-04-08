# encoding=utf-8

def test_cmp():
    s = ['sss', 's_', 'a', 'sssss']
    s.sort(lambda a, b: 1 if len(b) < len(a) else -1)
    print s


if __name__ == "__main__":
    test_cmp()
