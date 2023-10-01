import re

def grep(keyword, files, return_filename=False, content=None):
    """
    Search a file(s) files for keywords and print lines where pattern is found
    Command: grep [Options] keyword file
    
    Options:
    -l :  only return file names where the word or pattern is found

    """
    result_str = ""
    try:
        matching_files = []
        if content:
            for line_number, line in enumerate(content, start=1):
                if re.search(keyword, line):
                    if return_filename:
                        result_str += file_name + '\n'
                    else:
                        result_str += f"{file_name}:{line_number}: {line}"
        else:
            for file_name in files:
                with open(file_name, 'r') as file:
                    lines = file.readlines()
                    for line_number, line in enumerate(lines, start=1):
                        if re.search(keyword, line):
                            if return_filename:
                                result_str += file_name + '\n'
                            else:
                                result_str += f"{file_name}:{line_number}: {line}"
        
        return result_str[:-1]
    except FileNotFoundError as e:
        print(f"File not found: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


    