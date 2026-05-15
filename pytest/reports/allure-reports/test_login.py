import allure


@allure.title("User Login Test")
@allure.description("Verify login functionality")
@allure.severity(allure.severity_level.CRITICAL)
def test_login():

    with allure.step("Enter username"):
        username = "admin"

    with allure.step("Enter password"):
        password = "admin123"

    with allure.step("Validate credentials"):
        assert username == "admin"
        assert password == "admin123"

    allure.attach(
        "Login successful",
        name="result",
        attachment_type=allure.attachment_type.TEXT
    )