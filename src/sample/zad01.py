class Hamming:
    def distance(self, first, second):
        if first == '' and second == '':
            return 0
        if first == second:
            return 0


hamming = Hamming()
print(hamming.distance('', ''))
print(hamming.distance('A', 'A'))
