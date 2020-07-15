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

  #  print(csv_header)
	print(csv_header)
	
	for row in csvreader:
		print(row[0], row[1])
		months.append(row[0])
		profits_losses.append(int(row[1]))

	# .append allows me to get at the specific thing I need in each row so that I can manipulate the data
budget_data_zip = zip(months, profits_losses)

print("Financial Analysis")
print("--------------------")

# Print Total number of months included in dataset
# len function tells me how many things are in a list (diff from sum which tries to add integers)
print(f"Total Months: {len(months)}")

# Print net total amount of "Profit/Losses" over the entire period
print(f"Net Total: ${sum(profits_losses)}")

# Print average of the changes in "Profit/Losses" over the entire period
average = ((max(profits_losses) - min(profits_losses))/len(profits_losses))
print(f'Average Change: ${round(average, 2)}')

# Print Greatest increase in profits (date and amount) over the entire period
for date, profit_loss in budget_data_zip:
    if profit_loss == max(profits_losses):
        print(f'Greatest Profit: {date} ${max(profits_losses)}')
    if profit_loss == min(profits_losses):
        print(f'Greatest Decrease in Profit: {date} ${min(profits_losses)}')

		
# Print greatest decrease in losses (date and amount) over the entire period




