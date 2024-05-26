# INSTALL DOCKER Script

This script automates the process of updating the system, installing Docker, and setting up a virtual environment for Python development. It is designed to run on Linux systems, specifically Ubuntu.

## Features

- Creates and activates a Python virtual environment
- Installs necessary Python packages
- Updates the system packages
- Installs Docker and Docker Compose

## Prerequisites

- Python 3.x
- `venv` module for creating virtual environments
- Administrative (sudo) privileges

## Usage

1. **Clone the repository or copy the script to your local machine.**

2. **Make the script executable (if necessary):**
    ```sh
    chmod +x script_name.py
    ```

3. **Run the script:**
    ```sh
    python script_name.py
    ```

## Script Breakdown

### `create_and_activate_venv(venv_path)`

- Creates a virtual environment at the specified path if it doesn't exist.
- Activates the virtual environment.

### `install_dependencies(pip_executable)`

- Installs necessary Python packages using `pip`.

### `run_command(command)`

- Runs a shell command and returns the output.
- Raises an exception if the command fails.

### `update_system()`

- Updates the package lists for upgrades and new package installations.
- Lists the upgradable packages.
- Upgrades all the installed packages to the latest version.

### `install_docker()`

- Installs the necessary packages for Docker.
- Adds Docker's official GPG key.
- Sets up the Docker stable repository.
- Updates the package lists.
- Installs Docker and Docker Compose.
- Adds the current user to the Docker group.

### `main()`

- Runs the system update and Docker installation in sequence.

## Notes

- Ensure you have Python 3.x installed on your system.
- The script uses the `tqdm` package to display progress bars. If `tqdm` is not installed, the script will automatically install it.
- The script requires administrative privileges to update the system and install Docker. You may be prompted to enter your password during execution.

## Example

To run the script, simply execute:

```sh
python script_name.py
