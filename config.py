import logging

CLIENT_ID = "YOUR_SMART_HOME_NAME"
CLIENT_SECRET = "YOUR_SECRET"
API_KEY = "YOUR_API_KEY"
USERS_DIRECTORY = "/root/google_home/users"
TOKENS_DIRECTORY = "/root/google_home/tokens"
DEVICES_DIRECTORY = "/root/google_home/devices"

# Uncomment to enable logging
LOG_FILE = "/root/google-home/google-home.log"
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(asctime)s %(remote_addr)s %(user)s %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
