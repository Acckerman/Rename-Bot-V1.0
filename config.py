import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "18517936")

API_HASH = os.environ.get("API_HASH", "552ce63ba82ea7a633b039ee0dc87790")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5535408997:AAEmnT-ZdCsy43HsxwRJe0It0hzSC0e7zO8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "k2m_movies_series") 

DB_NAME = os.environ.get("DB_NAME","Autofilterpro")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Autofilterpro:acckerman@cluster0.apoqe80.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/1f04a86d2526b25b34d55.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1753576629').split()]

PORT = os.environ.get("PORT", "8080")
