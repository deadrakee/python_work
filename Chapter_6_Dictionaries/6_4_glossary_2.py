### 6-4. Glossary 2

glossary = {
    'list' : 'A sequence of variables.',
    'tuple' : 'An immutable list.',
    'dictionary' : 'Collection containing key-value pairs.',
    'interpreter' : 'A program that parses python code.',
    'variable' : 'Container for data.',
    'set' : 'Collection of unique elements.',
    'title()' : 'Method to format strings to capitalize each new word.',
}

for term, descr in glossary.items():
    print(f"{term.title()}:\n\t{descr}\n")
