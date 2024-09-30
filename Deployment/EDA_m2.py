import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.title('AutoShop Customer Churn Management')
    st.sidebar.title('About this page')
    st.sidebar.write('AutoShop adalah marketplace otomotif yang memanfaatkan kekuatan data untuk memberikan pelayanan terbaik. Tim data kami secara aktif menganalisis perilaku pengguna untuk mengidentifikasi tren, preferensi, dan potensi masalah. Salah satu fokus utama kami adalah mencegah churn, yaitu ketika pelanggan berhenti menggunakan aplikasi. Dengan memprediksi pelanggan mana yang berpotensi churn, kami dapat mengambil tindakan proaktif seperti memberikan penawaran khusus atau meningkatkan kualitas layanan pelanggan')
    _, cent_co, _ = st.columns(3)
    with cent_co:
        st.image(
            'https://static.vecteezy.com/system/resources/thumbnails/010/596/991/small/auto-shop-logo-isolated-on-black-background-vector.jpg'
        )
    st.write(
        'AutoShop adalah sebuah aplikasi marketplace yang hanya menjual barang-barang yang berhubungan dengan automotif, '
        'Seperti Sabun mobil, Aksesoris, dan semacamnya. Demi meningkatkan kualitas aplikasi AutoShop, tim data analis '
        'dari AutoShop berusaha mengidentifikasi kemungkinan pelanggan AutoShop untuk berhenti menggunakan AutoShop '
        'dan bekerja sama dengan tim marketing untuk memberikan insentif atau bantuan pada pelanggan yang memiliki '
        'kemungkinan berhenti yang tinggi.'
    )

    # st.subheader('Data Set')
    Data_eda = pd.read_csv('data_automotive.csv')
    # st.dataframe(Data_eda)

    st.subheader('Data Visualisasi')
    st.write('# 1. Churn Score Distribution')
    fig = plt.figure(figsize=(6, 6))
    churn_score_counts = Data_eda['churn_score'].value_counts()
    plt.pie(
        churn_score_counts.values,
        labels=churn_score_counts.index,
        autopct='%1.1f%%'
    )
    plt.title('Churn Score Distribution')
    st.pyplot(fig)
    st.write('Berdasarkan distribusi churn_score diatas, kita dapat mengetahui bahwa lebih banyak pelanggan yang memiliki kemungkinan churn tinggi dibandingkan yang memiliki kemungkinan churn rendah, oleh karena itu kita akan melakukan analisi kepada beberapa data dan keterhubungannya dengan churn_score.')

    st.write('# 2. Relation between membership_category and churn_score')
    f = plt.figure(figsize=(6, 6))
    sns.despine(f)
    sns.histplot(
        x=Data_eda['churn_score'],
        hue=Data_eda['membership_category'],  # Pass the column as a string
        multiple='stack')
    st.pyplot(f)
    st.write('Dari diagram diatas,kita dapat melihat data yang memiliki kemungkinan churn tingg yaitu pada churn_score 3 hingga 5 memiliki membership yang bervariasi. namun untuk yang memiliki chrun_scorre tertinggi hanya berasal dari 2 kategori yaitu No membership dan basic membership. hal tersebut bisa terjadi karena no membership dan basic membership pastinya tidak memiliki pelayanan yang sebalik membership diatasnya. Namun disebabkan  No membership dan basic membership memiliki presentase yang tinggi di persebaran membership, maka harus ada tindakan khusus untuk mengatasi churn_score tinggi tersebut.')

    st.write('# 3. Churn Score Distribution based on avg_transaction_value')
    f = plt.figure(figsize=(6, 6))
    x = Data_eda['avg_transaction_value']
    y1 = Data_eda['churn_score']
    sns.barplot(x=y1, y=x, hue=y1, palette="rocket")
    st.pyplot(f)
    st.write('Berdasarkan diagram diatas terlihat ada pola yang mana, orang yang memiliki avg_transaction_value yang rendah cenderung memiliki churn_score yang tinggi.')

    st.write('# 4. Churn Score Distribution based on past_complaints')
    f = plt.figure(figsize=(6, 6))
    sns.barplot(x='past_complaint', y='churn_score',hue='churn_score', data=Data_eda)
    st.pyplot(f)
    st.write('Berdasarkan diagram diatas, kita dapat melihat bahwa past_complaint atau riwayat complain tidak memiliki hubungan dengan churn_score, jadi terdapat orang yang tidak pernah melakukan complain namun tetap memiliki churn_score yang tinggi.')

    st.write('# 5. Churn Score Distribution based on preferred_offer_types')
    f = plt.figure(figsize=(6, 6))
    sns.displot(x=Data_eda['churn_score'],col=Data_eda['preferred_offer_types'])
    st.pyplot(f)
    st.write('Berdasarkan diagram diatas, kita dapat mengetahui bahwa tidak ada perbedaan signifikan antara preferred_offer_types.')

    st.write('# 6. Churn Score Distribution based on avg_time_spent')
    f = plt.figure(figsize=(6, 6))
    x = Data_eda['avg_time_spent']
    y = Data_eda['churn_score']
    sns.barplot(x=x, y=y, hue=y, palette="rocket")
    st.pyplot(f)
    st.write('Berdasarkan diagram diatas, kita dapat meilhat bahwa terdapat pola bahwa pelanggan yang memiliki churn_score rendah cenderung memiliki avg_time_spent yang lebih tinggi dibandingkan orang yang memiliki churn_score tinggi.')

    st.write('# 7. See customer feedback')
    f = plt.figure(figsize=(6,6))
    feedback_counts = Data_eda['feedback'].value_counts()
    plt.bar(feedback_counts.index, feedback_counts.values)
    plt.xlabel('Feedback')
    plt.xticks(rotation=45)
    plt.ylabel('Count')
    plt.title('Feedback Counts')
    st.pyplot(f)
    st.write('Berdasarkan feedback dari pelanggan, paling banyak pelanggan churn karena kualitas produk, terlalu banyak iklan di website, website yang kurang baik dan pelayanan customer service yang kurang memadai.')

