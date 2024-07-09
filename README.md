# GrammarSub
Kathleen Pham


This Python program generates random sentences based on a specified grammar file. It uses a mutually recursive algorithm to traverse the grammar and select random options according to defined weights.

How It Works
The program reads input from the user for:

The path to a grammar file.
The number of random sentences to generate.
The start variable from which sentence generation should begin.

The input file can look like this:
{
HowIsBoo
1 Boo is [Adjective] today
}

{
Adjective
3 happy
3 perfect
1 relaxing
1 fulfilled
2 excited
}

The output can look like this: 
Boo is perfect today
Boo is fulfilled today
Boo is happy today


Running the Program: 
Run python project4.py (Make sure Python 3.x is installed.)
Follow the prompts to input the grammar file path, number of sentences to generate, and start variable.
