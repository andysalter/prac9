
# from LinearProbeTable import Dictionary
from SeparateChainTable import Dictionary

class SpellChecker():
    def __init__(self):
        """
        Initialise dictionary - go through each word in dictionary file and
        add it along with common derivations to the data structure.
        complexity:             Best = Worst = O(1)
        pre-conditions:         There is a class Dictionary
        post-conditions:        A dictionary exists of the commonality of words

        **------------------------------------->
        these lines create common derivations of each dictionary word. This
        reduces our number of false negatives by quite a large number but is
        problematic as now the "dictionary" has misspelled words - those in
        which the derivation doesn't apply. This means words that ARE misspelt
        can potentially be seen as correctly spelled. eg. "accessorys". Thus,
        the following lines are optional depending on which facet (integrity or
        range) of the dictionary we wish to trade off...
        **------------------------------------->

        """
        self.freq_dict = Dictionary(131519, 7759)
        with open('word_frequencies_big.txt', 'r') as file:
            for line in file:
                line = line.split()
                self.freq_dict[line[0]] = line[1]
                # **------------------------------------->
                self.freq_dict[line[0] + 's'] = line[1]
                self.freq_dict[line[0] + 'ly'] = line[1]
                if line[0][-1] == 'e':
                    # if word ends in e, remove e for the following
                    line[0] = line[0][:-1]
                self.freq_dict[line[0] + 'ed'] = line[1]
                self.freq_dict[line[0] + 'er'] = line[1]
                self.freq_dict[line[0] + 'ing'] = line[1]
                # **------------------------------------->

    def remove_punc(self, word):
        """
        Remove trailing punctuation and ensure all letters are lowercase
        :param word:            The word to be processed
        :return:                Processed word
        """
        punctuation = ('"', "'", '--', '(', ')', '!', '.', ',', '?', ':', ';')
        for item in punctuation:
            word = word.strip(item)     # removes punctuation
        word = word.lower()             # ensures word is lowercase
        return word

    def query(self, word):
        """
        Returns the commonality class of a word
        complexity:             Best O(1) worst = O(n)
        pre-conditions:         There exists a class Dictionary
        :param word:            The word to be queried
        :return:                The commonality class of the queried word
        """
        value_dict = Dictionary(3, 7759, [
            ('1', 'Rare'), ('2', 'Uncommon'), ('3', 'Common')])
        try:
            value = self.freq_dict[word]
            if value is None:
                raise KeyError
            return value_dict[value]
        except KeyError:
            return 'Unknown'

    def class_count(self, filepath):
        """
        Counts the occurrences of each commonality class
        complexity:             Best = Worst = O(n)
        :param filepath:        filepath of text file to be analysed
        :return:                tuple of occurrences + total word count:
                                (rare, uncommon, common, misspelled, word_count)
        """
        rare = uncommon = common = misspelled = 0
        word_count = 0

        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.replace('-', ' ')      # separates hyphenated words
                for word in line.split():
                    word_count += 1
                    word = self.remove_punc(word)

                    try:
                        value = self.freq_dict[word]
                        if value == '1':
                            rare += 1
                        elif value == '2':
                            uncommon += 1
                        elif value == '3':
                            common += 1
                        elif value is None:
                            raise KeyError
                    except KeyError:
                        misspelled += 1
        counts = (rare, uncommon, common, misspelled, word_count)
        return counts

    def spell_check(self, filein, fileout='spellcheck.txt'):
        """
        Finds and writes to fileout the words in filein which
        are not in the dictionary
        complexity:             Best = Worst = O(n)
        pre-conditions:         n/a
        post-conditions:        n/a
        :param filepath:        filepath of text file to be analysed
        :return:                tuple of occurrences + total word count: (rare, uncommon, common, misspelled, word_count)
        """
        with open(filein, 'r', encoding='utf-8') as filein, open(fileout, 'w', encoding='utf-8') as fileout:

            for line_index, line in enumerate(filein):
                line = line.replace('-', ' ')       # separates hyphenated words
                misspelled_line = []
                for word in line.split():
                    word = self.remove_punc(word)

                    try:
                        value = self.freq_dict[word]
                        if value is None:
                            raise KeyError
                    except KeyError:
                        misspelled_line.append(word)

                if len(misspelled_line) != 0:
                    fileout.write(str(line_index) + '|\t')
                    for misspelled_word in misspelled_line:
                        fileout.write(str(misspelled_word) + ' ')
                    fileout.write('\n')
