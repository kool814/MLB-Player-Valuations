#This is the file that we will use to parse the Batter, Pitcher, and Salary data

f = open("2017_MLB_Batter_Info.md")
data = []
for line in f:
    data.append(line.split(','))
    
f.close()

for item in data[0]:
    print(item)
"""
Rk = rank
Name
Age
Tm = Team
Lg = League
G = Games Played
PA = Plate Appearance
AB = At-bat
R = Runs
H = Hits
2B = Double
3B = Triple
HR = Home Run
RBI = Runs Batted In
SB = Stolen Base
CS = Caught Stealing
BB = Walk
SO = Strikeout
BA = Batting Average
OBP = On-Base Percentage
SLG = Slugging Percentage
OPS = On Base Plus Slugging
OPS+ = On Base Plus Slugging Plus
TB = Total Bases
GDP = Grounded Into Double Play
HBP = Hit By Pitch
SH = Sacrifice Bunt
SF = Sacrifice Fly
IBB = Intentional Walk
Pos Summary 
"""