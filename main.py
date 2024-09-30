class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        g = len(list1 + list2)
        f = []
        for i, n in enumerate(list1):
            if n in list2:
                if i + list2.index(n) < g:
                    f = []
                    f.append(n)
                elif i + list2.index(n) == g:
                    f.append(n)
                else:
                    break
                g = i + list2.index(n)
        return f
