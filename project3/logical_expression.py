#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        logical_expression
# Purpose:     Contains logical_expression class, inference engine,
#              and assorted functions
#
# Created:     09/25/2011
# Last Edited: 04/06/2020
# Notes:       *Code modified for python3 by Chance Cardona
#              *This contains code ported by Christopher Conly from C++ code
#               provided by Dr. Vassilis Athitsos
#              *Several integer and string variables are put into lists. This is
#               to make them mutable so each recursive call to a function can
#               alter the same variable instead of a copy. Python won't let us
#               pass the address of the variables, so put it in a list which is
#               passed by reference. We can also now pass just one variable in
#               the class and the function will modify the class instead of a
#               copy of that variable. So, be sure to pass the entire list to a
#               function (i.e. if we have an instance of logical_expression
#               called le, we'd call foo(le.symbol,...). If foo needs to modify
#               le.symbol, it will need to index it (i.e. le.symbol[0]) so that
#               the change will persist.
#              *Written to be Python 3.8 compliant
#-------------------------------------------------------------------------------

import sys
from copy import copy

#-------------------------------------------------------------------------------
# Begin code that is ported from code provided by Dr. Athitsos
class logical_expression:
    """A logical statement/sentence/expression class"""
    # All types need to be mutable, so we don't have to pass in the whole class.
    # We can just pass, for example, the symbol variable to a function, and the
    # function's changes will actually alter the class variable. Thus, lists.
    def __init__(self):
        self.symbol = ['']
        self.connective = ['']
        self.subexpressions = []


def print_expression(expression, separator):
    """Prints the given expression using the given separator"""
    if expression == 0 or expression == None or expression == '':
        print('\nINVALID\n')

    elif expression.symbol[0]: # If it is a base case (symbol)
        sys.stdout.write('%s' % expression.symbol[0])

    else: # Otherwise it is a subexpression
        sys.stdout.write('(%s' % expression.connective[0])
        for subexpression in expression.subexpressions:
            sys.stdout.write(' ')
            print_expression(subexpression, '')
            sys.stdout.write('%s' % separator)
        sys.stdout.write(')')


def read_expression(input_string, counter=[0]):
    """Reads the next logical expression in input_string"""
    # Note: counter is a list because it needs to be a mutable object so the
    # recursive calls can change it, since we can't pass the address in Python.
    result = logical_expression()
    length = len(input_string)
    while True:
        if counter[0] >= length:
            break

        if input_string[counter[0]] == ' ':    # Skip whitespace
            counter[0] += 1
            continue

        elif input_string[counter[0]] == '(':  # It's the beginning of a connective
            counter[0] += 1
            read_word(input_string, counter, result.connective)
            read_subexpressions(input_string, counter, result.subexpressions)
            break

        else:  # It is a word
            read_word(input_string, counter, result.symbol)
            break
    return result


def read_subexpressions(input_string, counter, subexpressions):
    """Reads a subexpression from input_string"""
    length = len(input_string)
    while True:
        if counter[0] >= length:
            print('\nUnexpected end of input.\n')
            return 0

        if input_string[counter[0]] == ' ':     # Skip whitespace
            counter[0] += 1
            continue

        if input_string[counter[0]] == ')':     # We are done
            counter[0] += 1
            return 1

        else:
            expression = read_expression(input_string, counter)
            subexpressions.append(expression)


def read_word(input_string, counter, target):
    """Reads the next word of an input string and stores it in target"""
    word = ''
    while True:
        if counter[0] >= len(input_string):
            break

        if input_string[counter[0]].isalnum() or input_string[counter[0]] == '_':
            target[0] += input_string[counter[0]]
            counter[0] += 1

        elif input_string[counter[0]] == ')' or input_string[counter[0]] == ' ':
            break

        else:
            print('Unexpected character %s.' % input_string[counter[0]])
            sys.exit(1)


