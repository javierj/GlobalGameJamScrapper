__author__ = 'Javier'

import unittest

from globalgamejam.pages import GamePage, DetailPage
from testfixture import Fixture


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.client = Fixture().client
        self.page = GamePage(self.client)

    def test_get_games_link_from_html(self):
        page = GamePage(self.client)

        games = page.getGames()
        #print games
        self.assertEqual(games[0]['url'], u"http://globalgamejam.org/2014/games/return")

    def test_get_all_games(self):
        games = self.page.getGames()
        #print len(games)
        self.assertEqual(len(games), 25)

    #deprecated
    def test_go_to(self):
        self.assertEquals(self.client.count_click, 0)
        #self.page.go_to("")
        #self.assertEquals(self.client.count_click, 1)

    def test_goto_pagegame(self):
        gamepage = self.page.goto_pagegame("XX")
        self.assertEquals(gamepage.webclient.url, "XX")

    def test_next_url(self):
        url = self.page._next_url()
        self.assertEqual(url, "http://globalgamejam.org/2014/games?title=&country=All&city=&tools=All&diversifier=All&platforms=All&page=1")
        url = self.page._next_url()
        self.assertEqual(url, "http://globalgamejam.org/2014/games?title=&country=All&city=&tools=All&diversifier=All&platforms=All&page=2")
        url = self.page._next_url()
        self.assertEqual(url, "http://globalgamejam.org/2014/games?title=&country=All&city=&tools=All&diversifier=All&platforms=All&page=3")

    # deprecated
    def test_next_page(self):
        nextpage = self.page.next_page()
        #self.assertEqual(nextpage.webclient.url, "http://globalgamejam.org/2014/games?title=&country=All&city=&tools=All&diversifier=All&platforms=All&page=1")
        #nextpage = self.page.next_page()
        #self.assertEqual(nextpage.webclient.url, "http://globalgamejam.org/2014/games?title=&country=All&city=&tools=All&diversifier=All&platforms=All&page=2")


class TestDetailPage(unittest.TestCase):
    # dice que son distintos
    def test_sourceHTML(self):
        self.client = Fixture().client
        self.detail = DetailPage(self.client)

        #print self.detail.sourceHTML()
        #self.assertEquals(Fixture().html, self.detail.sourceHTML())

    def test_get_url(self):
        self.client = Fixture().client
        self.detail = DetailPage(self.client)
        self.assertEqual(self.detail.get_url(), self.client.url)



if __name__ == '__main__':
    unittest.main()
