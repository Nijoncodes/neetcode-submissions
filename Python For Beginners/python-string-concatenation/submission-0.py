def concatenate(s1: str, s2: str) -> str:
    total = s1 + s2
    if len(total) > 10:
        return "Too long!"
    else:
        return total
    pass




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
