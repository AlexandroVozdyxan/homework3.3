nums = []
number = (len(nums)+1)//2
# len - довжина масива (nums)
# len(nums)+1 - len = 3 + 1 = 4 тепер довжина масива 4
# //2 - ділення націло на 2
part1 = nums[:number]
# :number - береться перша части масива
# number: - друга частина масива
part2 = nums[number:]
result = [part1, part2]
print(result)