# Security Stack Docker Compose

This repository contains a Docker Compose configuration file to set up a comprehensive security stack, including PostgreSQL, Wuzzah, OSSEC, The Hive, and Rsyslog. The setup ensures that all data, alerts, and logs are saved to a PostgreSQL database server.

## Services

- **PostgreSQL**: A powerful, open-source object-relational database system.
- **Wuzzah**: An open-source security monitoring tool.
- **OSSEC**: An open-source host-based intrusion detection system (HIDS).
- **The Hive**: A scalable, open-source, and free Security Incident Response Platform.
- **Rsyslog**: A high-performance log processing system.

## Prerequisites

- Docker and Docker Compose installed on your server.
- A separate VM for running the PostgreSQL server, if desired.

## Configuration

Ensure you update the following environment variables in the `docker-compose.yaml` file:

- `POSTGRES_USER`: Your PostgreSQL username.
- `POSTGRES_PASSWORD`: Your PostgreSQL password.
- `POSTGRES_DB`: Your PostgreSQL database name.
- `DB_HOST`: Hostname of your PostgreSQL server (set to `postgres` for the local service).
- `DB_PORT`: Port number of your PostgreSQL server (default is `5432`).
- `DB_NAME`: Your PostgreSQL database name.
- `DB_USER`: Your PostgreSQL username.
- `DB_PASS`: Your PostgreSQL password.

## Volumes

The configuration uses named volumes to persist data:

- `postgres_data`: Stores PostgreSQL data.
- `ossec_data`: Stores OSSEC data.
- `the_hive_data`: Stores The Hive data.
- `rsyslog_config`: Stores Rsyslog configuration files.
- `rsyslog_data`: Stores Rsyslog logs.

## Usage

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/sec-stack.git
    cd sec-stack
    ```

2. **Update the `docker-compose.yaml` file** with your PostgreSQL credentials and other necessary configurations.

3. **Start the services**:
    ```sh
    docker-compose -f sec-stack-docker-compose.yaml up -d
    ```

4. **Access the services**:

    - **Wuzzah**: Open your browser and navigate to `http://localhost:5000`.
    - **OSSEC**: Use the OSSEC interface via `http://localhost:1514`.
    - **The Hive**: Open your browser and navigate to `http://localhost:9000`.
    - **Rsyslog**: Logs will be collected and can be viewed in the configured volume.

## Stopping the Services

To stop and remove all the services, run:

```sh
docker-compose -f sec-stack-docker-compose.yaml down
Troubleshooting
Ensure Docker and Docker Compose are correctly installed and running.
Verify the environment variables in the docker-compose.yaml file are correctly set.
Check the logs of individual services using:
sh
Copy code
docker logs <container_name>
Contributions
Contributions are welcome! Feel free to submit a pull request or open an issue to discuss improvements, additional features, or bugs.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
