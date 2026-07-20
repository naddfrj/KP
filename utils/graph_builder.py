import networkx as nx
import re

from utils.image_map import image_map, BRIN_LOGO, USER_DEFAULT


# ==========================================================
# Mapping ID Riset -> Nama Kelompok Riset
# ==========================================================

kelompok_short = {
    "R027": "Digital Government",
    "R028": "HCI & Visualisation",
    "R029": "Information Retrieval",
    "R030": "Knowledge & Data Engineering",
    "R031": "Natural Language Processing"
}

# ==========================================================
# Mapping Warna
# ==========================================================

kelompok_color = {
    "Pemerintahan Digital (Digital Government)": "#1F77B4",          # Biru
    "Interaksi Manusia-Komputer dan Visualisasi (HCI & Visualisation)": "#00BCD4",     # Cyan
    "Temu Kembali Informasi (Information Retrieval)": "#2CA02C",      # Hijau
    "Rekayasa Pengetahuan dan Data (Knowledge and Data Engineering)": "#D62728",     # Merah
    "Pengolahan Bahasa Alami (Natural Language Processing)": "#9467BD" # Ungu
}

# ==========================================================
# Membersihkan nama
# ==========================================================

def normalize_name(name):

    name = name.lower()

    titles = [
        "prof.",
        "dr.",
        "drs.",
        "dra.",
        "ir.",
        "dr.eng.",
        "dr. eng.",
        "dr.dr.",
        "apt."
    ]

    for t in titles:
        name = name.replace(t, "")

    name = name.split(",")[0]

    name = re.sub(r"[^a-z\s]", "", name)

    return name.strip()


# ==========================================================
# Menentukan foto
# ==========================================================

def get_photo(name, kategori):

    if kategori == "BRIN Non-PRSDI":
        return BRIN_LOGO

    if kategori == "Eksternal BRIN":
        return USER_DEFAULT

    clean = normalize_name(name)

    for key, value in image_map.items():
        if key in clean:
            return value

    return USER_DEFAULT


# ==========================================================
# Graph
# ==========================================================

def build_graph(df):

    G = nx.Graph()

    for _, row in df.iterrows():

        riset = row["ID Riset"]
        kelompok = row["Kelompok Riset"]
        label_riset = kelompok
        warna_riset = kelompok_color.get(kelompok, "#7F8C8D")
        peneliti = row["Nama"]
        peran = row["Peran"]
        kategori = row["Kategori"]

        if not G.has_node(riset):

            G.add_node(
                riset,
                label=label_riset,
                type="riset",
                color=warna_riset,
                size=30,
                title=(
                    f"ID Riset : {riset}"
                    f"\nKelompok Riset : {kelompok}"
                )
            )

        if not G.has_node(peneliti):

            warna = "#3498DB"

            if peran.lower() == "koordinator":
                warna = "#E74C3C"

            G.add_node(
                peneliti,
                label=peneliti,
                type="peneliti",
                color=warna,
                image=get_photo(peneliti, kategori),
                size=25,
                title=(
                    f"Nama : {peneliti}"
                    f"\nKategori : {kategori}"
                    f"\nPeran : {peran}"
                )
            )

        G.add_edge(riset, peneliti)

    # Ukuran node berdasarkan degree
    for node in G.nodes():

        if G.nodes[node]["type"] == "peneliti":

            degree = G.degree(node)

            G.nodes[node]["size"] = 20 + degree * 4

            G.nodes[node]["label"] = f"{node}\n({degree})"

            G.nodes[node]["title"] += (
                f"\nJumlah Keterlibatan : {degree}"
            )

        else:

            G.nodes[node]["size"] = 28

    return G