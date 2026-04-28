import pytest

@pytest.fixture
def user_data():
    return [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]

# Test function to check for a specific user by name and age
def test_user_exists(user_data):
    user = {"name": "Alice", "age": 30}

    # Check if the target user is in the list
    assert user in user_data

# Test average age of users
def test_average_age(user_data):
    ages = [user["age"] for user in user_data]
    avg_age = sum(ages) / len(ages)
    assert avg_age == 30
