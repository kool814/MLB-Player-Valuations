#This is the file that we will use to parse the Batter, Pitcher, and Salary data
class BatterInfo:
    def __init__(self, stats):
        self.rank = stats[0]
        self.name = stats[1].split('\\')[0].strip()
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
        self.pos_sum = stats[29]
        self.pos = ''
        
        if stats[29] != '':
            self.pos = stats[29].replace("/", "").replace("*","")[0]
            
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
                allStats[tempBatter.name][tempBatter.team] = tempBatter

    for batter in allStats:
        if len(allStats[batter]) > 1: # if there is more than one team, make a xTM stat
            numTeams = len(allStats[batter])
            mostGP = ""
            for team in allStats[batter]:
                if mostGP == "" or allStats[batter][mostGP].g < allStats[batter][team].g:
                    mostGP = team
            #print(batter, mostGP, numTeams)
            allStats[batter]["2TM"] = allStats[batter][mostGP]
        #else:
            #print(batter, allStats[batter])
    
    return allStats
            
def calculateRC(batter):
    """
    RC = (hits + walk) * tot_bases / (ab + walk)
    """
    if (int(batter.ab) + int(batter.walk)) != 0:
        RC = (int(batter.hits) + int(batter.walk)) * int(batter.tot_bases) \
        /(int(batter.ab) + int(batter.walk))
    else:
        RC = -1
    return RC
    

            
def calculateWAR(batter, lgAvg):
    """
    Wins Above Replacement (meaning if they were replaced by an average player)
    WAR = (Runs + Positional Adjustment + League Avg Adjustment +Replacement Runs) / (Runs Per Win)
    
    Pos. Adj = ((At Bats/9) / 162) * (pos. specific run value)
    
    League Avg Adjustment = ((-1)*(Runs + lgPositional Adjustment) / lgPA)*PA
    
    Runs Per Win = 9*(MLB Runs Scored / At Bats)*1.5 + 3
    
2. Catcher: +12.5 runs (all are per 162 defensive games)
3. First Base: -12.5 runs
4. Second Base: +2.5 runs
5. Third Base: +2.5 runs
6. Shortstop: +7.5 runs
7. Left Field: -7.5 runs
8. Center Field: +2.5 runs
9. Right Field: -7.5 runs
D. Designated Hitter: -17.5 runs

    
    
    """
    pos_specific = {'2': 12.5, '3': -12.5, '4': 2.5, '5': 2.5,\
                    '6': 7.5, '7': -7.5, '8': 2.5, '9': -7.5, 'D': -17.5}
    
    pos_adj = ((int(batter.ab)/9.0)/162.0) * pos_specific[batter.pos]
    # league average batter has been passed into this function already
    # we can access it like a regular batter
    
    lg_adj = ((-1)*(int(lgAvg.runs)) / int(lgAvg.pa))*int(batter.pa)
    
    WAR = (int(batter.runs) + pos_adj + lg_adj)
    return WAR
    
    
def parseBatterData(fileName):
    f = open("2017_MLB_Batter_Info.md")
    data = []
    f.readline()
    for line in f:
        if line.strip().split(',')[-1] != '' :
            if '1' not in line.strip().split(',')[-1]: # exclude pitchers from the data
                data.append(line.strip().split(','))
        elif "LgAvg" in line.strip().split(',')[1]:
            lgAvg = BatterInfo(line.strip().split(','))
            #print(lgAvg)
    f.close()
    statDict = createDict(data)
    return statDict,lgAvg

if __name__ == "__main__":
    """
    f = open("2017_MLB_Batter_Info.md")
    data = []
    f.readline()
    for line in f:
        if line.strip().split(',')[-1] != '' :
            if '1' not in line.strip().split(',')[-1]:
                data.append(line.strip().split(','))
        elif "LgAvg" in line.strip().split(',')[1]:
            lgAvg = BatterInfo(line.strip().split(','))
            #print(lgAvg)
    f.close()
    statDict = createDict(data)
    """
    statDict, lgAvg = parseBatterData("2017_MLB_Batter_Info.md")
    
    for player in statDict:
        for team in statDict[player]:
            pass#print("{:.2f}".format(calculateWAR(statDict[player][team], lgAvg)))
            
    
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