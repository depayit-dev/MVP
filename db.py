from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()  # โหลด .env ถ้ารัน local

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
