class PairSum:
    def find_pair(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
        return -1


n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target sum: "))

obj = PairSum()
result = obj.find_pair(nums, target)

if result != -1:
    print("Indices of elements:", result)
else:
    print("No pair found")
