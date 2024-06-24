from server.math import a
import os

def function_c():
    a.function_a()
    print("function c is called", os.getcwd())

if __name__ == "__main__":
    function_c()