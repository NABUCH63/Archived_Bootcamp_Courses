import csv
import os

input = "Data_Analytics/Python_PyPoll_Module_03/election_results.csv"
county_out = "Data_Analytics/Python_PyPoll_Module_03/county_summary.csv"
text_out = "Data_Analytics/Python_PyPoll_Module_03/election_summary.txt"

# Add a variable to load a file from a path.
file_to_load = os.path.join("..", input)
# Add a variable to save the file to a path.
county_summary_output = os.path.join("..", county_out)
txt_file_output = os.path.join("..", text_out)

# Initialize variables.
total_votes = 0
winning_candidate = ""
winning_county = ""
County_Voters = 0
winning_percentage = 0

# Dict for the initial audit. Automatically Ammended
candidate_options = ["All"]
county_options = ["All"]
candidate_votes = {"All": 0}
county_votes = {"All": 0}
candidate_pert = {}
county_pert = {}

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    # For each row in the CSV file.
    for row in reader:
        # Add to the total vote count
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # 3: Extract the county name from each row.
        county_name = row[1]
        #if a new county/candidate is found:
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate lists.
            candidate_votes[candidate_name] = 0
            candidate_pert[candidate_name] = 0
            candidate_options.append(candidate_name)
        # repeat the check for the county, add to list if missing.
        if county_name not in county_options:
            # Add the existing county to the list of counties.
            county_votes[county_name] = 0
            county_pert[county_name] = 0
            county_options.append(county_name)
        # Add a vote to the row's candidate's count
        candidate_votes[candidate_name] += 1
        # Add a vote to that row's county's vote count.
        county_votes[county_name] += 1

# create the dictionaries based on the county 
k = 1
county_nested_dict = {}
for i in range(len(county_options)):
    for j in range(len(candidate_options)):
        county_nested_dict[k] = {"County": county_options[i], "Candidate": candidate_options[j], "Votes": 0, "Percentage": 0}
        k += 1
county_votes["All"] = total_votes

# Reopen election results csv and tabulate the county and candidate results per county
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:
        # Get the candidate name from each row.
        candidate_name = row[2]
        # 3: Extract the county name from each row.
        county_name = row[1]

        #compare election results to nested dictionary
        for i in range(len(county_nested_dict)):
            if county_nested_dict[i + 1]["Candidate"] == candidate_name and county_nested_dict[i + 1]["County"] == county_name:
                county_nested_dict[i + 1]["Votes"] += 1
            elif county_nested_dict[i + 1]["Candidate"] == candidate_name and county_nested_dict[i + 1]["County"] == county_options[0]:
                county_nested_dict[i + 1]["Votes"] += 1
            elif county_nested_dict[i + 1]["Candidate"] == candidate_options[0] and county_nested_dict[i + 1]["County"] == county_name:
                county_nested_dict[i + 1]["Votes"] += 1
            elif county_nested_dict[i + 1]["Candidate"] == candidate_options[0] and county_nested_dict[i + 1]["County"] == county_options[0]:
                county_nested_dict[i + 1]["Votes"] += 1

# Calculate Percentages
for dict in range(len(county_nested_dict)):
    for index in range(len(county_options)):
        if county_nested_dict[dict + 1]["County"] == county_options[index] and county_nested_dict[dict + 1]["Candidate"] != candidate_options[0]:
            county_nested_dict[dict + 1]["Percentage"] = (county_nested_dict[dict + 1]["Votes"]/county_votes[county_options[index]])*100
        elif county_nested_dict[dict + 1]["Candidate"] == candidate_options[0] and county_nested_dict[dict + 1]["County"] == county_options[index]:
            county_nested_dict[dict + 1]["Percentage"] = (county_nested_dict[dict + 1]["Votes"]/total_votes)*100


        
# Dict percentage calcs that will updated based on the audit loop

for key in candidate_votes.keys():
    candidate_pert[key] = (candidate_votes[key]/total_votes)*100

for key in county_votes.keys():
    county_pert[key] = (county_votes[key]/total_votes)*100
    
#asign winners to variables
    #remove "All" keys from dictionaries
county_votes.pop("All")
candidate_votes.pop("All")
candidate_pert.pop("All")
county_pert.pop("All")

winning_candidate = max(candidate_votes, key=candidate_votes.get)
winning_county = max(county_votes, key=county_votes.get)
County_Voters = max(county_votes.values())

# Save the results to our csv file.
with open(county_summary_output, "w") as csv_file:
    header = ["County", "Candidate", "Votes", "Percentage"]
    #csv_file.write(election_results)
    writer = csv.DictWriter(csv_file, header)
    writer.writeheader()
    for key, val in sorted(county_nested_dict.items()):
        row = {"County": key}
        row.update(val)
        writer.writerow(row)
   
# Save results to a text file

with open(txt_file_output, "w") as txt_file:
    election_results = (f"Election Results\n"
                        f"__________________\n\n"
                        f"County Votes:\n"
                        f"Jefferson: {county_pert['Jefferson']:.2f}% ({county_votes['Jefferson']:,g})\n"
                        f"Denver: {county_pert['Denver']:.2f}% ({county_votes['Denver']:,g})\n"
                        f"Arapahoe: {county_pert['Arapahoe']:.2f}% ({county_votes['Arapahoe']:,g})\n\n"
                        f"__________________\n"
                        f"Largest County Turnout: {winning_county}\n"
                        f"Largest County Turnout: {County_Voters:,g}\n"
                        f"__________________\n\n"
                        f"Charles Casper Stockham: {candidate_pert['Charles Casper Stockham']:.2f}% ({candidate_votes['Charles Casper Stockham']:,g})\n"
                        f"Diana DeGette: {candidate_pert['Diana DeGette']:.2f}% ({candidate_votes['Diana DeGette']:,g})\n"
                        f"Raymon Anthony Doane: {candidate_pert['Raymon Anthony Doane']:.2f}% ({candidate_votes['Raymon Anthony Doane']:,g})\n\n"
                        f"__________________\n"
                        f"Winning Candidate: {winning_candidate}\n"
                        f"Winning Vote Count: {max(candidate_votes.values()):,g}\n"
                        f"Winning Vote Percentage: {(max(candidate_pert.values())):.2f}% \n"
                        f"___________________\n")
    print(election_results, end="")
    txt_file.write(election_results)
 