# Watchtower

This `docker-compose.yaml` file sets up Watchtower, a tool to automatically update running Docker containers.

## Prerequisites

- Docker and Docker Compose installed

## Usage

1. **Create and navigate to the directory:**
    ```sh
    mkdir -p ~/watchtower-docker
    cd ~/watchtower-docker
    ```

2. **Save the `docker-compose.yaml` file in this directory.**

3. **Deploy the container:**
    ```sh
    docker-compose up -d
    ```

## Notes

- The container is configured to restart always.
- The Docker socket is mounted to allow Watchtower to interact with other containers.
- The update interval is set to 30 seconds by default. Adjust as needed.
