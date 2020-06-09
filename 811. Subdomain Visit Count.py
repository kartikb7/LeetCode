class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counts = {}

        for item in cpdomains:
            count = int(item.split(' ')[0])
            domain = item.split(' ')[1]
            while len(domain.split('.')) > 1:
                if domain in counts:
                    counts[domain] += count
                else:
                    counts[domain] = count
                domain = domain.split('.', 1)[1]
            if domain in counts:
                counts[domain] += count
            else:
                counts[domain] = count

        output = []
        for key, value in counts.items():
            output.append(str(value) + ' ' + key)

        return output