from egcd import egcd
import numpy as np

#list of characters to index to
allchars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

encrypted_text = []
#keyword to use in hill cipher
keyword = "household"

#plaintext to encrypt
plaintext = "Success is the ability to go from one failure to another with no loss of enthusiasm"
plaintext = plaintext.replace(" ", "")
plaintext = plaintext.lower()
print(plaintext)

#creating the matrix for the keyword
kw_matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

#turning the keyword into a list of characters to iterate through
kw_list = list(keyword)

#list of numbers that are indexed to the allchars list. each character of the keyword will have an index value to put into the keyword matrix
kw_indexlist = []

#for loop to add the indexes to the kw_indexlist. indexes each character in the keyword to the allchars list and populates a list of all index values
for x in range(9):
    letter = kw_list[x]
    index = allchars.index(letter)
    kw_indexlist.append(index)

#for loop that adds the indexes of each letter in keyword to the matrix. starts at top of 3x3 matrix and goes down. matrix for the keyword
#is populated after this loop
counter = 0
for x in range(3):
  for i in range(3):
       kw_matrix[i][x] = kw_indexlist[counter]
       counter = counter + 1
 
print("Here is the kw matrix")
print(kw_matrix)

#breaking the plaintext into a list of characters 
pt_list = list(plaintext)

#getting length to see if the plaintext is divisible by 3. if not, will append x's until divisible by 3
plaintext_length = len(plaintext)

remainder = plaintext_length % 3 

#appending x's to make plaintext divisible by 3 to create a 1x3 matrix.
if remainder == 1:
    pt_list.append('x')
    pt_list.append('x')
elif remainder == 2: 
    pt_list.append('x')

# determines the number of loops to go through when doing the matrix multiplication
loops = int(len(pt_list)/3)

# creating the matrix for the plaintext
pt_matrix = np.array([0, 0, 0])

# creating a list for the indexes of the plaintext characters
pt_indexlist = []

#getting all indexes of all characters in the plaintext
for x in range(len(pt_list)):
        letter = pt_list[x]
        index = allchars.index(letter)
        pt_indexlist.append(index)

#counter to iterate through the entire index list
counter = 0

#for loop that loops the amount of 1x3 matrices we've broken the plaintext into
for i in range(loops):

   #creates the 1x3 matrix
    for x in range(3):
        pt_matrix[x] = pt_indexlist[counter]
        counter = counter + 1

    #multiplies the keyword matrix by the 1x3 plaintext matrix
    mod_matrix = kw_matrix * pt_matrix

    #print(mod_matrix)

    #for loop to get the totals for each row of matrix. from there you mod 26 each row and get the remainder which can be mapped to a letter
    #finds the letter the remainder corresponds to and adds that to the encrypted text list. 
    for x in range(3):
        total = mod_matrix[x][0] + mod_matrix[x][1] + mod_matrix[x][2]
        indexnum = total % 26
        letter = allchars[indexnum]
        encrypted_text.append(letter)

print(encrypted_text)

##### From here on is decryption
# This section get the inverse of the keyword matrix.
det = int(np.round(np.linalg.det(kw_matrix)))
det_inv = egcd(det, 26)[1] % 26
matrix_modulus_inv = (
    det_inv * np.round(det * np.linalg.inv(kw_matrix)).astype(int) % 26)

#matrix_modulus_inv is the inverse of keyword matrix
print("Here is k inverse")
print(matrix_modulus_inv)

#create an indexlist for the encrypted text letter
et_indexlist = []

#populating the indexlist of encrypted letters
for x in range(len(encrypted_text)):
        letter = encrypted_text[x]
        index = allchars.index(letter)
        et_indexlist.append(index)

#creating the 1x3 matrix to multiply the k inverse with
encrypted_matrix = np.array([0, 0, 0])
#resetting counter
counter = 0
#created a list for the unencrypted text to be populated into
unencrypted_text = []
for i in range(loops):

   #creates the 1x3 matrix
    for x in range(3):
        encrypted_matrix[x] = et_indexlist[counter]
        counter = counter + 1
    #multiplying k inverse with the encrypted matrix to perform a modulus 26 against
    result = matrix_modulus_inv * encrypted_matrix

    #calculating the letter and adding it 
    for x in range(3):
        total = result[x][0] + result[x][1] + result[x][2]
        indexnum = total % 26
        letter = allchars[indexnum]
        unencrypted_text.append(letter)
       
print(unencrypted_text)
    