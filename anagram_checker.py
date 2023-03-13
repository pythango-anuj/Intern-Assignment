def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    d1 = {}
    d2 = {}
    for i in range(len(s1)):
        if s1[i] in d1:
            d1[s1[i]] += 1
        else:
            d1[s1[i]] = 1
        if s2[i] in d2:
            d2[s2[i]] += 1
        else:
            d2[s2[i]] = 1
    for item in d1:
        if item not in d2:
            return False
        if d1[item] != d2[item]:
            return False
            break
    return True


s1 = input("Enter String 1:")
s2 = input("Enter String 2:")
print(is_anagram(s1, s2))



