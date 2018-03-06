#This is the file that we will use to parse the Batter, Pitcher, and Salary data
class BatterInfo:
    def __init__(self, stats):
        self.rank = stats[0]
        self.name = stats[1]
        self.age = stats[2]
        self.team = stats[3]
        self.league = stats[4]
        self.g = stats[5]
        self.pa = stats[6]
        self.ab = stats[7]
        self.runs = stats[8]
        self.hits = stats[9]
        self.doubles = stats[10]
        self.triples = stats[11]
        self.hr = stats[12]
        self.rbi = stats[13]
        self.stolen = stats[14]
        self.caught = stats[15]
        self.walk = stats[16]
        self.strikeouts = stats[17]
        self.ba = stats[18]
        self.obp = stats[19]
        self.slg = stats[20]
        self.ops = stats[21]
        self.ops_plus = stats[22]
        self.tot_bases = stats[23]
        self.gdp = stats[24]
        self.hbp = stats[25]
        self.sac_bunt = stats[26]
        self.sac_fly = stats[27]
        self.ibb = stats[28]
        self.summary = stats[29]
        self.statList = stats
    
    def __str__(self):
        return str(self.statList)
    

def createDict(data):
    allStats = dict()
    for batter in data:
        tempBatter = BatterInfo(batter)
        if tempBatter.name not in allStats:
            # add the player
            allStats[tempBatter.name] = dict()
            allStats[tempBatter.name][tempBatter.team] = tempBatter
        else:
            # add the new team
            if tempBatter.team in allStats[tempBatter.name]:
                # add the one with a higher gp
                if int(allStats[tempBatter.name][tempBatter.team].g) < int(tempBatter.g):
                    allStats[tempBatter.name][tempBatter.team] = tempBatter                    
                    
            else:
                allStats[tempBatter.name] = dict()
                allStats[tempBatter.name][tempBatter.team] = tempBatter
            
    return allStats
            

f = open("2017_MLB_Batter_Info.md")
data = []
f.readline()
for line in f:
    data.append(line.strip().split(','))
    
f.close()

statDict = createDict(data)




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