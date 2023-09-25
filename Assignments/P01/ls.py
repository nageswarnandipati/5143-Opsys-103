import os
import humanize

def ls(tokens):
    """
    List files and directories with specified options.
    Command: ls [Options]

    Options:
        -a	list all hidden files
        -l	long listing
        -h	human readable sizes
    """
    l = False
    a = False
    h = False

    result_str = ""
    # extract parameters
    if len(tokens) > 1:
        for param in tokens[1:]:
            if 'l' in param:
                l = True
            if 'a' in param:
                a = True
            if 'h' in param:
                h = True

    with os.scandir(os.getcwd()) as entries:
        for entry in entries:
            
            if not a and entry.name.startswith('.') and entry.name != '.':
                continue
            if l:
                file_info = entry.name
                if entry.is_file():
                    file_info += f" (File"
                    if h:
                        file_info += f", {humanize.naturalsize(entry.stat().st_size)} )"
                    else:
                        file_info += f", {entry.stat().st_size} bytes)"
                elif entry.is_dir():
                    file_info += " (Directory)"
                result_str += file_info + '\n'
            else:
                result_str += entry.name + '\n'
    return result_str[:-1]