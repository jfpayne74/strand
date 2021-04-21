#The Strand puzzle asked you to imagine a street numbered consecutively: 1, 2, 3, 4, etc.

#A man stood outside of his house and looked left and looked right.

#He realised that all the numbers below that of his house down to 1 added up to exactly the same as the numbers ascending up to the end of the street.

#For example, if there were four houses in the street and he was in house number 3...

#To his left would be 1 + 2 = 3, while to his right would be house 4... So that's not a solution. But what is the solution?

#As it turns out there are plenty of solutions, and the streets get big fast...

a = 0 #We'll calculate the first ten solutions, if the programme runs for enough time...

def calc(n):
    global a
    y = int(n / 2 + 1) #The man's house, y, needs to be at least half way along his street.
    z = 0
    x = 1 #This sets x as greater than z so our while loop may begin...
    while x > z: #As soon as the houses with numbers lower than the man's totals greater than those higher, we have moved far enough along the road the be satisfied there is no solution for this length street.
        z = (y * (y - 1)) / 2 #The formula for working out the total of the house numbers below the man's.
        x = (n * (n + 1) / 2) - (y * (y + 1)) / 2 #The formula for working out the total of the house numbers above the man's.
        if x == z: #If a solution is found...
            print(f"Total houses in the street = {n}; man's house = {y}") 
            print(x)
            print(z) #Printing x and z checks that the two totals are indeed the same.
            a += 1
        else:
            y += 1
n = 3
while a <= 10: #If we ever find the first ten solutions, the programme can have a well-deserved rest.
    calc(n)
    n += 1