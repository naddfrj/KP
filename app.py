import streamlit as st
import streamlit.components.v1 as components

from utils.preprocessing import load_data
from utils.graph_builder import build_graph
from utils.graph_visualizer import visualize_graph


# ==========================
# Konfigurasi Halaman
# ==========================

st.set_page_config(
    page_title="Dashboard Graf Kegiatan Riset",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Dashboard Graf Kegiatan Riset")
st.write(
    "Visualisasi hubungan peneliti, kelompok riset, dan kegiatan riset"
)


# ==========================
# Load Dataset
# ==========================

df = load_data()


st.success("Dataset berhasil dimuat!")


# ==========================
# Sidebar Filter
# ==========================

st.sidebar.header("🔎 Filter Data")


nama = st.sidebar.selectbox(
    "Pilih Peneliti",
    ["Semua"] + sorted(df["Nama"].unique())
)


kelompok = st.sidebar.selectbox(
    "Pilih Kelompok Riset",
    ["Semua"] + sorted(df["Kelompok Riset"].unique())
)


df_filter = df.copy()


if nama != "Semua":
    df_filter = df_filter[
        df_filter["Nama"] == nama
    ]


if kelompok != "Semua":
    df_filter = df_filter[
        df_filter["Kelompok Riset"] == kelompok
    ]



# ==========================
# KPI Dashboard
# ==========================

st.divider()

jumlah_peneliti = df_filter["Nama"].nunique()

jumlah_kelompok = df_filter["Kelompok Riset"].nunique()

jumlah_riset = df_filter["ID Riset"].nunique()

jumlah_kategori = df_filter["Kategori"].nunique()

c1, c2, c3, c4 = st.columns(4)


with c1:
    st.metric(
        "👨‍🔬 Peneliti",
        jumlah_peneliti
    )


with c2:
    st.metric(
        "🏢 Kelompok Riset",
        jumlah_kelompok
    )


with c3:
    st.metric(
        "📚 Kegiatan Riset",
        jumlah_riset
    )


with c4:
    st.metric(
        "📂 Kategori",
        jumlah_kategori
    )



# ==========================
# Ringkasan Kelompok Riset
# ==========================

st.divider()

st.subheader("📊 Ringkasan Kelompok Riset")


ringkasan = (
    df_filter.groupby("Kelompok Riset")["ID Riset"]
    .nunique()
    .reset_index()
)


ringkasan.columns = [
    "Kelompok Riset",
    "Jumlah Kegiatan Riset"
]


st.dataframe(
    ringkasan,
    use_container_width=True
)



# ==========================
# Grafik Aktivitas Riset
# ==========================

st.subheader(
    "📈 Jumlah Kegiatan Riset per Kelompok"
)


chart = (
    df_filter.groupby("Kelompok Riset")["ID Riset"]
    .nunique()
)


st.bar_chart(chart)



# ==========================
# Visualisasi Graf
# ==========================

st.divider()

st.subheader(
    "🕸️ Visualisasi Graf Kegiatan Riset"
)


G = build_graph(df_filter)

# Membuat graph.html
visualize_graph(G)

# Menampilkan graph.html
with open("graph.html", "r", encoding="utf-8") as f:
    html = f.read()

components.html(
    html,
    height=900,
    scrolling=True
)


# ==========================
# Statistik Graf
# ==========================

st.divider()

st.subheader("📌 Statistik Graf")


col1, col2 = st.columns(2)


with col1:
    st.metric(
        "Jumlah Node",
        G.number_of_nodes()
    )


with col2:
    st.metric(
        "Jumlah Edge",
        G.number_of_edges()
    )



# ==========================
# Preview Dataset
# ==========================

st.divider()

st.subheader(
    "📄 Preview Dataset"
)


st.dataframe(
    df_filter,
    use_container_width=True
)
