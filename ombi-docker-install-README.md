# Ombi

This `docker-compose.yaml` file sets up Ombi, a request management system for media content.

## Prerequisites

- Docker and Docker Compose installed

## Configuration

Update the following volume paths in the `docker-compose.yaml` file to match your system:

```yaml
volumes:
  - /path/to/ombi/config:/config
```

## Usage

1. **Create and navigate to the directory:**
    ```sh
    mkdir -p ~/ombi-docker
    cd ~/ombi-docker
    ```

2. **Save the `docker-compose.yaml` file in this directory.**

3. **Deploy the container:**
    ```sh
    docker-compose up -d
    ```

4. **Access Ombi:**
    - Open your web browser and navigate to `http://localhost:3579`.

## Notes

- The container is configured to restart always.
- Ensure you set the correct PUID and PGID for file permissions.
