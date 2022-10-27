"""
kittens.py

A programatic solution to calculate the number of descendants a cat has. This program uses the recursive function cat(t) to recursively call itself until the time (no. months) runs out.

Assumptions:
- First cat is already an adult so can instanly be pregnant
- Cats can become instantly pregnant after they give birth
- Cats can have pregnancies consecutively for 6 months but must wait 6 more months to become pregnant again (to maximize population)
"""

import argparse


CATS_PER_LITTER = 6
MIN_PREGNANCY_AGE = 4
LENGTH_OF_PREGNANCY = 2
AVG_PREGNANCIES_PER_YEAR = 3


def cat(t): 
    """c(t): the number of children a cat has (including itself) in _t_ months from birth"""

    sum = 1
    count = 0

    # cats to be born in t months
    t -= MIN_PREGNANCY_AGE
    while (t >= LENGTH_OF_PREGNANCY):
        count += 1
        t -= LENGTH_OF_PREGNANCY

        if count == AVG_PREGNANCIES_PER_YEAR:
            t -= 12-(LENGTH_OF_PREGNANCY*AVG_PREGNANCIES_PER_YEAR)
            count = 0
        
        sum += cat(t) * CATS_PER_LITTER
    
    return sum

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('months', type=int, help="months to model")
    args = parser.parse_args()
    print(cat(args.months+MIN_PREGNANCY_AGE)-1) # subtract 1, not including the first cat
