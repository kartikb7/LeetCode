class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = {}
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

        word_list = []

        sorted_word = dict(sorted(word_freq.items(), key=lambda x: x[0]))
        sorted_word_freq = sorted(sorted_word.items(), key=lambda x: x[1], reverse=True)

        for val in sorted_word_freq:
            word_list.append(val[0])
            k -= 1
            if k == 0:
                break

        return word_list