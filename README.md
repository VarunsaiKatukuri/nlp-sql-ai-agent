# 📊 AI Data Analyst Dashboard (NLP → SQL)

An AI-powered analytics dashboard that converts **natural language questions into SQL queries** and visualizes insights through an **interactive analytics dashboard**.

Users can simply ask questions in plain English, and the system will automatically:

1. Understand the query using NLP
2. Convert the query into SQL
3. Fetch results from a SQLite database
4. Display insights through interactive charts

---

# 🚀 Live Deployment

This application is deployed on **Replit**.

Users can interact with the dashboard by asking natural language questions and instantly visualizing the results.

---

# 💡 Example Queries

Try asking questions like:

```
top 5 laptop sales
cheapest phone sale in hyderabad
average sales in mumbai
sales from bangalore and hyderabad
top monitor sales in delhi
```

### Example Conversion

**User Query**

```
top 5 laptop sales in bangalore
```

**Generated SQL**

```sql
SELECT * FROM sales
WHERE product='Laptop' AND city='Bangalore'
ORDER BY amount DESC
LIMIT 5
```

---

# 📊 Dashboard Features

## KPI Cards

The dashboard automatically calculates important business metrics:

- 💰 **Total Sales**
- 📈 **Average Sale**
- 🔥 **Highest Sale**
- 📊 **Total Transactions**
- 🏙 **Top Performing City**
- 🛒 **Top Selling Product**

These KPIs update dynamically based on filters and queries.

---

## Interactive Charts

The dashboard provides multiple data visualizations:

- Sales by City
- Product Distribution
- Sales Trend
- Sales Distribution
- Sales by Product
- City Revenue Share
- Top Cities Leaderboard
- City vs Product Sales Heatmap

All visualizations dynamically update based on user queries.

---

# 🧠 How the AI Works

The system follows an **NLP → SQL pipeline**:

```
User Question
      ↓
Natural Language Processing
      ↓
SQL Query Generation
      ↓
SQLite Database
      ↓
Interactive Dashboard
```

The NLP engine supports:

- fuzzy matching for spelling mistakes
- detection of cities and products
- top / lowest queries
- multi-city queries
- natural language interpretation

Example supported queries:

```
sales in banglore
cheapest laptop sale
top 10 phone sales in mumbai
sales from hyderabad and pune
```

---

# 🗂 Project Structure

```
nlp-sql-ai-agent
│
├── app.py              # Streamlit dashboard
├── database.py         # SQLite database initialization
├── generate_data.py    # Generates synthetic dataset
├── llm_interpreter.py  # Optional LLM-based interpretation
├── nlp_to_sql.py       # NLP → SQL conversion logic
├── main.py             # CLI testing interface
├── sales.csv           # Sales dataset
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/VarunsaiKatukuri/nlp-sql-ai-agent.git
```

Navigate to the project folder:

```bash
cd nlp-sql-ai-agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Run the Streamlit dashboard:

```bash
streamlit run app.py
```

The dashboard will open in your browser:

```
http://localhost:8501
```

---

# ☁️ Running on Replit

The project is configured to run on **Replit** using Streamlit.

Run command used for deployment:

```bash
streamlit run app.py --server.port 3000 --server.address 0.0.0.0
```

Dependencies are installed automatically from:

```
requirements.txt
```

---

# 🛠 Technologies Used

- Python
- Streamlit
- Plotly
- SQLite
- Pandas
- RapidFuzz (for fuzzy matching)

---

# 📌 Use Case

This project demonstrates how AI can help **non-technical users analyze data without writing SQL**.

Potential applications include:

- AI-powered Business Intelligence tools
- Data analytics assistants
- Self-service analytics platforms
- AI dashboards for business insights

---

# 🧪 Sample Queries for Testing

```
top 5 sales
cheapest laptop sale
average sales in mumbai
top phone sales in hyderabad
sales from bangalore and pune
```

---

# 🔮 Future Improvements

Possible enhancements for the project:

- Integrating Large Language Models (LLMs)
- Adding more datasets
- Supporting complex SQL queries
- AI-generated insights
- Advanced filtering and forecasting

---

# 👨‍💻 Author

**Varun Sai Katukuri**

GitHub:  
https://github.com/VarunsaiKatukuri
