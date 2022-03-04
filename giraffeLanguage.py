def translate(phrase):
    translated=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translated=translated + "G"
            else:
                translated=translated + "g"
        else :
            translated=translated + letter
    return translated

print(translate(input("Translate a phrase: ")))