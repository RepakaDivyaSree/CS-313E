#  File: BST_Cipher.py

#  Description: Create encrypt/decrypt BST

#  Student Name: Adam Roach

#  Student UT EID: abr875

#  Partner Name: Eun Seo

#  Partner UT EID: es29857

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 28 April 2016

#  Date Last Modified: 30 April 2016

class Node (object):
    def __init__ (self, data = None):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = None

        for ch in encrypt_str:
            # only encrypt letters
            if (ord(ch) == 32):
                self.insert(ch.lower())
            elif ((ord(ch) >= 97 and ord(ch) <= 122)):
            #if (ch.isalpha() == True):
                self.insert(ch.lower())
            else:
                break

        return

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        newNode = Node(ch)

        if (self.root == None):
            self.root = newNode
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (ch == current.data):
                    break
                elif (ch < current.data):
                    current = current.lchild
                else: #elif (ch > current.data):
                    current = current.rchild

            if (ch < parent.data):
                parent.lchild = newNode
            elif (ch > parent.data):
                parent.rchild = newNode



    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        if (self.root.data == ch):
            return '*'

        current = self.root
        st = ''
        while (current != None):
            if (ch == current.data):
                return st
            elif (ch < current.data):
                st += '<'
                current = current.lchild
            elif (ch > current.data):
                st += '>'
                current = current.rchild
        return st

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        # change to all lowercase
        st = st.lower()

        secret_msg = ''

        for ch in st:
            if ((ord(ch) == 32) or ((ord(ch) >= 97) and (ord(ch) <= 122))):
                path = self.search(ch)
                # after end of each path, return !
                #secret_msg += str(path) + '!'
                if path:
                    secret_msg += path + '!'
        # get rid of the last '!'
        return secret_msg[:-1]

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding 
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, path):
        
        current = self.root
        for token in path:
            if (current != None):
                if (token == '*'):
                    return current.data
                elif (token == '<'):
                    current = current.lchild
                elif (token == '>'):
                    current = current.rchild
            else:
                return ''

        return current.data

    #put encrypt func here


    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt (self, st):
        msg = ''
        st = st.lower()
        paths = st.split('!')
        for path in paths:
            msg += self.traverse(path)
        
        return msg

def main():
    encrypt_key = 'the quick brown fox jumps over the lazy dog'
    #encrypt_key = 'meet me'
    tree = Tree(encrypt_key)

    encrypt_st = input('Enter string to be encrypted: ')
    print('Encrypted string: ', tree.encrypt(encrypt_st))

    print()

    decrypt_st = input('Enter string to be decrypted: ')
    print('Decrypted string: ', tree.decrypt(decrypt_st))  

main()