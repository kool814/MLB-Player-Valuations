#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <map>

int main(){
	std::vector <std::vector <std::string> > data;
	std::map<std::string, std::vector <std::vector <std::string> > > map_player_salary;

	std::vector <std::vector <std::string> > pitcher_data;
	std::map<std::string, std::vector <std::vector <std::string> > > map_pitcher_player;

	std::ifstream infile( "2017_MLB_Player_Salary_Info.md" );
	std::ifstream infile_batter( "2017_MLB_Batter_Info.md" );
	std::ifstream infile_pitcher( "2017_MLB_Pitcher_Info.md" );

	int count=0;
	while (infile){
		std::string s;
	    if (!getline( infile, s )){
	    	break;
	    }
	    std::istringstream ss( s );
	    std::vector <std::string> record;

	    while (ss){
	      std::string s;
	      if (!getline( ss, s, ',' )){
	      	break;
	      }
	      record.push_back( s );
	    }

	    data.push_back( record );
	    std::string full_name= data[count][1];
	    std::string modified_name="";
	    int x=0;
	    while(x<full_name.size()){
	    	if(full_name[x]!='\\'){
	    		modified_name.push_back(full_name[x]);
	    	}else{
	    		modified_name.pop_back();
	    		break;
	    	}
	    	x++;
	    }
		map_player_salary.insert(std::make_pair(modified_name, data));
		count++;
	}

	//test if player salary data works 
	for(int x=0; x<data.size(); x++){
		if((data[x][21])!=""){
			std::cout<<"Name: "<< data[x][1]<<" Salary: "<< data[x][21]<<std::endl;
		}
	}

	if(map_player_salary.find("Clayton Kershaw")!=map_player_salary.end()){
		std::cout<<"map works!!"<<std::endl;
	}

	//parse thru player pitcher info and store everything into a map
	count=0;
	while (infile_pitcher){
		std::string s;
	    if (!getline( infile_pitcher, s )){
	    	break;
	    }

	    std::istringstream ss( s );
	    std::vector <std::string> record;

	    while (ss){
	      std::string s;
	      if (!getline( ss, s, ',' )){
	      	break;
	      }
	      record.push_back( s );
	    }

	    pitcher_data.push_back( record );
	    std::string full_name= pitcher_data[count][1];
	    std::string modified_name="";
	    int x=0;
	    while(x<full_name.size()){
	    	if(full_name[x]!='\\'){
	    		modified_name.push_back(full_name[x]);
	    	}else{
	    		modified_name.pop_back();
	    		break;
	    	}
	    	x++;
	    }
		map_pitcher_player.insert(std::make_pair(modified_name, pitcher_data));
		count++;
	}


	//test if pitcher player data works 
	for(int x=0; x<pitcher_data.size(); x++){
		if((pitcher_data[x][1])!="Name"){
			std::cout<<"Name: "<< pitcher_data[x][1]<<" ERA: "<< pitcher_data[x][8]<<std::endl;
		}
	}

	if(map_pitcher_player.find("Mike Wright")!=map_pitcher_player.end()){
		std::cout<<"map works!!"<<std::endl;
	}

	return 0;
}
