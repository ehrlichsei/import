# in folder server/math, runable. python3 print_hello.py
# in folder server, runable. python3 math/print_hello.py
# in root, runable. python3 server/math/print_hello.py

from .b import b_function 


def function_a():
    b_function()
    print("function a is called")

if __name__ == "__main__":
    function_a()