# Glances

This `docker-compose.yaml` file sets up Glances, a cross-platform monitoring tool.

## Prerequisites

- Docker and Docker Compose installed

## Usage

1. **Create and navigate to the directory:**
    ```sh
    mkdir -p ~/glances-docker
    cd ~/glances-docker
    ```

2. **Save the `docker-compose.yaml` file in this directory.**

3. **Deploy the container:**
    ```sh
    docker-compose up -d
    ```

4. **Access Glances:**
    - Open your web browser and navigate to `http://localhost:61208`.

## Notes

- The container is configured to restart always and uses the host's PID namespace.
- The Docker socket is mounted read-only.
