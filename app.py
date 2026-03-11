import streamlit as st
import pandas as pd
import plotly.express as px

from database import initialize_database
from nlp_to_sql import generate_sql


# ---------- PAGE SETTINGS ----------
st.set_page_config(page_title="AI Data Analyst Dashboard", layout="wide")


# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.main {
    background-color:#eef1f7;
}

.block-container {
    border:2px solid #cbd5e1;
    padding:25px;
    border-radius:12px;
    background:white;
}

.kpi-card {
    background:white;
    padding:18px;
    border-radius:10px;
    border:2px solid #334155;
    box-shadow:0px 3px 8px rgba(0,0,0,0.08);
    text-align:center;
}

.chart-card {
    background:white;
    padding:18px;
    border-radius:10px;
    border:1.5px solid #cbd5e1;
    box-shadow:0px 2px 6px rgba(0,0,0,0.05);
}

</style>
""", unsafe_allow_html=True)


# ---------- DATABASE ----------
conn = initialize_database()


# ---------- HEADER ----------
st.title("📊 AI Data Analyst Dashboard")
st.write("Ask questions about the sales dataset using natural language.")


# ---------- LOAD DATA ----------
df_all = pd.read_sql_query("SELECT * FROM sales", conn)


# ---------- SIDEBAR ----------
st.sidebar.title("Filters")

selected_city = st.sidebar.selectbox(
    "Select City",
    ["All"] + sorted(df_all["city"].unique().tolist())
)

if selected_city != "All":
    df_all = df_all[df_all["city"] == selected_city]


# ---------- KPI SECTION ----------
st.subheader("Key Performance Indicators")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
    <h4 style="color:#374151;">Total Sales</h4>
    <h2 style="color:#2563eb;">${df_all['amount'].sum():,.0f}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
    <h4 style="color:#374151;">Average Sale</h4>
    <h2 style="color:#16a34a;">${df_all['amount'].mean():,.0f}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
    <h4 style="color:#374151;">Highest Sale</h4>
    <h2 style="color:#ea580c;">${df_all['amount'].max():,.0f}</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card">
    <h4 style="color:#374151;">Transactions</h4>
    <h2 style="color:#7c3aed;">{len(df_all)}</h2>
    </div>
    """, unsafe_allow_html=True)

st.divider()


# ---------- NLP QUERY ----------
st.subheader("Ask the AI Analyst")

question = st.text_input("Enter your question")

if st.button("Run Query"):

    sql_query = generate_sql(question)

    if sql_query is None:
        st.error("Sorry, I couldn't understand your question.")

    else:

        st.code(sql_query, language="sql")

        df = pd.read_sql_query(sql_query, conn)

        st.dataframe(df)


# ---------- DATA FOR VISUALIZATION ----------
if 'df' in locals() and not df.empty and {"city","product","amount"}.issubset(df.columns):
    viz_df = df
else:
    viz_df = df_all
st.subheader("Sales Analytics")

pastel_colors = px.colors.qualitative.Pastel


# ---------- ROW 1 ----------
col1,col2 = st.columns(2)

# Sales by City
with col1:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    city_sales = viz_df.groupby("city")["amount"].sum().reset_index()

    fig = px.bar(
        city_sales,
        x="city",
        y="amount",
        color="city",
        color_discrete_sequence=pastel_colors,
        title="Sales by City"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)


# Product Distribution
with col2:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    product_counts = viz_df["product"].value_counts().reset_index()
    product_counts.columns=["product","count"]

    fig = px.pie(
        product_counts,
        values="count",
        names="product",
        hole=0.45,
        color_discrete_sequence=pastel_colors,
        title="Product Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- ROW 2 ----------
col3,col4 = st.columns(2)

# Sales Trend
with col3:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    fig = px.line(
        viz_df,
        x="id",
        y="amount",
        markers=True,
        title="Sales Trend",
        color_discrete_sequence=pastel_colors
    )

    st.plotly_chart(fig,use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)


# Sales Distribution
with col4:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    fig = px.histogram(
        viz_df,
        x="amount",
        nbins=15,
        color_discrete_sequence=pastel_colors,
        title="Sales Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- ROW 3 ----------
col5,col6 = st.columns(2)

# Sales by Product
with col5:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    product_sales = viz_df.groupby("product")["amount"].sum().reset_index()

    fig = px.bar(
        product_sales,
        x="product",
        y="amount",
        color="product",
        color_discrete_sequence=pastel_colors,
        title="Sales by Product"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)


# City Revenue Share
with col6:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    city_sales = viz_df.groupby("city")["amount"].sum().reset_index()

    fig = px.pie(
        city_sales,
        values="amount",
        names="city",
        hole=0.55,
        color_discrete_sequence=pastel_colors,
        title="City Revenue Share"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- ROW 4 ----------
col7,col8 = st.columns(2)

# Top Cities Leaderboard
with col7:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    city_sales = viz_df.groupby("city")["amount"].sum().reset_index()
    city_sales = city_sales.sort_values("amount", ascending=False)

    fig = px.bar(
        city_sales,
        x="amount",
        y="city",
        orientation="h",
        color="city",
        color_discrete_sequence=pastel_colors,
        title="Top Cities by Sales"
    )

    fig.update_layout(yaxis={'categoryorder':'total ascending'})

    st.plotly_chart(fig,use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)


# Heatmap
with col8:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)

    pivot_table = viz_df.pivot_table(
        values="amount",
        index="city",
        columns="product",
        aggfunc="sum",
        fill_value=0
    )

    fig = px.imshow(
        pivot_table,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Blues",
        title="City vs Product Sales Heatmap"
    )

    st.plotly_chart(fig,use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)