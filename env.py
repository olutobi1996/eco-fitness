import os
os.environ.setdefault('MY_ENVIRONMENT_VARIABLE', 'variable_value')

os.environ["STRIPE_PUBLIC_KEY"] = "pk_test_51QuBP5F3sMCxmWUJ2FV3nIHuBXEWBHl1L27Q7ZAmVxvckYNjNQfv6c5NidU3sUMgMqW7Dm78nVUHVM8ryX3bLAdN00etfHfRSs"
os.environ["STRIPE_SECRET_KEY"] = "sk_test_51QuBP5F3sMCxmWUJyVJCyLfcRMAuiexloOR62tk0Ye8Gvm8KTUqJLSOxvTBa2v0VYYXAYKmNWgkbGBOCe2mO9Vet00XbgxUXR7"
os.environ["STRIPE_WH_SECRET"] = "whsec_12cd69daea2b6caaaf78e0fa190302ffa8a4b601569fb3e83e51b45a5bd95764"
os.environ.setdefault('DEVELOPMENT', '1')
