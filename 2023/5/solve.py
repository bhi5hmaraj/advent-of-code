from typing import Any, Dict, List
import sortedcontainers
from dataclasses import dataclass
from functools import partial, reduce
from itertools import accumulate

DEBUG = False

in_file = 'input_test.txt' if DEBUG else 'input'

with open(in_file) as f:
    lines = f.readlines()


@dataclass
class Piece:
    codomain_start: int
    domain_start: int
    size: int


class FoodFunc:

    def __init__(self, ranges: List[Piece]) -> None:
        # maps the domain start to the actual range
        self.pieces_dict = {r.domain_start: r for r in ranges}
        # sorted list of domain starts, used for fast lower bound lookup
        self.sorted_pieces_list = sortedcontainers.SortedKeyList(self.pieces_dict.keys())

    def __call__(self, x: int) -> int:
        eps = 0.001
        lower_bound = self.sorted_pieces_list.bisect_key_left(x + eps) - 1
        if lower_bound < 0:
            return x
        
        candidate_piece = self.pieces_dict[self.sorted_pieces_list[lower_bound]]
        if x < candidate_piece.domain_start + candidate_piece.size:
            return candidate_piece.codomain_start + (x - candidate_piece.domain_start)
        else:
            return x
    


def part_one():
    seeds = list(map(int, lines[0].split(':')[1].split()))
    foodfuncs = []
    curr_piece_list = []
    
    for line in lines[2:]:
        if 'map' in line:
            curr_piece_list = []
        elif line == '\n': # pesky bug, the final map was not added!!!!
            foodfuncs.append(FoodFunc(curr_piece_list))
        else:
            curr_piece_list.append(Piece(*tuple(map(int, line.split()))))
        
    
    # print(foodfuncs[0](99))

    apply = lambda x, f: f(x)
    seed_to_loc_func = partial(reduce, apply, foodfuncs)
    # seed_to_loc_func = lambda x: accumulate(foodfuncs, apply, initial=x)
    loc_list = list(map(seed_to_loc_func, seeds))
    # print(list(map(list, loc_list)))
    print(min(loc_list))
    # print(len(foodfuncs))
    # print(foodfuncs[-1])


part_one()