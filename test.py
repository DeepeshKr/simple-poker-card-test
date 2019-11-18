import unittest
from poker import *

class TestSum(unittest.TestCase):
    def test_values_returned(self):
        """
        Test that it can sum a list of cards
        """
        data = "aaakt"
        result = validatehand(data)
        self.assertEqual(result, 65)

    def test_five_cards_returned(self):
        """
        Test that it would pick only 5 cards
        """
        data = "aaaktq3"
        result = validatehand(data)
        self.assertEqual(result, 65)
       
    def test_no_double_star(self):
        """
        Test that no double star is allowed
        """
        data = "aaa**"
        result = validatehand(data)
        self.assertEqual(result, 0)

    def test_four_of_kind(self):
        """
        check if four of a kind
        four-of-a-kind (4 cards of the same value: AAAA5)
        """
        data = "AAAAK"
        result = four_of_kind(data, 100)
        # print('Test Result',result)
        self.assertEqual(result, ['AAAAK', 'four-of-a-kind', 100000000000000, False, {1: 'K', 4: 'A'}])
    
    def test_four_of_kind_star(self):
        """
        check if four of a kind
        four-of-a-kind (4 cards of the same value: AAAA5)
        """
        data = "AAAA*"
        result = four_of_kind(data, 100)
        # print('Test Result',result)
        self.assertEqual(result, ['AAAA*', 'four-of-a-kind', 100000000000000, True, {1: '*', 4: 'A'}])
    
    def test_not_four_of_kind(self):
        """
        check if four of a kind
        four-of-a-kind (4 cards of the same value: AAAA5)
        """
        data = "AAAKK"
        result = four_of_kind(data, 100)
        self.assertNotEqual(result, ['AAAAK', 'four-of-a-kind', 100000000000000])

    def test_full_house(self):
        """
        check if four of a kind
        full house (3 of one, and 2 of another: KKKQQ)
        """
        data = "AAAKK"
        result = full_house(data, 100)
        self.assertEqual(result, ['AAAKK', 'full-house', 1000000000000, [42, 26]])

    def test_not_full_house(self):
        """
        check if NOT four of a kind
        full house (3 of one, and 2 of another: KKKQQ)
        """
        data = "AAJKK"
        result = full_house(data, 100)
        self.assertNotEqual(result, ['AAAKK', 'full-house', 1000000000000, [42, 26]])

    def test_straight(self):
        """
        check if straight
        straight (all 5 in sequential order: 6789T)
        """
        data = "6789T"
        result = straight(data, 100)
        self.assertEqual(result, ['6789T', 'straight', 10000000000])
    
    def test_straight_exception(self):
        """
        check if straight
        straight (all 5 in sequential order: 6789T)
        Straights are compared by the highest card in the hand, except for A2345, in which case the 5 is considered the highest card in the straight.
        """
        data = "A2345"
        result = straight(data, 100)
        self.assertEqual(result, ['A2345', 'straight', 537824])

    def test_not_straight(self):
        """
        check if NOT straight
        straight (all 5 in sequential order: 6789T)
        """
        data = "6789K"
        result = straight(data, 100)
        self.assertNotEqual(result, ['6789T', 'straight', 10000000000])

    def test_three_of_a_kind (self):
        """
        check if three-of-a-kind
        three-of-a-kind (3 cards of the same value: KKK23)
        """
        data = "KKK23"
        result = three_of_a_kind(data, 100)
        # print('Result Three of Kind', result)
        self.assertEqual(result, ['KKK23', 'three-of-a-kind', 100000000])
    
    def test_not_three_of_a_kind (self):
        """
        check if NOT three-of-a-kind
        three-of-a-kind (3 cards of the same value: KKK23)
        """
        data = "KKJ23"
        result = three_of_a_kind(data, 100)
        self.assertNotEqual(result, ['KKK23', 'three-of-a-kind', 100000000])
    
    def test_two_pair (self):
        """
        check if two-pair
        two pair (AA33J)
        """
        data = "AA33J"
        result = two_pair(data, 100)
        self.assertEqual(result,['AA33J', 'two-pair', 1000000,[28, 11, 6]])

    def test_not_two_pair (self):
        """
        check if NOT two-pair
        two pair (AA33J)
        """
        data = "AA32J"
        result = two_pair(data, 100)
        self.assertNotEqual(result,['AA33J', 'two-pair', 1000000,[28, 11, 6]])
    
    def test_pair (self):
        """
        check if pair
        pair (44KQA)
        """
        data = "44KQA"
        result = pair(data, 100)
        self.assertEqual(result, ['44KQA', 'pair', 10000])

    def test_not_pair (self):
        """
        check if not pair
        pair (44KQA)
        """
        data = "43KQA"
        result = pair(data, 100)
        self.assertNotEqual(result, ['44KQA', 'pair', 10000])
    
    def test_high_card (self):
        """
        check if high card
        high card (nothing else: A267J)
        """
        data = "A267J"
        result = high_card(data, 100)
        self.assertEqual(result, ['A267J', 'high-card', 100])

    def test_compare_cards_1 (self):
        """
        test to compare_cards three-of-a-kind to full-house
        AAAKT three-of-a-kind < 22233 full house
        """
        data1 = "AAAKT"
        data2 = "22233"
        result = compare_cards(data1, data2)
        self.assertEqual(result, 'Hand 1 Wins (Hand 1 AAAKT-three-of-a-kind) (Hand 2 22233-full-house)')

    def test_compare_cards_2 (self):
        """
        test to compare_cards straight to two-pair
        2345* straight > KKJJ2 two pair
        """
        data1 = "2345*"
        data2 = "KKJJ2"
        result = compare_cards(data1, data2)
        self.assertEqual(result, 'Hand 1 Wins (Hand 1 2345*-straight) (Hand 2 KKJJ2-two-pair)')

    def test_compare_cards_3 (self):
        """
        test to compare_cards two-pair == two-pair
        AAKKT two pair == AAKKT two pair
        """
        data1 = "AAKKT"
        data2 = "AAKKT"
        result = compare_cards(data1, data2)
        self.assertEqual(result, 'Tie (Hand 1 AAKKT-two-pair) (Hand 2 AAKKT-two-pair)')

    def test_compare_cards_4 (self):
        """
        test to compare_cards two-pair == two-pair
        KKKKA four-of-a-kind == KKKK* four-of-a-kind
        """
        data1 = "KKKKA"
        data2 = "KKKK*"
        result = compare_cards(data1, data2)
        self.assertEqual(result, 'Tie (Hand 1 KKKKA-four-of-a-kind) (Hand 2 KKKK*-four-of-a-kind)')

    def test_compare_cards_5 (self):
        """
        test to compare_cards compare the highest pair first
        When comparing two pair hands, compare the highest pair first, then the next pair. i.e. AA223 > KKQQT, since AA > KK.
        """
        data1 = "AA223"
        data2 = "KKQQT"
        result = compare_cards(data1, data2)
        self.assertEqual(result, 'Hand 1 Wins (Hand 1 AA223-two-pair) (Hand 2 KKQQT-two-pair)')
    
    def test_compare_cards_6 (self):
        """
        test to compare_cards compare the highest pair first
        When the highest pair is a tie, move on to the next pair. i.e. AA993 > AA88K.
        """
        data1 = "AA993"
        data2 = "AA88K"
        result = compare_cards(data1, data2)
        self.assertEqual(result, 'Hand 1 Wins (Hand 1 AA993-two-pair) (Hand 2 AA88K-two-pair)')

    def test_compare_cards_7 (self):
        """
        test to compare_cards compare the highest pair first
        Similarly, when comparing full house hands, the three-card group is compared first. AAA22 > KKKQQ
        """
        data1 = "AAA22"
        data2 = "KKKQQ"
        result = compare_cards(data1, data2)
        self.assertEqual(result, 'Hand 1 Wins (Hand 1 AAA22-full-house) (Hand 2 KKKQQ-full-house)')

    def test_compare_cards_8 (self):
        """
        test to compare_cards compare the highest pair first
        In the case of ties, determine a winner by comparing the next highest card in the hand. i.e. AA234 < AA235 because AAs tie, 2s tie, 3s tie, but 4 < 5.
        """
        data1 = "AA234"
        data2 = "AA235"
        result = compare_cards(data1, data2)
        self.assertEqual(result, 'Hand 2 Wins (Hand 1 AA234-pair) (Hand 2 AA235-pair)')
    
    def test_compare_cards_9 (self):
        """
        test to compare_cards compare the highest pair first
        In the case of ties, determine a winner by comparing the next highest card in the hand. i.e. AA234 > KK235.
        """
        data1 = "AA234"
        data2 = "KK235"
        result = compare_cards(data1, data2)
        self.assertEqual(result, 'Hand 1 Wins (Hand 1 AA234-pair) (Hand 2 KK235-pair)')

    def test_compare_cards_10 (self):
        """
        test to compare_cards compare the highest pair first
        Straights are compared by the highest card in the hand, except for A2345, in which case the 5 is considered the highest card in the straight.
        """
        data1 = "A2345"
        data2 = "23456"
        result = compare_cards(data1, data2)
        self.assertEqual(result, 'Hand 2 Wins (Hand 1 A2345-straight) (Hand 2 23456-straight)')

if __name__ == '__main__':
    unittest.main()