def search_closing(string, i, close):
    """
    Function to search for closing parenthesis
    """
    found = False
    while not found:
        if string[i] == close:
            return True
        if string[i] == '(':
            if search_closing(string, i + 1, ')'):
                continue
            else:
                return False
        if string[i] == '{':
            if search_closing(string, i + 1, '}'):
                continue
            else:
                return False
        if string[i] == '[':
            if search_closing(string, i + 1, ']'):
                continue
            else:
                return False


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid = True

        if len(s) != 0:
            if s[0] == '(':
                valid = search_closing(s, 1, ')')
            if s[0] == '{':
                valid = search_closing(s, 1, '}')
            if s[0] == '[':
                valid = search_closing(s, 1, ']')

        return valid
