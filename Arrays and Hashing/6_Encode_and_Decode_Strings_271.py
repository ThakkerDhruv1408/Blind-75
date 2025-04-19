'''
271. Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]
'''

# Encoding 

strs = ["neet","code","love","you"]
encode = ""

for s in strs:
    encode += str(len(s)) + "#" + s
print(encode)


# Decoding 

Encoded = "4#neet4#code4#love3#you"
res = []
i = 0

while i < len(Encoded):
    j = i

    while Encoded[j] != "#":
        j += 1

    length = int(Encoded[i:j])
    res.append(Encoded[j+1:j+1+length])
    i = j + 1 + length

print(res)

