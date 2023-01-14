name = input ("Type your name: ")
print ('Welcome', name, 'to this adventure!')

answer = input('You are on a dirt road, it has come to an end you can go left or right. Which way do you wanna go? ').lower()

if answer == 'left':
    answer = input('You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ').lower()

    if answer =='swim':
        print('You swam accross and were eaten by an alligator.')
    elif answer == 'walk':
        print('You walked for many miles, ran out of water and you lost the game.')
    else:
        print ('Not a valid option. You lose.')

elif answer == 'right':
    answer = input('You come to a bridge. Do you want to cross it (cross/back?')

    if answer =='back':
        print('You came back to main road. And lose.')
    elif answer == 'cross':
        answer = input('You meet startnger. Talk (no/yes)? ')

        if answer =='yes':
            print('You talk to starnger, they give you gold. You win!')
        elif answer == 'no':
            print('You ignore sranger, he offends, you lose!')
        else:
            print ('Not a valid option. You lose.')
    else:
        print ('Not a valid option. You lose.')
else:
    print('Not a valid option. You lose.')

print('Thank you for trying', name)

