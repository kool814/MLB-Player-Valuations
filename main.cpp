#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main(){
	std::vector <std::vector <std::string> > data;
	std::ifstream infile( "2017_MLB_Player_Info.md" );

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
	}

	std::cout<<"yes"<<std::endl;
	for(int x=0; x<data.size(); x++){
		std::cout<<data[x][1]<<std::endl;
	}

	return 0;
}
