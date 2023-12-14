#Anthony Menghi (20212098) 
def removeSpace(chr :str) -> str : 
    chaineRenvoye = ""
    for k in chr : 
        if k != " " : 
            chaineRenvoye += k
    return  chaineRenvoye
 
def reverseChaine(chr :str) -> str : 
    counter = len(chr) -1
    chaineRenvoye = ""
    while counter >= 0 : 
        chaineRenvoye += chr[counter]
        counter = counter - 1
    return chaineRenvoye 
 
def isPallindrome(chaine : str ) -> True  : 
    chaine = chaine.lower()
    chaine = removeSpace(chaine)
    return chaine == reverseChaine(chaine)
 
print(isPallindrome("Test"))
print(isPallindrome("radar"))
print(isPallindrome("race car"))
print(isPallindrome("rotor"))
print(isPallindrome("toto"))
print(isPallindrome("RaDar"))
print(isPallindrome("A man a plan a canal Panama"))