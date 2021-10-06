from itertools import permutations

for i in permutations(input('enter your text: ')):
    print(''.join(i))
