# Data Query AI Assistant

An AI-powered analytics assistant that converts natural language questions into SQL queries, executes them on a PostgreSQL database, and visualizes insights through charts.

---

## Problem Statement

Traditional database querying requires SQL knowledge, making data exploration difficult for non-technical users. This project bridges the gap by allowing users to query databases using plain English.

---

## Features

- Natural Language → SQL conversion
- PostgreSQL database integration
- Dynamic schema loading
- SQL execution pipeline
- Interactive data tables
- Automatic chart generation

---

## Tech Stack

### Languages
- Python

### Libraries & Frameworks
- LangChain
- Streamlit
- SQLAlchemy
- Pandas
- Plotly

### Database
- PostgreSQL

### LLM
- Groq API

---

## Project Architecture

```text
User Query
    ↓
Streamlit UI
    ↓
LangChain + LLM
    ↓
Schema Context Injection
    ↓
SQL Generation
    ↓
PostgreSQL Execution
    ↓
Pandas DataFrame
    ↓
Visualization Layer
    ↓
Charts + Insights
```
---

## Workflow

**Step 1: User Query**

User asks a question in plain English.

```text
Example:

Show top 5 regions with maximum profit 
```

**Step 2: Schema Injection**

Database schema is dynamically loaded and sent to the LLM.

**Step 3: SQL Generation**

The LLM converts the query into PostgreSQL SQL.

**Step 4: Query Execution**

Generated SQL is executed safely on PostgreSQL.

**Step 5: Visualization**

Results are displayed as:

- Tables
- Bar Charts
- Line Charts
- Pie Charts

---

## Folder Structure

```text
Data Query AI Assistant/
│   .env
│   .gitignore
│   README.md
│   requirements.txt
│   main.py
|
└───app
    │
    ├───database
    │   │   db_connection.py
    │   │   schema_loader.py
    │
    ├───dataset
    │       Amazon Dataset.csv
    │
    ├───llm
    │   │   prompt_template.py
    │   │   sql_generator.py
    │
    ├───utils
    │   │   query_executor.py
    │   │   visualization.py

```

---

## Installation

```bash
# Clone Repository
git clone https://github.com/Vaishnavi-020/AI-SQL-Assistant.git

cd AI-SQL-Assistant

# Create Virtual Environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Setup Environment Variables
# Create .env

DATABASE_URL=
API_KEY=

# Run Application
streamlit run main.py

```

---

## Example Queries

### Try asking:
- Top 3 categories with maximum sales.
- Top 3 regions with maximum profit
- Payment method distribution

---

## Challenges Faced

### Automatic chart detection

One of the major challenges was designing a system that could automatically choose the most suitable visualization for dynamically generated query results.

Since users can ask any type of analytical question, the structure of the returned dataset changes frequently (e.g., categorical vs numerical data, time-series data, single-column outputs, aggregated metrics). A single fixed chart type was not practical.

To address this, I implemented a rule-based visualization layer that analyzes the returned Pandas DataFrame and selects charts based on data patterns:

- **Category + Numeric → Bar Chart**
- **Datetime + Numeric → Line Chart**
- **Single Numeric Column → Histogram**
- **Small Category Groups → Pie Chart**

---

## Future Improvements
- Authentication System
- Query Explanation
- Deployment

---

## Author

Vaishnavi Sinha
