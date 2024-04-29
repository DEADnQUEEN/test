def recursion(palindrome: str) -> bool:
    if len(palindrome) == 0:
        return True
    
    if palindrome[0] != palindrome[-1]:
        ...