import pandas as pd 
import streamlit as st 
# st.header("Dashboard")
# # Load data from data folder
# def load_data():
#   sales = pd.read_csv("data/sales.csv")
#   products = pd.read_csv("data/products.csv")
#   inventory = pd.read_csv("data/inventory.csv")
#   suppliers = pd.read_csv("data/suppliers.csv")
  
# # ------------------------------------------------
# #  1. Data Ingestion (Reading Multiple CVSs)
# # -------------------------------------------------
  
#   return ( sales, products, inventory, suppliers)

# sales, products, inventory, suppliers = load_data()


# # display loaded data in terminal 
# print("\n****************** Original data files, sales, products, inventory, suppliers")
# # print(sales.head())
# # print(products.head())
# # print(inventory.head())
# # print(suppliers.head())

# # --------------------------------------------------
# #  2. Data Cleaning & Preparation 
# # --------------------------------------------------

# # Standarding column names
# for df in [sales, products, inventory, suppliers]:
#   df.columns.str.strip().str.lower()

# # ensure data column exists
# date_col = "date_of_sale" if "date_of_sale" in sales.columns else "date"
# if date_col not in sales.columns:
#   print("Date should be recorded")
#   exit()

# # Convert to datetime (with coercing invalid values)
# sales["date_of_sale"] = pd.to_datetime(sales[date_col], errors="coerce", dayfirst=True)

# # Drop rows and with invalid or missing dates
# sales.dropna(subset=[date_col], inplace=True)


# # Standardize medicine names (important merging)
# sales["medicine"] = sales["medicine"].astype(str).str.strip().str.title()
# products["medicine"] = products["medicine"].astype(str).str.strip().str.title()


# # Remove duplicates
# sales.drop_duplicates(inplace=True)



# # Flat File Format

# #  Merge all datasets - pandas relations joins

# merged = sales.merge(products, on="medicine", how="left")
# merged = merged.merge(inventory, on="medicine", how="left")
# merged = merged.merge(suppliers, on="supplier_id", how="left")

# print("\n************************ Merged: Sales + Products + Inventory + Suppliers")
# print(merged.head())



# @st.cache_data
# def load_data():
#     sales = pd.read_csv("data/sales.csv")
#     products = pd.read_csv("data/products.csv")
#     inventory = pd.read_csv("data/inventory.csv")
#     suppliers = pd.read_csv("data/suppliers.csv")

#     return (sales, products, inventory, suppliers)

# # -------------------------------------------------------
# # 1. Data Ingestion (Reading Multiple CSVs)
# # -------------------------------------------------------

# sales, products, inventory, suppliers = load_data()

# # print("\n****************** Original data files: sales, products, inventroy, suppiler")
# # print(sales.head())
# # print(products.head())
# # print(inventory.head())
# # print(suppliers.head())

# # -------------------------------------------------------
# # 1. Data Cleaning & Preparation
# # -------------------------------------------------------

# # standardizing column names
# for df in [sales, products, inventory, suppliers]:
#     df.columns = df.columns.str.strip().str.lower()

# # ensure date column exits
# date_col = "date_of_sale" if "date_of_sale"  in sales.columns else "date"
# if date_col not in sales.columns:
#     print("Date should be recorded")
#     exit()

# # Convert to datetime (with coercing invalid values)
# sales[date_col] = pd.to_datetime(sales[date_col], errors="coerce", dayfirst=True)

# # drop rows with invalid or missing dates
# sales.dropna(subset=[date_col], inplace=True)

# # standardize medicine names (important for merging)
# sales["medicine"] = sales["medicine"].astype(str).str.strip().str.title()
# products["medicine"] = products["medicine"].astype(str).str.strip().str.title()

# # Remove duplicates
# sales.drop_duplicates(inplace=True)

# # Flat File Format
# # Merge all datasets - panads relations joins
# merged = sales.merge(products, on='medicine', how="left")
# merged = merged.merge(inventory, on='medicine', how="left")
# merged = merged.merge(suppliers, on='supplier_id', how="left")
# merged.rename(columns={date_col: "date"}, inplace=True)

# # print("\n****************** merged: sales + products + inventry + suppliers")
# print(merged.head())

# st.set_page_config(
#   page_title=" Pharma Sales Dashboard",
#   page_icon="⚙️",
#   layout="wide"
# )

# st.title("Pharma Retail Sales & Inventory Intelligence Dashboard ")
# st.markdown("Analyze sales performance, Inventory levels, and suppliers info in retails pharmcy chains")

# # -----------------------
# #  Sidebar
# # -----------------------

