import os
import dotenv 
dotenv.load_dotenv()
salt = os.getenv('SALT')
print("salt >", salt)