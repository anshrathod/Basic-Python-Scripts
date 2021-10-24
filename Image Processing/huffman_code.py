from cv2 import cv2
import numpy as np
from operator import attrgetter

class Node:
    def __init__(self, val, name, left=None, right=None, parent=None, code=None):
        self.val = val
        self.name = name
        self.left = left
        self.right = right
        self.parent = parent
        self.code = code


    def traverse(self, st, pos, length):
        if pos >= length:
            return self.name, pos
        if st[pos] == '0':
            if self.left == None:
                return self.name, pos
            else:
                node = self.left
                return node.traverse(st, pos+1, length)
        else:
            if self.right == None:
                return self.name, pos
            else:
                node = self.right
                return node.traverse(st, pos+1, length)



img = cv2.imread('lena.jpg', 0)

# cv2.imshow('Orginal image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

height, width = img.shape
no = list(range(0,256))
s = [0]*256


for r in range(height):
    for c in range(width):
        val = img[r,c]
        s[val] = s[val] + 1 


if 0 in s:
    i = 0
    while i < len(s):
        if s[i] == 0:
            del s[i]
            del no[i]
        else:
            i += 1


print('Pixel values ',len(no), no)
print()
print('No of occurrences ',len(s), s)
print()
div = sum(s)
prob = [0]*len(s)

for i in range(len(s)):
    prob[i] = s[i]/div

print('Probabilities ', len(prob),prob)
print()

node_list = []
for i in range(len(no)):
    n = Node(prob[i], no[i])
    node_list.append(n)

copy_list = node_list.copy()
j = 0
while len(node_list) > 1:
    min_1 = min(node_list,key=attrgetter('val'))
    node_list.remove(min_1)
    min_2 = min(node_list,key=attrgetter('val'))
    node_list.remove(min_2)
    new_val = min_1.val + min_2.val
    new_node = Node(new_val, None, min_1, min_2)
    min_1.parent = new_node
    min_1.code = 0
    min_2.parent = new_node
    min_2.code = 1
    node_list.append(new_node)
    j += 1


root = node_list[0]
code = []
for node in copy_list:
    c = ''
    par = node.parent
    while par != None:
        c = c + str(node.code)
        node = par
        par = node.parent

    code.append(c[::-1])


print('Codes: ')
for i in range(len(code)):
    print(f'{i} -> {code[i]}')


final = [0]*len(s)
for i in range(len(s)):
    final[i] = len(code[i]) *s[i]


org = height*width*8
comp = sum(final)
print() 
print('No of bits required for original image: ', org)
print('No of bits required for compressed image:: ', comp)
print('Compression Ratio: ', org/comp)


inter = [[0]*1]*height
for r in range(height):
    inter_code = ''
    for c in range(width):
        val = img[r,c]
        i = no.index(val)
        inter_code = inter_code + code[i]

    inter[r] = inter_code


comp_img = np.zeros([height,width],dtype=np.uint8)
comp_img.fill(0)
for r in range(height):
    pos = 0
    c = 0
    while pos < len(inter[r]):
        pixel, pos = root.traverse(inter[r],pos,len(inter[r]))
        comp_img[r,c] = pixel
        c += 1


print("Compressed image shape: ", comp_img.shape)
print("Compressed image type: ", comp_img.dtype)
cv2.imshow('Compressed Image', comp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()