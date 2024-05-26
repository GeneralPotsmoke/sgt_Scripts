# Gitea Docker Compose Setup

This repository contains a Docker Compose configuration to set up a Gitea server, a lightweight Git service.

## Features

- Runs Gitea in a Docker container
- Configures persistent storage for Gitea data
- Sets up necessary environment variables for user ID and group ID
- Exposes ports for web access and SSH

## Prerequisites

- Docker
- Docker Compose

## Usage

1. **Clone the repository or copy the `docker-compose.yml` file to your local machine.**

2. **Create the required directories on your host machine:**
    ```sh
    sudo mkdir -p /mnt/docker/gitea
    sudo chown -R 1000:999 /mnt/docker/gitea
    ```

3. **Run Docker Compose to start the Gitea service:**
    ```sh
    docker-compose up -d
    ```

4. **Access Gitea:**
    - Open your web browser and navigate to `http://localhost:3000` to access the Gitea web interface.
    - Use port `222` for SSH access to your repositories.

## Configuration

### Docker Compose Configuration

- **Networks:**
  - `gitea`: Internal Docker network for the Gitea service.

- **Services:**
  - **server:**
    - `image`: Uses the `gitea/gitea:1.21.11` Docker image.
    - `container_name`: Names the container `gitea`.
    - `environment`:
      - `USER_UID=1000`: Sets the user ID for the Gitea user.
      - `USER_GID=999`: Sets the group ID for the Gitea user.
    - `restart`: Always restarts the container if it stops.
    - `networks`: Connects the container to the `gitea` network.
    - `volumes`:
      - `/mnt/docker/gitea:/data`: Mounts the host directory for persistent data storage.
      - `/etc/timezone:/etc/timezone:ro`: Synchronizes the host timezone with the container.
      - `/etc/localtime:/etc/localtime:ro`: Synchronizes the host local time with the container.
    - `ports`:
      - `3000:3000`: Maps the container's port 3000 to the host's port 3000 for web access.
      - `222:22`: Maps the container's port 22 to the host's port 222 for SSH access.

## Notes

- Ensure the directories and files mounted as volumes are correctly set up on your host machine.
- You may need to adjust file permissions to ensure Gitea can read and write to the mounted directories.

## License

This project is licensed under the MIT License.
