import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

#create empty lists for data I need to show to live
months = []
profits_losses = []


with open(budget_data_csv) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvfile)
	# "next" makes sure that the program will move on to the next thing after the header

  #  print(csvr_header)
	print(csv_header)
	
	for row in csvreader:
		print(row[0], row[1])
		months.append(row[0])
		profits_losses.append(int(row[1]))

	# .append allows me to get at the specific thing I need in each row so that I can manipulate the data


# Print Total number of months included in dataset
# len function tells me how many things are in a list (diff from sum which tries to add integers)
print("Total Number of Months Included in Dataset")
print(len(months))

# Print net total amount of "Profit/Losses" over the entire period
print("Net Total of Profits/Losses over Entire Period")

print(sum(profits_losses))

# Print average of the changes in "Profit/Losses" over the entire period

# Print Greatest increase in profits (date and amount) over the entire period
print("Greatest increase in profits")
print(max(profits_losses))

# Print greatest decrease in losses (date and amount) over the entire period
print("greatest decrase in losses")
print(min(profits_losses))


