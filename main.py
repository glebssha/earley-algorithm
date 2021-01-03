from utils import Rule
from algorithm import Earley


if __name__ == '__main__':
    n = int(input())
    grammar = []
    for i in range(n):
        s = input().split('->')
        grammar.append(Rule(s[0],s[1]))
    word = input()
    algo = Earley(grammar, word)
    print(algo.Earley())
