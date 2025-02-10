import json
import argparse

def update_env_file(env_file_path, new_configs):
    with open(env_file_path, 'w') as env_file:
        for key, value in new_configs.items():
            # Check if value is a string or dictionary, then handle accordingly
            if isinstance(value, str):
                env_file.write(f"{key}={value}\n")
            else:
                value_str = json.dumps(value, indent=2)
                env_file.write(f"{key}='{value_str}'\n")

def main():
    parser = argparse.ArgumentParser(description="Update environment file with configurations.")
    
    # Adding arguments for NEXT_PUBLIC_BASE_URL and NEXT_PUBLIC_APP_URL
    parser.add_argument('--backend-url', required=True, help='Base URL for the frontend application')
    parser.add_argument('--frontend-url', required=True, help='App URL for the frontend application')
    parser.add_argument('--socket-url', required=True, help='Base URL for the frontend application')
    parser.add_argument('--env-file-path', default='frontend.env', help='Path to the environment file')

    args = parser.parse_args()

    # Define the configuration dictionary with dynamic values passed from command line
    new_configurations = {
        "NEXT_PUBLIC_BASE_URL": f"https://{args.backend_url}",
        "NEXT_PUBLIC_APP_URL": f"https://{args.frontend_url}",
        "NEXT_PUBLIC_GOOGLE_CLIENT_ID": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "NEXT_PUBLIC_GOOGLE_CLIENT_SECRET": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "NEXT_PUBLIC_SENTRY_URL": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "NEXT_PUBLIC_FCM_PUBLIC_KEY": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "NEXT_PUBLIC_CHARGEBEE_URL": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "NEXT_PUBLIC_CHAT_ID": "xxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "NEXT_PUBLIC_SOCKET_BASE_URL": f"wss://{args.socket_url}",

        # Firebase Config
        "NEXT_PUBLIC_API_KEY": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
        "NEXT_PUBLIC_AUTH_DOMAIN": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "NEXT_PUBLIC_PROJECT_ID": "xxxxxxxxxxxxxxxxxxxxxxxx",
        "NEXT_PUBLIC_STORAGE_BUCKET": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "NEXT_PUBLIC_MESSAGING_SENDER_ID": "xxxxxxxxxxxxxxxxxxxxxxx",
        "NEXT_PUBLIC_APP_ID": "1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "NEXT_PUBLIC_SERVER": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "NEXT_PUBLIC_DIALER_URL": f"https://{args.frontend_url}/dialer"
    }

    # Call the function to write to the specified env file
    update_env_file(args.env_file_path, new_configurations)
    print(f"Environment file '{args.env_file_path}' updated successfully.")

if __name__ == "__main__":
    main()
