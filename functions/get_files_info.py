import os
def get_files_info(working_directory, directory = "."):
    working_directory_absolute = os.path.abspath(working_directory)

    target_dir = os.path.normpath(os.path.join(working_directory_absolute, directory))

    if os.path.commonpath([working_directory_absolute, target_dir]) == working_directory_absolute:
        if os.path.isdir(target_dir):
            try:
                file_strings = []
                files = os.listdir(target_dir)
                for file in files:
                    full_path = os.path.join(target_dir, file)
                    file_string = "\t- " + file + ": file_size="
                    file_string += str(os.path.getsize(full_path)) + " bytes, is_dir="
                    file_string += str(os.path.isdir(full_path))
                    file_strings.append(file_string)
                return "\n".join(file_strings)
            except Exception as e:
                return f"\tError: {e}"
        else:
            return f'\tError: "{target_dir}" is not a directory'
    else:
        return f'\tError: Cannot list "{directory}" as it is outside the permitted working directory'