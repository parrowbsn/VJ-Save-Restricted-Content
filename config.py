import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28837889"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9d5e9c5b8abcf8b7b930abd259de254e")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "8004931028"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://akaneji1433:DcRECkH1PSIJL1js@cluster0.d0vhr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "akaneji1433")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
