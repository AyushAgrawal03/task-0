N = int(input())
nums = list(map(int, input().split()))

largest = nums[0]
smallest = nums[0]
total = 0
even = 0
odd = 0

for i in nums:
    if i>largest:
        largest = i
    if i<smallest:
        smallest=i
    total += i
    if i%2 == 0:
        even += 1
    else:
        odd += 1

print("Largest: ", largest)
print("Smallest: ", smallest)
print("Sum: ", total)
print("Even Count: ", even)
print("Odd Count: ", odd)
print("Reversed: ", end = " ")
for i in range(len(nums)-1, -1, -1):
    print(nums[i], end = " ")
