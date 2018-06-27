import csv
from matplotlib import pyplot as plt

#create a short word... plt... for matplotlib.pyplot
filename="C:/python crash course/columbus.csv"
with open(filename) as f1:
    #read csv file
    reader=csv.reader(f1)
    #read header 1
    header=next(reader)
    #read header 2
    header2=next(reader)
    header3=next(reader)
    print(header)
    print(header2)
#create an empty list for (high,low) temperatures and
# for days and events
    high=[]
    days=[]
    low=[]
    events=[]
#append row[1] in empty list high
#row[1] is the 2nd column of our csv file
    for row in reader:
        high.append(row[1])
        low.append(row[3])
        events.append(row[20])
        days.append(row[0])
#print all the list we created

    print("temperature",high)
    print("events", events)
    print("days",days)
    print("duration",len(days),"days")

#This part is for visualization

#This is to adjust the image according to our system
fig = plt.figure(dpi=128, figsize=(18, 7))
plt.plot(high,c="red",label="High")
plt.plot(low,c="green",label="Low")
plt.plot(events,c='cyan',label="Events")

plt.title("Columbus ( Ohio ) Temperature  June 2018")
plt.xlabel("Days",fontsize=16)
plt.ylabel("Temperatures",fontsize=16)
plt.tick_params(labelsize=10)
plt.legend()

#save the file as columbus.svg
plt.savefig("columbus.svg")

#last... show our plot
plt.show()

#create a loop for header 3 where we can print the
#index and column of csv file
for index,column in enumerate(header3):
   print(index,column)
for index, column in enumerate(header2):
   print(index, column)