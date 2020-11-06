Currently working towards a model predicting wins and losses for the NFL.

'current_predictions.png' displays what the model is seeing in the next time frame.

'01_bear_data_get_test.ipynb' was my testbed for scraping and cleaning the data

'02_general_data_ingest.ipynb' is the program that ingests and cleans all the data from the source. It outputs a set of 32 dataframes as an excel file for each team in the data/ind_team_data folder.
It further outputs an excel file for the full set of data combined into one frame.

'bear_viz.ipynb' is a quick example of the visualizations possible with the clean data. Also that my whole experience as a bears fan has empirically been downhill since 2006.

'03_predictions.ipynb' generates predictions for the next week of games. It is very basic and clunky at the moment, and needs some reorganization. Functional, but ugly.

Data is being scraped from https://www.pro-football-reference.com/

TO DO is over in the projects tab
