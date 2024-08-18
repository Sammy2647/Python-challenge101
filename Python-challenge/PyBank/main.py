import csv


total_months = 0
net_total = 0
previous_profit = 0
changes = []
dates = []

# Read the CSV file
with open("Resources/budget_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip first row
    header = next(csvreader)

    for row in csvreader:
        date = row[0]
        profit = int(row[1])

        total_months += 1
        net_total += profit

        # Calculate change in profit
        if total_months > 1:
            change = profit - previous_profit
            changes.append(change)
            dates.append(date)

        previous_profit = profit

# Average change
average_change = sum(changes) / len(changes)

# Find greatest increase and decrease
greatest_increase = max(changes)
greatest_decrease = min(changes)
increase_date = dates[changes.index(greatest_increase)]
decrease_date = dates[changes.index(greatest_decrease)]

# Results
analysis = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {increase_date} (${greatest_increase})
Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})
"""

# Print the analysis to the terminal
print(analysis)

# Export to a text file
with open("financial_analysis.txt", 'w') as file:
    file.write(analysis)
