__author__ = 'Javier'


class Director():
    def __init__(self, listpage):
        self.listpage = listpage
        self.engines = ["Unity (any product)",
                        "Game Maker",
                        "Web standard", "XNA", "Apple Sprite",
                        "pygame",
                        # Web standard (HTML5, Java, JavaScript, Flash)

                        "Flash",
                        "DirectX",
                        "LibGDX",
                        "Java",
                        "Duality",
                        "Corona SDK",
                        "cocos2d-x", "Cocos2D-X",
                        "C++",
                        "Blender",
                        "minecraft",
                        "Construct 2"]
        self.enginesused = dict()
        for engine in self.engines:
            self.enginesused[engine] = 0
        self.readed = list()
        self.games = 0

    def search_games(self):
        read = True
        while read:
            for game in self.listpage.getGames():
                gamepage = self.listpage.goto_pagegame(game['url'])
                self.search_engines_in(gamepage)
            self.listpage.next_page()
            read = self.listpage.has_next_page()
            print "-- Next Page: ", self.listpage.pagecount+1, ", ", self.listpage.get_url()

            if (self.listpage.pagecount % 3) == 0:
                self.print_stats()
                self.save_results()


    def search_engines_in(self, gamepage):
        self.games += 1
        game = dict()
        game['name'] = gamepage.get_name()
        game['engine'] = ""
        game['engine'] = "not found"
        game['oculus'] = "no"
        game['url'] = gamepage.get_url()
        for engine in self.engines:
            source = gamepage.sourceHTML()
            if engine in source:
                self.enginesused[engine] += 1
                game['engine'] = engine
                break
        if "Oculus Rift" in source:
            game['oculus'] = "yes"
        #if  game['engine'] == "":
            #game['engine'] = "not found"
        self.readed.append(game)
        print game['engine'], ",", "oculus:", game['oculus'], ",", game['url']

    def print_stats(self):
        print "Games: ", self.games
        print "Engines: "
        unkown = 0
        for engine in self.engines:
            print engine, ": ", self.enginesused[engine]
            unkown +=  self.enginesused[engine]
        print "Unkown :", self.games - unkown


    def save_results(self):
        print "Saving.....", self.listpage.pagecount+2
        # "+str(self.listpage.pagecount)+"
        with open("games.txt", 'a') as f:
            for game in self.readed:
                f.write(str(game))
                f.write("\n")
        self.readed[:] = []


