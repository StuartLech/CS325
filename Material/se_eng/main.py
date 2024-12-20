#import module1.function1 as hi
from module1 import function1 as hello

def demo() -> None:
    hello.hello_world()

if __name__=="__main__":
    demo()