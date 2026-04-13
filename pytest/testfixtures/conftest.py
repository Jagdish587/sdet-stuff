# conftest.py
import pytest

# scope="class" means this setup and cleanup runs once per test class
@pytest.fixture(scope="class")
def shared_database():
    # --- SETUP ---
    print("\n[Global Setup] Connecting to the shared database...")
    db_connection = {"status": "connected", "records": []}
    
    yield db_connection  # This is where your test classes will execute
    
    # --- CLEANUP ---
    print("\n[Global Cleanup] Dropping tables and disconnecting...")
    db_connection["records"].clear()
    db_connection["status"] = "disconnected"
