class calculator():
    n = int(input())
    square = n ** 2
    cube = n** 3
    square_root = n ** 0.5

    @staticmethod
    def greet():
        print("hello")

liza = calculator()
liza.greet()
print(liza.square,liza.cube,liza.square_root)


