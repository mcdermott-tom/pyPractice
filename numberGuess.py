if __name__=="__main__":
    import random

    def compGuess(x):
        return(random.randint(1,x))

    def guess(x):
        random_num=random.randint(1,x)
        guess=0
        while(guess!=random_num):
            guess=int(input(f'Guess a number between 1 and {x}: '))
            if guess > random_num:
                print('\nToo high!')
            elif guess < random_num:
                print('\nToo low!')
            com=compGuess(x)
            print(f'\nCOM guessed {com}!\n')
            if com==random_num:
                print('COM has no intelligence and it managed to \
                    beat you! Good try, keep your chin up.')


        print(f"CONGRATS! You guessed {random_num}, the random number!\n")

    

    guess(200)
