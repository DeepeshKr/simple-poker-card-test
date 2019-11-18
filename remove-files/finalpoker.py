def main(players=2):
    """
    (players) -> number of players in this game
    """
    Pcard = []
    i2 = 0
    while len(Pcard) < players:
        P2 = (input("Player "+str(len(Pcard)+1)+" -- input your card: "))
        Pcard.append(P2.split())
        i2 += 1
    hand_rank = []
    print("==============Result==============")
    for i in xrange(players):
        hand_rank.append(check_hand_rank(Pcard[i]))
        if hand_rank[i][0] == 0:
            print("Player "+str(i+1)+" have: High card")
        elif hand_rank[i][0] == 1:
            print("Player "+str(i+1)+" have: One pair")
        elif hand_rank[i][0] == 2:
            print("Player "+str(i+1)+" have: Two pair")
        elif hand_rank[i][0] == 3:
            print("Player "+str(i+1)+" have: Three of a kind")
        elif hand_rank[i][0] == 4:
            print("Player "+str(i+1)+" have: Straight")
        elif hand_rank[i][0] == 5:
            print("Player "+str(i+1)+" have: Flush")
        elif hand_rank[i][0] == 6:
            print("Player "+str(i+1)+" have: Full house")
        elif hand_rank[i][0] == 7:
            print("Player "+str(i+1)+" have: Four of a kind")
        elif hand_rank[i][0] == 8:
            print("Player "+str(i+1)+" have: Straight flush")
        elif hand_rank[i][0] == 9:
            print("Player "+str(i+1)+" have: Royal straight flush")
    if len(str(winner(hand_rank)))/2 >= 2:
        return  "-- >" + 'Winner are players: ' +str(winner(hand_rank)) + " < --"
    return "-- > The Winner is player: " + str(winner(hand_rank))+ " < --"

def check_hand_rank(hand):
        """
        (hand) -> list
        This function use to check hand rank
        return list of hand rank
        ======
        Royal straight flush = 9
        Straight flush = 8
        Four of a kind = 7
        Full house = 6
        Flush = 5
        Straight = 4
        Three of a kind = 3
        Two pair = 2
        One pair = 1
        High card = 0
        """
        card_rank = ['--23456789TJQKA'.index(n) for n,h in hand]
        card_rank.sort()
        card_rank.reverse()
        #for royal straight flush
        card_rank_rsf = ['HDSC'.index(h) for n,h in hand]
        card_rank_rsf.sort()
        card_rank_rsf.reverse()
        if card_rank == [14,5,4,3,2]:
                card_rank = [5,4,3,2,1]
        if royal_straight_flush(hand):
                return 9,card_rank_rsf[0]
        elif straight_flush(hand):
                return 8,max(card_rank)
        elif four_of_a_kind(hand):
                return 7,max(card_rank)
        elif full_house(hand):
                tong = 0
                kuu = 0
                s = [n for n,h in hand]
                for i in xrange(len(s)):
                        if(s.count(s[i])==3):
                           tong = s[i]
                        else:
                           kuu = s[i]
                return 6,int(tong),int(kuu)
        elif flush(hand):
                return 5,max(card_rank)
        elif straight(hand):
                return 4,max(card_rank)
        elif three_of_a_kind(hand):
            ld = 0
            a = 0
            for i in xrange(0,3):
                if card_rank.count(card_rank[i]) > 1 :
                    ld = (card_rank[i])
                else:
                    a = card_rank[i]
            return 3,ld,a
        elif two_pair(hand):
            ld = []
            a = 0
            for i in xrange(0,3):
                if card_rank.count(card_rank[i]) >=2:
                    ld.append(card_rank[i])
                    card_rank.pop(i)
                else:
                    a = card_rank[i]
            ld.sort(reverse=True)
            return 2,ld[0],ld[1],a
        elif one_pair(hand):
            ld = 0
            a = []
            for i in xrange(len(card_rank)):
                if card_rank.count(card_rank[i]) > 1 :
                    ld = (card_rank[i])
                else:
                    a.append(card_rank[i])
            a.sort(reverse = True)
            return 1,ld,a[0],a[1],a[2]
        else:
                return 0,max(card_rank)

poker_dict = ['A','K','Q','J','T','1','2','3','4','5','6','7','8','9', '*']
while(True):
    select = input("[+] Select Mode [+]\n 1.)Start Game\n 2.)Exit \n\nInput number : ")
    if select.isdigit() and (select == '1'):
        if select == '1':
            print('==============Poker Start==============')
            print('  Starting 2 Player Game: ')
            main(2)
        else:
            print('  Starting 2 Player Game: ')
            break
    else:
        print('  Invalid input exiting game: ')
        break
        

# if __name__ == '__main__':
# 	import doctest
# 	doctest.testmod()

def validate ():
    poker_dict = ['A','K','Q','J','T','1','2','3','4','5','6','7','8','9', '*']
    print('Enter the Cards in Hand \n')  
    print('Valid inputs AKQJT 123456789 and *  \n')  
    print('Enter 5 Characters from above  \n')

    hand1 = input ('Enter Hand 1: ')
    print('You entered' + hand1.upper())
    while hand1.upper() not in poker_dict:
        print('Enter Valid inputs AKQJT123456789*  \n')
        hand1 = input ('Enter Valid Card for Hand 1: ')
    hand2 = input ('Enter Hand 2: ')
    print('You entered' + hand1.upper())
    while hand1.upper() not in poker_dict:
        print('Enter Valid inputs AKQJT123456789*  \n')
        hand2 = input ('Enter Valid Card for Hand 2: ')