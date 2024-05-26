# Update Domains Script

This script automates the process of updating DNS records and obtaining SSL certificates for domains managed by Nginx Proxy Manager and Pi-hole, using Cloudflare for DNS management and Certbot for SSL certificate generation.

## Features

- Retrieves public and local subdomains from Nginx Proxy Manager
- Updates DNS records on Cloudflare
- Obtains and distributes SSL certificates using Certbot
- Updates local DNS records in Pi-hole
- Periodically checks for IP address changes and updates records as needed

## Prerequisites

- Python 3.x
- `requests` library
- `loguru` library
- `certbot` and the `certbot-dns-cloudflare` plugin
- Docker (for Nginx Proxy Manager and Pi-hole)

## Setup

1. **Install required Python packages:**
    ```sh
    pip install requests loguru
    ```

2. **Install Certbot and the Cloudflare DNS plugin:**
    ```sh
    sudo apt-get install certbot python3-certbot-dns-cloudflare
    ```

3. **Create the Cloudflare credentials file (`cloudflare.ini`):**
    ```ini
    dns_cloudflare_api_token = YOUR_CLOUDFLARE_API_TOKEN
    ```

4. **Set environment variables or update script constants:**
    - `NGINX_PROXY_MANAGER_API`: URL to the Nginx Proxy Manager API
    - `PIHOLE_API`: URL to the Pi-hole API
    - `CLOUDFLARE_API`: URL to the Cloudflare API
    - `CLOUDFLARE_ZONE_ID`: Your Cloudflare Zone ID
    - `CLOUDFLARE_API_TOKEN`: Your Cloudflare API token
    - `PIHOLE_API_TOKEN`: Your Pi-hole API token
    - `CERTBOT_EMAIL`: Your email address for Certbot registration

## Usage

1. **Run the script:**
    ```sh
    python update_domains.py
    ```

## Script Breakdown

### `get_public_subdomains()`

- Fetches public subdomains from Nginx Proxy Manager.

### `update_cloudflare_records(subdomains)`

- Updates DNS records on Cloudflare for each subdomain.

### `obtain_certificates(subdomains)`

- Obtains SSL certificates for each subdomain using Certbot and Cloudflare DNS plugin.

### `distribute_certificates(subdomains)`

- Placeholder for distributing SSL certificates to Nginx Proxy Manager and Cloudflare.

### `get_local_domains()`

- Fetches locally routable domains from Nginx Proxy Manager.

### `update_pihole_records(domains)`

- Updates local DNS records in Pi-hole for each domain.

### `get_public_ip()`

- Retrieves the current public IP address.

### `main()`

- Main function that checks for IP changes and updates records and certificates accordingly.

## Notes

- The script logs activities and errors to `script.log`.
- Adjust the sleep duration in the main loop as needed (default is 30 minutes).

## License

This project is licensed under the MIT License.
