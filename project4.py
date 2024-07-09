# project4.py
#
# ICS 33 Spring 2024
# Project 4: Still Looking for Something
import random
from option import Option
from rule import Rule
from symbols import TerminalSymbol, VariableSymbol


class Grammar:
    """Class for Grammar"""
    def __init__(self):
        """Stores the rules in a dictionary"""
        self.rules = {}

    def add_rule(self, rule):
        """Function for adding rules"""
        self.rules[rule.variable] = rule

    def get_rule(self, variable):
        """Function for returning a single rule"""
        try:
            rule = self.rules[variable]
            return rule
        except KeyError as e:
            print(f"{e}. Could not find rule for {variable}.")

    def output_sentence(self, start_variable):
        """Returns a sentence given a start variable"""
        rule_instance = self.get_rule(start_variable)
        sentence = rule_instance.generate_rule(self)
        return sentence


def grammar_parser(path):
    """Parsing function that reads the file then iterate over the lines"""
    grammar = Grammar()

    with open(path, 'r') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line == '{':
            options = []

            i += 1
            variable_name = lines[i].strip()

            i += 1
            while lines[i].strip() != '}':
                line = lines[i].strip()
                symbols = line.split()
                weight = int(symbols[0])

                symbol_list = []
                for symbol in symbols[1:]:
                    if symbol.startswith('[') and symbol.endswith(']'):
                        # Store the symbol in corresponding class
                        clean_symbol = symbol[1:-1]
                        symbol = VariableSymbol(clean_symbol)
                    else:
                        symbol = TerminalSymbol(symbol)
                    # Append the symbol to our list of symbols
                    symbol_list.append(symbol)
                # Lastly now that we have our weight + symbols, we can store it in Option class
                option = Option(weight, symbol_list)
                options.append(option)

                i += 1  # Continue iteration
            # Add the rule to Rule class
            rule = Rule(variable_name, options)
            grammar.add_rule(rule)

        i += 1

    return grammar


def main() -> None:
    file = input()
    sentence_num = int(input())
    start_variable = input()

    grammar = grammar_parser(file)

    for x in range(sentence_num):
        print(grammar.output_sentence(start_variable))


if __name__ == '__main__':
    main()
