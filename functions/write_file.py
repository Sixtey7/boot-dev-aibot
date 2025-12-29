import os

def write_file(working_directory, file_name, content):
    working_directory_abs = os.path.abspath(working_directory)

    file_path = os.path.normpath(os.path.join(working_directory_abs, file_name))
    if os.path.commonpath([working_directory_abs, file_path]) == working_directory_abs:
        if os.path.isdir(file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        # create all of the directories required to get to file path
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        try:
            with open(file_path, "w") as f:
                f.write(content)
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f"Error: {e}"
    else:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'