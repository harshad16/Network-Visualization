# Network-Visualization
# This was a submission at the MIT CAVE Hackathon 2018.
# Try out the actual website at the url: https://pure-hamlet-40297.herokuapp.com/
# Check out our website related documentation at : https://devpost.com/software/cave-hack
# The 1st page consists of 4 graph plots (3 pie charts and 1 stacked-bar graph) which compare 4 major supply chains.
# Transitions:
# The pie chart visualizing the metric demand per cost and time has interactive pies which take you to different links of different supply chain companies and gives specific data about the chain in terms of the metrics involved in each of the stages. There is also a search bar which helps u search for a particular stage node (facility) of the supply chain and displays in the center of a scatter plot along with all of its immediate neighbours. Clicking on either of them will refresh the page to show the clicked node at the center with all of its neighbours in the plot. 
# Format for text to be entered in the search bar:
# 1) Raw Materials/Parts facility/node : Part_ID (For eg: Part_001, Part_005, etc)
# 2) Manufacturing facility/node : Manuf_ID (For eg: Manuf_001, Manuf_005, etc)
# 3) Distribution facility/node : Dist_ID (For eg: Dist_001, Dist_005, etc)
# 4) Retail facility/node : Retail_ID (For eg: Retail_001, Retail_005, etc)
# 5) Transportation facility/node : Trans_ID (For eg: Trans_001, Trans_005, etc)
# Technologies used: Python, Flask, Canvas.js, Html, CSS
