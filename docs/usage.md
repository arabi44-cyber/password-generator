# Usage

## Running the Password Generator

To generate a password, use the following command in your terminal:

```bash
python src/passwdgen.py

```

## Command-Line Options

You can customize the password generation process using various command-line options:

    -l, --length

    Description: Specify the length of the generated password.
    Usage: -l <length>
    Example: -l 12 generates a password with 12 characters.
    -d, --digits

    Description: Include digits in the password.
    Usage: -d
    Example: -d ensures that digits are included in the generated password.
    -a, --alpha

    Description: Include alphabetic characters in the password.
    Usage: -a
    Example: -a ensures that alphabetic characters (both uppercase and lowercase) are included.
    -s, --special

    Description: Include special characters in the password.
    Usage: -s
    Example: -s includes characters like @, #, $, etc.

### Examples

1. Generate a 12-character password with digits and special characters:

```bash
python src/passwdgen.py -l 12 -d -s
```

2. Generate a 16-character password with only alphabetic characters:

```bash
python src/passwdgen.py -l 16 -a
```

3. Generate an 8-character password with digits, alphabetic characters, and special characters:

```bash
python src/passwdgen.py -l 8 -d -a -s
```

### Output

The generated password will be displayed in the terminal. Each run of the script will produce a new random password according to the specified options.

# Additional Notes

-> Default Settings: If no options are provided, the script will generate a default password of 8 characters including letters and digits.

-> Error Handling: If invalid options or arguments are provided, the script will display an error message and exit.
