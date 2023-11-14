# 1. There is a 30% chance of rain today, and a 40% chance your umbrella order will
# arrive on time. You are eager to walk in the rain today and cannot do so without
# either!
# What is the probability it will rain AND your umbrella will arrive?
#
# P(r) = 0.3
# P(u) = 0.4
#
# P(r) u P(u) = 0.3 * 0.4 = 0.12

print(0.3*0.4)

# 2. There is a 30% chance of rain today, and a 40% chance your umbrella order will
# arrive on time.
# You will be able to run errands only if it does not rain or your umbrella arrives.
# What is the probability it will not rain OR your umbrella arrives?
#
#P(r) = 0.3 P(notr) = 0.7
#P(u) = 0.4
#
#P(notr) or P(u) = 0.7 + 0.4 - 0.7*0.4 = 0.82

print(0.7 + 0.4 - 0.7*0.4)

# 3. There is a 30% chance of rain today, and a 40% chance your umbrella order will
# arrive on time.
# However, you found out if it rains there is only a 20% chance your umbrella will
# arrive on time.
# What is the probability it will rain AND your umbrella will arrive on time?
#
#P(u|r) = 0.2
#P(r) and P(u|r) = 0.3 * 0.2 = 0.06
#
# 4. You have 137 passengers booked on a flight from Las Vegas to Dallas. However, it
# is Las Vegas on a Sunday morning and you estimate each passenger is 40% likely
# to not show up.
# You are trying to figure out how many seats to overbook so the plane does not fly
# empty.
# How likely is it at least 50 passengers will not show up?
#
#P(notshowup) = 0.4

from scipy.stats import binom
n = 137
p = .40
p_50_or_more_noshows = 0.0
for x in range(50,138):
 p_50_or_more_noshows += binom.pmf(x, n, p)
print(p_50_or_more_noshows) # 0.822095588147425

# 5. You flipped a coin 19 times and got heads 15 times and tails 4 times.
# Do you think this coin has any good probability of being fair? Why or why not?

from scipy.stats import beta
heads = 15
tails = 4
p = 1.0 - beta.cdf(.5, heads, tails)
print(p) # 0.98046875
