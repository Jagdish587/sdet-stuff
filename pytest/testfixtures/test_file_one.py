# test_file_one.py
import pytest

class TestDataInsertion:
    
    def test_insert_user(self, shared_database):
        print("Running test_insert_user in File One...")
        shared_database["records"].append("user_alice")
        
        assert "user_alice" in shared_database["records"]
        assert shared_database["status"] == "connected"

    def test_insert_another_user(self, shared_database):
        print("Running test_insert_another_user in File One...")
        shared_database["records"].append("user_bob")
        
        assert len(shared_database["records"]) == 2
