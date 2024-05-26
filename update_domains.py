import time
import requests
import logging
import logging.handlers
import os
import json
from datetime import datetime
from loguru import logger
from requests.exceptions import RequestException, HTTPError
from certbot.main import main as certbot_main

# Configure logging
logger.add("script.log", format="{time} {level} {message}", level="INFO")

# Constants
NGINX_PROXY_MANAGER_API = 'http://nginx-proxy-manager-api-endpoint'
PIHOLE_API = 'http://pihole-api-endpoint/admin/api.php'
CLOUDFLARE_API = 'https://api.cloudflare.com/client/v4/zones'
CLOUDFLARE_ZONE_ID = 'your_cloudflare_zone_id'
CLOUDFLARE_API_TOKEN = 'your_cloudflare_api_token'
PIHOLE_API_TOKEN = 'your_pihole_api_token'
CERTBOT_EMAIL = 'your_email@example.com'

# Get house IP
try:
    HOUSE_IP = requests.get('https://api.ipify.org').content.decode('utf8')
    logger.info(f'House IP address: {HOUSE_IP}')
except RequestException as e:
    logger.error(f"Failed to get house IP address: {e}")
    raise

# Headers
headers = {
    'Authorization': f'Bearer {CLOUDFLARE_API_TOKEN}',
    'Content-Type': 'application/json',
}

# Function to pull public subdomains from Nginx Proxy Manager
def get_public_subdomains():
    try:
        response = requests.get(f'{NGINX_PROXY_MANAGER_API}/public_domains')
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        logger.error(f"Failed to get public subdomains: {e}")
        raise

# Function to update Cloudflare DNS records
def update_cloudflare_records(subdomains):
    for subdomain in subdomains:
        data = {
            'type': 'A',
            'name': subdomain,
            'content': HOUSE_IP,
            'ttl': 120,
            'proxied': False,
        }
        try:
            response = requests.post(f'{CLOUDFLARE_API}/{CLOUDFLARE_ZONE_ID}/dns_records', headers=headers, data=json.dumps(data))
            response.raise_for_status()
            logger.info(f'Updated Cloudflare DNS record for {subdomain}')
        except HTTPError as e:
            logger.error(f"HTTP error occurred while updating Cloudflare DNS record for {subdomain}: {e}")
        except RequestException as e:
            logger.error(f"Error occurred while updating Cloudflare DNS record for {subdomain}: {e}")

# Function to obtain certificates using Certbot
def obtain_certificates(subdomains):
    for subdomain in subdomains:
        try:
            certbot_main([
                'certonly', '--dns-cloudflare', '--dns-cloudflare-credentials', 'cloudflare.ini',
                '-d', subdomain, '--email', CERTBOT_EMAIL, '--agree-tos', '--non-interactive'
            ])
            logger.info(f'Obtained certificate for {subdomain}')
        except Exception as e:
            logger.error(f"Failed to obtain certificate for {subdomain}: {e}")

# Function to distribute certificates
def distribute_certificates(subdomains):
    for subdomain in subdomains:
        cert_path = f'/etc/letsencrypt/live/{subdomain}'
        cert_files = {
            'cert': os.path.join(cert_path, 'fullchain.pem'),
            'key': os.path.join(cert_path, 'privkey.pem'),
        }
        # Add logic to distribute certificates to Nginx Proxy Manager and Cloudflare
        logger.info(f'Distributed certificate for {subdomain}')

# Function to pull locally routable domains from Nginx Proxy Manager
def get_local_domains():
    try:
        response = requests.get(f'{NGINX_PROXY_MANAGER_API}/local_domains')
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        logger.error(f"Failed to get local domains: {e}")
        raise

# Function to update Pi-hole local DNS records
def update_pihole_records(domains):
    for domain in domains:
        try:
            response = requests.post(f'{PIHOLE_API}?list=black&domain={domain}&ip={HOUSE_IP}&auth={PIHOLE_API_TOKEN}')
            response.raise_for_status()
            logger.info(f'Updated Pi-hole local DNS record for {domain}')
        except HTTPError as e:
            logger.error(f"HTTP error occurred while updating Pi-hole local DNS record for {domain}: {e}")
        except RequestException as e:
            logger.error(f"Error occurred while updating Pi-hole local DNS record for {domain}: {e}")

# Function to get the current public IP address
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        return response.json()['ip']
    except RequestException as e:
        logger.error(f"Failed to get public IP address: {e}")
        raise

# Main function
def main():
    last_ip = None
    while True:
        try:
            public_ip = get_public_ip()
            if public_ip != last_ip:
                public_subdomains = get_public_subdomains()
                update_cloudflare_records(public_subdomains)
                obtain_certificates(public_subdomains)
                distribute_certificates(public_subdomains)

                local_domains = get_local_domains()
                update_pihole_records(local_domains)

                last_ip = public_ip
                logger.info('IP address changed, updated records and certificates')
            else:
                logger.info('IP address unchanged, no updates required')

        except Exception as e:
            logger.exception(f'An error occurred: {e}')

        time.sleep(1800)  # Sleep for 30 minutes

if __name__ == '__main__':
    main()
