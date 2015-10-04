from SpellChecker import SpellChecker
from menu import Menu


def freq_analysis(spellchecker):
    """
    description:            Prints the occurrences of each commonality class and their relative proportions in a given file
    complexity:             Best = worst = O(n) where n is the number of words in the file
    :param spellchecker:    Instance of SpellChecker
    """
    filepath = input("> Enter the filepath of a text file: \n# ")
    try:
        print('> Working...')
        class_counts = spellchecker.class_count(filepath)
    except UnicodeDecodeError:
        print("> File must be a unicode text file.")
        return
    except OSError:
        print("> File does not exist.")
        return

    word_count = class_counts[4]

    print('> Frequency analysis for file', filepath.rpartition('/')[-1] + ':')
    if word_count == 0:
        print("> The file contains no words.")
        return
    print('Total word count: '.ljust(22), word_count)
    print('Rare words: '.ljust(22), str(class_counts[0]).ljust(12), 'Proportion: ', class_counts[0] / word_count)
    print('Uncommon words: '.ljust(22), str(class_counts[1]).ljust(12), 'Proportion: ', class_counts[1] / word_count)
    print('Common words: '.ljust(22), str(class_counts[2]).ljust(12), 'Proportion: ', class_counts[2] / word_count)
    print('Misspelled words: '.ljust(22), str(class_counts[3]).ljust(12), 'Proportion: ', class_counts[3] / word_count)


def query(spellchecker):
    """
    description:            Prints the commonality class of a word
    complexity:             Best O(1) worst = O(n)
    :param spellchecker:    Instance of SpellChecker
    """
    word = input("> Enter a word to query: \n# ")
    print('Commonality: '.ljust(22), spellchecker.query(word))


def spell_check(spellchecker):
    """
    description:            Finds and writes to fileout the words in filein which are classified as misspelt
    complexity:             Best = Worst = O(n) where n is the total number of words in text file: filein
    pre-conditions:         n/a
    post-conditions:        n/a
    :param spellchecker:    Instance of SpellChecker
    """
    filein = input('> Enter the filepath of file to spell check: \n# ')
    try:
        open(filein, 'r', encoding='utf-8')
    except UnicodeDecodeError:
        print('> File must be a unicode text file.')
        return
    except OSError:
        print("> File does not exist.")
        return

    fileout = input('> Enter the filepath of output file: \n# ')
    try:
        open(fileout, 'w')
    except OSError:
        print("> Invalid directory structure.")
        return

    print('> Working...')
    spellchecker.spell_check(filein, fileout)


def quit_menu(none):
    print('> Goodbye.')
    quit()


# initialisation:
checker = SpellChecker()
the_menu = Menu(['Frequency Analysis', 'Frequency Query', 'Spell Checker', 'Quit'])
compute = {'1': freq_analysis, '2': query, '3': spell_check, '4': quit_menu}

# control structure:
while True:

    while True:
        print(the_menu)
        selection = input('# ')
        if selection in (str(i) for i in range(1, len(compute) + 1)):
            break
        print("> Enter integer 1 -", len(compute))

    compute[selection](checker)


