import pytest

class TestFileOperations:

    @classmethod
    def setup_class(cls):
        """ Runs ONCE before all tests in this class """
        print("\n[Setup Class] Creating temporary directory...")
        cls.temp_dir = "/tmp/test_dir"

    @classmethod
    def teardown_class(cls):
        """ Runs ONCE after all tests in this class """
        print("\n[Teardown Class] Deleting temporary directory...")
        del cls.temp_dir

    def setup_method(self, method):
        """ Runs before EVERY individual test method """
        print(f"\n[Setup Method] Preparing file for {method.__name__}...")
        self.file_data = []

    def teardown_method(self, method):
        """ Runs after EVERY individual test method """
        print(f"\n[Teardown Method] Cleaning up file after {method.__name__}...")
        self.file_data.clear()

    # --- Actual Tests ---
    
    def test_write_operation(self):
        print("Executing test_write_operation...")
        self.file_data.append("hello")
        assert "hello" in self.file_data

    def test_another_operation(self):
        print("Executing test_another_operation...")
        assert len(self.file_data) == 0  # Freshly cleared by teardown_method!
