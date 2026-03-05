def is_paired(input_string):
    stack = []
    
    for char in input_string:
        if char in '([{':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False
        elif char == ']':
            if not stack or stack.pop() != '[':
                return False
        elif char == '}':
            if not stack or stack.pop() != '{':
                return False
    
    return len(stack) == 0
