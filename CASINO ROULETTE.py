import random
print("\tTHE ROULETTE GAME!!\n")
money = int(input('TOTAL AMOUNT INVESTING: '))
'\n'
op = 1
while op == 1:
    lucky_number = random.randint(0, 49)
    bet = int(input('AMOUNT TO BET: '))
    if bet > money or bet == 0:
        print('\nNOT ENOUGH MONEY TO CONTINUE ):')
        break
    selected_number = int(input('ENTER YOUR LUCKY NUMBER: '))
    money = money - bet
    print('THE LUCKY NUMBER IS ', lucky_number)
    if selected_number == lucky_number:
        '\n'
        print('\tCONGRATS YOU WON!!\n')
        bet = bet*50
        money = money+bet
        print('YOU WON ', bet)
        print('\nTOTAL AMOUNT IN HAND: ', money)
    else:
        print("\t!!BETTER LUCK NEXT TIME!!")
        print('TOTAL AMOUNT IN HAND: ', money)
    op = int(input('\nPRESS 1 TO CONTINUE: '))
print('\n THANKS FOR PLAYING! :)')
