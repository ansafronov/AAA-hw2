from typing import List

class CountVectorizer:
    def __init__(self):
        """
        Class for transforming text corpus to a number of integers >= 0. Each number in returned sequnce represnts one word, its value account for number of particular wod in a given string.
        """
        self.unique_words = []

    def fit(self, text:str):
        """
        Fit string data. Remember all unique words
        """
        self.unique_words = []
        for string in text:
            arr_string = string.split(" ")
            for word in arr_string:
                if word not in self.unique_words:
                    self.unique_words.append(word.lower())
        return self
    
    def transform(self, text: List[str]):
        """
        Transforms text to arrays of integer numbers > 0
        """
        count_encoded = [[0 for _ in self.unique_words] for _ in text]
        # [[0] * len(self.unique_words)] * len(text)
        for i, string in enumerate(text):
            for j, word in enumerate(self.unique_words):
                if word in string.lower():
                    count_encoded[i][j] = self._count_words(word, string.lower())
        return count_encoded

    def fit_transform(self, text: str):
        """
        perfrom fit transform for text corpus and return arrays of integer numbers > 0
        """
        self.fit(text)
        return self.transform(text)

    def get_feature_names(self):
        """
        Return unique words from fitted corpus
        """
        return self.unique_words

    def _count_words(self, key_word, string):
        """
        util function for counting the number of words in a string
        """
        splitted_string = string.split(" ")
        i = 0
        for word in splitted_string:
            if word == key_word:
                i += 1
        return i