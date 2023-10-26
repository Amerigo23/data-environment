# pylint: disable=missing-docstring

import os

def start():
    flask_env = os.getenv('FLASK_ENV', 'empty')
    return f"Starting in {flask_env} mode..."

if __name__ == "__main__":
    print(start())
