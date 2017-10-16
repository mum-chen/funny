def calc(n, step = 16):
    return step + ((not not n >> step).real and calc(n >> step, step))

data = [1 << i * 4 for i in range(17)]

def test_base(base):
    print("test base {}".format(base))
    for b in data:
        print(calc(b, base))

test_base(4)
test_base(8)
test_base(16)
test_base(32)
