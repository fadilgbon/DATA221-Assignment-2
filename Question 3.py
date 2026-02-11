import string
from collections import defaultdict

with open("sample-file.txt", "r") as file: # open the file for reading
    original_lines = file.readlines() # read all lines into a list

def normalize_lines(current_line): # define function to normalize a line
    current_line = current_line.lower().strip() # lowercase and trim whitespace
    current_line = current_line.translate(str.maketrans('', '', string.punctuation)) # remove punctuation
    current_line = " ".join(current_line.split()) # collapse multiple spaces
    return current_line # return cleaned line

normalized_lines = [] # list to store normalized lines
line_number_mapping = [] # list to store original line numbers
for index, line in enumerate(original_lines): # iterate through original lines
    normalized_line = normalize_lines(line) # normalize current line
    if normalized_line: # check if line is not empty after cleaning
        normalized_lines.append(normalized_line) # store normalized line
        line_number_mapping.append(index + 1) # store original line number

line_groups_by_content = defaultdict(list) # dictionary mapping content to line numbers
for lineindex, norm_line in enumerate(normalized_lines): # iterate through normalized lines
    line_number = lineindex + 1 # compute normalized line index
    line_groups_by_content[norm_line].append(line_number) # group by identical content

near_duplicate_line_sets = [ # list of groups with duplicates
    line_number_list
    for line_number_list in line_groups_by_content.values()
    if len(line_number_list) > 1
]

print(f"Number of near-duplicate sets: {len(near_duplicate_line_sets)}\n") # print number of duplicate sets
for set_index, line_number_list in enumerate(near_duplicate_line_sets[:2], start=1): # show first two sets
    print(f"Set {set_index}:") # label the set
    for line_number in line_number_list: # iterate through line numbers in the set
        original_line = original_lines[line_number - 1].rstrip() # fetch original line text
        print(f"Line {line_number}: {original_line}") # print line number and content
print() # print blank line at end
