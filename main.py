#This is the file that we will use to parse the Batter, Pitcher, and Salary data

#Dictionary with key: Player and value: Dictionary containing key:Team and value: stats 

import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress
# import pandas as pd
from Pitcher import *
from Batter import *


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

    parse_salary_data(salary_data_dict,"2017_MLB_Player_Salary_Info.md")

    pitcher_data = {}
    parse_pitcher_data(pitcher_data, "2017_MLB_Pitcher_Info.md")
    
    strikeouts  = []
    salary_data = []
    for p in pitcher_data:
        for team in pitcher_data[p]:
            if p in salary_data_dict and team in salary_data_dict[p] and salary_data_dict[p][team] != '':
                salary_data.append(int(salary_data_dict[p][team]))
                strikeouts.append(int(pitcher_data[p][team].so))
                
    plt.figure(1)
    fit = np.polyfit(strikeouts, salary_data ,1)
    fit_fn = np.poly1d(fit) 
    # fit_fn is now a function which takes in x and returns an estimate for y
    
    plt.figure(1)
    plt.plot(strikeouts,salary_data,'go', strikeouts, fit_fn(strikeouts), '--k')
    plt.xlim(0, max(strikeouts)+10)
    plt.ylim(0, max(salary_data)*1.1)
    plt.title('Strikeouts vs. Salary')
    plt.xlabel('Strikeouts')
    plt.ylabel('Salary (Million per year)')

    print(linregress(strikeouts,salary_data))
    
    era  = []
    ip = []
    whip = []
    wins  = []
    salary_winslosses = []
    losses = []
    for p in pitcher_data:
        for team in pitcher_data[p]:
            if p in salary_data_dict and team in salary_data_dict[p] and salary_data_dict[p][team] != '':
                salary_winslosses.append(int(salary_data_dict[p][team]))
                wins.append(int(pitcher_data[p][team].wins))
                losses.append(int(pitcher_data[p][team].losses))
         
    era_salary = []           
    for p in pitcher_data:
        for team in pitcher_data[p]:
            if p in salary_data_dict and team in salary_data_dict[p] and salary_data_dict[p][team] != '':    
                if pitcher_data[p][team].eraplus == '' or pitcher_data[p][team].whip == '':
                    continue
                era_salary.append(int(salary_data_dict[p][team]))
                era.append(float(pitcher_data[p][team].eraplus))
                ip.append(float(pitcher_data[p][team].ip))
                whip.append(float(pitcher_data[p][team].whip))                
    
    
    plt.figure(2)          
    plt.plot(wins,salary_winslosses,'go', wins, fit_fn(wins), '--k')
    plt.xlim(0, max(wins)+10)
    plt.ylim(0, max(salary_winslosses)*1.1)
    plt.xlabel('Wins')
    plt.ylabel('Salary (Million per year)')
    plt.title('Wins vs. Salary')
    plt.show()
    print("\nWins vs. Salary: ", linregress(wins,salary_winslosses),"\n")
    
    plt.figure(3)         
    plt.plot(losses,salary_winslosses,'go', losses, fit_fn(losses), '--k')
    plt.xlim(0, max(losses)+10)
    plt.ylim(0, max(salary_winslosses)*1.1)
    plt.xlabel('Loss')
    plt.ylabel('Salary (Million per year)')
    plt.title('Loss vs. Salary')
    plt.show()    

    print("\nLoss vs. Salary: ", linregress(losses,salary_winslosses),"\n")


    plt.figure(4)         
    plt.plot(era,era_salary,'go', era, fit_fn(era), '--k')
    plt.xlim(0, max(era)+10)
    plt.ylim(0, max(era_salary)*1.1)
    plt.xlabel('Era')
    plt.ylabel('Salary (Million per year)')
    plt.title('Era vs. Salary')
    plt.show()

    print("\nEra vs. Salary: ", linregress(era,era_salary),"\n")

    plt.figure(5)         
    plt.plot(ip,era_salary,'go', ip, fit_fn(ip), '--k')
    plt.xlim(0, max(ip)+10)
    plt.ylim(0, max(era_salary)*1.1)
    plt.xlabel('IP')
    plt.ylabel('Salary (Million per year)')
    plt.title('IP vs. Salary')
    plt.show()    

    print("\nIP vs. Salary: ", linregress(ip,era_salary),"\n")

    plt.figure(6)         
    plt.plot(whip,era_salary,'go', whip, fit_fn(whip), '--k')
    plt.xlim(0, max(whip)+1)
    plt.ylim(0, max(era_salary)*1.1)
    plt.xlabel('WHIP')
    plt.ylabel('Salary (Million per year)')
    plt.title('WHIP vs. Salary')
    plt.show()    

    print("\nWHIP vs. Salary: ", linregress(whip,era_salary),"\n")    




    homeruns  = []
    # # salary_data = []
    # for p in pitcher_data:
    #     for team in pitcher_data[p]:
    #         if p in salary_data_dict and team in salary_data_dict[p] and salary_data_dict[p][team] != '':
    #             # salary_data.append(int(salary_data_dict[p][team]))
    #             homeruns.append(int(pitcher_data[p][team].so))
    #             # print(p, salary_data[team], strikeouts[team]) 
                

    # batteravg  = []
    # for p in pitcher_data:
    #     for team in pitcher_data[p]:
    #         if p in salary_data_dict and team in salary_data_dict[p] and salary_data_dict[p][team] != '':
    #             batteravg.append(int(pitcher_data[p][team].so))
                

    # plt.figure(7)
    # fit = np.polyfit(batteravg, salary_data ,1)
    # fit_fn = np.poly1d(fit) 
    # # fit_fn is now a function which takes in x and returns an estimate for y

    # plt.plot(batteravg,salary_data,'yo', batteravg, fit_fn(batteravg), '--k')
    # plt.xlim(0, max(batteravg)+10)
    # plt.ylim(0, max(salary_data)*1.1)
    # plt.title('Batter Avg. vs. Salary')
    # plt.xlabel('Batter Avg.')
    # plt.ylabel('Salary (Million per year)')
    # plt.title('Batter Avg. vs. Salary')

    # plt.show()

    # print("\nBatter Avg. vs. Salary: ", linregress(batteravg,salary_data),"\n")

    batterSalaries = []
    WAR = []
    RC = []
    hits = []
    batterDict, lgBatterAvg = parseBatterData("2017_MLB_Batter_Info.md")
    for b in batterDict:
        if b not in batterDict or b not in salary_data_dict:
            continue
        if "2TM" in batterDict[b]:
            
            for t in salary_data_dict[b]:
                if salary_data_dict[b][t].isdigit()\
                   and calculateRC(batterDict[b]["2TM"]) != -1:
                    
                    batterSalaries.append(int(salary_data_dict[b][t]))
                    WAR.append(int(calculateWAR(batterDict[b]["2TM"], lgBatterAvg)))
                    RC.append(int(calculateRC(batterDict[b]["2TM"])))
                    hits.append(int(batterDict[b]["2TM"].hits))
                    homeruns.append(int(batterDict[b]["2TM"].hr))
                break              
                
                   
        elif "3TM" in batterDict[b]:
            for t in salary_data_dict[b]:
                if salary_data_dict[b][t].isdigit() \
                   and calculateRC(batterDict[b]["3TM"]) != -1:
                    
                    batterSalaries.append(int(salary_data_dict[b][t]))
                    WAR.append(calculateWAR(batterDict[b]["3TM"], lgBatterAvg))
                    RC.append(calculateRC(calculateRC(batterDict[b]["3TM"])))
                    hits.append(int(batterDict[b]["3TM"].hits))
                    homeruns.append(int(batterDict[b]["3TM"].hr))
                break 
        else:
            for t in salary_data_dict[b]:
                if salary_data_dict[b][t].isdigit():
                    for t1 in batterDict[b]:
                        if  calculateRC(batterDict[b][t1]) != -1:
                        
                            batterSalaries.append(int(salary_data_dict[b][t]))
                            WAR.append(calculateWAR(batterDict[b][t1], lgBatterAvg))
                            RC.append(calculateRC(batterDict[b][t1]))
                            hits.append(int(batterDict[b][t1].hits))
                            homeruns.append(int(batterDict[b][t1].hr))
                            
                        break
                break             
        
        ## below here will not work
        #if b in salary_data_dict and team in salary_data_dict[b]:
            #WAR.append(calculateWAR(batterDict[b][team], lgBatterAvg))
            #batterSalaries.append(salary_data_dict[b][team])
        #elif "2TM" in salary_data_dict[b]:
            #noData += 1
            #print(b,team, " has no salary data", noData)
            #if b in salary_data_dict:
                #print('\t', salary_data_dict[b], batterDict[b])
    plt.figure(7)
    fit = np.polyfit(homeruns, batterSalaries ,1)
    fit_fn = np.poly1d(fit) 

    plt.plot(homeruns,batterSalaries,'bo', homeruns, fit_fn(homeruns), '--k')
    plt.xlim(0, max(homeruns)+10)
    plt.ylim(0, max(batterSalaries)*1.1)
    plt.title('Home Runs vs. Salary')
    plt.xlabel('Home Runs')
    plt.ylabel('Salary (Million per year)')
    plt.title('Home Runs vs. Salary')
    plt.show()

    print("\nHome Runs vs. Salary: ", linregress(homeruns,batterSalaries),"\n")

    fit = np.polyfit(WAR, batterSalaries ,1)
    fit_fn = np.poly1d(fit) 
    # fit_fn is now a function which takes in x and returns an estimate for y
    plt.figure(8)
    plt.plot(WAR,batterSalaries,'bo', WAR, fit_fn(WAR), '--k')
    plt.xlim(0, max(WAR)+10)
    plt.ylim(0, max(batterSalaries)*1.1)
    plt.title('WAR vs. Salary')
    plt.xlabel('WAR')
    plt.ylabel('Salary (Million per year)')
    plt.title('WAR vs. Salary')
    plt.show()

    print("\nWAR vs. Salary: ", linregress(WAR,batterSalaries))
    
    fit = np.polyfit(RC, batterSalaries ,1)
    fit_fn = np.poly1d(fit) 
    # fit_fn is now a function which takes in x and returns an estimate for y
    plt.figure(9)
    plt.plot(RC,batterSalaries,'bo', RC, fit_fn(RC), '--k')
    plt.xlim(0, max(RC)+10)
    plt.ylim(0, max(batterSalaries)*1.1)
    plt.title('Run Creation vs. Salary')
    plt.xlabel('Run Creation')
    plt.ylabel('Salary (Million per year)')
    plt.title('Run Creation vs. Salary')
    plt.show()

    print("\nRun Creation vs. Salary: ", linregress(RC,batterSalaries))       
    
    
    plt.figure(10)
    plt.plot(hits,batterSalaries,'bo', hits, fit_fn(hits), '--k')
    plt.xlim(0, max(hits)+10)
    plt.ylim(0, max(batterSalaries)*1.1)
    plt.title('Strikeouts vs. Salary')
    plt.xlabel('Strikeouts')
    plt.ylabel('Salary (Million per year)')
    plt.title('Strikeouts vs. Salary')
    plt.show()

    print(linregress(hits,batterSalaries))     
    plt.show()

    print("\nStrikeouts vs. Salary: ", linregress(strikeouts,salary_data),"\n")
