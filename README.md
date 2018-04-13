# MLB Player Valuations
Analysis of Major League Baseball Player value through salary compensation

This project analyzes the most undervalued and overvalued MLB players by using metrics to determine the true value of a player when compared to their salary.


## Theory
In Major League Baseball, statistics like Runs Batted In (RBI), Batting Average (BA), and Earned Run Average (ERA) are the most common metrics used to determine the overall value of a player and the player's impact to a team. Given these statistics, most major league teams offer salaries and contracts that are largely based on these metrics. 

However these metrics are often relics of a pre-modern view of the game. Statisical analysis has proven that On-base percentage (OBP) and Slugging percentage (SLG) are better indicators of offensive success and with newer metrics like Wins Above Replacement (WAR) and Fielding Independent Pitching (FIP), teams can get a better indication of how much a player is truly worth to a team. 

## Outcome
Based on these newer metrics, we can recalculate a player's overall value and using their current salary, project which players are MLB's most undervalued and overvalued players.

## Data
Data and statistics taken from [www.fangraphs.com](http://www.fangraphs.com/) and [www.baseball-reference.com](http://www.baseball-reference.com/).



Batter Performance = ((Hits + Walks)* TotalBases)/(AtBats + Walks)
Pitcher Performance = ((ERA+*9 + WHIP)*StrikeOuts)/9
