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

    def __hash__(self):
        return hash((self.rule.first, self.rule.second, self.divider, self.index))
