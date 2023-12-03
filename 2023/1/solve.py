DEBUG = False

in_file = 'input_test.txt' if DEBUG else 'input.txt'

with open(in_file) as f:
    lines = f.readlines()

def part_one():
    print(sum(map(lambda nums: int(nums[0] + nums[-1]), 
              map(lambda l : list(filter(lambda ch: ch >= '0' and ch <= '9', l)), lines))))