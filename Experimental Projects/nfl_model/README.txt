Currently working towards a model predicting wins and losses for the NFL.

Data is being scraped from https://www.pro-football-reference.com/

TO DO:

Stage 1 - Test Data Ingestion
1.) clean bye weeks into standardized form
2.) handle playoff rows. 
    Where team reaches the playoffs there is a row at index 17 that has NaN's in every column but Date. Next row/s has game with week set to 'DIVISION' or 'Wild Card' Etc
3.) check NaNs in rest of columns
4.) convert columns to datatypes

Stage 2 - General Data Ingestion
1.) organize for loop to pull data for every team, for all seasons in window
2.) organize for loop to clean data in line with test structure
3.) figure out how to deal with duplicate games (that is, there will be two rows per game, one from perspective of home team, one from away team)
4.) export

Stage 3 - ELO Generation
1.) figure out how to generate ELO scores from beginning of 2000 season.
2.) create ELO scores at different levels of granularity.

Stage 4 - Current Season Data
1.) Figure out how to pull in data from current season for each team
2.) generate elos through season to current week.
3.) upcoming games.
Stage 5 - Predictions
1.) feed data into scikitlearn/keras
2.) generate predicted statistics for each relevant column


Future - deeper stats
1.) quantify teams being strong/weak vs rush/pass
2.) player updates, i.e QB1 being out from injury
3.) betting odds
4.) predict likely upsets.
