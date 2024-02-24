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


def count_tabu_free(raw: str) -> int:
    parsed = parse_raw(raw)
    print(parsed)
    return 0
