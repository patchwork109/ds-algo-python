# https://leetcode.com/problems/climbing-stairs/
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct 
# ways can you climb to the top?

# n = 2, 2 (1 step + 1 step and 2 steps)
# n = 3, 3 (1 step + 1 step + 1 step, 1 step + 2 steps, and 2 steps + 1 step)

n = 2
n2 = 3
n3 = 9

def climbing_stairs(n):
    if n == 1:
        return 1
    
    distinct_ways = [0] * (n + 1)
    distinct_ways[0] = 1
    distinct_ways[1] = 1

    for i in range(2, n + 1):
        distinct_ways[i] = distinct_ways[i - 1] + distinct_ways[i - 2]

    return distinct_ways[n] 

print(climbing_stairs(n))
print(climbing_stairs(n2))
print(climbing_stairs(n3))