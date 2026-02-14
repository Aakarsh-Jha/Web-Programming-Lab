class Subsets:
    def get_subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [curr + [num] for curr in result]
        return result



n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter distinct integers: ").split()))

obj = Subsets()
print(obj.get_subsets(nums))
