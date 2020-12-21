class Rule:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __eq__(self, other):
        return self.first == other.first and self.second == other.second


class Situation:
    def __init__(self, rule, index, divider):
        self.rule = rule
        self.index = index
        self.divider = divider

    def __eq__(self, other):
        return self.rule == other.rule and \
               self.index == other.index and \
               self.divider == other.divider


class Earley:
    @staticmethod
    def Scan(situation_list, word, j):
        if j == 0:
            return
        for situation in situation_list[j - 1]:
            if situation.rule.second[situation.divider] == word[j - 1]:
                situation_list[j].add(Situation(situation.rule, situation.divider + 1, situation.index))



if __name__ == '__main__':
    grammar = [Rule('S', 'Sa'), Rule('S', 'Sb'), Rule('S', 'C'), Rule('C', 'Dd'), Rule('D', 'cD'), Rule('D', '')]
    word = 'cdba'
    #res = Earley.Check(grammar, word)
    #print(res)
