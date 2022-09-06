import getpass
def guess_the_number(x,guess):
    if guess!=0:
        y=int(input('Choose the chosen  number'))
        if x==y:
            print("Great Job you have the right number")
            return
        elif x<y:
            print("The number is  bigger")
            guess-=1
            guess_the_number(x,guess)
        elif x>y:
            print("The number is smaller")
            guess-=1
            guess_the_number(x,guess)
    else:
        print("You are out of guesses  the right answer is:",x)
x=int(getpass.getpass(" Choose the Wanted Number: "))

g=int(input(" Choose the number of Avilable gusses"))
guess_the_number(x,g)


