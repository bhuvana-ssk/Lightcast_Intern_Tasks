def isPalindrome(ip):
    try:
        word = str(ip)
        word = ''.join(word.split()).lower()
        start, end = 0, len(word) - 1
        while start < end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
        return True
    except Exception as e:
        print("Error: ",e)
        return False
    
print(isPalindrome("madam")) 
print(isPalindrome("Do geese see God"))    
print(isPalindrome(1221))                    
print(isPalindrome("hello"))                 
print(isPalindrome(""))                       
print(isPalindrome("a"))                    
print(isPalindrome("Not a palindrome"))      
print(isPalindrome(123456))                 
print(isPalindrome("Able was I ere I saw Elba")) 
print(isPalindrome("A man, a plan, a canal, Panama!"))
print(isPalindrome(None))