class Isomorphic:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_map = {}
        seen_chars = set()
        for i in range(len(s)):
            if s[i] in char_map:
                if char_map[s[i]] != t[i]:
                    return False  # If the mapping is inconsistent, return False
            else:
                if t[i] in seen_chars:
                    return False  # If t[i] is already mapped, return False
                char_map[s[i]] = t[i]  # Map s[i] to t[i]
                seen_chars.add(t[i])   # Add t[i] to seen_chars

        return True

                
            
iso = Isomorphic()
iso.isIsomorphic('tra','ora')