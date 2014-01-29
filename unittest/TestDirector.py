__author__ = 'Javier'

import unittest
from testfixture import Fixture
from globalgamejam.pages import GamePage
from globalgamejam.process import Director

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Fixture().client

    # Deprecated
    def test_director_enters_web(self):

        page = GamePage(self.client)

        director = Director(page)

        #director.search_games()

        #self.assertEquals(len(page.getGames()), self.client.count_click)

    def test_director_contains_multiset(self):
        page = GamePage(self.client)
        director = Director(page)

        self.assertEquals(len(director.engines), len(director.enginesused))

    # deprecated
    def test_search_engines_in(self):
        page = GamePage(self.client)
        director = Director(page)

        #director.search_engines_in(director.engines[0])
        #self.assertEquals(director.enginesused[director.engines[0]], 1)

if __name__ == '__main__':
    unittest.main()
