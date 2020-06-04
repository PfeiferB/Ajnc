import unittest
from anjc import Anjc

class AnjcTestCase(unittest.TestCase):
    def test_size_of_deck(self):
        game_test = Anjc()
        deck = game_test.create_deck()
        self.assertEqual(len(deck), 52, "Deck ima 52 karte")
    
    def test_shuffle_randomizes_deck(self):
        game_test = Anjc()
        deck_one = game_test.create_deck()
        deck_one = game_test.shuffle_deck(deck_one)
        deck_two = game_test.create_deck()
        deck_two = game_test.shuffle_deck(deck_two)
        self.assertNotEqual(str(deck_one), str(deck_two), "Karte su promiješanje")
    
    def test_deal_removes_a_card(self):
        game_test = Anjc()
        deck = game_test.create_deck()
        inital_deck_num = len(deck)
        card = game_test.deal_card(deck)
        after_deal_deck_num = len(deck)
        self.assertEqual(inital_deck_num, after_deal_deck_num + 1, "Miče se jedna karata iz decka")
    
    def test_does_a_new_card_get_added_in_hand(self):
        game_test = Anjc()
        deck = game_test.create_deck()
        hand = game_test.deal_card(deck)
        self.assertEqual(len(hand), 1, "Imam jednu kartu u ruci")
        hand = game_test.add_card_in_hand(hand, deck)
        self.assertEqual(len(hand), 2, "Imam dvije karte u ruci")
    
    def test_sum_cards_in_SPIL(self):
        game_test = Anjc()
        hand = ['Dama', 'Kralj', 'Kec']
        summed_card_values = game_test.sum_cards_values(hand)
        self.assertEqual(summed_card_values, 21, "Vrijednost karata treba biti 21")
        
    def test_value_of_cards_in_SPIL(self):
        game_test = Anjc()
        card = game_test.SPIL['Dama']
        self.assertEqual(card, 10, "Vrijednost Dame je 10")
        card = game_test.SPIL['Kralj']
        self.assertEqual(card, 10, "Vrijednost Kralja je 10")
        card = game_test.SPIL['Kec']
        self.assertEqual(card, 1, "Vrijednost Keca je 1")
        
    def test_card_kec_value(self):
        game_test = Anjc()
        kec = list(game_test.SPIL.keys())[list(game_test.SPIL.values()).index(1)]
        self.assertEqual(kec, "Kec", "Kec ima vrijednost 1")
    
    
    
    
    
    

if __name__ == "__main__":
    unittest.main()
    