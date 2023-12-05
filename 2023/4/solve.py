from typing import Dict 
DEBUG = False

in_file = 'input_test.txt' if DEBUG else 'input'

with open(in_file) as f:
    lines = f.readlines()

def get_inter_cnt(line: str) -> int:
    """Find the count of winning lottery numbers given the scratch card description."""
    log = line.strip().split(':')[1]
    win, have = log.split('|')
    parse_int_list = lambda x: list(map(int, x.split()))
    win_set = set(parse_int_list(win))
    have_set = set(parse_int_list(have))
    inter_cnt = len(win_set & have_set)
    return inter_cnt

def part_one():
    total = 0
    for idx, l in enumerate(lines):
        inter_cnt = get_inter_cnt(l)
        total += pow(2 , inter_cnt - 1) if inter_cnt >= 1 else 0
    
    print(total)

def part_two():
    n = len(lines)
    cnt = [0] * (n + 1)
    cnt[0] = 1
    total = 0
    for idx, line in enumerate(lines):
        total += cnt[idx]
        inter_cnt = get_inter_cnt(line)
        if inter_cnt > 0:
            cnt[idx + 1] += cnt[idx]
            cnt[min(idx + inter_cnt, n - 1) + 1] -= cnt[idx]
        cnt[idx + 1] += cnt[idx]

        # print(cnt)

    print(total)

# part_one()

part_two()