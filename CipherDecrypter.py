#Cipher-Decrypter
# Author: Subhash
# Title: Offensive Penetration Testing Student
# Organisation: HackerAssociate
#Usage : On plain text : put plain text 
# On encrypted text: put cipher text
# Note: Try exact same text and try after avoiding/deleting the special characters.

plaintext = "Plain-text-message"
ciphertext = "encrypted-text"
key = ""
for i in range(len(plaintext)):
 num_key = ((ord(ciphertext[i]) - ord(plaintext[i])) % 26) + 97
 char_key = chr(num_key)
 key = key + char_key
print key
