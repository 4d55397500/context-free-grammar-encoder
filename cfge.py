import nltk
from nltk.parse.generate import generate
import numpy as np


SAMPLE_GRAMMAR_STRING = """
S -> NP VP
VP -> V NP | V NP PP
V -> "saw" | "ate"
NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
Det -> "a" | "an" | "the" | "my"
N -> "dog" | "cat" | "cookie" | "park"
PP -> P NP
P -> "in" | "on" | "by" | "with"
"""


ARITHMETIC_GRAMMAR_STRING = """
S -> S '+' T | S '*' T | S '/' T | T
T -> '(' S ')' | 'sin(' S ')' | 'exp(' S ')'
T -> 'x' | '1' | '2' | '3'
"""


class ContextFreeGrammarEncoder(object):

    def __init__(self, grammar_string):
        self.grammar = nltk.CFG.fromstring(grammar_string)
        self.productions = self.grammar.productions()
        self.n = len(self.productions)
        self.production_indices = dict(zip([str(pr) for pr in self.productions], range(0, self.n)))
        self.parser = nltk.RecursiveDescentParser(self.grammar)

    def encode(self, statement):
        indices = []
        ContextFreeGrammarEncoder.preorder_traverse(self.parser.parse(statement).__next__(), self.cbk(indices))
        k = len(indices)
        x = np.zeros((k, self.n))
        x[np.arange(k), indices] = 1.
        return x

    def generate_statements(self, depth):
        return generate(self.grammar, depth=depth)

    @staticmethod
    def preorder_traverse(p, cb):
        cb(p)
        if len(p) > 1:
            for child in p:
                ContextFreeGrammarEncoder.preorder_traverse(child, cb)

    def cbk(self, arr):
        def f(p):
            arr.append(self.production_indices[str(p.productions()[0])])
        return f



cf = ContextFreeGrammarEncoder(SAMPLE_GRAMMAR_STRING)
for statement in cf.generate_statements(depth=4):
    print("statement: {}".format(statement))
    print("encoding: {}".format(cf.encode(statement)))
    print("-----")
