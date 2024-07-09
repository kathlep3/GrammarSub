class Option:
    """Class for Option"""
    def __init__(self, weight, symbols):
        """Stores the weight and symbols of options"""
        self.weight = weight
        self.symbols = symbols

    def generate_option(self, grammar):
        """Generates the options based on weight and symbols without needing to knowing the symbol type"""
        symbol_list = []
        for symbol in self.symbols:
            symbol_list.append(symbol.generate(grammar))
        option = ' '.join(symbol_list)
        return option
