import os

app_config = {
            'host': os.getenv('MICROSERVICE_EXAMPLE_HOST', '0.0.0.0'),
            'port': int(os.getenv('MICROSERVICE_EXAMPLE_PORT', 8080)),
            'debug': os.getenv('DEBUG') == "1"
            }
