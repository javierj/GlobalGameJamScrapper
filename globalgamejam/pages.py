__author__ = 'Javier'

from bs4 import UnicodeDammit, BeautifulSoup
from urllib2 import urlopen
import re

class WebClient():
    def __init__(self, url = None):
        self.url = url
        self.bs = None
    def sourceCode(self):
        if self.bs == None:
            self.html = urlopen(self.url)
            self.bs = BeautifulSoup(self.html)
        return self.bs
    def setUrl(self, url):
        self.url = url
        self.bs = None


class GamePage(object):
    def __init__(self, webclient):
        self.webclient = webclient
        self.pagecount = 22
        self.y2014 = re.compile("2014")
        self.result = list()

    def getGames(self):
        source = self.webclient.sourceCode()
        content = source.find('div', 'item-list')
        self.result[:] = []
        for gameinfo in content.find_all('a', href = self.y2014):
            game = {"url": "http://globalgamejam.org"+gameinfo['href']
            }
            self.result.append(game)

        return self.result

    def goto_pagegame(self, url):
        #self.webclient.click(url)
        return DetailPage(WebClient(url))

    def _next_url(self):

        url = ("http://globalgamejam.org/2014/games?title=&country=All&city=&tools=All&diversifier=All&platforms=All&page="
                 +str(self.pagecount) )
        self.pagecount -= 1
        return url
    def has_next_page(self):
        #next = self.pagecount + 1
        #return "/2014/games?title=&country=All&city=&tools=All&diversifier=All&platforms=All&page="+str(next) in str(self.webclient.sourceCode()) or "/2014/games?title=&amp;country=All&amp;city=&amp;tools=All&amp;diversifier=All&amp;platforms=All&amp;page="+str(next) in str(self.webclient.sourceCode())
        return next >= 0

    def next_page(self):
        self.webclient.setUrl(self._next_url())
    def get_url(self):
        return self.webclient.url

class DetailPage():
    def __init__(self, webclient):
        self.webclient = webclient

    def sourceHTML(self):
        source = self.webclient.sourceCode()
        return str(source)

    def get_name(self):
        source = self.webclient.sourceCode()
        uname = UnicodeDammit(source.find("h1").contents[0])
        return uname.unicode_markup

    def get_url(self):
        return self.webclient.url