def valid_expression(expression):
    """Determines if the given expression is valid according to our rules"""
    if expression.symbol[0]:
        return valid_symbol(expression.symbol[0])

    if expression.connective[0].lower() == 'if' or expression.connective[0].lower() == 'iff':
        if len(expression.subexpressions) != 2:
            print('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() == 'not':
        if len(expression.subexpressions) != 1:
            print('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() != 'and' and \
         expression.connective[0].lower() != 'or' and \
         expression.connective[0].lower() != 'xor':
        print('Error: unknown connective %s.' % expression.connective[0])
        return 0

    for subexpression in expression.subexpressions:
        if not valid_expression(subexpression):
            return 0
    return 1


def valid_symbol(symbol):
    """Returns whether the given symbol is valid according to our rules."""
    if not symbol:
        return 0

    for s in symbol:
        if not s.isalnum() and s != '_':
            return 0
    return 1

# End of ported code
#-------------------------------------------------------------------------------
# Add all your functions here

def check_true_false(knowledge_base, statement):
    """Determines if a knowledge base kb entails a statement."""
    statementEntailed = False
    negationEntailed = False
    negation = logical_expression()
    negation.connective[0] = 'not'
    negation.subexpressions.append(statement)
    if tt_entails(knowledge_base, statement):
        statementEntailed = True
    if tt_entails(knowledge_base, negation):
        negationEntailed = True

    if statementEntailed and negationEntailed:
        return 'both true and false'
    elif statementEntailed:
        return 'definitely true'
    elif negationEntailed:
        return 'definitely false'
    else:
        return 'possibly true, possibly false'

#TODO implement TT_entails Algorithm for truth table entailment.
#       check_all and extract symbols.
#TODO extract symbols stores in a list the set of all symbols from all 3 txt files

#TODO check_true_false takes a kb, a statement, and set of boolean assignments
#   for each symbol to check if kb entails statement.
#   this may be just the code used for hw q 5 for def true, etc w/ resolution alg.

def tt_entails(knowledge_base, statement):
    symbols = set({})
    extract_symbols(knowledge_base, symbols)
    extract_symbols(statement, symbols)
    return tt_check_all(knowledge_base, statement, symbols, model={})

def tt_check_all(knowledge_base, statement, symbols, model):
    if len(symbols) == 0:
        if pl_true(knowledge_base, model):
            return pl_true(statement, model)
        else:
            return True
    else:
        P = symbols.pop()
        model[P] = True
        pTrue = tt_check_all(knowledge_base, statement, symbols, model)
        model[P] = False
        pFalse = tt_check_all(knowledge_base, statement, symbols, model)
        return pTrue and pFalse

def pl_true(statement, model):
    if statement.symbol[0]:		#base case
        return model[statement.symbol[0]]
    if statement.connective[0].lower() == 'and':
        if len(statement.subexpressions) == 0:
            return True
        for subexpression in statement.subexpressions:
            if not pl_true(subexpression, model):
                return False
        return True
    elif statement.connective[0].lower() == 'or':
        for subexpression in statement.subexpressions:
            if pl_true(subexpression, model):
                return True
        return True
    elif statement.connective[0].lower() == 'xor':
        numTrue = 0
        for subexpression in statement.subexpressions:
            if pl_true(subexpression, model):
                numTrue += 1
        if numTrue == 1:
            return True
        return False
    elif statement.connective[0].lower() == 'not':
        return not pl_true(statement.subexpressions[0], model)
    elif statement.connective[0].lower() == 'if':
        if pl_true(statement.subexpressions[0], model) and not pl_true(statement.subexpressions[1], model):
            return False
        return True
    elif statement.connective[0].lower() == 'iff':
        if pl_true(statement.subexpressions[0], model) == pl_true(statement.subexpressions[1], model):
            return True
        return False

def extract_symbols(statement, symbols): #symbols is a set.
    if statement.symbol[0]:
        symbols.add(statement.symbol[0])
    else:
        for subexpression in statement.subexpressions:
            extract_symbols(subexpression, symbols)
