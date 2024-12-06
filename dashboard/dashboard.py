import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import BytesIO

sns.set(style='dark')
# Color palette
color_palette = sns.color_palette("ch:s=.25,rot=-.25")

# visualisasi dashboard
st.markdown(
    """
    # :hotel: Hotel's Pricing Dashboard :hotel:
    """
)

# helper function (visualisasi categorical features)
def chart_for_cat(df, cat):

    # deskripsi
    st.subheader(f"Distribusi Data {cat}")

    # univariate analysis
    fig, ax = plt.subplots(figsize=(12,8))

    # Barplot untuk kategori
    sns.barplot(
        x=df[cat].value_counts().index,
        y=df[cat].value_counts().values,
        palette=color_palette,
        ax=ax
    )
    ax.set_xlabel(cat, fontsize=18, color="white")
    ax.tick_params(axis='y', labelsize=14, colors="white")
    ax.tick_params(axis='x', labelsize=14, colors="white")
    if len(df[cat].value_counts()) > 5:
        ax.tick_params(axis='x', labelsize=14, colors="white", labelrotation=90)
    ax.set_facecolor('none')
    for spine in ax.spines.values():
        spine.set_visible(False)
    plt.tight_layout()

    # Simpan grafik ke buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png', transparent=True)
    buffer.seek(0)
    st.image(buffer)

    # hasil EDA setiap fitur
    if cat == 'property_type':
        st.markdown("""
        Terdapat **19 kategori** pada fitur Property Type. Dari data persentase dapat disimpulkan bahwa sebagian besar orang lebih memilih memesan **kamar apartment (66.1%)** atau **rumah (22.3%)**.
        """)
    elif cat == 'room_type':
        st.markdown("""
        Terdapat **3 kategori** pada fitur Room Type. Dari data persentase dapat disimpulkan bahwa sebagian besar orang lebih memilih memesan **entire home/apt (55.7%)** atau **private room (41.3%)**.
        """)
    elif cat == 'bed_type':
        st.markdown("""
        Terdapat **5 kategori** pada fitur Bed Type, secara berurutan dari jumlahnya yang paling banyak yaitu Real Bed, Fution, Pull-out Sofa, Airbed, dan Couch. Dari data persentase dapat disimpulkan bahwa sebagian besar property memiliki tempat tidur berjenis **real bed (97.2%)**. Persentase ini sangat berbeda jauh dengan tipe tempat tidur lainnya dengan rata-rata hanya **0.7%**.
        """)
    elif cat == 'cancellation_policy':
        st.markdown("""
        Terdapat **4 kategori** pada fitur Cancellation Policy, secara berurutan dari jumlahnya yang paling banyak yaitu Strict, Flexible, Moderate, dan Super Strict. Dari data persentase dapat disimpulkan bahwa sebagian besar property memiliki aturan pembatalan yang cukup ketat atau **strict (43.7%)**. Namun, terdapat beberapa property yang memberlakukan aturan pembatalan yang **flexible (30.4%)** dan **moderate(25.7%)**. Properti yang menetapkan aturan pembatalan** sangat ketat** hanya sebagian kecil dari keseluruhan properti yang ada **(0.2%)**.
        """)
    elif cat == 'city':
        st.markdown("""
        Pada dataset Airbnb Price, terdapat **6 kategori** kota yang dianalisis, secara berurutan dari jumlahnya yang paling banyak yaitu NYC (New York City), LA (Los Angeles), SF (San Fransisco), DC (District of Columbia), Chicago, dan Boston. Dari data persentase dapat disimpulkan bahwa sebagian besar property berada di kota **NYC (43.6%)** dan LA **(30.3%)**.
        """)
    elif cat == 'host_identity_verified':
        st.markdown(""""
        Terdapat **2 kategori** pada fitur Host Identify Verified, secara berurutan dari jumlahnya yang paling banyak yaitu True dan False. Dari data persentase dapat disimpulkan bahwa **67.4%** pemilik properti telah memverifikasi identitas mereka, sedangkan **32.6%** lainnya belum memverifikasi identitas mereka.
        """)
    elif cat == 'instant_bookable':
        st.markdown("""
        Terdapat **2 kategori** pada fitur Instant Bookable, secara berurutan dari jumlahnya yang paling banyak yaitu False dan True. Dari data persentase dapat disimpulkan bahwa **73.8%** properti tidak dapat dipesan tanpa persetujuan pemilik, sedangkan **26.2%** lainnya dapat dipesan secara instan tanpa harus menunggu persetujuan pemilik.  
        """)
    else: # cat = cleaning_fee
        st.markdown("""
        Terdapat **2 kategori** pada fitur Cleaning Fee, secara berurutan dari jumlahnya yang paling banyak yaitu True dan False. Dari data persentase dapat disimpulkan bahwa **73.4%** properti memberlakukan tarif untuk kebersihan, sedangkan **26.6%** lainnya tidak memberlakukan tarif untuk kebersihan.  
        """)

    # deskripsi violion chart
    st.subheader(f"Variasi Harga pada Tiap Kategori {cat}")

    # Multivariate analysis
    fig, ax = plt.subplots(figsize=(12,8))

    sns.violinplot(
        x=df[cat],
        y=df['log_price'],
        palette=color_palette,
        ax=ax
    )

    ax.set_xlabel(cat, fontsize=18, color="white")
    ax.set_ylabel("log_price", fontsize=18, color="white")
    ax.tick_params(axis='y', labelsize=14, colors="white")
    ax.tick_params(axis='x', labelsize=14, colors="white")
    if len(df[cat].value_counts()) > 5:
        ax.tick_params(axis='x', labelsize=14, colors="white", labelrotation=90)
    ax.set_facecolor('none')
    for spine in ax.spines.values():
        spine.set_visible(False)
    plt.tight_layout()

    # Simpan grafik ke buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png', transparent=True)
    buffer.seek(0)
    st.image(buffer)

    # hasil EDA setiap fitur
    if cat == 'property_type':
        st.markdown("""
        Dari visualisasi tersebut diketahui bahwa median properti tipe **Timeshare** merupakan yang **paling tinggi**, sedangkan **Hostel** memiliki median yang **paling rendah**. Hal ini menunjukkan bahwa harga Timeshare cenderung lebih tinggi dibanding harga tipe properti lainnya.
        """)
    elif cat == 'room_type':
        st.markdown("""
        Dari visualisasi tersebut diketahui bahwa ruangan bertipe **Entire home/apt** memiliki median yang **paling tinggi** dibandingkan tipe ruang lainnya. Sedangkan ruangan bertipe **Shared room** memiliki median yang **paling rendah**. Hal ini menunjukkan bahwa harga tipe ruangan entire home/apt cenderung lebih tinggi, sedangkan harga tipe ruangan shared room cenderung rendah.
        """)
    elif cat == 'bed_type':
        st.markdown("""
        Dari visualisasi tersebut diketahui bahwa tempat tidur bertipe **Real bed** memiliki median yang **paling tinggi** dibandingkan tipe tempat tidur lainnya. Sedangkan tempat tidur bertipe **Futon** dan **Couch** memiliki median yang **paling rendah**. Namun, dalam visualisasi tersebut perbedaan median antar setiap tipe tempat tidur tidak terlalu besar. Hal ini menunjukkan bahwa setiap tipe tempat tidur memiliki harga yang cenderung sama.
        """)
    elif cat == 'cancellation_policy':
        st.markdown("""
        Dari visualisasi tersebut diketahui bahwa properti yang menerapkan aturan pembatalan **super ketat (super strict)** memiliki median yang **paling tinggi**. Hal ini menunjukkan bahwa setiap properti yang menerapkan aturan pembatalan sangat ketat memiliki harga yang cenderung tinggi jika dibandingkan dengan properti yang menerapkan aturan pembatalan berbeda.
        """)
    elif cat == 'city':
        st.markdown("""
        Dari visualisasi tersebut diketahui bahwa properti yang berada di kota **San Fransisco** memiliki median yang **paling tinggi**. Hal ini menunjukkan bahwa properti yang berada di San Fransisco memiliki harga yang cenderung tinggi jika dibandingkan dengan properti di kota-kota lain.
        """)
    elif cat == 'host_identity_verified':
        st.markdown(""""
        Dari visualisasi tersebut diketahui bahwa properti dengan **pemilik yang sudah terverifikasi** memiliki median yang **lebih tinggi** dibading properti dengan **pemilik yang tidak terverifikasi**. Namun, visualisasi tersebut juga menunjukkan bahwa perbedaan median antara kedua kategori tersebut tidak terlalu besar, sehingga menimbulkan interpretasi bahwa harga untuk kedua kategori tersebut cenderung sama.
        """)
    elif cat == 'instant_bookable':
        st.markdown("""
        Dari visualisasi tersebut diketahui bahwa properti dengan kebjikan **instant booking** dan kebijakan **non-instant booking** memiliki median yang cenderung sama. Hal ini menunjukkan bahwa harga untuk kedua kategori tersebut cenderung sama.  
        """)
    else: # cat = cleaning_fee
        st.markdown("""
        Dari visualisasi tersebut diketahui bahwa properti yang **menerapkan tarif untuk kebersihan** memiliki median yang **lebih tinggi** dibandingkan **properti yang tidak menerapkan tarif untuk kebersihan**. Hal ini menunjukkan bahwa harga untuk properti yang menerapkan tarif kebersihan cenderung lebih tinggi.  
        """)

