import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="Alpha Core Nexus — عقارات كلاّ السّرحنا", layout="wide")

# --- Utilities
@st.cache_data
def load_properties(path="properties.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)

def format_price(p):
    return f"{p:,.0f} د.م."

# --- Load data
df = load_properties()

# --- Sidebar filters
st.sidebar.header("فلترة العقارات")
type_options = ["كل الأنواع"] + sorted(df["type"].unique().tolist())
selected_type = st.sidebar.selectbox("النوع", type_options)
locations = ["كل المناطق"] + sorted(df["location"].unique().tolist())
selected_location = st.sidebar.selectbox("المنطقة", locations)

min_price = int(df["price_mad"].min())
max_price = int(df["price_mad"].max())
price_range = st.sidebar.slider("سعر (د.م.)", min_value=min_price, max_value=max_price, value=(min_price, max_price), step=1000)

area_min = int(df["area_m2"].min())
area_max = int(df["area_m2"].max())
area_range = st.sidebar.slider("المساحة (م²)", min_value=area_min, max_value=area_max, value=(area_min, area_max), step=10)

query = st.sidebar.text_input("بحث نصي (وصف أو عنوان)")

# --- Apply filters
mask = (
    (df["price_mad"] >= price_range[0]) &
    (df["price_mad"] <= price_range[1]) &
    (df["area_m2"] >= area_range[0]) &
    (df["area_m2"] <= area_range[1])
)
if selected_type != "كل الأنواع":
    mask &= df["type"] == selected_type
if selected_location != "كل المناطق":
    mask &= df["location"] == selected_location
if query:
    mask &= df["title"].str.contains(query, case=False, na=False) | df["description"].str.contains(query, case=False, na=False)

results = df[mask].reset_index(drop=True)

# --- Main layout
st.title("قائمة العقارات — كلاّ السّرحنا")
st.markdown(f"### النتائج: {len(results)} عقار/عقارات")

# Map view (if coordinates present)
if not results.empty and {"latitude", "longitude"}.issubset(results.columns):
    map_df = results[["latitude", "longitude", "title"]].dropna()
    if not map_df.empty:
        st.subheader("موقع العقارات على الخريطة")
        st.map(map_df.rename(columns={"latitude":"lat","longitude":"lon"}), zoom=10)

st.write("---")

# Display cards
for i, row in results.iterrows():
    cols = st.columns([1, 2])
    with cols[0]:
        if row.get("images"):
            st.image(row["images"][0], use_column_width=True)
        else:
            st.write("لا توجد صورة")
    with cols[1]:
        st.subheader(f"{row['title']} — {row['type']}")
        st.write(f"**المنطقة:** {row['location']}")
        st.write(f"**المساحة:** {row['area_m2']} م²")
        st.write(f"**السعر:** {format_price(row['price_mad'])}")
        st.write(row["description"])
        st.write(f"**الحالة:** {row.get('status','متاح')}")
        contact = f"{row.get('contact_name','—')} — {row.get('contact_phone','—')}"
        st.write(f"**للاتصال:** {contact}")
        if row.get("latitude") and row.get("longitude"):
            lat, lon = row["latitude"], row["longitude"]
            st.write(f"[عرض على خرائط جوجل](https://www.google.com/maps/search/?api=1&query={lat},{lon})")
    st.write("---")

# Footer / add property note
st.sidebar.info("لإضافة عقار جديد، حرر ملف properties.json أو أضف واجهة رفع لاحقًا.")
