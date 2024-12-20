from pathlib import Path
from collections import defaultdict


def read_patterns(patterns_filepath: Path):
    with patterns_filepath.open("r") as f:
         patterns = [item.strip() for item in f.readline().split(",")]
    return patterns


def read_designs(designs_filepath: Path):
    with designs_filepath.open("r") as f:
        designs = [item.strip() for item in f.readlines()]
    return designs


class Designer:
    def __init__(self, patterns):
        self.__patterns = patterns
        self.__patterns_dict = dict()
        # self.__clean_patterns()
        
    def __clean_patterns(self):
        new_patterns = []
        for pattern in self.__patterns:
            candidates = self.solve(pattern)
            self.__patterns_dict[pattern] = candidates
            
            if len(candidates) == 1:
                new_patterns.append(pattern)
                
        self.__patterns = new_patterns
        print(self.__patterns_dict)
             
       
    def solve_part1(self, design: str) -> list[str]:
        candidates = [[""]]
        
        for pos in range(len(design)):
            
            text_to_match = design[:pos + 1]
            new_candidates = []
            print(text_to_match)
            
            for candidate in candidates:
                candidate_len = len("".join(candidate))
                candidate_text = "".join(candidate)
                need_to_add_pattern = candidate_len < pos + 1
                
                if need_to_add_pattern:
                    for pattern in self.__patterns:
                        text = candidate_text + pattern
                        if text[:pos + 1] == text_to_match and len(text) <= len(design):
                            new_candidates.append(candidate + [pattern])
                            # print("Add", pattern)
                else:
                    if candidate_text[:pos + 1] == text_to_match:
                        new_candidates.append(candidate)
                        # print(candidate_text, "continue to be OK")
            candidates = [*new_candidates]
        
        # Clean
        for candidate in candidates:
            candidate.pop(0)
            
        for candidate in candidates:
            print(candidate)
            
        # print(candidates)
        return candidates
        
    def solve(self, design: str) -> list[str]:
        # Ajout d'un cache et traitement de la string complète pour gagner en performance
        candidates = {"": 1}
        design_len = len(design)
        
        for pos in range(design_len):
            text_to_match = design[:pos + 1]
            print(text_to_match)
            new_candidates = defaultdict(lambda: 0)
            
            for candidate, value in candidates.items():
                need_to_add_pattern = len(candidate) < pos + 1
                
                if need_to_add_pattern:
                    for pattern in self.__patterns:
                        text = candidate + pattern
                        if text[:pos + 1] == text_to_match and len(text) <= design_len:
                            new_candidates[text] += value
                            
                else:
                    if candidate[:pos + 1] == text_to_match:
                        new_candidates[candidate] += value

            candidates = new_candidates
        
        return candidates    
               
                    
if __name__ == "__main__":
    patterns_filepath = Path(__file__).parent / "inputs" / "patterns.txt"
    designs_filepath = Path(__file__).parent / "inputs" / "designs.txt"
    
    patterns = read_patterns(patterns_filepath)
    designs = read_designs(designs_filepath)
    
    designer = Designer(patterns)
    
    counter = 0
    counter_2 = 0
    nb_designs = len(designs)
    for pos, design in enumerate(designs):
        print(f"Solving {pos + 1}/{nb_designs}: {design}")
        result = designer.solve(design)
        print(dict(result))
        for key, value in result.items():
            counter_2 += value
        if result != []:
            counter += 1
         
            
            
    print("Part I", counter)
    print("Part II", counter_2)