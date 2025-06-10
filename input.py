def process_file():
    """Reads a file, modifies its content, and writes to a new file with error handling."""

    try:
        input_filename = input("Enter the input filename: ")
        with open(input_filename, "r") as infile:
            content = infile.readlines()  # Read lines to preserve line breaks

        # Modify the content (example: add line numbers)
        modified_content = [f"{i+1}: {line}" for i, line in enumerate(content)]

        output_filename = "output.txt"  # Hardcoded output filename for simplicity
        with open(output_filename, "w") as outfile:
            outfile.writelines(modified_content)  # Write lines back to the file

        print(f"Successfully processed '{input_filename}' and wrote to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    process_file()
