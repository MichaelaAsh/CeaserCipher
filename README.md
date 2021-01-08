## Program 

A simple Ceaser Cipher to encrypt/decrypt a file.

## Run 
1. python3 CeaserCipher.py <inputfile.txt> shift encrypt
2. python3 CeaserCipher.py <inputfile.txt> shiftç
3. python3 CeaserCipher.py <inputfile.txt> decrypt 

replace <inputfile.txt> with the file you to apply the ceaser cipher to.
shift should be replaced with the shift you want applied
if the shift is not mentioned for decrypt then "brute force" will be applied. 

## RULE 
shift must be between 1 and 26 (inclusive)

## NOTE 
The encrypt/decrypt will be written to a file named output.txt