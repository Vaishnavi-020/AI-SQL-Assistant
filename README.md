# Data Query AI Assistant

Built an AI-powered SQL Analytics Assistant using LangChain, PostgreSQL, and Streamlit that converts natural language into SQL queries, executes them on structured databases, generates dynamic visualizations, and produces automated business insights using LLMs.

---

## Screenshots

### Natural Language to SQL
Users can ask business questions in natural language, and the system generates SQL automatically.

<img src="frontend\images\sql_generation.png" width="800" />

### Result & Visualization
Automatic chart generation from SQL results.

<img src="frontend\images\Result.png" width="800" />

### AI-Powered Business Insights
LLM-generated explanation of query results.

<img src="frontend\images\Explanation.png" width="800" />

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
- Key insights & observations generation for business purpose.

---

## Tech Stack

### Languages
- Python

### Backend
- FastAPI

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
┌─────────────────────┐
│       User          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Streamlit Frontend  │
│                     │
│ • User Interface    │
│ • Data Visualization│
│ • Results Display   │
└──────────┬──────────┘
           │ HTTP Request
           ▼
┌─────────────────────┐
│   FastAPI Backend   │
│                     │
│ • Request Validation│
│ • Query Processing  │
│ • Error Handling    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   LLM Service       │
│   (Groq)            │
│                     │
│ • SQL Generation    │
│ • Result Analysis   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ PostgreSQL Database │
│                     │
│ • Execute Queries   │
│ • Return Results    │
└─────────────────────┘
```
---

## Workflow
```text
User Question
      │
      ▼
Streamlit Frontend
      │
      ▼
POST /query
      │
      ▼
FastAPI Router
      │
      ▼
Query Service
      │
      ├── Generate SQL (LLM)
      │
      ├── Execute Query
      │
      └── Generate Analysis (LLM)
      │
      ▼
JSON Response
      │
      ▼
Streamlit Frontend
      │
      ▼
Table + Charts + Insights
```
---

## Folder Structure

```text
Data Query AI Assistant/
│   .gitignore
│   README.md
│
│
├───backend
│   │   .env
│   │   main.py
│   │   requirements.txt
│   │
│   ├───database
│   │   │   load_data.py
│   │   │   schema_loader.py
│   │
│   ├───dataset
│   │       customers (1).csv
│   │       orders (1).csv
│   │       products (1).csv
│   │
│   ├───model
│   │   │   llm_model.py
│   │   │   prompt_template.py
│   ├───router
│   │   │   query_router.py
│   │   │
│   │
│   ├───schema
│   │   │   query_response.py
│   │   │   question_schema.py
│   │   │
│   │
│   ├───services
│   │   │   analysis_service.py
│   │   │   process_query.py
│   │   │   query_executor.py
│   │   │   query_service.py
│   │   │
│   │
│
└───frontend
    │   app.py
    │   clean_df.py
    │   requirements.txt
    │   visualization.py
    │
    ├───images
    │       Explanation.png
    │       Result.png
    │       sql_generation.png

```

---

## Installation
```bash
# Clone Repository
git clone https://github.com/Vaishnavi-020/Data-Query-AI-Assistant.git

cd Data-Query-AI-Assistant

# Create Virtual Environment
python -m venv venv

# Activate virtual environment

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# Install Frontend Dependencies
pip install -r frontend/requirements.txt

# Install Backend Dependencies
pip install -r backend/requirements.txt
```

Create a `.env` file inside:

```text
backend/.env
```

```env
DATABASE_URL=your_database_url
GROQ_API_KEY=your_groq_api_key
```

### Load Dataset

```bash
python backend/database/load_data.py
```

### Start Backend (Terminal 1)

```bash
cd backend
uvicorn main:app --reload
```
### API Documentation
After starting the backend, visit:
http://127.0.0.1:8000/docs

### Start Frontend (Terminal 2)

```bash
cd frontend
streamlit run app.py

```

---

## Example Queries

### Try asking:
- How many products were sold over time?
- Show the top 10 products with the highest total sales revenue along with their category and brand.
- Which product categories generated the most revenue, and how many unique customers purchased from each category?

---

## Challenges Faced

### Automatic chart detection

Since the generated SQL queries could return different column combinations every time, creating reliable charts was difficult. In several cases, visualizations were not getting generated correctly because columns were being interpreted with incorrect data types (for example, dates being treated as objects or numeric values not being detected properly).

To solve this, I repeatedly debugged and improved the datatype detection logic by dynamically converting columns into appropriate formats such as numeric and datetime whenever possible. I also refined the visualization conditions to handle different query outputs instead of assuming a fixed structure. This process involved multiple iterations of testing and debugging to make the dashboard more reliable for real-world, unpredictable SQL results.

---

## Author

Vaishnavi Sinha

- **LinkedIn**: [https://www.linkedin.com/in/vaishnavi-sinha-v2005/]
- **GitHub**: [https://github.com/Vaishnavi-020]
