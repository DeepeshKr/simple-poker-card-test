from poker import *


# poker_dict = ['A','K','Q','J','T','1','2','3','4','5','6','7','8','9', '*']
print('Enter the Cards in Hand \n')  
print('Valid inputs AKQJT 123456789 and *  \n')  
print('Enter 5 Characters from above  \n')

hand1 = input ('Enter Hand 1: ')
print(f'You Entered {hand1.upper()}  \n')

# while hand1.upper() not in poker_dict:  
#     print('Enter Valid inputs AKQJT123456789*  \n')
#     hand1 = input ('Enter Valid Card for Hand 1: ')


hand2 = input ('Enter Hand 2: ')
print(f'You Entered {hand2.upper()}  \n')
# while hand1.upper() not in poker_dict:
#     print('Enter Valid inputs AKQJT123456789*  \n')
#     hand2 = input ('Enter Valid Card for Hand 2: ')

print(compare_cards(hand1, hand2))