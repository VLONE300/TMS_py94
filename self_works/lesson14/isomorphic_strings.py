def isomorphic_strings(s, t):
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            continue
        if t[i] in d.values():
            return False
        else:
            d.setdefault(s[i], t[i])
    else:
        for i in range(len(s)):
            if t[i] == d[s[i]]:
                continue
            else:
                return False
        return True


print(isomorphic_strings('egg', 'add'))
