from random import randint

def make_a_guess(magic):
    x = input("What is your guess [1-10]? ")
    x = int(x)
    q = (x == magic)
    return q


if __name__ == "__main__":
    print("Welcome to the number guessing game!")

    r = randint(1, 10)
    
    while True:
        hit = make_a_guess(r)

        if hit == True:
            print("You got it! r = ", r)
            break


