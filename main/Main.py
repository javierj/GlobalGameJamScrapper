__author__ = 'Javier'

from globalgamejam.process import Director
from globalgamejam.pages import WebClient, GamePage
import sys

client = WebClient("http://globalgamejam.org/2014/games")
mainpage = GamePage(client)
director = Director(mainpage)

try:
    director.search_games()
except:
    print "Unexpected error:", sys.exc_info()[0]
else:
    director.print_stats()

print "End."
