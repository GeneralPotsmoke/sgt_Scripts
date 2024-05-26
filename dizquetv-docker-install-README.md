# DizqueTV

This `docker-compose.yaml` file sets up DizqueTV, a tool for creating custom live TV channels.

## Prerequisites

- Docker and Docker Compose installed

## Configuration

Update the following volume paths in the `docker-compose.yaml` file to match your system:

```yaml
volumes:
  - /path/to/dizquetv/config:/app/config
```

## Usage

1. **Create and navigate to the directory:**
    ```sh
    mkdir -p ~/dizquetv-docker
    cd ~/dizquetv-docker
    ```

2. **Save the `docker-compose.yaml` file in this directory.**

3. **Deploy the container:**
    ```sh
    docker-compose up -d
    ```

4. **Access DizqueTV:**
    - Open your web browser and navigate to `http://localhost:8666`.

## Notes

- The container is configured to restart unless stopped manually.
