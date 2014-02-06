create table games (engine TEXT NOT NULL, url TEXT NOT NULL, name TEXT PRIMARY KEY, oculus TEXT NOT NULL);

SELECT name FROM GAMES WHERE name = "ITWSBSWNTKEO! (I think we're stuck but still we need to kill each other!)";file:/C:/code/workspaces/Python/GlobalGameJamStats/pages/games.txtfile:/C:/code/workspaces/Python/GlobalGameJamStats/pages/games.txt

sqlite> select count(engine) from games where engine like "%Unity (any product)%";
2276

sqlite> select count(oculus) from games where oculus like "%yes%";
77

sqlite> select engine from games where oculus like "%yes%" group by engine;
 Flash
 Unity (any product)
 not found
Unity (any product)


sqlite> select count(engine) from games where oculus like "%yes%" and engine like "%Unity (any product)%" group by engine;
68
2

select count(engine) from games where engine like "%Apple Sprite%" group by engine;
select count(engine) from games where engine like "%Blender%" group by engine;
select count(engine) from games where engine like "%C++%" group by engine; 
select count(engine) from games where engine like "%cocos2d-x%" group by engine;
select count(engine) from games where engine like "%Construct%" group by engine; 
select count(engine) from games where engine like "%Corona SDK%" group by engine; 
select count(engine) from games where engine like "%DirectX%" group by engine; 
select count(engine) from games where engine like "%Duality%" group by engine; 
select count(engine) from games where engine like "%Flash%" group by engine; 
select count(engine) from games where engine like "%Game Maker%" group by engine; 
select count(engine) from games where engine like "%Java%" group by engine; 
select count(engine) from games where engine like "%LibGDX%" group by engine; 
select count(engine) from games where engine like "%pygame%" group by engine;
select count(engine) from games where engine like "%not found%" group by engine;
select count(engine) from games where engine like "%Unity (any product)%" group by engine;
select count(engine) from games where engine like "%Web standard%" group by engine;
select count(engine) from games where engine like "%XNA%" group by engine;

select count(engine) from games where engine like "%not found%" group by engine;

 
 