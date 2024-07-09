class TerminalSymbol:
    """Class for the terminal symbols"""
    def __init__(self, value):
        """Holds the value of the terminal symbol"""
        self.value = value

    def generate(self, grammar):
        """allows you to generate the value of the terminal"""
        return self.value


class VariableSymbol:
    """Class for the variable symbols"""
    def __init__(self, name):
        """Stores the name of the variable"""
        self.name = name

    def generate(self, grammar):
        """Generates a value for the variable"""
        rule = grammar.get_rule(self.name)
        variable = rule.generate_rule(grammar)
        return variable
