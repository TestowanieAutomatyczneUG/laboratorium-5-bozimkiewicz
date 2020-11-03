class Hamming:
    def distance(self, first, second):
        if first == '' and second == '':
            return 0


hamming = Hamming()
print(hamming.distance('', ''))
