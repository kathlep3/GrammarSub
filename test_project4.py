import unittest
from project4 import Grammar, grammar_parser, main
from rule import Rule
from option import Option
from symbols import TerminalSymbol, VariableSymbol
from test_double import TestDoubleInput, TestDoubleOutput


class TestGrammar(unittest.TestCase):
    """Test class for project 4 file and Grammar class"""
    def test_add_rule(self):
        grammar = Grammar()
        rule = Rule('Hello', [])
        grammar.add_rule(rule)
        self.assertEqual(grammar.rules["Hello"], rule)

    def test_get_rule(self):
        """Tests grammar.get_rule()"""
        grammar = Grammar()
        rule = Rule('Hello', [])
        grammar.rules["Hello"] = rule
        self.assertEqual(grammar.get_rule("Hello"), rule)

    def test_output_sentence(self):
        """Tests for exception in grammar.get_rule()"""
        grammar = Grammar()
        options = [Option(1, [TerminalSymbol("Output"), TerminalSymbol("Sentence")])]
        rule = Rule("Grammar", options)
        grammar.rules["Grammar"] = rule

        start_variable = "Grammar"
        result = grammar.output_sentence(start_variable)
        expected = "Output Sentence"
        self.assertEqual(result, expected)

    def test_grammar_parser(self):
        """Tests the grammar parser"""
        grammar = grammar_parser("grammar_file_input.txt")
        self.assertIsInstance(grammar, Grammar)
        self.assertIn("HowIsBoo", grammar.rules)
        self.assertIn("Adjective", grammar.rules)


class TestRule(unittest.TestCase):
    """Test class for Rule class"""
    def test_generate_rule(self):
        pass


class TestOption(unittest.TestCase):
    """Test class for Option class"""
    def test_generate_option(self):
        grammar = Grammar()
        options = [Option(1, [TerminalSymbol("Option"), TerminalSymbol("Working")])]
        result = options.generate_option(grammar)
        expected = "Option Working"
        self.assertEqual(result, expected)


class TestTerminalSymbol(unittest.TestCase):
    """Test class for TerminalSymbol class in symbols.py"""
    def test_generate(self):
        grammar = Grammar()
        terminal = TerminalSymbol("Terminal")
        result = terminal.generate(grammar)
        self.assertEqual(result, "Terminal")


class TestVariableSymbol(unittest.TestCase):
    """Test class for VariableSymbol class in symbols.py"""
    def test_generate(self):
        variable = VariableSymbol("Variable")
        grammar = Grammar()
        rule = Rule("Variable", [Option(1, [TerminalSymbol("Variable")])])
        grammar.add_rule(rule)
        result = variable.generate(grammar)
        self.assertEqual(result, "Variable")


class TestMain(unittest.TestCase):
    def test_main(self):
        file = "grammar_file_input.txt"
        sent_num = 10
        start_var = "HowIsBoo"

        start_output = TestDoubleOutput()
        print_builtin = print
        print = start_output.write

        main()

        print = print_builtin

        final_output = start_output.output()
        self.assertTrue(final_output.strip())


if __name__ == '__main__':
    unittest.main()
