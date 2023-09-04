def main():
    print("Hello, world!")
    a = int(input("Enter a number: "))
    number(a)
    


    game_over()


def number(a):
    print("You entered: ", a)

    if a % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
        
def game_over():
    print("Game over.")
    
    
    


main()
