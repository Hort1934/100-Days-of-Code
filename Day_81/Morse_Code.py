DIC =  {'a': '.- ',
        'b': '-... ',
        'c': '-.-. ',
        'd': '-.. ',
        'e': '. ',
        'f': '..-. ',
        'g': '--. ',
        'h': '.... ',
        'i': '.. ',
        'j': '.--- ',
        'k': '-.- ',
        'l': '.-.. ',
        'm': '-- ',
        'n': '-. ',
        'o': '--- ',
        'p': '.--. ',
        'q': '--.- ',
        'r': '.-. ',
        's': '... ',
        't': '- ',
        'u': '..- ',
        'v': '...- ',
        'w': '.-- ',
        'x': '-..- ',
        'y': '-.-- ',
        'z': '--.. ',
        '1': '.---- ',
        '2': '..--- ',
        '3': '...-- ',
        '4': '....- ',
        '5': '..... ',
        '6': '-.... ',
        '7': '--... ',
        '8': '---.. ',
        '9': '----. ',
        '0': '-----',
        ' ': '   ',
        '.': '       ',
        '?': '..-..',
        }

class Converter:
    def MorseCode(self, input):
        global DIC
        morse_code = ""

        for char in input:
            morse_code += (DIC[char.lower()])

        print(f"Output: {morse_code}")


converter = Converter()

input = input("Text to Morse Code Converter\n\n input: ")
converter.MorseCode(input)