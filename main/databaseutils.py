__author__ = 'Javier'

import sqlite3

class SQLiteDatabase():
    def __init__(self):
        self.conn = sqlite3.connect('../database/gamejam.db')

    def exist_name(self, name):
        c = self.conn.cursor()
        sql = """SELECT name FROM GAMES WHERE name = " """+ name + """ "; """
        #print sql
        try:
            res = c.execute(sql)
        except:
            print "Error in: ", sql
        return res.fetchone() <> None

    def execute_insert(self, stm):
        c = self.conn.cursor()
        try:
            c.execute(stm)
        except:
            print "Error in: ", stm
            None / 2
        self.conn.commit()

    def closeandopen(self):
        self.conn.commit()
        self.conn.close()
        self.conn = sqlite3.connect('../database/gamejam.db')

class File():
    def open(self):
        self.f = open("../pages/games.txt", "r")
    def nextgame(self):
        return eval(self.f.readline())
    def close(self):
        self.f.close()


class GUI():
    def game_exists(self, game):
        print "Game already exists: ", game
    def games_inserted(self, num):
       print "Games: ", num
    def inserted(self, game):
        print "Inserted: ", game

class InsertDatosFromTextFile():
    def __init__(self, database, file, gui = GUI()):
        self.database = database
        self.file = file
        self.gui = gui
        self.dbname = "games"

    def insert(self):
        self.file.open()
        self.games = 0
        game = self.file.nextgame()
        while game <> "" :
            name = game['name'].replace('\"', '')
            if not self.database.exist_name(name):
                sqlinsert = ("INSERT INTO "
                    + self.dbname
                    + """ VALUES (" """ + game['engine']
                    + """ ",' """+game['url'] + """ '," """
                    + name + """ ", ' """
                    +game['oculus'] + "');"
                )
                self.database.execute_insert(sqlinsert)
                self.gui.inserted(game)
                self.games += 1
            else:
                self.gui.game_exists(game)

            game = self.file.nextgame()
        self.file.close()
        self.gui.games_inserted(self.games)
