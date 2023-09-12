import matplotlib.pyplot as plt

# collect the data 
data = [] # empty list 
print (" enter pokeman data;")
print("day 1:", end="")
day1 = int(input())
print("day 2:", end="")
day2 = int(input())
print("day 3:", end="")
day3 = int(input())


# NEW VERSION - Loop and get each day at a time
num_day = [] # empty list
num_days = int(input(" how many days? "))
for day in range(num_days):
  print("Day",day,":", end="")
  today = int(input())
  data.append(today) # add it to the end of the list 

# put the data in a list (DONE)
# print min and max 
print("best day:", max (data))
print("worst day:",min(data))
# TODO: graph the real data
fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title("pokeman data")
plt.xlabel('day #')
plt.ylabel('pokrmans collected')
plt.show()