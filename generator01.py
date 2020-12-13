# generator01.py

def test():
    print("A")
    yield 1
    print("B")
    yield 2
    print("C")

output = test()

print("D")

a = next(output)
print(a)

print("E")

b = next(output)
print(b)

print("F")
