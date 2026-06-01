from codecs import utf_8_decode
import regex as re # regex handles unicode categories better than built-in re
data_path = "data/frineds_script.txt"

def _bytes_to_unicode() -> dict[int, str]:
    """Build a dictionary of unicode characters, unsafe change to something else.
    Keys - numbers (0-255), values - characters
    """
    # this returns ints for printable unicode chars:
    printable = list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    printable_copy = printable[:]
    
    # Fill in the gaps if any
    n = 0
    for number in range(256):
        if number not in printable:
            printable.append(number)
            printable_copy.append(256 + n)
            n += 1
            
    # convert number to character
    printable_copy = [chr(number) for number in printable_copy]
    return dict(zip(printable, printable_copy))

def _pre_tokenize(text: str) -> list[str]:
    """Using GPT-2 regex pattern chunk text corpus into words, punctunations and contractions"""
    gpt2_pattern = r"""'s|'t|'re|'ve|'m|'ll|'d| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
    return re.findall(gpt2_pattern, text)

if __name__ == "__main__":
    byte_encoder_dict = _bytes_to_unicode()
    # load text:
    with open(data_path, 'r', encoding = 'utf_8') as f:
        text = f.read()
    chunks = _pre_tokenize(text)
    print(print(chunks[:100]))