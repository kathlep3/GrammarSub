import random


class Rule:
    """Class for Rules"""
    def __init__(self, variable, options):
        """Stores the variable and options"""
        self.variable = variable
        self.options = options

    def generate_rule(self, grammar):
        """Generates a sentence based on the rule"""
        sum_weight = sum(option.weight for option in self.options)
        if sum_weight == 0:
            print("Error. Weight sum is 0.")
            return None

        chosen_option = random.uniform(0, sum_weight)
        current_weight = 0
        for option in self.options:
            current_weight += option.weight
            if chosen_option <= current_weight:
                sentence = option.generate_option(grammar)
                return sentence

        print("Error. No option chosen.")
        return None
