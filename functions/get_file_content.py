import os
def get_file_content(working_directory, file_name):
    working_directory_abs = os.path.abspath(working_directory)

    file_path = os.path.normpath(os.path.join(working_directory_abs, file_name))
    if os.path.commonpath([working_directory_abs, file_path]) == working_directory_abs:
        if os.path.isfile(file_path):
            MAX_CHARS = 10000
            file_content_string = ""
            try:
                with open(file_path, "r") as f:
                    file_content_string = f.read(MAX_CHARS)
                    # check if we got the entire file
                    if f.read(1):
                        file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return file_content_string
            except Exception as e:
                return f"Error: {e}"
        else:
            return f'Error: File not found or is not a regular file: "{file_path}"'
    else:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'