########################################################################################################################


class Rule:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __eq__(self, other):
        return self.first == other.first and self.second == other.second


########################################################################################################################


class Situation:
    def __init__(self, rule, index, divider):
        self.rule = rule
        self.index = index
        self.divider = divider

    def __eq__(self, other):
        return self.rule == other.rule and \
               self.index == other.index and \
               self.divider == other.divider


########################################################################################################################


class AlgorithmEarley:
    def __init__(self, grammar, word):
        self.word = word
        self.grammar = grammar
        self.D = [set() for i in range(len(self.word) + 1)]

    def Scan(self, j):
        if j == 0:
            return
        for situation in self.D[j - 1]:
            try:
                if situation.rule.second[situation.divider] == self.word[j - 1]:
                    self.D[j].add(Situation(situation.rule, situation.divider + 1, situation.index))
            except Exception:
                pass

    def Predict(self, j):
        counter = 0
        for situation in self.D[j]:
            if situation.divider >= len(situation.rule.second):
                continue
            for rule in self.grammar:
                try:
                    if rule.first == situation.rule.second[situation.divider]:
                        s = Situation(rule, 0, j)
                        if s not in self.D[j]:
                            self.D[j].add(s)
                            counter += 1
                except Exception:
                    pass
        return counter

    def Complete(self, j):
        counter = 0
        for situation in self.D[j]:
            if situation.divider != len(situation.rule.second):
                continue
            for second_situation in self.D[situation.index]:
                try:
                    if situation.rule.first == second_situation.rule.second[second_situation.divider]:
                        s = Situation(second_situation.rule, second_situation.divider + 1, second_situation.index)
                        if s not in self.D[j]:
                            self.D[j].add(s)
                            counter += 1
                except Exception:
                    pass
        return counter

#        def Earley(self):
#            self.D[0].add(Situation(Rule('S1', 'S'), 0, 0))
#            for j in range(len(self.word) + 1):
#                self.Scan(j)
#                ...
#            if Situation(Rule('S1', 'S'), 1, 0) in self.D[len(self.word)]:
#                return True
#            else:
#                return False


if __name__ == '__main__':
    grammar = [Rule('S', 'Sa'), Rule('S', 'Sb'), Rule('S', 'C'), Rule('C', 'Dd'), Rule('D', 'cD'), Rule('D', '')]
    word = 'cdba'
    algo = AlgorithmEarley(grammar, word)
    print(algo.Earley())