# helper function (visualisasi numerical features)
def chart_for_num(df, num):
    # deskripsi
    st.subheader(f"Distribusi Data {num}")

    col1, col2 = st.columns(2)

    # distribusi bar chart
    with col1:
        fig, ax = plt.subplots()

        sns.histplot(
            data=df,
            x=df[num],
            color='skyblue',
            ax=ax
        )

        ax.set_xlabel(num, fontsize=18, color="white")
        ax.tick_params(axis='y', labelsize=14, colors="white")
        ax.tick_params(axis='x', labelsize=14, colors="white")
        ax.set_facecolor('none')
        for spine in ax.spines.values():
            spine.set_visible(False)
        plt.tight_layout()

        # Simpan grafik ke buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png', transparent=True)
        buffer.seek(0)
        st.image(buffer)

    # outlier box plot
    with col2:
        fig, ax = plt.subplots()

        sns.boxplot(
            data=df,
            x=df[num],
            color='skyblue',
            ax=ax
        )

        ax.set_xlabel(num, fontsize=18, color="white")
        ax.tick_params(axis='y', labelsize=14, colors="white")
        ax.tick_params(axis='x', labelsize=14, colors="white")
        ax.set_facecolor('none')
        for spine in ax.spines.values():
            spine.set_visible(False)
        plt.tight_layout()

        # Simpan grafik ke buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png', transparent=True)
        buffer.seek(0)
        st.image(buffer)
    
    # hasil EDA setiap fitur
    if num == 'log_price':
        st.markdown("""
        Terlihat distribusi yang cenderung **condong ke kanan (right skewed)**. Hal tersebut menunjukkan banyak properti dengan harga realtif rendah, namun ada beberapa properti dengan harga yang sangat tinggi. Dari visualisasi boxplot diketahui apakah fitur tersebut memiliki outlier.
        """)
    elif num == 'amenities':
        st.markdown("""
        Sebagian besar properti memiliki jumlah fasilitas yang relatif sedikit, namun terdapat beberapa properti dengan jumlah yang sangat banyak. Hal ini menunjukkan adanya variasi yang cukup besar dalam hal fasilitas yang ditawarkan oleh setiap properti. Dari visualisasi boxplot diketahui apakah fitur tersebut memiliki outlier.
        """)
    elif num == 'accommodates':
        st.markdown("""
        Sebagian besar properti dapat menampung jumlah tamu yang relatif sedikit. Hal ini menunjukkan bahwa banyak properti yang cocok untuk individu atau kelompok kecil.
        """)
    elif num == 'bathrooms':
        st.markdown("""
        Sebagian besar properti memiliki jumlah kamar mandi yang sedikit. Visualisasi histogram tersebut menunjukkan properti yang memiliki satu atau dua kamar mandi adalah yang paling umum.
        """)
    elif num == 'host_response_rate':
        st.markdown("""
        Sebagian besar pemilik properti memiliki tingkat respons yang tinggi.
        """)
    elif num == 'number_of_reviews':
        st.markdown("""
        Sebagian besar properti memiliki jumlah ulasan yang relatif sedikit. Hal tersebut mengindikasikan beberapa properti mungkin merupakan properti baru atau kurang populer.
        """)
    elif num == 'review_scores_rating':
        st.markdown("""
        Sebagian besar properti memiliki skor ulasan yang cukup tinggi. Hal ini menunjukkan bahwa kualitas properti secara umum cukup baik.  
        """)
    elif num == 'bedrooms':
        st.markdown("""
        Sebagian besar properti memiliki jumlah kamar tidur yang sedikit. Hal ini sejalan dengan kapasitas properti yang juga cukup rendah dan cocok untuk menampung individu atau kelompok kecil.
        """)
    else: # num = beds
        st.markdown("""
        Sebagian besar properti memiliki jumlah tempat tidur yang sedikit. Hal ini juga sejalan dengan temuan sebelumnya tentang jumlah kamar tidur, jumlah kamar mandi, dan kapasitas tamu.  
        """)

    # deskripsi violion chart
    st.subheader(f"Hubungan {num} dengan Harga Sewa")

    # pair plot num vs log_price
    fig, ax = plt.subplots(figsize=(12,6))
        
    sns.scatterplot(
        x=df[num],
        y=df['log_price'],
        color='skyblue',
        ax=ax
    )

    ax.set_xlabel(num, fontsize=18, color="white")
    ax.set_ylabel('log_price', fontsize=18, color="white")
    ax.tick_params(axis='y', labelsize=14, colors="white")
    ax.tick_params(axis='x', labelsize=14, colors="white")
    ax.set_facecolor('none')
    for spine in ax.spines.values():
        spine.set_visible(False)
    plt.tight_layout()

    # Simpan grafik ke buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png', transparent=True)
    buffer.seek(0)
    st.image(buffer)

    # correlation value num vs log_price
    choosen = [num, 'log_price']

    # Pastikan kedua kolom ada di DataFrame
    if all(col in df.columns for col in choosen):
        if num == 'log_price':
            return None
        else:
            correlation_matrix = df[choosen].corr()
                
            # Validasi untuk memastikan matriks korelasi memiliki nilai
            if not correlation_matrix.empty:
                # Ambil nilai korelasi antara kedua kolom
                correlation_value = correlation_matrix.loc[num, 'log_price']
                    
                # Tampilkan nilai korelasi dalam 
                st.write(f"Korelasi antara kolom {num} dan log_price adalah {round(correlation_value, 2)}")
                if num == 'log_price':
                    return None
                elif num == 'amenities':
                    st.markdown("""
                    Nilai tersebut menunjukkan adanya **korelasi positif lemah** dengan log_price. Hal ini menunjukkan bahwa semakin banyak fasilitas yang tersedia pada suatu properti, harganya akan cendrung sedikit lebih tinggi. Namun, hubungan ini tidak terlalu kuat.
                    """)
                elif num == 'accommodates':
                    st.markdown("""
                    Nilai tersebut menunjukkan adanya **korelasi positif sedang** dengan log_price. Hal ini menunjukkan bahwa semakin banyak orang yang bisa ditampung pada suatu properti, harganya akan cendrung lebih tinggi. Hal tersebut sejalan dengan semakin besar ukuran properti maka harga sewanya akan semakin tinggi.
                    """)
                elif num == 'bathrooms':
                    st.markdown("""
                    Nilai tersebut menunjukkan adanya **korelasi positif sedang** dengan log_price. Hal ini menunjukkan bahwa semakin banyak kamar mandi pada suatu properti, sehingga harga sewanya akan semakin tinggi.
                    """)
                elif num == 'host_response_rate':
                    st.markdown("""
                    Nilai tersebut menunjukkan adanya **korelasi sangat lemah** (mendekati nol) dengan log_price. Hal ini menunjukkan bahwa tingkat respon pemilik properti tidak memiliki pengaruh yang signifikan terhadap harga properti.
                    """)
                elif num == 'number_of_reviews':
                    st.markdown("""
                    Nilai tersebut menunjukkan adanya **korelasi negatif sangat lemah** dengan log_price. Hal ini menunjukkan bahwa banyaknya ulasan tidak hubungan yang jelas dengan harga sewa yang ditetapkan.
                    """)
                elif num == 'review_scores_rating':
                    st.markdown("""
                    Nilai tersebut menunjukkan adanya **korelasi positif sangat lemah** dengan log_price. Hal ini menunjukkan bahwa skor ulasan memiliki sedikit pengaruh positif terhadap penentuan harga sewa, namun dengan hubungan yang sangat lemah.  
                    """)
                elif num == 'bedrooms':
                    st.markdown("""
                    Nilai tersebut menunjukkan adanya **korelasi positif sedang** dengan log_price. Hal ini menunjukkan bahwa semakin banyak kamar tidur, semakin tinggi harganya.
                    """)
                else: # num = beds
                    st.markdown("""
                    Nilai tersebut menunjukkan adanya **korelasi positif sedang** dengan log_price. Hal ini menunjukkan bahwa semakin banyak tempat tidur, maka harga sewa properti akan cenderung lebih tinggi. Hal ini sejalan dengan hasil interpretasi jumlah kamar mandi, jumlah kamar tidur, dan kapasitas properti.  
                    """)
            else:
                st.error("Matriks korelasi kosong. Periksa apakah data memiliki nilai yang valid.")
    else:
        st.error("Kolom yang dipilih tidak ditemukan dalam DataFrame.")

