#This is the file that we will use to parse the Batter, Pitcher, and Salary data

#Dictionary with key: Player and value: Dictionary containing key:Team and value: stats 

import math
from Pitcher import *

def parse_salary_data(salary_dict, salary_data):
    '''
    Given the salary data info, parse the info and store the player, team, 
    and yearly salary data.
    '''
    #data = open(salary_data, "r")

    with open(salary_data) as data_parse:
        for line in data_parse:
            line = line.strip().split(",")

            player_name_split_space=line[1].split()
            player_name=player_name_split_space[0]

            if(len(player_name_split_space)>=2):
                player_name +=" "
                player_name +=player_name_split_space[1]
            
            team= line[3]
            salary= line[21]
            if(salary==''):
                if(line[22]=='Free Agency' or line[22]=='Traded' or line[22]=='Amateur Free Agent' or 
                    line[22]=='Waivers' or line[22]=='Purchased'):
                    salary='520000'
                if(line[22]=='Amateur Draft'):
                    salary='543750'
            
            team_dict={}
            team_dict[team]=salary
            
            if player_name in salary_dict:
                ''' if the player is already in the dictionary, then add them to another team '''
                salary_dict[player_name].update(team_dict)
            else:
                ''' add them to the dictionary'''
                # print(salary_dict)
                salary_dict[player_name]=team_dict
    
            # print(player_name)

def parse_pitcher_data(pitcher_dict, pitcher_data):
    
    with open(pitcher_data) as data:
        
        firstline = True
        for line in data:
            if firstline:
                firstline = False
                continue
            line = line.strip().split(",")
            
            playername = line[1].strip().split(" ")
            name = ""
            for i in range(len(playername)-1):
                name += (" " + playername[i])
            name = name.strip()
            
            p = Pitcher(name, line[2],line[3], line[4])
            p.set_wl(line[5],line[6],line[7])
            p.set_stats(line[8:])
            team = line[3]
            if name in pitcher_dict.keys():
                pitcher_dict[name][team] = p
            else:
                team_dict = {}
                team_dict[team] = p
                pitcher_dict[name] = team_dict

            



if __name__ == "__main__":
    salary_data_dict = {}
    salary_data_dict['player'] = {}
    salary_data_dict['player']['team'] = 'stats'
    #print(salary_data_dict)

    parse_salary_data(salary_data_dict,"2017_MLB_Player_Salary_Info.md")


    for player in salary_data_dict:
        for team in salary_data_dict[player]:
            if(salary_data_dict[player][team]!=''):
                print(player+': '+salary_data_dict[player][team])
            else:
                print(player+' has no salary!')
    #         print(salary_data_dict[player])
    # print(salary_data_dict)
    
    
    pitcher_data = {}
    parse_pitcher_data(pitcher_data, "2017_MLB_Pitcher_Info.md")
    for p in pitcher_data:
        for team in pitcher_data[p]:
            print(p, team, pitcher_data[p][team].w_l, pitcher_data[p][team].so)
            
            
    strikeouts  = {}
    for p in pitcher_data:
        pdict = {}
        for team in pitcher_data[p]:
            if p in salary_data_dict and team in salary_data_dict[p] and salary_data_dict[p][team] != '':
                pdict[team] = (pitcher_data[p][team].so, salary_data_dict[p][team])
                print(p, pdict[team])
    
    