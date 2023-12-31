
# File:Project3.py
# Student: Caroline Snell
# UT EID: crs4775
# Course Name: CS303E
# 
# Date: November 26th
# Description of Program: This is a program I created to encrypt and decrypt a file based on a key. 



import random
import os.path

# A global constant defining the alphabet. 
LETTERS = "abcdefghijklmnopqrstuvwxyz"

# You are welcome to use the following two auxiliary functions, or 
# define your own.   They use some constructs we haven't covered. 

def isLegalKey( key ):
    # A key is legal if it has length 26 and contains all letters.
    # from LETTERS.
    key = key.lower()
    return ( len(key) == 26 and all( [ ch in key for ch in LETTERS ] ) )

def makeRandomKey():
    # A legal random key is a permutation of LETTERS.
    lst = list( LETTERS )    # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    return ''.join( lst )    # Assemble them back into a string
      
def encryptCharacter(ch, key): ##given a character and a key, what is the encrypted letter?    
    placeinalph=0
    lowerversion=ch.lower()
    dictionary= makeConversionDictionary(LETTERS, key)
    if (lowerversion in LETTERS)== True:
        if ch.isupper()==True:
            return dictionary[lowerversion].upper()
        else:
            return dictionary[lowerversion]
    else:
        return(ch)

def encryptText(text,key):
    key=key.lower()
    s=""
    for ch in text:
         s=s+encryptCharacter(ch, key)
    return s

def makeConversionDictionary(key1, key2):
    dictionary={}
    for i in range(0,26):
        letter = key1[i]
        letter2 = key2[i]
        dictionary[letter]=letter2
    return dictionary 

def decryptCharacter(ch, key):  ### given a character in an encrypted text, what is the character 
    location=0
    lowerversion=ch.lower()
    dictionary=makeConversionDictionary(key, LETTERS)
    if (lowerversion in LETTERS)==True:
        if ch.isupper()==True:
            return dictionary[lowerversion].upper()
        else:
            return dictionary[lowerversion]
    else:
        return(ch)
   

def decryptText(text,key): 
    key=key.lower()
    s=""
    for ch in text:
        s=s+decryptCharacter(ch, key)
    return s
    
##################################################################################################################################
class SubstitutionCipher:
    def __init__ (self, key = makeRandomKey() ):
        self.__key=key
        
    def getKey( self ):
        return self.__key 

    def setKey( self ):
        while True:
            user=input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ")
            if user== 'quit':
                    print()
                    break
            elif user=='random':
                new=makeRandomKey()
                self.__key= new
                print("    New cipher key: ", new)
                print()
                break
            else:
                if isLegalKey( user )==False:
                    print("    Illegal key entered. Try again!")
                elif isLegalKey(user)==True:
                    self.__key=user
                    print("    New cipher key: ", user)
                    print()
                    break 
                       
                

    def encryptFile( self, inFile, outFile ):
        outf=open(outFile, "w")
        inf=open(inFile,"r")
        converted=""
        for line in inf:
            converted=encryptText(line, self.__key)
            outf.write(converted)
        inf.close()
        outf.close()

    
    def decryptFile( self, inFile, outFile ):
        ##Decrypt the contents of inFile using the stored key
        ##and write the results into outFile.  Assume inFile exists.""
        outf=open(outFile, "w")
        inf=open(inFile,"r")
        deconverted=""
        for line in inf:
            deconverted=decryptText(line, self.__key)
            outf.write(deconverted)
        inf.close
        outf.close


        

##################################################################################################################################

def main():
    Joe= SubstitutionCipher()
    while True:
        user=input("Enter a command (getKey, changeKey, encryptFile, decryptFile, quit): ") 
        lowerversion=user.lower()
        if lowerversion=="quit":
            print("Thanks for visiting!")
            break
        elif lowerversion=='getkey':
            print("  Current cipher key: ", Joe.getKey())
            print()
        elif lowerversion=='changekey':
            Joe.setKey()
        elif lowerversion=='encryptfile':
            infile=input("  Enter a filename: ")
            if os.path.isfile(infile)==False:
                print("File does not exist")
                print()
            else:
                extension = "-Enc"
                if infile.endswith(".txt"):
                     outfile = infile[:-4] + extension + ".txt"
                else:
                    outfile = infile + extension
                Joe.encryptFile(infile, outfile)
                print("The encrypted output filename is " + outfile)
                print()
                
        elif lowerversion== 'decryptfile':
            incoming=input("  Enter a filename: ")
            if os.path.isfile(incoming)==False: 
                print("File does not exist")
            else:
                extensionn ='-Dec'
                if incoming.endswith(".txt"):
                    outfile= incoming[:-4] + extensionn + ".txt"
                else:
                    outfile = incoming + extensionn
                Joe.decryptFile(incoming, outfile)
                print("The decrypted output filename is " + outfile)
                print()
        else:
            print("  Command not recognized. Try again!")
            print()
            
            
                
        
        

              

main()
