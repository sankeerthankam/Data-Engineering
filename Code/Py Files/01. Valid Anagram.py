def isAnagram(s, t):
    # Approach 1 - Use Counter from Collections
    from collections import Counter
    if Counter(s) == Counter(t):
        return True
    return False
    
    # Approach 2 - Implement Counter and Compare the Counter objects for the two strings        
    def Counter(st):
        d = {}
        for i in st:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return d

    if len(s) == len(t):
        s_ = Counter(s)
        t_ = Counter(t)
        if s_ == t_:
            return True
        else:
            return False
    else:
        False
