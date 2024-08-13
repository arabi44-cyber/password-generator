# Installation Guide

## Prerequisites

- Python 3.x
- Git

### Steps

1. **Clone the Repository**:

```bash
    git clone https://github.com/yourusername/password-generator.git
    cd password-generator
```

2. **Verify Installation**:

   Run the script to ensure it’s installed correctly:

```bash
    python src/passwdgen.py
```

### Troubleshooting

-> Issue: If you encounter any issues, check the error messages for hints.

-> Solution: Refer to the FAQ or open an issue on GitHub if you need further assistance.

## Usage

### Running the Password Generator

To generate a password, run the script from the command line:

```bash

python src/passwdgen.py
```

### Command-Line Options

    -l, --length: Specify the length of the password (e.g., -l 12).
    -d, --digits: Include digits in the password (e.g., -d).
    -a, --alpha: Include alphabetic characters (e.g., -a).
    -s, --special: Include special characters (e.g., -s).

#### Example

Generate a 12-character password with digits and special characters:

```bash
    python src/passwdgen.py -l 12 -d -s
```

#### Output

The generated password will be displayed in the terminal.

### Additional Information

For more detailed usage information, refer to the FAQ or open an issue on GitHub.
