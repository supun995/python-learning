def is_palindrome_word(word: str) -> bool:
    ''' Implement the body of this function so it returns True if the word is a palindrome otherwise returns False.

        Note:
            Palindromes are words that are the same forward and backward.
            For example: kayak spelled backwards is: kayak.
        Args:
            word: an individual word without any whitespace characters.

        Example:
        >>> # All of the strings below are palindromes.
        >>> all(is_palindrome_word(word) for word in 'redivider deified civic radar level rotor kayak reviver racecar madam refer'.split())
        True
        >>> # None of the strings below are palindromes.
        >>> not any(is_palindrome_word(word) for word in 'fish dive fraction splinter wheel'.split())
        True
    '''
    # normalize the word to be lowercase
    word = word.lower()
    # utilize the Pythonic manner of reversing a list.
    return word == word[::-1]

def is_palindrome_phrase(phrase: str) -> bool:
    ''' Implement the body of this function so it returns True if the phrase is a palindrome otherwise returns False.

        All non-ascii characters are removed before checking the phrase.

        Note:
            Palindromes are words that are the same forward and backward.
            For example: kayak spelled backwards is: kayak.
        Args:
            phrase: one or more words separated by whitespace characters.

        Example:
        >>> # All of the strings below are palindromes.
        >>> all(is_palindrome_phrase(phrase) for phrase in ['Mr. Owl ate my metal worm', 'Do geese see God?', 'Was it a car or a cat I saw?', 'Murder for a jar of red rum',  'Rats live on no evil star', 'Live on time, emit no evil', 'Step on no pets'])
        True
        >>> # None of the strings below are palindromes.
        >>> not any(is_palindrome_phrase(phrase) for phrase in ['Time is not real', 'Changes in state require no governance'])
        True
    '''
    # normalize the phrase to be lowercase and remove any non-alpha-numeric characters.
    phrase = ''.join([char for char in phrase.lower() if char.isalnum()])
    return phrase == phrase[::-1]


if __name__ == '__main__':
    import doctest
    print(doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL))