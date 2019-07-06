from random import randint

def make_a_guess(magic):
    x = input("What is your guess [1-10]? ")
    x = int(x)
    q = (x == magic)
    return q


if __name__ == "__main__":
    print("Welcome to the number guessing game!")

    max_guess = 5
    count = 0

    r = randint(1, 10)
    hit = False
    
    while count < max_guess:
        hit = make_a_guess(r)

        count += 1

        if hit == True:
            break

    if hit:
        print("You got it with ", count, " trials: magic number = ", r)
    else:
        print("You didn't get with ", count, " trials." )
            


