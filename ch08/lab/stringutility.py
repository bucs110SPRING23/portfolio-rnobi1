class StringUtility:
    def __init__(self, string): 
        self.string = string
    def __str__(self):
        return self.string
    def vowels(self):
        count = sum([1 for char in self.string if char.lower() in "aeiou"])
        if count < 5:
            return str(count)
        else:
            return "many"
    def bothEnds(self):
        if len(self.string) <= 2:
            return ""
        else:
            return self.string[:2] + self.string[-2:]
    def fixStart(self):
        if len(self.string) <= 1:
            return self.string
        else:
            return self.string[0] + self.string[1:].replace(self.string[0], "*")
    def asciiSum(self):
        total = sum(ord(char) for char in self.string)
        return total
    def cipher(self):
        shift = len(self.string)
        ciphered_string = ""
        for char in self.string:
            if char.isalpha():
                if char.isupper():
                    shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                shifted_char = char
            ciphered_string += shifted_char
        return ciphered_string