def make_divisible_by_3(nums):
    n= 0
    for num in nums:
        r = num % 3
        print(r)
        if r != 0:
            if num > 3:
                
            n = n+r 
        
    return n




nums = [1, 2, 3, 4]
print(make_divisible_by_3(nums))

nums = [3, 6, 9]
print(make_divisible_by_3(nums))