from unittest import TestCase
from projects.watsonj3 import testUtility
from projects.watsonj3.dominion import Dominion



class TestAction_card(TestCase):

    def test_init(self):

        action_card = Dominion.Woodcutter()

        self.assertEqual(action_card.name, "Woodcutter")
        self.assertEqual(action_card.cost, 3)
        self.assertEqual(action_card.actions, 0)
        self.assertEqual(action_card.cards, 0)
        self.assertEqual(action_card.buys, 1)
        self.assertEqual(action_card.coins, 2)





