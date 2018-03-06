# Naive-Substring-DFA-Generator
Wrote this code to answer a course question.

Given a predicate function, a list of strings of length 1 (the alphabet) and a string size,
it will generate a naive or unoptimized DFA that will only accept strings whose substrings 
satisfy the predicate function for every possible substring.

It is very simple code that makes no optimizations to the basic strategy of enumerating
all possible subsets of the string as states.
