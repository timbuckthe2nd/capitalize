def solve(s):
    result = s[0].capitalize()
    for x in range(1, len(s)):
        if s[x-1] == " ":
            letter = s[x].capitalize()
        else:
            letter = s[x]
        result += letter
    return result
