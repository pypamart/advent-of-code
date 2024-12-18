from pathlib import Path
import re

INPUT_FILE = Path(__file__).parent / "inputs" / "calibrations.txt"

CORRESPONDANCE_TABLE = {
    "0": "0", 
    "1": "1", 
    "2": "2", 
    "3": "3", 
    "4": "4", 
    "5": "5", 
    "6": "6", 
    "7": "7", 
    "8": "8", 
    "9": "9", 
    # "zero": "0", not asked to convert zero
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine":  "9"
}

def read_input(filepath: Path=INPUT_FILE.absolute()) -> str:
    with open(filepath) as f:
        lines = f.readlines()
    return lines


def retrieve_calibration_in_text(text: str) -> int:
    pattern = re.compile(r"\d")
    digits = pattern.findall(text)
    if digits:
        return int(digits[0] + digits[-1])
    return 0


def retrieve_calibration_in_text_with_text_convertion(text: str) -> int:
    # pattern = re.compile(r"\d|one|two|three|four|five|six|seven|eight|nine")
    # Modification de l'expression régulière pour prendre en compte les chiffres qui ont une lettre en commun
    # Utilisation de la fonctionnalité lookahead
    # https://docs.python.org/3/howto/regex.html#lookahead-assertions
    pattern = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")
    digits = pattern.findall(text)
    digits = [CORRESPONDANCE_TABLE[digit] for digit in digits]
    if digits:
        return int(digits[0] + digits[-1])
    return 0
    
    
def replace_text_to_number(text: str) -> str:
    for word, number in CORRESPONDANCE_TABLE:
        text = text.replace(word, number)
    return text


def solve_part_1(filepath: Path=INPUT_FILE.absolute()) -> int:
    lines = read_input(filepath)
    calibration = sum([retrieve_calibration_in_text(line) for line in lines])
    print("Part I solution: ", calibration)
    return calibration


def solve_part_2(filepath: Path=INPUT_FILE.absolute()) -> int:
    lines = read_input(filepath)
    calibration_values = [retrieve_calibration_in_text_with_text_convertion(line) for line in lines]
    with open("output_new.txt", "w") as file:
        file.write("\n".join([str(value) for value in calibration_values]))
    calibration = sum([retrieve_calibration_in_text_with_text_convertion(line) for line in lines])
    print("Part II solution: ", calibration)
    return calibration


if __name__ == "__main__":
    pass