# halaman pertama
def page1():
    st.title("Overview Data")

    # load data Airbnb
    df = pd.read_csv("https://raw.githubusercontent.com/afifahrahma22/hotel_price_prediction/main/data/Airbnb_clean_data.csv")

    kolom = st.selectbox("Filter berdasarkan kolom:", df.columns)
    cat_column = df.select_dtypes(include=['object', 'bool'])
    num_column = df.select_dtypes(include=['number'])

    if kolom in cat_column:
        chart_for_cat(df, kolom)
    else:
        chart_for_num(df, kolom)

# halaman kedua
def page2():
    st.title("Hasil Pemodelan Analitik")

    st.subheader("Evaluasi Metrik pada Test Set")

    # data evaluasi metrik linear regression, decision tree, dan random forest
    eval_metrics = {
        'Model': ['LinearRegression', 'DecisionTreeRegressor', 'RandomForestRegressor'],
        'MAE': [0.357642, 0.364427, 0.360036],
        'RMSE': [0.473351, 0.482769, 0.476035]
    }
    df = pd.DataFrame(eval_metrics)

    # custom tampilan tabel
    st.markdown(
        """
        <style>
        .css-k1ih3n {
            font-family: "Arial", sans-serif;
            color: #FFFFFF;
        }
        .dataframe th, .dataframe td {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # tampilkan tabel
    st.dataframe(df)

    # deskripsi evaluasi metrik
    st.markdown("""
    Output di atas menunjukkan bahwa nilai mean absolute error (MAE) yang dimiliki ketiga model pada test set juga *tidak berbeda jauh satu sama lain*. Secara berurutan, model yang memiliki nilai MAE terkecil hingga terbesar adalah: `LinearRegression`, `RandomForestRegressor`, dan `DecisionTreeRegressor`.
    """)

    st.subheader("Perbandingan Hasil Prediksi Model")
    st.write("Berikut adalah beberapa sampel data pada test set")

    # tabel perbandingan dan difference
    # contoh data
    data = {
        'Actual': [5.010635, 5.129899, 4.976734, 6.620073, 4.744932],
        'LinearRegression': [4.393626, 4.122584, 3.588877, 3.706106, 3.616253],
        'DecisionTreeRegressor': [4.499362, 4.292741, 3.828294, 3.370806, 3.370806],
        'RandomForestRegressor': [4.397259, 4.280040, 3.605742, 3.762488, 3.651317]
    }
    df_diff = pd.DataFrame(data)
    st.dataframe(df_diff)

    st.write("Berikut adalah hasil tabulasi data aktual, prediksi, dan perbedaan antara prediksi dan aktual")
    # akurasi setiap model
    correctness = {
        'Metrik': ['MAE', 'MAE/Mean Ratio', 'Correctness'],
        'LinearRegression': [0.3576416411972841, '7.48%', '92.52%'],
        'DesionTreeRegressor': [0.3644265617728542, '7.62%', '92.38%'],
        'RandomForestRegressor': [0.36003562996445976, '7.53%', '92.47%']
    }
    df_correct = pd.DataFrame(correctness)
    st.dataframe(df_correct)

    st.markdown("""
    Dengan membandingkan ketiga model tersebut dapat disimpulkan bahwa model **Linear Regression** memiliki ketepatan paling tinggi yaitu **92.52%**. Namun, hasil tersebut tidak berbeda jauh satu sama lain dengan ketepatan model **Random Forest 92.47%** dan model **Decision Tree 92.38%**.
    """)

    st.subheader("Fitur Paling Berpengaruh")

    col1, col2 = st.columns(2)

    with col1:

        st.write("Fitur Penting untuk Model Decision Tree")
        # Fitur yang paling berpengaruh Decision Tree
        important = {
            'Fitur': ['room_type_Entire home/apt', 'bathrooms', 'bedrooms', 'city_SF', 'number_of_reviews'],
            'Value': [0.657, 0.2037, 0.0319, 0.0273, 0.0256]
        }
        df_dt = pd.DataFrame(important)
        st.dataframe(df_dt)

    with col2:
        st.write("Fitur Penting untuk Model Random Forest")
        # Fitur yang paling berpengaruh Random Forest
        important_2 = {
            'Fitur': ['room_type_Entire home/apt', 'room_type_Private room', 'bedrooms', 'accommodates', 'bathrooms'],
            'Value': [0.3628, 0.2172, 0.123, 0.0997, 0.0799]
        }
        df_rf = pd.DataFrame(important_2)
        st.dataframe(df_rf)
    
    st.markdown("""
    Dari hasil pemodelan menggunakan model Decision Tree dan Random Forest, fitur **room_type_Entire home/apt** menjadi fitur yang paling berkontribusi dalam prediksi harga hotel.
    """)

    
# sidebar
with st.sidebar:
    st.image("https://raw.githubusercontent.com/afifahrahma22/hotel_price_prediction/main/image/Airbnb_Logo.png") 
    st.subheader("Selamat datang di Final Projek Big Data - Hotel's Pricing Prediction")

    st.write(
        """
        \U0001F464 **Nama**: Dzakiyyah Afifah Rahma \n
        \U0001F194 **NIM**: 215150701111027 \n
        :ledger: **Kelas**: Big Data dan Analitik - A\n  
        """
    )

    page = st.selectbox("Pilih halaman untuk dikunjungi", ("Overview Data", "Pemodelan Analitik"))

if page == "Overview Data":
    page1()
elif page == "Pemodelan Analitik":
    page2()
