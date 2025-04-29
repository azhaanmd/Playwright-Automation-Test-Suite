@echo off
echo Running all tests with HTML and JSON report...
pytest tests/ --html=report/report.html --self-contained-html --json-report --json-report-file=report/report.json
pause