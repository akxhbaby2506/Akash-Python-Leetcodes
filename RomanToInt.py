def roman_to_int(s: str) -> int:
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    prev = 0
    for i in range(len(s)-1, -1, -1):
        curr = roman_map[s[i]]
        if prev > curr:
            num -= curr
        else:
            num += curr
        prev = curr
    print(num)
roman_to_int("IV")
roman_to_int("VI")