import json
import argparse

def update_env_file(env_file_path, new_configs):
    with open(env_file_path, 'a') as env_file:
        for key, value in new_configs.items():
            value_str = json.dumps(value, indent=2)
            env_file.write(f"\n{key}='{value_str}'\n")

def main():
    parser = argparse.ArgumentParser(description="Update environment file with configurations.")
    parser.add_argument('--namespace', required=True, help='Kubernetes namespace (e.g., namespace-dev)')
    parser.add_argument('--env-file-path', default='.env', help='Path to environment file')

    args = parser.parse_args()

    new_configurations = {
        "SECRET": {
            "SECRET_KEY": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        },
        "REDIS": {
            "HOST": f"xxxxxxxxxxxx-release-{args.namespace}-redis",
            "PORT": "6379",
            "SECRET": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        }

    }

    update_env_file(args.env_file_path, new_configurations)
    print(f"Environment file '{args.env_file_path}' updated successfully.")
if __name__ == "__main__":
    main()
