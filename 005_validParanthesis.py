def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map:  # If it's a closing bracket
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                print(f"Mismatch: expected {bracket_map[char]}, found {top_element}")
                return False
        else:
            stack.append(char)
            print(f"Pushed: {char} -> Stack: {stack}")

    print(f"Final Stack: {stack}")
    return  stack


print(isValid("()"))