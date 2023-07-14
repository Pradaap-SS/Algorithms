'''
Huffman Coding:
Huffman coding is a lossless data compression algorithm that assigns variable-length codes to characters 
based on their frequencies. Characters that occur more frequently are assigned shorter codes.
'''

import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_map = {}
    for char in text:
        freq_map[char] = freq_map.get(char, 0) + 1
    
    heap = []
    for char, freq in freq_map.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(heap, node)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = HuffmanNode(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)
    
    return heap[0]

def build_huffman_codes(node, code, codes_map):
    if node is None:
        return
    
    if node.char is not None:
        codes_map[node.char] = code
        return
    
    build_huffman_codes(node.left, code + '0', codes_map)
    build_huffman_codes(node.right, code + '1', codes_map)

def huffman_encoding(text):
    if len(text) == 0:
        return '', None
    
    root = build_huffman_tree(text)
    codes_map = {}
    build_huffman_codes(root, '', codes_map)
    
    encoded_text = ''
    for char in text:
        encoded_text += codes_map[char]
    
    return encoded_text, root

def huffman_decoding(encoded_text, root):
    if len(encoded_text) == 0:
        return ''
    
    decoded_text = ''
    current = root
    for bit in encoded_text:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        
        if current.char is not None:
            decoded_text += current.char
            current = root
    
    return decoded_text


text = "Huffman coding is a data compression algorithm."
encoded_text, root = huffman_encoding(text)
print(encoded_text)
decoded_text = huffman_decoding(encoded_text, root)
print(decoded_text)


'''
Time Complexity: The time complexity of building the Huffman tree is O(n log n), 
where n is the number of unique characters in the input text. This is due to the sorting 
step when constructing the initial heap. The time complexity of encoding and decoding is O(m), 
where m is the length of the encoded/decoded text.

Space Complexity: The space complexity is O(n), where n is the number of unique characters in the input text. 
This is because we need to store the Huffman nodes and codes for each character.
'''
