valueDictionary = {'*': 0, '2': 2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def validatehand(hand):
    hand = list(hand[0:5].upper())
    hand = sorted(hand,reverse=True)
    totalvalue = 0
    allowone = False
    for var in hand:
        # print (var)
        if var not in valueDictionary:
            print(f'You used invalid value {var} - terminated with 0 value')
            totalvalue = 0
            break
            # return False

        if var == '*' and allowone == False:
            allowone = True
        elif var == '*' and allowone == True:
            print(f'You used multiple {var} - terminated with 0 value')
            totalvalue = 0
            break
            # return False
        totalvalue += valueDictionary.get(var)
    # print('Line 31', hand, totalvalue)
    return totalvalue

def recalculateValue(hand):
    totalvalue =0
    for var in (hand):
        totalvalue += valueDictionary.get(var)
    
    return totalvalue

def four_of_kind(hand, value):
    # hand = list(hand[0:5].upper())
    # hand = sorted(hand,reverse=True)
    listed = []
    card_dict = {}
    star_found = False
    for var in set(hand):
        count = hand.count(var)
        listed.append(count)
        card_dict[count] = var
        if var == '*':
            star_found = True
        
    
    listed.sort(reverse=True)
    if listed[0] == 4:
        totalhandvalue = value ** 7
        # strHand = ''.join(hand)
        return [hand, 'four-of-a-kind', totalhandvalue, star_found, card_dict]
    

def full_house(hand, value):
    # hand = list(hand[0:5].upper())
    # hand = sorted(hand,reverse=True)
    value_listed = []
    count = 0
    listed = []
    for var in set(hand):
        count = hand.count(var)
        value_listed.append(valueDictionary.get(var) * count)
        listed.append(count)

    listed.sort(reverse=True)
    value_listed.sort(reverse=True)
    if listed[0] == 3 and listed[1] == 2:
        totalhandvalue = value ** 6
        return [hand, 'full-house',totalhandvalue, value_listed]
 

def straight(hand, value):
    listed = []
    for var in (hand):
        listed.append(valueDictionary.get(var))

    listed.sort()
    if (listed[3] == 5 and listed[4] == 14):
        listed.remove(14)
        value =0
        for var in (hand):
            if valueDictionary.get(var) != 14:
                value += valueDictionary.get(var)

    pre_var = 0
    
    # i = 0
    for var in listed:
        # print(var)
        if pre_var == 0:
            pre_var = var - 1

        # print('pre_var', pre_var, 'var', var)
        if pre_var + 1 != var:
            # print('pre_var', pre_var, 'var', var)
            # break
            return None
        pre_var = var
            
    totalhandvalue = value ** 5
    return [hand, 'straight',totalhandvalue]

def three_of_a_kind(hand, value):
    count = 0
    listed =[]
    for var in set(hand):
        count = hand.count(var)
        listed.append(count)

    listed.sort(reverse=True)
    if listed[0] == 3:
        totalhandvalue = value ** 4
        # print(hand, 'three-of-a-kind', totalhandvalue)
        return [hand, 'three-of-a-kind',totalhandvalue]

def two_pair(hand, value):
    count = 0
    listed = []
    value_listed = []
    for var in set(hand):
        count = hand.count(var)
        listed.append(count)
        value_listed.append(valueDictionary.get(var) * count)
    
    listed.sort(reverse=True)
    value_listed.sort(reverse=True)
    if listed[0] == 2 and listed[1] == 2:
        totalhandvalue = value ** 3
        # print(hand, 'two-pair', totalhandvalue)
        return [hand, 'two-pair',totalhandvalue, value_listed]

def pair(hand, value):
    count = 0
    listed = []
    
    for var in set(hand):
        count = hand.count(var)
        listed.append(count)
    
    listed.sort(reverse=True)

    if listed[0] == 2:
        totalhandvalue = value ** 2
        return [hand, 'pair',totalhandvalue]

def high_card(hand, value):
    totalhandvalue = value 
    return [hand, 'high-card',totalhandvalue]

def compare_cards(deck1, deck2):
    card1 = validatehand(deck1)
    card2 = validatehand(deck2)
    if card1 > 0 and card2 > 0 :
        print('Both the cards are valid lets play')
    else:
        print('There were invalid cards we found, game terminated')
        return ''
        

    hand1 = classify(deck1, card1)
    hand2 = classify(deck2, card2)

    if (hand1[1] == 'four-of-a-kind' and hand2[1] == 'four-of-a-kind'):
        # print('two four-of-a-kind found do the extra processing')
        if (hand1[3] == True or hand2[3] == True):
            # print('Star found') # check which value is higher
            f_card_hand1_value = valueDictionary.get(hand1[4].get(4))
            f_card_hand2_value = valueDictionary.get(hand2[4].get(4))
            if f_card_hand1_value > f_card_hand2_value:
                return f'Hand 1 Wins (Hand 1 {hand1[0]}-{hand1[1]}) (Hand 2 {hand2[0]}-{hand2[1]})'
            if f_card_hand1_value < f_card_hand2_value:
                return f'Hand 2 Wins (Hand 1 {hand1[0]}-{hand1[1]}) (Hand 2 {hand2[0]}-{hand2[1]})'
            return f'Tie (Hand 1 {hand1[0]}-{hand1[1]}) (Hand 2 {hand2[0]}-{hand2[1]})'

    if (hand1[1] == 'full-house' and hand2[1] == 'full-house'):
        # print('two four-of-a-kind found do the extra processing')
        f_card_hand1_value = hand1[3][0]
        f_card_hand2_value = hand2[3][0]
        # print('Full House Hand 1', f_card_hand1_value,  ' Hand 2 ', f_card_hand2_value)
        if f_card_hand1_value > f_card_hand2_value:
            return f'Hand 1 Wins (Hand 1 {hand1[0]}-{hand1[1]}) (Hand 2 {hand2[0]}-{hand2[1]})'
        if f_card_hand1_value < f_card_hand2_value:
            return f'Hand 2 Wins (Hand 1 {hand1[0]}-{hand1[1]}) (Hand 2 {hand2[0]}-{hand2[1]})'
        return f'Tie (Hand 1 {hand1[0]}-{hand1[1]}) (Hand 2 {hand2[0]}-{hand2[1]})'

    if (hand1[1] == 'two-pair' and hand2[1] == 'two-pair'):
            # print('two four-of-a-kind found do the extra processing')
        f_card_hand1_value = hand1[3][0]
        f_card_hand2_value = hand2[3][0]
        # print('two-pair Hand 1', f_card_hand1_value,  ' Hand 2 ', f_card_hand2_value)
        if f_card_hand1_value > f_card_hand2_value:
            return f'Hand 1 Wins (Hand 1 {hand1[0]}-{hand1[1]}) (Hand 2 {hand2[0]}-{hand2[1]})'
        if f_card_hand1_value < f_card_hand2_value:
            return f'Hand 2 Wins (Hand 1 {hand1[0]}-{hand1[1]}) (Hand 2 {hand2[0]}-{hand2[1]})'
        f_card_hand11_value = hand1[3][1]
        f_card_hand21_value = hand2[3][1]
        if f_card_hand11_value > f_card_hand21_value:
                return f'Hand 1 Wins (Hand 1 {hand1[0]}-{hand1[1]}) (Hand 2 {hand2[0]}-{hand2[1]})'
        if f_card_hand11_value < f_card_hand21_value:
            return f'Hand 2 Wins (Hand 1 {hand1[0]}-{hand1[1]}) (Hand 2 {hand2[0]}-{hand2[1]})'
        return f'Tie (Hand 1 {hand1[0]}-{hand1[1]}) (Hand 2 {hand2[0]}-{hand2[1]})'

    if hand1[2] > hand2[2]:
        return f'Hand 1 Wins (Hand 1 {hand1[0]}-{hand1[1]}) (Hand 2 {hand2[0]}-{hand2[1]})'
    if hand2[2] > hand1[2]:
        return f'Hand 2 Wins (Hand 1 {hand1[0]}-{hand1[1]}) (Hand 2 {hand2[0]}-{hand2[1]})'
    # if hand2[2] == hand1[2]:
    return f'Tie (Hand 1 {hand1[0]}-{hand1[1]}) (Hand 2 {hand2[0]}-{hand2[1]})'

def classify(deck, cardvalue):
    deck = deck.upper()
    result = four_of_kind(deck, cardvalue)
    if result == None:
        result = full_house(deck, cardvalue)
    if result == None:
        result = straight(deck, cardvalue)
    if result == None:
        result = three_of_a_kind(deck, cardvalue)
    if result == None:
        result = two_pair(deck, cardvalue)
    if result == None:
        result = pair(deck, cardvalue)
    if result == None:
        result = high_card(deck, cardvalue)
    return result
