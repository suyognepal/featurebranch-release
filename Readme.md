# Feature branch release Pipeline Deployment and Automation

## Overview
This repository contains Ansible playbooks and Jenkins pipelines for automating the deployment and management of various environments. The automation scripts assist in installation, configuration, infrastructure management, and CI/CD pipeline execution.

## Project Structure
```
├── ansible
│   ├── inventory
│   │   └── edgedb.ini                    # Ansible inventory file for deployment hosts
│   ├── roles
│   │   └── deployment
│   │       ├── handlers
│   │       │   └── main.yaml             # Handlers for restarting services
│   │       ├── tasks
│   │       │   ├── cloudfare.yaml        # Cloudflare-related configurations
│   │       │   ├── configureprovider.yaml # Configurations for cloud providers
│   │       │   ├── createenv.yaml        # Environment setup tasks
│   │       │   ├── delete.yaml           # Cleanup tasks
│   │       │   ├── expose.yaml           # Exposing services to the network
│   │       │   ├── install.yaml          # Installation script for dependencies
│   │       │   ├── main.yaml             # Main Ansible task file
│   │       │   ├── migration.yaml        # Database migration tasks
│   │       │   ├── repositories.yaml     # Repository configurations
│   │       │   └── ssl.yaml              # SSL setup and configurations
│   │       └── vars
│   │           └── vars.yaml              # Variables for deployment
│   └── sitefiles
│       └── edgedb.yaml                # Site-wide configurations for deployments
├── Jenkins
│   └── featurebranch-release
│       ├── genenvfront.py                 # Script for generating frontend environment variables
│       ├── genenv.py                      # Script for backend environment variables
│       ├── genenvsocket.py                # Script for WebSocket environment variables
│       ├── Jenkinsfile                    # Jenkins pipeline for feature branch releases (automates creation of socket, worker, backend deployment, and frontend environments)
│       └── Jenkinsfile-Delete-Resources   # Jenkins pipeline for resource cleanup
└── Readme.md                              
```

## Installation & Usage

### Ansible Deployment
1. Install Ansible:
   ```sh
   sudo apt update && sudo apt install -y ansible
   ```
2. Update the `ansible/inventory/servers.ini` file with the appropriate server details.
3. Run the Ansible playbook:
   ```sh
   ansible-playbook -i ansible/inventory/edgedb.ini ansible/sitefiles/deployment.yaml --private-key ~/.ssh/id_rsa
   ```

### Jenkins Pipelines
#### Feature Branch Release
- The `Jenkinsfile` automates the deployment process for feature branches.
- It creates the entire environment, including socket, worker, backend deployment, and frontend.
- Environment variables are generated using the `genenv` scripts.
- The pipeline is triggered on feature branch updates.

#### Resource Cleanup
- The `Jenkinsfile-Delete-Resources` script is used to delete all the resources that was created
- Can be triggered manually to clean up environments.


## License
This project is licensed under the MIT License.

## Contact
For any issues or contributions, reach out to **suyog.nepal10@gmail.com**.

