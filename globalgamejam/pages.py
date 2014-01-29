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
        self.pagecount = 0

    def getGames(self):
        source = self.webclient.sourceCode()
        content = source.find('div', 'item-list')
        result = list()
        y2014 = re.compile("2014")
        for gameinfo in content.find_all('a', href = y2014):
            game = {"name": "name",
                      "url": "http://globalgamejam.org"+gameinfo['href']
            }
            result.append(game)

        return result

    def goto_pagegame(self, url):
        #self.webclient.click(url)
        return DetailPage(WebClient(url))

    def next_url(self):
        self.pagecount += 1
        return "http://globalgamejam.org/2014/games?title=&country=All&city=&tools=All&diversifier=All&platforms=All&page="+str(self.pagecount)

    def has_next_page(self):
        next = self.pagecount + 1
        #return "/2014/games?title=&country=All&city=&tools=All&diversifier=All&platforms=All&page="+str(next) in str(self.webclient.sourceCode()) or "/2014/games?title=&amp;country=All&amp;city=&amp;tools=All&amp;diversifier=All&amp;platforms=All&amp;page="+str(next) in str(self.webclient.sourceCode())
        return next < 172

    def next_page(self):
        nexturl = self.next_url()
        self.webclient.setUrl(nexturl)


class DetailPage():
    def __init__(self, webclient):
        self.webclient = webclient

    def sourceHTML(self):
        source = self.webclient.sourceCode()
        return str(source)

    def get_name(self):
        source = self.webclient.sourceCode()
        return source.find("h1").contents[0]