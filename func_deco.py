# func_deco.py

def test(function):
    def wrapper():
        print("start")
        function()
        print("end")

    return wrapper

@test
def hello():
    print("hello")

hello()
