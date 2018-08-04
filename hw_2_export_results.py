import os
import csv
final_csv = os.path.join("C:/Users/Sal/Desktop/Python_hw/budget_data.csv","budget_data.csv")
# Lists to store data
month = []
netgains = []
monthly_delta=[]
with open("C:/Users/Sal/Desktop/Python_hw/budget_data.csv", "rt") as f:
   csvreader = csv.reader(f, delimiter=",")
   headers = next(csvreader)
   
   for row in csvreader:
       # Add month
       month.append(row[0])
       
       # Add + or minus gains
       netgains.append(row[1])
       
#dictionary emptpy; until populated by for loop;
my_dictionary = {}
y=0
for x in month:
   my_dictionary[x]=float(netgains[y])
#increments by 1
   y=y+1
#print(my_dictionary)

#Total_months=86
Total_months = len (my_dictionary)

Total_profits=sum(list(my_dictionary.values()))

delta=[]

netgains=list(map(int,netgains))

for i in range(1,len(netgains)):
    delta.append(netgains[i]-netgains[i-1])

avg_change=(sum(delta)/len(delta))

max_val=max(delta)

min_val=min(delta)

#max corresponding month
lst_ind_max=delta.index(max_val)

max_month= month[lst_ind_max+1]

lst_ind_min=delta.index(min_val)

min_month=month[lst_ind_min+1]

print("Financial Analysis")
print("-------------------------------------------------------------")
print("Total Months: "+str(Total_months))
print("Total: $"+str(Total_profits))
print("Average Change: $"+str(avg_change))
print("Greatest Increase in Profits: "+max_month+" ($"+str(max_val)+")")
print("Greatest decrease in Profits: "+min_month+" ($"+str(min_val)+")")

cleaned_csv = zip(month, netgains, delta)

#variabl to output file
output_file = os.path.join("pybank_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

# Write in zipped rows
    writer.writerows(cleaned_csv)

