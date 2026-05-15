import allure


@allure.feature("Authentication")
@allure.story("Valid Login")
@allure.title("User can login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login():

    with allure.step("Enter username"):
        username = "admin"

    with allure.step("Enter password"):
        password = "admin123"

    with allure.step("Validate credentials"):
        assert username == "admin"
        assert password == "admin123"

    allure.attach(
        "Login successful",
        name="Result",
        attachment_type=allure.attachment_type.TEXT
    )


@allure.feature("Authentication")
@allure.story("Invalid Login")
@allure.title("User cannot login with invalid password")
@allure.severity(allure.severity_level.NORMAL)
def test_invalid_login():

    with allure.step("Enter username"):
        username = "admin"

    with allure.step("Enter password"):
        password = "wrongpassword"

    with allure.step("Validate credentials"):
        assert username == "admin"
        assert password == "admin123"

    allure.attach(
        "Login failed",
        name="Result",
        attachment_type=allure.attachment_type.TEXT
    )