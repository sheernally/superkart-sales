import streamlit as st
import requests

st.title("SuperKart Sales Prediction")

# ---- IMPORTANT ----
# Replace this with your actual Render backend URL once deployed, e.g.
# "https://superkart-sales-backend.onrender.com/v1/predict"
BACKEND_URL = "https://REPLACE-WITH-YOUR-RENDER-URL.onrender.com/v1/predict"

with st.sidebar:
    st.caption("Backend endpoint (override for testing)")
    BACKEND_URL = st.text_input("API URL", value=BACKEND_URL)

# Input fields for product and store data
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area = st.number_input("Product Allocated Area", min_value=0.0, max_value=1.0, value=0.05)
Product_MRP = st.number_input("Product MRP", min_value=0.0, value=150.0)
Store_Size = st.selectbox("Store Size", ["High", "Medium", "Small"])
Store_Location_City_Type = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"])
Store_Type = st.selectbox("Store Type", ["Departmental Store", "Supermarket Type1", "Supermarket Type2", "Food Mart"])
Product_Id_char = st.selectbox("Product Id Char", ["FD", "DR", "NC"])
Store_Age_Years = st.number_input("Store Age (Years)", min_value=0, value=15, step=1)
Product_Type_Category = st.selectbox("Product Type Category", ["Perishables", "Non Perishables"])

product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_char": Product_Id_char,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category
}

if st.button("Predict", type='primary'):
    try:
        response = requests.post(BACKEND_URL, json=product_data, timeout=60)
        if response.status_code == 200:
            result = response.json()
            predicted_sales = result["Sales"]
            st.write(f"Predicted Product Store Sales Total: ₹{predicted_sales:.2f}")
        else:
            st.error(f"Error in API request: {response.status_code} — {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Could not reach the backend: {e}. "
                 f"Note: Render free-tier services sleep after inactivity and can take "
                 f"30–50s to wake up on the first request — try again in a moment.")
