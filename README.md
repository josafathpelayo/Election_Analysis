# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent congressional election.

1. Calculate the total number of votes cats.
2. Get a complete list of canidates who recieve votes.
3. Calculate the total number of votes each canidate received.
4. Calculate the percentage of votes each canidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio, 1.38.1

## Summary
The analysis of the election show that:
- There were "369,711" votes cast in the election.
- The candidates were:
  -Charles Casper Stockham 
  -Diana DeGette
  -Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham recieved "23.0%" of the vote and "85,213" number of votes.
  - Diana DeGette recieved "73.8%" of the vote and "272,892" number of votes.
  - Raymon Anthony Doane recieved "3.1%" of the vote and "11,606" number of votes.
- The winner of the election was:
  - Diana DeGette recieved "73.8%" of the vote and "272,892" number of votes.
  
  ## Challenge Overview
In the recent congressional election, the election commision has requested additional data to complete the audit. These items include: 
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

  ## Challange Results
The analysis of the election show that:
- There were a total of 369,711 number of votes.
- From the total votes:
  - Jefferson county had 10.5% of the vote and 38,855 number of votes
  - Denver county had 82.8% of the vote and 306,055 number of votes
  - Arapahoe county hasd 6.7% of the vote and 24,801 number of votes
- With the data split in three counties, Denver had the largest.
- The candidate results were:
  - Charles Casper Stockham recieved 23.% of the vote and 85,213 number of votes.
  - Diana DeGette recieved 73.8 of the vote and 272,892 number of votes.
  - Raymon Anthony Doane recieved 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  -Diana DeGette recieved 73.8 of the vote and 272,892 number of votes.
-[Data image](https://github.com/josafathpelayo/Election_Analysis/blob/main/election%20txt%20results.png)
  ## Challenge Summary
  Overall, the script used in this analysis can be used in many ways outside this election audit. The script can be changed to meet any other election as long as one refractors the code to handle more than just three canindates or counties. The code can be changed by changing the csv file to what ever election data being analized.

- Ex. Read the csv and convert it into a list of dictionaries
    - with open(file_to_load) as election_data:
    - file_reader = csv.reader(NEW CSV FILE HERE)
    
Once this is done, the script can me modfied to run the amount of candidates and change counties to states. etc. Another example isto modify the script so that you can see the percentages of votes that a candidate had with the a specific county or state.
