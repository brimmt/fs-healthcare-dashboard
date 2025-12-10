import os
from supabase import create_client, Client

USE_FAKE_SUPABASE = os.getenv("USE_FAKE_SUPABASE", "false").lower() == "true"

if USE_FAKE_SUPABASE:
    from app.services.supabase_client_mock import supabase
else:
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("Supabase credentials missing.")

    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)