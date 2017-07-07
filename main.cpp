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
	std::map<std::string, std::vector <std::vector <std::string> > > map_data;

	std::ifstream infile( "2017_MLB_Player_Salary_Info.md" );
	std::ifstream infile_batter( "2017_MLB_Batter_Info.md" );
	std::ifstream infile_pitcher( "2017_MLB_Pitcher_Info.md.md" );
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

		map_data.insert(std::make_pair(modified_name, data));
		count++;
	}

	for(int x=0; x<data.size(); x++){
		if((data[x][21])!=""){
			std::cout<<"Name: "<< data[x][1]<<" Salary: "<< data[x][21]<<std::endl;
		}
	}

	if(map_data.find("Clayton Kershaw")!=map_data.end()){
		std::cout<<"map works!!"<<std::endl;
	}

	return 0;
}
