"""Using the dict constructor and zip, build a dictionary of numbers from
zero to fifteen and the hexadecimal equivalent (string is fine)."""
dict = {}
nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen"]
numbers = range(16)
for written, x in zip(nums, numbers):
    dict[written] = "%x" % (x)
print dict
