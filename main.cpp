#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <map>

void parse_data(std::ifstream &instream_data,std::map<std::string, std::vector <std::string> > & map_data){

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

	    std::string full_name= record[1];
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
		map_data.insert(std::make_pair(modified_name, record));
		count++;
	}
}

//int main(int argc, char** argv)
int main(){
	std::map<std::string, std::vector <std::string> >  map_salary;
	std::map<std::string, std::vector <std::string> >  map_pitcher_player;
	std::map<std::string, std::vector <std::string> >  map_batter_player;

	std::ifstream infile( "2017_MLB_Player_Salary_Info.md" );
	std::ifstream infile_pitcher( "2017_MLB_Pitcher_Info.md" );
	std::ifstream infile_batter( "2017_MLB_Batter_Info.md" );

	// std::string user_option = "";
	// std::cout << "Would you like to view a particular player's value or a list of players ranked by value?: ";
	// getline(std::cin, player_name);
	// std::cout << "You entered: " << player_name << std::endl;
	// std::cin.clear();



	// std::string player_name = "";
	// std::cout << "Please enter a players name: ";
	// getline(std::cin, player_name);
	// std::cout << "You entered: " << player_name << std::endl;
	// std::cin.clear();

	std::string player_position = "";
	std::cout << "Is "<< player_name<< " a Pitcher or Batter?: ";
	getline(std::cin, player_position);
	std::cout << "You entered: " << player_position << std::endl;

	//parse_data for salary info
	parse_data(infile, map_salary);
	if(map_salary.find("Yoenis Cespedes")!=map_salary.end()){
		std::cout<< "Yoenis Cespedes's Salary: "<< map_salary.find("Yoenis Cespedes")->second[21]<<std::endl;
	}

	//parse data for pitcher info
	parse_data(infile_pitcher, map_pitcher_player);
	if(map_pitcher_player.find("Tim Adleman")!=map_pitcher_player.end()){
		std::cout<<"Tim Adleman's ERA: "<<map_pitcher_player.find("Tim Adleman")->second[8]<<std::endl;
	}

	//parse data for batter info
	parse_data(infile_batter, map_batter_player);
	if(map_batter_player.find("Ryan Zimmerman")!=map_batter_player.end()){
		std::cout<<"Ryan Zimmerman's BA: "<< map_batter_player.find("Ryan Zimmerman")->second[18]<<std::endl;
		// std::cout<<"map works!!"<<std::endl;
	}

	float run_creation=0.0;
	//Run Creation = ((Hits + Walks)* TotalBases)/(AtBats + Walks)
	parse_data(infile_batter, map_batter_player);
	if(map_batter_player.find("LgAvg per 600 PA")!=map_batter_player.end()){
		run_creation= (map_batter_player.find("LgAvg per 600 PA")->second[9] + map_batter_player.find("LgAvg per 600 PA")->second[9])
		//std::cout<<"Ryan Zimmerman's BA: "<< map_batter_player.find("Ryan Zimmerman")->second[18]<<std::endl;
	}

	
	return 0;
}
