from typing import List
from dataclasses import dataclass

@dataclass
class TabuBigramParams:
    """
    Simple dataclass to hold parameters for counting the number of tabu-
    free numbers in an input string

    Args:
        m       (int):         base numbers        (1 <= m <= 36)
        n       (int):         number of digits    (1 <= n <= 100)
        bigrams (List[str]):   list tabu bigrams
    """
    m: int
    n: int
    bigrams: List[str]


def parse_raw(raw: str, delimeter: str = " ") -> TabuBigramParams:
    str_tokens = raw.split(delimeter)

    if len(str_tokens) < 2:
        raise ValueError('Error: Raw string must contain >=2 integers')

    m = int(str_tokens[0])
    if m < 1 or m > 36:
        raise ValueError('Error: m (first number) must meet criteria 1 <= m <= 36')

    n = int(str_tokens[1])
    if n < 1 or n > 100:
        raise ValueError('Error: n (first number) must meet criteria 1 <= n <= 100')

    bigrams = str_tokens[2:]

    return TabuBigramParams(int(m), int(n), bigrams)


def i_to_str(n: int, base: int = 10) -> str:
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if n < base:
        return chars[n]
    else:
        return i_to_str(n // base, base) + chars[n % base]
    
def count_tabu_free(raw: str) -> int:
    parsed = parse_raw(raw)
    print(parsed)

    count = 0
    for i in range(pow(parsed.m, parsed.n)):
        raw_str = i_to_str(i, parsed.m)
        str_rep = raw_str.rjust(parsed.n, '0')
        
        print(f"{str(i).rjust(2, '0')}: {str_rep}")
        if str_rep.startswith('0'):
            print(f"{str_rep} starts with '0'")
            continue
        if str_rep in parsed.bigrams:
            print(f"{str_rep} is a bigram'")
            continue


        count += 1

    return count

