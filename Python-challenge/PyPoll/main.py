import csv

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open("Resources/election_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip first row
    header = next(csvreader)

    for row in csvreader:
        candidate = row[2]

        # Count total votes
        total_votes += 1

        # Count votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# results
analysis = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

# Calculate percentage and find the winner
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    analysis += f"{candidate}: {percentage:.3f}% ({votes})\n"

    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

analysis += f"-------------------------\n"
analysis += f"Winner: {winner}\n"
analysis += f"-------------------------"


print(analysis)

# Export to text file
with open("election_results.txt", 'w') as file:
    file.write(analysis)
