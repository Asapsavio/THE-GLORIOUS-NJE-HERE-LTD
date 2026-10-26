from dotenv import load_dotenv
import os

load_dotenv()
shop_name = os.getenv("SHOP_NAME", "Unknown shop")
print(f"Welcome to {shop_name}")