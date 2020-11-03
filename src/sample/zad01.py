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
            counter = 0
            for i in range(0, len(first)):
                if first[i] != second[i]:
                    counter += 1
            return counter
        if len(first) > len(second):
            raise ValueError('First can\'t be longer than second')
        if len(first) < len(second):
            raise ValueError('Second can\'t be longer than first')
        if len(first) == 0 and len(second) > 0:
            raise ValueError('First can\'t be empty')


hamming = Hamming()
print(hamming.distance('', ''))
print(hamming.distance('A', 'A'))
print(hamming.distance('G', 'T'))
print(hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG"))
print(hamming.distance("GGACGGATTCTG", "AGGACGGATTCT"))
# print(hamming.distance("AATG", "AAA"))
# print(hamming.distance("ATA", "AGTG"))
# print(hamming.distance("", "G"))
