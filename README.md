Welcome to SGT_Scripts! This repository is a comprehensive collection of various scripts and Docker Compose configurations that I've crafted in the mysterious depths of my home office. Whether you're looking to automate your home, manage your network, or just prove to your friends that you know what you're doing, this repository has got you covered. It’s also my way of showing off my coding prowess – because nothing says “I can code” like a well-organized repository!

Project Overview
SGT_Scripts features a motley crew of scripts written in Python, Bash, and PowerShell. These scripts are the unsung heroes of my home setup, quietly making everything run smoothly. Plus, you’ll find my own Docker Compose files – anonymized for your security and my peace of mind. These gems demonstrate my ability to set up and manage services using Docker, and they’ll make you wonder how you ever lived without them.

Key Features
Home Automation: Scripts for automating various home tasks using tools like Home Assistant. Because who wants to do things manually?
Network Management: Scripts for managing and monitoring network configurations, including dynamic DNS updates using Cloudflare and Pi-hole. Your network will be the envy of all the neighbors.
Security and Maintenance: Scripts for maintaining and securing home servers, including certificate management and automatic updates. Sleep better knowing your servers are safe.
Data Management: Scripts for handling and organizing data, including backup solutions and data synchronization. No more lost files or messy data.
Development Tools: Various utilities and helper scripts that streamline the development process and improve productivity. Work smarter, not harder.
Docker Compose Configurations: My Docker Compose files, demonstrating how to deploy and manage services with Docker Compose. Containers, containers everywhere!
Example Scripts and Configurations
Python Scripts
update_domains.py: Automates the process of updating DNS records and obtaining SSL certificates for public and local domains. Integrates with Nginx Proxy Manager, Cloudflare, and Pi-hole. Because security should be easy!
install_docker.py: Sets up Docker and Docker Compose on a system, including the necessary updates and configurations. Get your Docker fix here.
Bash Scripts
network_monitor.sh: Monitors network status and alerts you to any changes or issues, including logging and notification functionalities. It’s like having your own network watchdog.
PowerShell Scripts
windows_maintenance.ps1: Designed for routine maintenance on Windows systems, including cleanup tasks, updates, and security checks. Keep your Windows system in tip-top shape.
Docker Compose Files
plex-docker-compose.yaml: Sets up Plex Media Server with GPU support using NVIDIA. Stream all the things!
dizquetv-docker-compose.yaml: Configures DizqueTV for creating custom live TV channels. Be your own TV network.
glances-docker-compose.yaml: Sets up Glances, a cross-platform monitoring tool. Keep an eye on everything.
ombi-docker-compose.yaml: Configures Ombi, a request management system for media content. Make your media requests without the hassle.
tautulli-docker-compose.yaml: Sets up Tautulli, a monitoring and tracking tool for Plex Media Server. Know what’s playing and who’s watching.
watchtower-docker-compose.yaml: Configures Watchtower to automatically update running Docker containers. Set it and forget it.
Usage
Each script and configuration comes with detailed comments and instructions. Just clone this repository, navigate to the script or configuration directory, and follow the instructions. It’s as easy as pie – and way more useful.

sh
Copy code
```git clone https://github.com/GeneralPotsmoke/sgt_Scripts.git
cd sgt_Scripts```
Contributions
Contributions are welcome! If you’ve got improvements, additional scripts, or Docker Compose configurations that you think would make this repository even more awesome, feel free to submit a pull request. For major changes, please open an issue first to discuss what you’d like to change. Let's make this repository the best it can be, together!

License
This project is licensed under the MIT License. See the LICENSE file for more details. Use it, love it, and maybe even improve it.
