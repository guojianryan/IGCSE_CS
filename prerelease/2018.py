import os
import simulation

sim = simulation.Simulation()

N = 10 # number of cows
codes = list()
first_yields,sec_yields = list(), list()

input = sim.simulate_code_reading()

#task1
for cow in range(N):
    codes.append(input("Enter an identity code:"))

input = sim.simulate_yield_reading()

for day in range(7):
    for cow in range(N):
        first_yields.append(int(input("The yield of the 1st milking of day {0} for cow {1}".format(day + 1, codes[cow])))) 
        sec_yields.append(int(input("The yield of the 2nd milking of day {0} for cow {1}".format(day + 1, codes[cow]))))

input = sim.restore()

#task 2A
total_volume = int(round(sum(first_yields) + sum(sec_yields),0))
print("The total volume for the herd to the nearest whole litre: ", total_volume)
        
#task 2B
print("The average yield per cow to the nearest whole litre: ", int(round(total_volume/N,0)))

#task 3
max_yield = 0
max_cow_idx = 0

for cow in range(N):
    total_per_cow = 0
    days_less_than_12 = 0
    for day in range(7):
        day_yield = first_yields[cow + N * day] + sec_yields[cow + N * day]
        total_per_cow = total_per_cow + day_yield
        if day_yield < 12: 
            days_less_than_12 = days_less_than_12 + 1

    if total_per_cow > max_yield:
        max_yield = total_per_cow
        max_cow_idx = cow

    if days_less_than_12 >= 4:
        print("Cow {0} has 4 days or more with a yield of less than 12.".format(codes[cow]))

print("Cow {0} has produced the most milk: {1}".format(codes[max_cow_idx], max_yield))