def is_valid(s: str) -> bool:
    stack=[]
    pairs={')':'(','}':'{',']':'['}
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)

        elif c == '}' or c == ')' or c == ']':
            if stack==[]:
                return False
            else:
                last=stack.pop()
                if last==pairs[c]:
                    continue
                else:
                    return False
    
    if stack==[]:
        return True
    else:
        return False
print(is_valid("()" ))
print(is_valid("()[]{}"))
print(is_valid("(]" ))
print(is_valid("([)]" ))
print(is_valid("{[]}" ))
print(is_valid("(((" ))
print(is_valid(")("))