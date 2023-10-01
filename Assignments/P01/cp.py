def cp(source, destination):
    """
    Create copy of a file
    Command: cp source_file copied_file

    """
    try:
        with open(source, 'rb') as source_file:
            with open(destination, 'wb') as destination_file:
                while True:
                    data = source_file.read(4096)
                    if not data:
                        break
                    destination_file.write(data)
        
        return f"File '{source}' copied to '{destination}'"
    except FileNotFoundError:
        return f"Source file '{source}' not found."
    except PermissionError:
        return f"Permission denied to copy '{source}' to '{destination}'."
    except Exception as e:
        return f"An error occurred: {str(e)}"
