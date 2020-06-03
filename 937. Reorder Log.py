import re


class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        numeric_logs = []
        word_logs = []

        if logs == None:
            return logs

        for i in range(len(logs)):
            if re.match('[0-9]', logs[i].split(' ')[1]) != None:
                numeric_logs.append(logs[i])
            else:
                word_logs.append(logs[i])
                print(word_logs[-1].split(' ', 1))
                index = len(word_logs) - 1
                while word_logs[index].split(' ', 1)[1] <= word_logs[index - 1].split(' ', 1)[1] and index >= 1:
                    temp = word_logs[index]
                    word_logs[index] = word_logs[index - 1]
                    word_logs[index - 1] = temp
                    index -= 1

        return word_logs + numeric_logs