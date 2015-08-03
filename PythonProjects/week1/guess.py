__author__ = 'Abdul'

"""
Write a program that generates a secret random number and asks the user to guess it.
It should count how many attempts were made before the number is guessed.
The program must also give hints to the user.
Example:
    python guess_a_number.py
    > Guess your number
    > 3
    > Wrong! Try with a larger one
    > 5
    > Wrong! Try with a smaller one
    > 4
    > You guessed correctly! The number was 4 indeed!
"""
import random


def guess_a_number():
    s = input('Guess your number: ')
    g = random.randint(0, 100)
    counter = 1

    while s != g:
        if s > g:
            print(g)
            print 'Wrong! Try with a smaller one'

        else:
            print(g)
            print 'Wrong! Try with a larger one'

        counter += 1
        s = input('Guess your number: ')

    print 'You guessed correctly! The number was %s indeed!' % g
    print 'You guessed %s times!' % counter

guess_a_number()
