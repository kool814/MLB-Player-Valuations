#This is the file that we will use to parse the Batter, Pitcher, and Salary data

#Dictionary with key: Player and value: Dictionary containing key:Team and value: stats 

import math

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


if __name__ == "__main__":
    salary_data_dict = {}
    salary_data_dict['player'] = {}
    salary_data_dict['player']['team'] = 'stats'
    #print(salary_data_dict)

    parse_salary_data(salary_data_dict, 
                "/Users/karthiksuresh/Documents/GitHub/MLB-Player-Valuations/2017_MLB_Player_Salary_Info.md")

    for player in salary_data_dict:
        for team in salary_data_dict[player]:
            if(salary_data_dict[player][team]!=''):
                print(player+': '+salary_data_dict[player][team])
            else:
                print(player+' has no salary!')
            # print(salary_data_dict[player])
    # print(salary_data_dict)
    