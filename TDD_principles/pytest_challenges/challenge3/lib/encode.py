def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char != ' ':
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1
    letter = sorted(counter.keys(), key=lambda item : counter[item])[-1]
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
