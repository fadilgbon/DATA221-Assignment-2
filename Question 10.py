def find_lines_containing(filename, keyword): # define a function to search for a keyword in a file
    matches = [] # list to store matching (line_number, line_text)
    keyword_lower = keyword.lower() # convert keyword to lowercase for case-insensitive search

    with open(filename, "r") as file: # open the file for reading
        for idx, line in enumerate(file, start=1): # loop through file with line numbers
            if keyword_lower in line.lower(): # check if keyword appears in this line
                matches.append((idx, line.rstrip())) # save line number and trimmed text

    return matches # return all matches


filename = "sample-file.txt" # file to search
keyword = "lorem" # keyword to look for

matching_lines = find_lines_containing(filename, keyword) # run the search

print(f"Number of matching lines: {len(matching_lines)}\n") # print how many matches were found

for line_info in matching_lines[:3]: # loop through the first three matches
    line_number, line_text = line_info # unpack the tuple
    print(f"Line {line_number}: {line_text}") # print the line number and text
