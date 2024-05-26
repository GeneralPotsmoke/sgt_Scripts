import subprocess
import sys
import os
import venv
from pathlib import Path
import platform

def create_and_activate_venv(venv_path):
    """
    Create a virtual environment if it doesn't exist and activate it.
    """
    if not venv_path.exists():
        print(f"Creating virtual environment at {venv_path}...")
        venv.create(venv_path, with_pip=True)

    print(f"Activating virtual environment at {venv_path}...")
    if platform.system() == "Windows":
        activate_script = venv_path / "Scripts" / "activate"
    else:
        activate_script = venv_path / "bin" / "activate"

    return str(activate_script)

def install_dependencies(pip_executable):
    """
    Install necessary Python packages using pip.
    """
    print("Installing necessary Python packages...")
    subprocess.check_call([pip_executable, "install", "tqdm"])
    print("Dependencies installed.")

def run_command(command):
    """
    Run a shell command and return the output.
    Raise an exception if the command fails.
    """
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}\n{result.stderr}")
    return result.stdout

def update_system():
    """
    Update the system by running the following steps:
    1. Update the package lists for upgrades and new package installations.
    2. List the upgradable packages.
    3. Upgrade all the installed packages to the latest version.
    """
    from tqdm import tqdm
    print("Updating the system...")
    steps = [
        "sudo apt update",
        "sudo apt list --upgradable",
        "sudo apt upgrade -y"
    ]
    for step in tqdm(steps, desc="System Update", unit="step"):
        run_command(step)
    print("System updated.")

def install_docker():
    """
    Install Docker and Docker Compose by performing the following steps:
    1. Install the necessary packages for Docker.
    2. Add Docker's official GPG key.
    3. Set up the Docker stable repository.
    4. Update the package lists.
    5. Install Docker and Docker Compose.
    6. Add the current user to the Docker group.
    """
    from tqdm import tqdm
    print("Installing Docker and Docker Compose...")
    steps = [
        "sudo apt install apt-transport-https ca-certificates curl software-properties-common -y",
        "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -",
        'sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"',
        "sudo apt update",
        "sudo apt install docker-ce docker-compose -y",
        f"sudo usermod -aG docker {subprocess.getoutput('whoami')}"
    ]
    for step in tqdm(steps, desc="Docker Installation", unit="step"):
        run_command(step)
    print("Docker and Docker Compose installed.")

def main():
    """
    Main function to run the system update and Docker installation in sequence.
    """
    update_system()
    install_docker()
    print("Setup completed successfully.")

if __name__ == "__main__":
    venv_path = Path("./venv")
    activate_script = create_and_activate_venv(venv_path)

    python_executable = str(venv_path / "bin" / "python") if platform.system() != "Windows" else str(venv_path / "Scripts" / "python")
    pip_executable = str(venv_path / "bin" / "pip") if platform.system() != "Windows" else str(venv_path / "Scripts" / "pip")

    try:
        from tqdm import tqdm
    except ImportError:
        install_dependencies(pip_executable)
        # Re-execute the script using the virtual environment's Python interpreter
        subprocess.check_call([python_executable, __file__])
        sys.exit()

    main()
