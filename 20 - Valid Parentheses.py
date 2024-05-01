def parenthese(s):
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            open_char = stack.pop()
            if (open_char == "(" and char != ")") or \
               (open_char == "[" and char != "]") or \
               (open_char == "{" and char != "}"):
                return False
    return len(stack) == 0

if __name__ == "__main__":
    s = "()[]{}[([])]"
    print(parenthese(s))  # Salida: True

    s = "([)]"
    print(parenthese(s))  # Salida: False
