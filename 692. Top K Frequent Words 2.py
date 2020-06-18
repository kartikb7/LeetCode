class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        word_list = []

        sorted_word = sorted(word_freq, key=lambda word: (-word_freq[word], word))

        return sorted_word[:k]