
# Duplicate File Remover

This project contains a script to identify and remove duplicate files within a specified directory. The script can be used in either Python (`rm_duplicates.py`) or PowerShell (`rm_duplicates.ps1`).

## Features

- Scans a specified directory for duplicate files.
- Uses MD5, SHA1, or SHA256 hash algorithms for file comparison.
- Option to operate in quiet mode to suppress output.
- Replaces duplicate files with symbolic links to the original files.

## Usage (Python)

### Prerequisites

- Python 3.x installed

### Running the Script

1. Clone the repository or download `rm_duplicates.py`.
2. Open a terminal and navigate to the directory containing `rm_duplicates.py`.
3. Run the script:
    ```sh
    python rm_duplicates.py
    ```

### Script Menu Options

1. **Select Directory**: Prompts for a directory to search for duplicate files.
2. **Quiet Mode**: Toggles quiet mode to suppress output.
3. **Change Hash Algorithm**: Allows changing the hash algorithm (MD5, SHA1, SHA256).
4. **Exit**: Exits the script.

## Usage (PowerShell)

### Prerequisites

- Windows PowerShell or PowerShell Core installed

### Running the Script

1. Clone the repository or download `rm_duplicates.ps1`.
2. Open a PowerShell terminal and navigate to the directory containing `rm_duplicates.ps1`.
3. Run the script:
    ```sh
    .m_duplicates.ps1
    ```

### Script Menu Options

1. **Select Directory**: Prompts for a directory to search for duplicate files.
2. **Quiet Mode**: Toggles quiet mode to suppress output.
3. **Change Hash Algorithm**: Allows changing the hash algorithm (MD5, SHA1, SHA256).
4. **Exit**: Exits the script.

## Example

### Python

```sh
python rm_duplicates.py
```

### PowerShell

```sh
.m_duplicates.ps1
```

## License

This project is licensed under the MIT License.
