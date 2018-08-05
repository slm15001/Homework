import csv
from collections import Counter
#List to store data
voter_id=[]
county=[]
candidate=[]

with open("C:/Users/Sal/Desktop/Python_hw/election_data.csv","rt") as f:
    csvread = csv.reader(f, delimiter=",")
    headers = next(csvread)

    for i in csvread:
        voter_id.append(i[0])
        county.append(i[1])
        candidate.append(i[2])

#length of voter id list
voter_len = len(voter_id)
#Candidate vote Count
Khan_count = candidate.count("Khan")
Correy_count = candidate.count("Correy")
Li_count = candidate.count("Li")
O_Tool_count = candidate.count("O'Tooley")

# Distint candidate list

#Candidate % of votes, has to be a more elegant solution than the one that i got to work
Khan_ = Khan_count/voter_len
Correy_= Correy_count/voter_len
Li_=Li_count/voter_len
O_Tool_=O_Tool_count/voter_len


print("Election Results")
print("--------------------------------------------------------------------------------")
print("Total Votes: "+str(voter_len))
print("-------------------------------------------------------------------------------")
print("Khan: "+str("{:.2%}".format(Khan_))+" ("+str(Khan_count)+")")
print("Correy: "+str("{:.2%}".format(Correy_))+" ("+str(Correy_count)+")")
print("Li: "+str("{:.2%}".format(Li_))+" ("+str(Li_count)+")")
print("O'Tooley: "+str("{:.2%}".format(O_Tool_))+" ("+str(O_Tool_count)+")")


