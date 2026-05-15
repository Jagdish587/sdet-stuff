# Run Tests and Generate Allure Report

## Run pytest and generate allure results

```bash
pytest --alluredir=allure-results
```

## Open Allure Report

```bash
allure serve allure-results
```

## Alternative: Generate Static HTML Report

```bash
allure generate allure-results -o allure-report --clean
```

## Open Generated Report

```bash
allure open allure-report
```