# st.sidebar.header("🔎Filter your Views")

# min_date = merged["date"].min().date()
# max_date = merged["date"].max().date()


# date_range = st.sidebar.slider(
#   "Select Date Range",
#   min_value= min_date,
#   max_value = max_date,
#   value=(min_date, max_date)
  
# )

# filtered = merged[
#   (merged["date"].dt.date >= date_range[0]) & (merged["date"].dt.date <= date_range[1])
# ]
# print(filtered)

# #  Category Filter
# category = st.sidebar.selectbox(
#   "Select Medicine Category",
#   options= ["All"] + sorted(filtered["category"].dropna().unique().tolist())
# )

# print(category)

# if category != "All":
#   filtered = filtered[filtered["category"] == category]
  
# # print(filtered.head())

# branch = st.sidebar.selectbox(
#   "Select Branch Region",
#   options=["All"] + sorted(filtered["branch"].dropna().unique().tolist())
# )

# if branch != "All":
#   filtered = filtered[filtered["branch"]== branch]
  
# print(branch)
# print(filtered.head())


@st.cache_data
def load_data():
    sales = pd.read_csv("data/sales.csv")
    products = pd.read_csv("data/products.csv")
    inventory = pd.read_csv("data/inventory.csv")
    suppliers = pd.read_csv("data/suppliers.csv")

    return (sales, products, inventory, suppliers)

# -------------------------------------------------------
# 2. Stream Page Config
# -------------------------------------------------------
st.set_page_config(
    page_title="Pharma Sales Dashboard",
    page_icon="⚙️",
    layout="wide"
)
st.title("⚙️ Pharma Retail Sales & Imventory Intelligence Dashboard")
st.markdown("Analyze sales performance, Inventory levels, and suppliers info in retail pharamcy chians")

# -------------------------------------------------------
# 1. Data Ingestion (Reading Multiple CSVs)
# -------------------------------------------------------

sales, products, inventory, suppliers = load_data()

# print("\n****************** Original data files: sales, products, inventroy, suppiler")
# print(sales.head())
# print(products.head())
# print(inventory.head())
# print(suppliers.head())

# -------------------------------------------------------
# 1. Data Cleaning & Preparation
# -------------------------------------------------------

# standardizing column names
for df in [sales, products, inventory, suppliers]:
    df.columns = df.columns.str.strip().str.lower()

# ensure date column exits
date_col = "date_of_sale" if "date_of_sale"  in sales.columns else "date"
if date_col not in sales.columns:
    print("Date should be recorded")
    exit()

# Convert to datetime (with coercing invalid values)
sales[date_col] = pd.to_datetime(sales[date_col], errors="coerce", dayfirst=True)

# drop rows with invalid or missing dates
sales.dropna(subset=[date_col], inplace=True)

# standardize medicine names (important for merging)
sales["medicine"] = sales["medicine"].astype(str).str.strip().str.title()
products["medicine"] = products["medicine"].astype(str).str.strip().str.title()

# Remove duplicates
sales.drop_duplicates(inplace=True)

# Flat File Format [300 rows x 19 columns]
# Merge all datasets - panads relations joins
merged = sales.merge(products, on='medicine', how="left")
merged = merged.merge(inventory, on='medicine', how="left")
merged = merged.merge(suppliers, on='supplier_id', how="left")

merged.rename(columns={date_col: "date"}, inplace=True)

# print("\n****************** merged: sales + products + inventry + suppliers")
# print(merged.head())

# -------------------------------------------------------
# 3. Sidebar Filters
# -------------------------------------------------------
st.sidebar.header("🔎 Filter Your View")

min_date = merged["date"].min().date()
max_date = merged["date"].max().date()

# date range selector
date_range = st.sidebar.slider(
    "Select Date Range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date)
)

print(date_range)
filtered = merged[
    (merged["date"].dt.date >= date_range[0]) &
    (merged["date"].dt.date <= date_range[1])
]

# print(filtered.head())

# Category Filter
category = st.sidebar.selectbox(
    "Select Medicine Category",
    options= ["All"] + sorted(filtered["category"].dropna().unique().tolist())
)

print(category)

if category != "All":
    filtered =  filtered[filtered["category"] == category]

# print(filtered.head())

 # Branch Filter
branch = st.sidebar.selectbox(
    "Select Branch",
    options= ["All"] + sorted(filtered["branch"].dropna().unique().tolist())
)

if branch != "All":
    filtered =  filtered[filtered["branch"] == branch]

print(branch)
print(filtered.head())
