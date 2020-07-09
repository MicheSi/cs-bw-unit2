def twoStrings(s1, s2):
    for i in range(len(s1)):
        if s1[i] in s2:
            return 'YES'
    else:
        return 'NO'

# alternate solution
# create sets and compare the 2 sets
def two_strings(s1, s2):
    return "YES" if len(set(s1+s2)) < len(set(s1))+len(set(s2)) else "NO"