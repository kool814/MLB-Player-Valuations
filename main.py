#This is the file that we will use to parse the Batter, Pitcher, and Salary data

#Dictionary with key: Player and value: Dictionary containing key:Team and value: stats 

import math

def parse_salary_data(dict, salary_data):
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
            
            team= line[4]
            salary= line[22]
            
            if player_name in dict:
                ''' if the player is already in the dictionary, then add them to another team '''
            else:
                ''' add them to the dictionary'''

            print(player_name)


if __name__ == "__main__":
    salary_data_dict = {}
    salary_data_dict['player'] = {}
    salary_data_dict['player']['team'] = 'stats'
    print(salary_data_dict)

    parse_salary_data(salary_data_dict, 
                "/Users/karthiksuresh/Documents/GitHub/MLB-Player-Valuations/2017_MLB_Player_Salary_Info.md")
    