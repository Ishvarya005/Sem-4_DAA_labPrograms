def minCandies(ratings):
    n = len(ratings)
    candies = [1] * n  # Step 1: Initially, give each child 1 candy
    
    # Step 2: Scan from left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    # Step 3: Scan from right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    # The total number of candies needed is the sum of the candies list
    return sum(candies)

def pylons(k, arr):
    n = len(arr)
    plants = 0
    i = 0

    while i < n:
        j = min(i + k - 1, n - 1)
        while j >= i - k + 1 and arr[j] == 0:
            j -= 1

        if j < i - k + 1:
            return -1

        plants += 1
        i = j + k

    return plants

def maximumPeople(p, x, c, r):
    n = len(p)
    m = len(c)
    ans = sum(p)  # Initialize the answer with the total population

    # Loop through each cloud
    for i in range(m):
        cur = 0
        # Calculate the coverage range of the cloud
        coverage_start = max(0, c[i] - r[i])
        coverage_end = min(max(x), c[i] + r[i])

        # Loop through each town and check if it's covered by the cloud
        for j in range(n):
            if coverage_start <= x[j] <= coverage_end:
                cur += p[j]

        # Remove the current cloud and find the maximum population in sunny towns
        removed_cloud_population = sum([p[j] for j in range(n) if coverage_start <= x[j] <= coverage_end])
        ans = max(ans, ans - removed_cloud_population + cur)

    return ans
   


def main():
    # Part 1: Min Candies
    ratings = input("Enter the ratings separated by space: ")
    ratings = list(map(int, ratings.split()))
    print("Min. candies that can be distributed is:", minCandies(ratings))

    # Part 2: Pylons
    n, k = map(int, input("Enter the number of cities and distribution range separated by space: ").split())
    arr = list(map(int, input("Enter the suitability for building a plant separated by space: ").split()))
    result_pylons = pylons(k, arr)
    print("Minimum number of plants required:", result_pylons)

    # Part 3: Maximum People
    # Input
    n = int(input("Enter the number of towns: "))
    p = list(map(int, input("Enter the populations of each town separated by space: ").split()))
    x = list(map(int, input("Enter the locations of the towns separated by space: ").split()))
    m = int(input("Enter the number of clouds: "))
    c = list(map(int, input("Enter the locations of the clouds separated by space: ").split()))
    r = list(map(int, input("Enter the extents of coverage of the clouds separated by space: ").split()))

    # Output
    result_maximum_people = maximumPeople(p, x, c, r)
    print("Maximum number of people in sunny towns after removing exactly one cloud:", result_maximum_people)


if __name__ == "__main__":
    main()
