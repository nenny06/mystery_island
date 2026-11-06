import unittest
from game import new_game, available_actions, is_win, apply_action


class TestNewGame(unittest.TestCase):

    def test_new_game(self):
        player = new_game()

        self.assertEqual(player["energy"], 5)
        self.assertEqual(player["inventory"], [])
        self.assertEqual(player["current_location"], "Beach")
        self.assertEqual(player["bridge_crossed"],False)

    def test_available_actions(self):
        actions = available_actions()

        self.assertIn("Explore Beach", actions)
        self.assertIn("Explore Jungle", actions)
        self.assertIn("Explore Cave", actions)
        self.assertIn("Visit Old Bridge", actions)
        self.assertIn("Visit Lighthouse", actions)
        self.assertIn("Check Inventory", actions)
        self.assertIn("Quit Game", actions)
        self.assertEqual(len(actions), 7)

    def test_is_win(self):
        #player = new_game


        player = {
        "inventory": ["Rope", "Lantern"],
        "energy": 5,
        "visited_locations": [
            "Beach",
            "Jungle",
            "Cave",
            "Old Bridge",
            "Lighthouse"
        ],
        "current_location": "Lighthouse",
        "bridge_crossed": True
    }

        self.assertTrue(is_win(player))

    def test_player_loses_without_energy(self):

        player = {
        "inventory": ["Rope", "Lantern"],
        "energy": 0,
        "visited_locations": [
            "Beach",
            "Jungle",
            "Cave",
            "Old Bridge",
            "Lighthouse"
        ],
        "current_location": "Lighthouse",
        "bridge_crossed": True
    }

        self.assertFalse(is_win(player))

    
    def test_player_loses_without_Rope(self):

        player = {
        "inventory": ["Lantern"],
        "energy": 5,
        "visited_locations": [
            "Beach",
            "Jungle",
            "Cave",
            "Old Bridge",
            "Lighthouse"
        ],
        "current_location": "Lighthouse",
        "bridge_crossed": True
    }

        self.assertFalse(is_win(player))



    def test_player_loses_without_Lantern(self):

        player = {
        "inventory": ["Rope"],
        "energy": 5,
        "visited_locations": [
            "Beach",
            "Jungle",
            "Cave",
            "Old Bridge",
            "Lighthouse"
        ],
        "current_location": "Lighthouse",
        "bridge_crossed": True
    }

        self.assertFalse(is_win(player))


    def test_player_loses_without_crossing_bridge(self):

        player = {
            "inventory": ["Rope", "Lantern"],
            "energy": 5,
            "visited_locations": [
                "Beach",
                "Jungle",
                "Cave",
                "Old Bridge",
                "Lighthouse"
            ],
            "current_location": "Lighthouse",
            "bridge_crossed": False
    }
        self.assertFalse(is_win(player))


    def test_collect_rope(self):
        player = new_game()

        apply_action(player, "Explore Beach", "yes")

        self.assertIn("Rope", player["inventory"])
        self.assertEqual(player["energy"], 7)


    def test_player_refuses_rope(self):
        player = new_game()

        apply_action(player, "Explore Beach", "no")
        self.assertNotIn("Rope", player["inventory"])
        self.assertEqual(player["energy"], 5)


    def test_collect_lantern(self):
        player = new_game()

        apply_action(player, "Explore Jungle", "yes")
        
        self.assertIn("Lantern", player["inventory"])
        self.assertEqual(player["energy"], 6)
        self.assertIn("Jungle", player["visited_locations"])


    def test_player_refuses_lantern(self):
        player = new_game()

        apply_action(player, "Explore Jungle", "no")

        self.assertNotIn("Lantern", player["inventory"])
        self.assertEqual(player["energy"], 4)
        self.assertIn("Jungle", player["visited_locations"])

'''
    def test_revisit_jungle(self):
        player = new_game()

        apply_action(player, "Explore Jungle", "no")

        apply_action(player, "Explore Beach", "no")

        apply_action(player, "Explore Jungle", "no")

        self.assertEqual(player["energy"], 2)

        '''





        



    

