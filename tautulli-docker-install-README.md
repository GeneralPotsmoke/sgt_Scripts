# Tautulli

This `docker-compose.yaml` file sets up Tautulli, a monitoring and tracking tool for Plex Media Server.

## Prerequisites

- Docker and Docker Compose installed

## Configuration

Update the following volume paths in the `docker-compose.yaml` file to match your system:

```yaml
volumes:
  - /path/to/tautulli/config:/config
```

## Usage

1. **Create and navigate to the directory:**
    ```sh
    mkdir -p ~/tautulli-docker
    cd ~/tautulli-docker
    ```

2. **Save the `docker-compose.yaml` file in this directory.**

3. **Deploy the container:**
    ```sh
    docker-compose up -d
    ```

4. **Access Tautulli:**
    - Open your web browser and navigate to `http://localhost:8181`.

## Notes

- The container is configured to restart always and uses host network mode.
- Ensure you set the correct PUID and PGID for file permissions.
