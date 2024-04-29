def recursion(palindrome: str) -> bool:
    if len(palindrome) == 0:
        return True
    
    if palindrome[0] != palindrome[-1]:
        return False
    
    return recursion(palindrome[1:-1])

if __name__ == '__main__':
    recursion(input())