#Name - Shinde Suvarna Sambhaji
#RollNo -59
#Title of Exp: Implementation of PlayFair Cipher 
import string
import itertools
def chunker(seq, size):
    it = iter(seq)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            return
        
        yield chunk
def prepare_input(capital):
   
 
    capital = "".join([c.upper() for c in capital if c in string.ascii_letters])
    clean = ""
 
    if len(capital) < 2:
        return capital
 
    for i in range(len(capital) - 1):
        clean += capital[i]
 
        if capital[i] == capital[i + 1]:
            clean += "X"
 
    clean += capital[-1]
 
    if len(clean) & 1:
        clean += "X"
   
    return clean

def generate_table(key):
 
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    table = []
 
    
    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)
 
    
    for char in alphabet:
        if char not in table:
            table.append(char)
 
    
    return table
 
 
def encode(plaintext, key):
    table = generate_table(key)
    plaintext = prepare_input(plaintext)
    ciphertext = ""
 
   
    for char1, char2 in chunker(plaintext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)
        
        if row1 == row2:
            ciphertext += table[row1 * 5 + (col1 + 1) % 5]
            ciphertext += table[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += table[((row1 + 1) % 5) * 5 + col1]
            ciphertext += table[((row2 + 1) % 5) * 5 + col2]
        else: 
            ciphertext += table[row1 * 5 + col2]
            ciphertext += table[row2 * 5 + col1]
 
    return ciphertext
def decode(ciphertext, key):
    table = generate_table(key)
    plaintext = ""
 
   
    for char1, char2 in chunker(ciphertext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)
 
        if row1 == row2:
            plaintext += table[row1 * 5 + (col1 - 1) % 5]
            plaintext += table[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += table[((row1 - 1) % 5) * 5 + col1]
            plaintext += table[((row2 - 1) % 5) * 5 + col2]
        else: 
            plaintext += table[row1 * 5 + col2]
            plaintext += table[row2 * 5 + col1]
 
    return plaintext
 
if __name__=="__main__":
    plaintext=input("Enter the text: ")
    key=input("Enter the Key: ")
    print("original text=",plaintext)
    cypher=encode(plaintext,key)
    print("cypher text="," ".join(cypher[i:i+2] for i in range(0, len(cypher), 2)))
    original=decode(cypher,key)
        
    print("decoded text="," ".join(original[i:i+2] for i in range(0,len(original),2)))



# input-
# Enter the text: Information and Cyber Security
# Enter the Key: sinhgad
# original text= Information and Cyber Security
# cypher text= NH KF TL CP GK SB IB MH CA PN AE PT HQ ZY
# decoded text= IN FO RM AT IO NA ND CY BE RS EC UR IT YX