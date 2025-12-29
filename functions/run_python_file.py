import os 
import subprocess

def run_python_file(working_directory, file_name, args=None):
    working_directory_abs = os.path.abspath(working_directory)

    file_path = os.path.normpath(os.path.join(working_directory_abs, file_name))
    if os.path.commonpath([working_directory_abs, file_path]) == working_directory_abs:
        if os.path.isfile(file_path):
            if file_path[-3:] == '.py':
                command = ['python', file_path]
                # add arguments if provided
                if args:
                    command.extend(args)
                try:
                    execution_result = subprocess.run(command, text=True, timeout=30, capture_output=True, cwd=working_directory_abs)
                    if type(execution_result) == subprocess.CompletedProcess:
                        responses = []
                        if execution_result.returncode != 0:
                            responses.append(f"Process exited with code {execution_result.returncode}")
                        if execution_result.stdout or execution_result.stderr:
                            if execution_result.stdout:
                                responses.append(f"STDOUT: {execution_result.stdout}")
                            if execution_result.stderr:
                                responses.append(f"STDERR: {execution_result.stderr}")
                        else:
                            responses.append("No output produced")
                        return "\n".join(responses)
                    else:
                        return f"Unexpected result type from running subprocess: {type(execution_result)}" 
                except Exception as e:
                    return f"Error: executing Python file: {e}"
            else:
                return f'Error: "{file_name}" is not a Python file'
        else:
            return f'Error: "{file_name}" does not exist or is not a regular file'
    else:
        return f'Error: Cannot execute "{file_name}" as it is outside the permitted working directory'