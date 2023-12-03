from typing import Dict 
DEBUG = False

in_file = 'input_test.txt' if DEBUG else 'input'

with open(in_file) as f:
    lines = f.readlines()

MAX_FREQ = {'r': 12, 'g': 13, 'b': 14}

def get_freq(state: str) -> Dict[str, int]:
    freq = {}
    for cube_cnt in state.split(','):
        cnt_raw, color_raw = cube_cnt.split()
        freq[color_raw[0]] = int(cnt_raw.strip())

    if DEBUG:
        print(freq)
    return freq

def check_invalid(freq: Dict[str, int]) -> bool:
    """Returns true if the given state is invalid"""
    return any([freq[k] > MAX_FREQ[k] for k in freq.keys()])

def part_one():
    ans = 0
    get_freq_and_check = lambda s: check_invalid(get_freq(s))

    for idx, l in enumerate(lines):
        log = l.strip().split(':')[1]
        ans += (idx + 1) if not any(map(get_freq_and_check, log.split(';'))) else 0
    
    print(ans)


part_one()