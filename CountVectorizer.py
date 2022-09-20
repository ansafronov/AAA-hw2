from typing import List

class CountVectorizer:
    def __init__(self):
        self.unique_words = []

    def fit(self, text:str):
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
        self.fit(text)
        return self.transform(text)

    def get_feature_names(self):
        return self.unique_words

    def _count_words(self, key_word, string):
        splitted_string = string.split(" ")
        i = 0
        for word in splitted_string:
            if word == key_word:
                i += 1
        return i