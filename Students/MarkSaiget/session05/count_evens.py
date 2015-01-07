"""Solution to count_evens at codingbat.com"""
# http://codingbat.com/prob/p189616

def count_evens(nums):
    return len([x for x in nums if x % 2 == 0])
