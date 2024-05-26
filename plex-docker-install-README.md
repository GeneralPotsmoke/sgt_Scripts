# Plex Media Server

This `docker-compose.yaml` file sets up a Plex Media Server with GPU support using NVIDIA.

## Prerequisites

- Docker and Docker Compose installed
- NVIDIA GPU with drivers and Docker runtime installed

## Configuration

Update the following volume paths in the `docker-compose.yaml` file to match your system:

```yaml
volumes:
  - /path/to/media:/media
  - /path/to/plex/config:/config
  - /path/to/plex/transcoder:/transcode
```

## Usage

1. **Create and navigate to the directory:**
    ```sh
    mkdir -p ~/plex-docker
    cd ~/plex-docker
    ```

2. **Save the `docker-compose.yaml` file in this directory.**

3. **Deploy the container:**
    ```sh
    docker-compose up -d
    ```

4. **Access Plex:**
    - Open your web browser and navigate to `http://localhost:32400/web`.

## Networks

The service is connected to an external network named `external_network`. Ensure this network exists or create it with:

```sh
docker network create external_network
```

## Notes

- Make sure your NVIDIA drivers and Docker runtime are properly set up.
