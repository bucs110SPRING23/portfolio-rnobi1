
class StringUtility:
    def __init__(self, string):
        self.string = string
    def __str__(self):
        return self.string
    def vowels(self):
        return str(sum([1 for char in self.string if char.lower() in "aeiou"])) if sum([1 for char in self.string if char.lower() in "aeiou"]) < 5 else "many"
    def bothEnds(self):
        return self.string[:2] + self.string[-2:] if len(self.string) > 2 else ""   
    def fixStart(self):
        return self.string[0] + self.string[1:].replace(self.string[0], "*") if len(self.string) > 1 else self.string
    
    def asciiSum(self):
        return sum([ord(char) for char in self.string])
    
    def cipher(self):
        return "".join([chr((ord(char) - 65 + len(self.string)) % 26 + 65) if char.isupper() else (chr((ord(char) - 97 + len(self.string)) % 26 + 97) if char.islower() else char) for char in self.string])
