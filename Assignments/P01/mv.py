import os

def mv(source, destination):
    """
    move a file from one locatio to another
    Command: mv source_file moved_file
    """
    try:
        os.rename(source, destination)
        return f"Moved '{source}' to '{destination}'"
    except FileNotFoundError:
        return f"Source file/directory '{source}' not found."
    except PermissionError:
        return f"Permission denied to move '{source}' to '{destination}'."
    except Exception as e:
        return f"An error occurred: {str(e)}"