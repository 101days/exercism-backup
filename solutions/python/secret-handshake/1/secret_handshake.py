def commands(binary_str):
    actions = ["wink", "double blink", "close your eyes", "jump"]
    ans = []

    for i in range(4):
        if binary_str[4 - i] == '1':
            ans.append(actions[i])

    if binary_str[0] == '1':
        ans.reverse()

    return ans