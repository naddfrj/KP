import os
import base64


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def image_to_base64(path):
    full_path = os.path.join(BASE_DIR, path)

    if not os.path.exists(full_path):
        print(f"Gambar tidak ditemukan: {full_path}")
        return ""

    ext = os.path.splitext(full_path)[1].lower()

    if ext == ".png":
        mime = "image/png"
    else:
        mime = "image/jpeg"

    with open(full_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    return f"data:{mime};base64,{encoded}"


# ==========================================================
# Default Image
# ==========================================================

BRIN_LOGO = image_to_base64(
    "assets/brin_logo.png/logo_brin.jpeg"
)

USER_DEFAULT = image_to_base64(
    "assets/default_user.png/user_default.jpg"
)

# ==========================================================
# Mapping Path
# ==========================================================

image_map = {

    "abdurrakhman prasetyadi": "assets/photos/Abdurrakhman_Prasetyadi.jpg",
    "agung santosa": "assets/photos/Agung_Santosa.jpg",
    "ambar yoganingrum": "assets/photos/Ambar_Yoganingrum.jpg",
    "andi djalal": "assets/photos/Andi_Djalal.jpg",
    "andrari grahitandaru": "assets/photos/Andrari_Grahitandaru.jpg",
    "andria arisal": "assets/photos/Andria_Arisal.jpg",
    "andri fachrur": "assets/photos/Andri_Fachrur.jpg",
    "anne parlina": "assets/photos/Anne_Parlina.jpg",
    "arafat febriandirza": "assets/photos/Arafat_Febriandirza.jpg",
    "aria bisri": "assets/photos/Aria_Bisri.jpg",
    "arya adhyaksa": "assets/photos/Arya_Adhyaksa.jpg",
    "asril": "assets/photos/Asril.jpg",

    "budi nugroho": "assets/photos/Budi_Nugroho.jpg",
    "christine cecylia": "assets/photos/Christine_Cecylia.jpg",
    "devi munandar": "assets/photos/Devi_Munandar.jpg",
    "dianadewi riswantini": "assets/photos/Dianadewi_RIswantini.jpg",
    "ekasari nugraheni": "assets/photos/Ekasari_Nugraheni.jpg",
    "ekawati marlina": "assets/photos/Ekawati_Marlina.jpg",
    "elvira nurfadhilah": "assets/photos/Elvira_Nurfadhilah.jpg",
    "esa prakasa": "assets/photos/Esa_Prakasa.jpg",

    "foni agus": "assets/photos/Foni_Agus.jpg",
    "gunarso": "assets/photos/Gunarso.jpg",
    "halim hamadi": "assets/photos/Halim_Hamadi.jpg",
    "harnum": "assets/photos/Harnum.jpeg",
    "hengki muradi": "assets/photos/Hengki_Muradi.jpg",

    "iftitahu ni": "assets/photos/Iftitahu_Ni'mah.jpg",
    "ira maryati": "assets/photos/Ira_Maryati.jpg",
    "irfan asfy": "assets/photos/Irfan_Asfy.jpg",

    "kokoy siti": "assets/photos/Kokoy_Siti.jpg",
    "lindung parningotan manik": "assets/photos/Lindung_Parningotan_Manik.jpg",
    "lyla ruslana": "assets/photos/Lyla_Ruslana.jpg",

    "mohammad teduh": "assets/photos/Mohammad_Teduh.jpg",
    "muhamad jafar elly": "assets/photos/Muhamad_Jafar_Elly.jpg",
    "muhammad yudhi": "assets/photos/Muhammad_Yudhi.jpg",

    "nimas ayu": "assets/photos/Nimas_Ayu.jpg",
    "nungki dian": "assets/photos/Nungki_Dian.jpg",
    "nuraisa novia": "assets/photos/Nuraisa_Novia.jpg",

    "prabu kresna": "assets/photos/Prabu_Kresna.jpg",
    "purnomo husnul": "assets/photos/Purnomo_Husnul.jpg",

    "radhiyatul fajri": "assets/photos/Radhiyatul_Fajri.jpg",
    "rahardito dio prastowo": "assets/photos/Rahardito_Dio_Prastowo.jpg",
    "rezzy eko caraka": "assets/photos/Rezzy_Eko_Caraka.jpg",
    "ridwan suhud": "assets/photos/Ridwan_Suhud.jpg",
    "rini wijayanti": "assets/photos/Rini_Wijayanti.jpg",
    "rio nurtantyana": "assets/photos/Rio_Nurtantyana.jpg",
    "rival adrian": "assets/photos/Rival_Adrian.jpg",
    "rumadi": "assets/photos/Rumadi.jpg",

    "satrio adi priyambada": "assets/photos/Satrio_Adi_Priyambada.jpg",
    "siska pebiana": "assets/photos/Siska_Pebiana.jpg",
    "siti kania": "assets/photos/Siti_Kania.jpg",

    "tedy mutakin": "assets/photos/Tedy_Mutakin.jpg",
    "tri sampurno": "assets/photos/Tri_Sampurno.jpg",

    "wawan hendriawan": "assets/photos/Wawan_Hendriawan.jpg",
    "wiwin suwarningsih": "assets/photos/Wiwin_Suwarningsih.jpg",

    "yaniasih": "assets/photos/Yaniasih.jpg",
    "yuyun": "assets/photos/Yuyun.jpg",
    "zain saifullah": "assets/photos/Zain_Saifullah.jpg"

}


# ==========================================================
# Ubah semua path menjadi Base64 otomatis
# ==========================================================

for key in image_map:
    image_map[key] = image_to_base64(image_map[key])