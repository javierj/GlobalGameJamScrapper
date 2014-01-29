__author__ = 'Javier'


class Director():
    def __init__(self, listpage):
        self.listpage = listpage
        self.engines = ["Unity (any product)",
                        "Corona SDK", "C++", "Web standard", "XNA", "Apple Sprite",
                        "pygame",
                        "Flash",
                        "Game Maker",
                        "DirectX",
                        "Java",
                        "Duality"]
        self.enginesused = dict()
        for engine in self.engines:
            self.enginesused[engine] = 0
        self.readed = list()

    def search_games(self):
        read = True
        while read:
            for game in self.listpage.getGames():
                gamepage = self.listpage.goto_pagegame(game['url'])
                self.search_engines_in(gamepage)
            self.listpage.next_page()
            read = self.listpage.has_next_page()
            print "Page: ", self.listpage.pagecount

            if (self.listpage.pagecount % 10) == 0:
                self.print_stats()


    def search_engines_in(self, gamepage):
        game = dict()
        game['name'] = gamepage.get_name()
        game['engine'] = ""
        game['engine'] = "not found"
        game['oculus'] = "no"
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
        print game

    def print_stats(self):
        print "Games: ", len(self.readed)
        print "Engines: "
        for engine in self.engines:
            print engine, ": ", self.enginesused[engine]
        self.save_results()

    def save_results(self):
        print "Saving....."
        with open("games"+str(self.listpage.pagecount)+".txt", 'w') as f:
            for game in self.readed:
                f.write(str(game))
                f.write("\n")

