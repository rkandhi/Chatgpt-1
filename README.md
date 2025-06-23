# Financial Data Analyzer

This repository contains a simple Flask application that provides basic analysis of
CSV files with financial data. It demonstrates how to run a web service that
responds with summary statistics for a dataset.

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the app

From the repository root directory, run:

```bash
python app/main.py
```

By default it loads `app/data/sample.csv`. You can specify a different dataset by
providing a `dataset` query parameter. For example:

```
http://localhost:5000/analyze?dataset=sample.csv
```

The service will return a JSON object with the number of rows, column names and
mean values for numeric columns.
