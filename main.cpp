#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <map>

void parse_data(std::ifstream &instream_data, std::vector <std::vector <std::string> >& vec_data,
	std::map<std::string, std::vector <std::vector <std::string> > >& map_data){
	int count=0;
	while (instream_data){
		std::string s;
	    if (!getline( instream_data, s )){
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
	    vec_data.push_back(record);
	    std::string full_name= vec_data[count][1];
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
		map_data.insert(std::make_pair(modified_name, vec_data));
		count++;
	}
}

int main(){
	std::vector <std::vector <std::string> > data;
	std::map<std::string, std::vector <std::vector <std::string> > > map_player_salary;

	std::vector <std::vector <std::string> > pitcher_data;
	std::map<std::string, std::vector <std::vector <std::string> > > map_pitcher_player;

	std::vector <std::vector <std::string> > batter_data;
	std::map<std::string, std::vector <std::vector <std::string> > > map_batter_player;

	std::ifstream infile( "2017_MLB_Player_Salary_Info.md" );
	std::ifstream infile_pitcher( "2017_MLB_Pitcher_Info.md" );
	std::ifstream infile_batter( "2017_MLB_Batter_Info.md" );


	//parse_data for salary info
	parse_data(infile, data, map_player_salary);
	
	//test if player salary data works 
	for(int x=0; x<data.size(); x++){
		if((data[x][21])!=""){
			std::cout<<"Name: "<< data[x][1]<<" Salary: "<< data[x][21]<<std::endl;
		}
	}
	if(map_player_salary.find("Clayton Kershaw")!=map_player_salary.end()){
		std::cout<<"map works!!"<<std::endl;
	}


	//parse data for pitcher info
	parse_data(infile_pitcher, pitcher_data, map_pitcher_player);

	//test if pitcher player data works 
	for(int x=0; x<pitcher_data.size(); x++){
		if((pitcher_data[x][1])!="Name"){
			std::cout<<"Name: "<< pitcher_data[x][1]<<" ERA: "<< pitcher_data[x][8]<<std::endl;
		}
	}
	if(map_pitcher_player.find("Mike Wright")!=map_pitcher_player.end()){
		std::cout<<"map works!!"<<std::endl;
	}


	//parse data for batter info
	parse_data(infile_batter, batter_data, map_batter_player);

	//test if pitcher player data works 
	for(int x=0; x<batter_data.size(); x++){
		if((batter_data[x][1])!="Name"){
			std::cout<<"Name: "<< batter_data[x][1]<<" BA: "<< batter_data[x][18]<<std::endl;
		}
	}
	if(map_batter_player.find("Jose Abreu")!=map_batter_player.end()){
		std::cout<<"map works!!"<<std::endl;
	}
	
	return 0;
}
