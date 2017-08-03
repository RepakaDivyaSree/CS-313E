#  File: TestCipher.py

#  Description: program to program cryptography

#  Student's Name: Eun Seo

#  Student's UT EID: es29857

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 03/30/2016

#  Date Last Modified: 03/30/2016

def substitution_encode ( strng ):
  plain = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u','v','w','x','y','z']
  cipher = ['q', 'a', 'z', 'w', 's', 'x', 'e','d','c','r','f','v','t','g','b','y','h','n','u','j','m','i','k','o','l','p']

  strng = strng.lower()

  encoded = ""
  # to find substution for 1st char convert char into indx for array cipher
  for i in range (len(strng)):
    # if index char is a string, convert
    if strng[i] in plain:
      idx = ord (strng[i]) - ord ('a')
      # substitute cipher with plain
      encoded += cipher[idx]
    else: # stays the same
      encoded += strng[i]
  return encoded


def substitution_decode ( strng ):
  plain = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u','v','w','x','y','z']
  cipher = ['q', 'a', 'z', 'w', 's', 'x', 'e','d','c','r','f','v','t','g','b','y','h','n','u','j','m','i','k','o','l','p']
  
  strng = strng.lower()

  decoded = ""
  # to find substution for 1st char convert char into indx for array cipher
  for i in range (len(strng)):
    # if index char is a string, convert
    if strng[i] in cipher:
      # get index of this char
      idx = cipher.index(strng[i])
      # substitute cipher with plain
      decoded += plain[idx]
    else: # stays the same
      decoded += strng[i]
  return decoded



def vigenere_encode ( strng, passwd ):
  plain = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u','v','w','x','y','z']
  
  strng = strng.lower()
  passwd = passwd.lower()

  # get length of strng
  len_st = len(strng)
  
  # create passwd repeated so that it's longer than strng
  new_passwd = len_st * passwd

  vig_encoded = "" #seals eals
  encoded = ""

  j = 0
  for i in range (len_st):
    # if char is a letter
    if strng[i] in plain:
      vig_encoded += new_passwd[j]
      j += 1
    else:
      vig_encoded += strng[i]

  
  for i in range (len_st):
    # if char is a letter
    if strng[i] in plain:
      idx = (plain.index(strng[i]) + plain.index(vig_encoded[i])) % 26
      encoded += plain[idx]
    else:
      encoded += strng[i]
  return encoded


def vigenere_decode ( strng, passwd ):
  plain = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u','v','w','x','y','z']

  strng = strng.lower()
  passwd = passwd.lower()

  # get length of strng
  len_st = len(strng)
  
  # create passwd repeated so that it's longer than strng
  new_passwd = len_st * passwd
  # new_passwd = sealsealsealseal

  vig_encoded = ""
  decoded = ""

  j = 0
  for i in range (len_st):
    # if char is a letter
    if strng[i] in plain:
      vig_encoded += new_passwd[j]
      j += 1
    else:
      vig_encoded += strng[i]
  
  #strng = zilwg aocdh
  #vig_encoded = seals ealse

  for i in range (len_st):
    # if char is a letter
    if strng[i] in plain:
      idx = (plain.index(strng[i]) - plain.index(vig_encoded[i])) % 26
      decoded += plain[idx]
    else:
      decoded += strng[i]
  return decoded


def main():
  # open file for reading
  in_file = open ("./cipher.txt", "r")

  # print header for substitution cipher
  print ("Substitution Cipher")
  print ()

  # read line to be encoded
  line = in_file.readline()
  line = line.strip()

  # encode using substitution cipher
  encoded_str = substitution_encode (line)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded
  line = in_file.readline()
  line = line.strip()

  # decode using substitution cipher
  decoded_str = substitution_decode (line)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (line, passwd)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (line, passwd)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # close file
  in_file.close()

main()