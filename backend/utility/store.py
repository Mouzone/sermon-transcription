from typing import Dict
import os
from supabase import Client, create_client


def store(sermon_data: Dict[str, str]) -> None:
    """Store sermon data in Supabase"""
    try:
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")

        if not url or not key:
            raise ValueError("Supabase credentials not found")

        logger.info("Connecting to Supabase")
        supabase: Client = create_client(url, key)

        logger.info("Storing sermon data")
        result = supabase.table("Sermon").insert(sermon_data).execute()

        if hasattr(result, "error") and result.error:
            logger.error(f"Supabase storage failed: {result.error}")
            raise SermonProcessingError(f"Database error: {result.error}")

        logger.info("Sermon stored successfully")

    except Exception as e:
        logger.error(f"Failed to store sermon: {str(e)}")
        raise SermonProcessingError("Sermon storage failed") from e
