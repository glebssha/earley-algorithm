from utils import Rule, Situation


class Earley:
    def __init__(self, grammar, word):
        self.word = word
        self.grammar = grammar
        self.D = [set() for i in range(len(self.word) + 1)]
        self.D[0].add(Situation(Rule('S1', 'S'), 0, 0))

    def Scan(self, j):
        if j == 0:
            return
        for situation in self.D[j - 1]:
            try:
                if situation.rule.second[situation.divider] == self.word[j - 1]:
                    self.D[j].add(Situation(situation.rule, situation.index, situation.divider + 1))
            except Exception:
                pass

    def Predict(self, j):
        situations_to_add = []
        for situation in self.D[j]:
            if situation.divider < len(situation.rule.second):
                for rule in self.grammar:
                    try:
                        if rule.first == situation.rule.second[situation.divider]:
                            situations_to_add.append(Situation(rule, j, 0))
                    except Exception:
                        pass
        for s in situations_to_add:
            self.D[j].add(s)

    def Complete(self, j):
        situations_to_add = []
        for situation in self.D[j]:
            if situation.divider != len(situation.rule.second):
                continue
            for second_situation in self.D[situation.index]:
                try:
                    if situation.rule.first == second_situation.rule.second[second_situation.divider]:
                        s = Situation(second_situation.rule, second_situation.index, second_situation.divider + 1)
                        situations_to_add.append(s)
                except Exception:
                    pass
        for s in situations_to_add:
            self.D[j].add(s)

    def Earley(self):
        for i in range(0, len(self.word) + 1):
            self.Scan(i)
            old_length = len(self.D[i])
            self.Predict(i)
            self.Complete(i)
            new_length = len(self.D[i])
            while new_length != old_length:
                old_length = new_length
                self.Predict(i)
                self.Complete(i)
                new_length = len(self.D[i])

        if Situation(Rule('S1', 'S'), 0, 1) in self.D[len(self.word)]:
            return 'YES'
        else:
            return 'NO'
