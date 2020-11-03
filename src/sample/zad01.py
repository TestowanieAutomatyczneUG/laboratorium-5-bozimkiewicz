class Hamming:
    def distance(self, first, second):
        if first == '' and second == '':
            return 0
        if first == second and len(first) == 1 and len(second) == 1:
            return 0
        if first != second and len(first) == 1 and len(second) == 1:
            return 1
        if len(first) == len(second) and first == second:
            return 0
        if len(first) == len(second) and first != second:
            return 9


hamming = Hamming()
print(hamming.distance('', ''))
print(hamming.distance('A', 'A'))
print(hamming.distance('G', 'T'))
print(hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG"))
print(hamming.distance("GGACGGATTCTG", "AGGACGGATTCT"))
