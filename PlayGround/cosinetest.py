def word2vec(word):
    from collections import Counter
    from math import sqrt
    
    # Count the characters in the word
    cw = Counter(word)
    
    # Precompute a set of the different characters
    sw = set(cw)
    
    # Precompute the "length" of the word vector
    lw = sum(c * c for c in cw.values())
    print(cw.values())
    print(lw)
    # Return a tuple
    return cw, sw, lw

def cosdis(v1, v2):
    # Which characters are common to the two words?
    common = v1[1].intersection(v2[1])
    
    # Compute cosine similarity
    return sum(v1[0][ch] * v2[0][ch] for ch in common) / (v1[2] * v2[2])

# Example usage
a = 'Hello World'
b = 'Peter'
c = 'optykop;lvhopijresokpghwji7'

va = word2vec(a)
vb = word2vec(b)
vc = word2vec(c)

# print(va)
# print(vb)
# print(vc)

print("Cosine similarity between 'a' and 'b':", cosdis(va, vb))
print("Cosine similarity between 'b' and 'c':", cosdis(vb, vc))
print("Cosine similarity between 'c' and 'a':", cosdis(vc, va))
