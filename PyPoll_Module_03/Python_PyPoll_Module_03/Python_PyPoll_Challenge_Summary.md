# **Python PyPoll Analysis**

### Overview of Project

An automated audit of the election results in Colorado that provides the count and percentage of votes for each candidate and county. The winner of the election is output as a text file and comma separated-values (CSV), along with a summary results table.

### Purpose

The purpose of this analysis was to provide an automated way to tabulate the results of the Colorado election. Given the data provided, the votes were calculated for each candidate and county. The script written allows a quick audit of the results while being independent of vote counters in order to validate any election results.

The outputs offer three summaries: an output of the summary within the terminal, an output showing the summary in a text file, and an output showing the summary as a comma separated-values worksheet.

### Election Results

1. The below is a summary of the elections results:

  * Total Votes Cast: 

          * Total: 369,711
          * Charles C. Stockham: 85,213 (23.05%)
          * Diana DeGette: 272,892 (73.81%)
          * Raymon A. Doane: 11,606 (3.14%)

  * County Votes Cast:

      Jefferson:
          
          * Total: 38,855 (10.51%)
          * Charles C. Stockham: 19,723 (50.76%)
          * Diana DeGette: 17,963 (46.23%)
          * Raymon A. Doane: 1,196 (3.01%)

      Arapahoe:

          * Total: 24,801 (82.78%)
          * Charles C. Stockham: 8,302 (33.47%)
          * Diana DeGette: 15,647 (63.09%)
          * Raymon A. Doane: 852 (3.44%)

      Denver:

          * Total: 306,055 (6.71%)
          * Charles C. Stockham: 57,188 (18.69%)
          * Diana DeGette: 239,282 (78.18%)
          * Raymon A. Doane: 9,585 (3.13%)

2. The above results can be concluded that Diana DeGette won the election with 73.81% (272,892) of the total votes cast. Her highest voting county was Denver with a vote count of 239,282 out of 306,055 total votes cast. 

### Election-Audit Summary

This script includes the ability for an election to be quickly tablulated for each candidate, county, and a county breakdown by candidate. These outputs are pushed as both total counts and percentage of votes recieved. The CSV output file includes a full breakdown of the election based on any candidate or county present.

The only modification necessary for this script to capture other elections is the text file output/terminal output. It is specifically set to show the known cadidates values in the "election_results" variable, which are manually entered. If the election goes beyond the individual state level, it would be necessary for the script to be ammended to accurately reflect state totals/state assignments as well.