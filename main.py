import string

from Scanner import Scanner
from FiniteAutomata import FiniteAutomata


if __name__ == '__main__':
    fa = FiniteAutomata('integer_fa.in')
    print(str(fa))
    print(fa.verify('+454235'))
    print(fa.verify('+123032'))
    print(fa.verify('-1207200'))
    print(fa.verify('-0'))
    print(fa.verify('0'))
    print(fa.verify('10009'))
    file = open('p1.in', 'r')
    scanner = Scanner(file.read())
