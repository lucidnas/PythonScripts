import random

def guess_a_number():
    s = input('Guess your number: ')
    g = random.randint(0,100)
    counter = 1

    while s != g:
        if s > g:
            print(g)
            print 'Wrong! Try with a smaller one'
            counter += 1
            s = input('Guess your number: ')
            #guess_a_number()
        
        else:
            print(g)
            print 'Wrong! Try with a larger one'
            counter += 1
            s = input('Guess your number: ')
            #guess_a_number()

    print 'You guessed correctly! The number was %s indeed!'%g
    print 'You guessed %s times!'%counter
        

guess_a_number()
        
