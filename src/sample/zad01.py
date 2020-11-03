class Hamming:
    def distance(self, first, second):
        if len(first) != len(second):
            raise ValueError('Values cannot be of different length')
        counter = 0
        for i in range(0, len(first)):
            if first[i] != second[i]:
                counter += 1
        return counter


hamming = Hamming()
print(hamming.distance('', ''))
print(hamming.distance('A', 'A'))
print(hamming.distance('G', 'T'))
print(hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG"))
print(hamming.distance("GGACGGATTCTG", "AGGACGGATTCT"))
# print(hamming.distance("AATG", "AAA"))
# print(hamming.distance("ATA", "AGTG"))
# print(hamming.distance("", "G"))
# print(hamming.distance("G", ""))
