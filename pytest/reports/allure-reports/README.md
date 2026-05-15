# Pytest + Allure Report Example

A simple project demonstrating how to generate beautiful test reports using **pytest** and **Allure Framework**.





## Run Tests

Generate Allure result files:

```bash
pytest --alluredir=allure-results
```

## View the Report

Launch the interactive report:

```bash
allure serve allure-results
```

Or generate a static HTML report:

```bash
allure generate allure-results -o allure-report --clean
```

Open the generated report:

```text
allure-report/index.html
```

## Example Test

This project contains two example tests:

| Test                                    | Result |
| --------------------------------------- | ------ |
| User can login with valid credentials   | ✅ Pass |
| User cannot login with invalid password | ❌ Fail |

The examples demonstrate:

* Allure titles
* Descriptions
* Severity levels
* Features and stories
* Test steps
* Attachments
* Assertion failures

## Sample Report

When executed, the report includes:

* Dashboard
* Test summary
* Pass/Fail statistics
* Test execution steps
* Attachments
* Stack traces for failures
* Feature and Story grouping

## Technologies

* Python
* pytest
* Allure Framework

## Learning Resources

* Pytest basics
* Allure annotations
* Test reporting
* Test organization
* Debugging failed tests

## License

This project is provided for educational and learning purposes.
