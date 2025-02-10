import json
import argparse

def update_env_file(env_file_path, new_configs):
    with open(env_file_path, 'a') as env_file:
        for key, value in new_configs.items():
            value_str = json.dumps(value, indent=2)
            env_file.write(f"\n{key}='{value_str}'\n")

def main():
    parser = argparse.ArgumentParser(description="Update environment file with configurations.")
    parser.add_argument('--frontend-domain', required=True, help='Front-end domain (e.g., example.frontend.com)')
    parser.add_argument('--backend-domain', required=True, help='Backend service domain (e.g., example.backend.com)')
    parser.add_argument('--database-branch', required=True, help='Database branch (e.g., main)')
    parser.add_argument('--database-domain', required=True, help='Database domain (e.g., example.database.com)')
    parser.add_argument('--namespace', required=True, help='Kubernetes namespace (e.g., namespace)')
    parser.add_argument('--env-file-path', default='../../ansible/devel.env', help='Path to environment file')

    args = parser.parse_args()

    new_configurations = {
        "DEFAULT": {
            "FRONT_END_DOMAIN": f"https://{args.frontend_domain}",
            "FCM_PROJECT_ID": "dev",
            "DATA_DIRECTORY": "/usr/app/data/"
        },
        "SECRET": {
            "SECRET_KEY": "xxxxxxxxxxxxxxx"
        },
        "EDGEDB_AUTH": {
            "EDGEDB_AUTH_BASE_URL": f"https://{args.database_domain}/db/{args.database_branch}/ext/auth",
            "PASSWORD_RESET_URL": f"https://{args.frontend_domain}/reset/password",
            "USER_VERIFY_URL": f"https://{args.database_domain}/auth/verify",
            "FRONT_END_DOMAIN": f"https://{args.frontend_domain}"
        },
        "MAIL": {
            "SENDER_EMAIL": "noreply@example.com",
            "API_KEY": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        },
        "CHARGEBEE": {
            "API_KEY": "xxxxxxxxxxxxxxxxxxxxxxx",
            "SITE_NAME": "xxxxxxxxxxxxxxx",
            "AUTH_EMAIL": "xxxxxxxxxxxxx@example.com",
            "AUTH_PASSWORD": "xxxxxxxxxxxxxxxx",
            "DEFAULT_CHARGE": "xxxxxxxxxxxx",
            "PLAN_FAMILY": "xxxxxxxxxxxxxx",
        },
        "VOIP": {
            "TELNYX_API_KEY": "xxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "TWILIO_ACCOUNT_SID": "xxxxxxxxxxxxxxxxxxxxx",
            "TWILIO_AUTH_TOKEN": "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "TELNYX_ANDROID_PUSH_CREDENTIAL_ID": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
            "WEBHOOK_URI": f"https://{args.backend_domain}",
            "SERVER_TYPE": "xxxxxxxxxxxxxx"
        },
        "JWT": {
            "REFRESH_TOKEN_TTL_SECONDS": 240000,
            "ACCESS_TOKEN_TTL_SECONDS": 18000000,
            "DEVICE_REFRESH_TOKEN_TTL_SECONDS": 6048000,
            "DEVICE_ACCESS_TOKEN_TTL_SECONDS": 8640000,
            "SECRET_KEY": "{\"crv\":\"Ed25519\",\"d\":\"xxxxxxxxxxxxxxxxx\",\"kid\":\"server\",\"kty\":\"OKP\",\"x\":\"xc1-xxxxxxxxxxxxxxxxxx\"}"
        },
        "SUPPORT": {
            "EMAIL": "xxxxxxxxxxxx@example.com",
            "PASSWORD": "password@123",
            "FIRST_NAME": "xxxxxxx",
            "LAST_NAME": "xxxxxxxxxxx"
        },
        "AWS": {
            "AWS_ACCESS_KEY_ID": "xxxxxxxxxxxxxxx",
            "AWS_SECRET_ACCESS_KEY": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "REGION": "xxxxxxxxxxxxx",
            "BUCKET": "xxxxxxxxxxxxxxxxxxxxx",
            "SIGNATURE_VERSION": "xxxxxxxxxxx"
        },
        "LOGGING": {
            "LOG_LEVEL": "ERROR",
            "BACKUP_COUNT": 30,
            "INTERVAL": 1,
            "WHEN": "D",
            "DIR_PATH": "/var/log/app/"
        },
        "REDIS": {
            "HOST": f"xxxx-release-{args.namespace}-redis",
            "PORT": "6379",
            "SECRET": "xxxxxxxxxxx"
        },
        "RABBITMQ": {
            "HOST": "rabbitmq.rabbitmq.svc.cluster.local",
            "PORT": "5672",
            "USER": "xxxxxxxxx",
            "PASSWORD": "xxxxxxxxxxxxx",
            "PREFIX": f"{args.namespace}"
        },
        "INTEGRATIONS": {
            "HUBSPOT": {
                    "CLIENT_ID": "xxxxxxxxxxxxxxxxxxxxxxx",
                    "CLIENT_SECRET": "xxxxxxxxxxxxxxxxxxxx",
                    "REDIRECT_URI": "http://localhost:3000/integrations/connect/"
                }
        }
    }

    update_env_file(args.env_file_path, new_configurations)
    print(f"Environment file '{args.env_file_path}' updated successfully.")
if __name__ == "__main__":
    main()
