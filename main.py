import UC3MCare
from UC3MCare import VaccineRequest
import string


#GLOBAL VARIABLES
LETTERS = string.ascii_letters + string.punctuation + string.digits
SHIFT = 3


def Encode(word):
    """
    @encodes a word: string, char or integer. As a parameter
    @param: word
    @return: encoded
    @throw:
    @warning:
    """
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x_1 = (LETTERS.index(letter) + SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x_1]
    return encoded

def Decode(word):
    """
    @decodes a word: string, char or integer. As a parameter
    @param: word
    @return: decoded
    @throw:
    @warning:
    """
    encoded = ""
    for letters_1 in word:
        if letters_1 == ' ':
            encoded = encoded + ' '
        else:
            x_1 = (letters_1.index(letters_1) - SHIFT) % len(letters_1)
            encoded = encoded + letters_1[x_1]
    return encoded

def Main():
    mng = UC3MCare.VaccineManager()
    res = mng.ReadaccessrequestfromJSON("test.json")
    str_res = res.__str__()
    print(str_res)
    encode_res = Encode(str_res)
    print("Encoded Res "+ encode_res)
    decode_res = Decode(encode_res)
    print("Decoded Res: " + decode_res)


if __name__ == "__main__":
    Main()
