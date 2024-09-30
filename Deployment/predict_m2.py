import streamlit as st
import pandas as pd
import numpy as np

import pickle
import json

def run():
    st.title('Customer Churn Prediction')
    # load model

    # load model yang udah dibuat
    with open('model_XGBoost.pkl', 'rb') as file_1:
        model = pickle.load(file_1)

    # load scaler yang sudah di fit
    with open('data_model.txt', 'r') as file_2:
        data = json.load(file_2)

    st.write('## Input Data')
    with st.form(key = 'data'):
        customer_id = st.text_input('Customer ID')
        Name = st.text_input('Name')
        age = st.number_input('Age')
        gender = st.selectbox('Gender', ['F', 'M'])
        security_no = st.text_input('Security No')
        region_category = st.selectbox('Region Category', ['Town', 'City','Village'])  
        membership_category = st.selectbox('Membership Category', ['No Membership', 'Basic Membership', 'Silver Membership','Gold Membership', 'Premium Membership', 'Platinum Membership']) 
        joining_date = st.date_input('Joining Date')
        joined_through_referral = st.selectbox('Joined Through Referral', ['Yes', 'No'])
        referral_id = st.text_input('Referral ID')
        preferred_offer_types = st.selectbox('Preferred Offer Types', ['Gift Vouchers/Coupons', 'Credit/Debit Card Offers','Without Offers'])  
        medium_of_operation = st.selectbox('Medium of Operation', ['Desktop', 'Smartphone', 'Both'])  
        internet_option = st.selectbox('Internet Option', ['Wi-Fi', 'Mobile_Data', 'Fiber_Optic'])  
        last_visit_time = st.time_input('Last Visit Time')
        days_since_last_login = st.number_input('Days Since Last Login')
        avg_time_spent = st.number_input('Average Time Spent')
        avg_transaction_value = st.number_input('Average Transaction Value')
        avg_frequency_login_days = st.number_input('Average Frequency Login Days')
        points_in_wallet = st.number_input('Points in Wallet')
        used_special_discount = st.selectbox('Used Special Discount', ['Yes', 'No'])
        offer_application_preference = st.selectbox('Offer Application Preference', ['Yes', 'No'])  # replace with actual options
        past_complaint = st.selectbox('Past Complaint', ['Yes', 'No'])
        complaint_status = st.selectbox('Complaint Status', ['Open', 'Closed', 'In Progress'])  # replace with actual statuses
        feedback = st.selectbox('Feedback',['Poor Website', 'Poor Product Quality', 'Too many ads','No reason specified', 'Poor Customer Service','Products always in Stock', 'User Friendly Website','Reasonable Price', 'Quality Customer Care'])
        content = st.text_input('Content')
        summary = st.text_input('Summary')
        sentiment = st.selectbox('Sentiment', ['0', '1'])
        #submit button
        submit = st.form_submit_button('predict')

    if submit:
        data = {
            'customer_id': customer_id,
            'Name': Name,
            'age': age,
            'gender': gender,
            'security_no': security_no,
            'region_category': region_category,
            'membership_category': membership_category,
            'joining_date': joining_date,
            'joined_through_referral': joined_through_referral,
            'referral_id': referral_id,
            'preferred_offer_types': preferred_offer_types,
            'medium_of_operation': medium_of_operation,
            'internet_option': internet_option,
            'last_visit_time': last_visit_time.hour,
            'days_since_last_login': days_since_last_login,
            'avg_time_spent': avg_time_spent,
            'avg_transaction_value': avg_transaction_value,
            'avg_frequency_login_days': avg_frequency_login_days,
            'points_in_wallet': points_in_wallet,
            'used_special_discount': used_special_discount,
            'offer_application_preference': offer_application_preference,
            'past_complaint': past_complaint,
            'complaint_status': complaint_status,
            'feedback': feedback,
            'content': content,
            'summary': summary,
            'sentiment': sentiment}
        data = pd.DataFrame([data])
        st.dataframe(data)


        # ubah tipe data


        def categorize_time(hour):
            if 0 <= hour < 6:
                return 'Dini Hari'
            elif 6 <= hour < 12:
                return 'Pagi'
            elif 12 <= hour < 3:
                return 'Siang'
            elif 3 <= hour < 6:
                return 'Sore'
            else:  
                return 'Malam'
            
        data['last_visit_time'] = data['last_visit_time'].apply(categorize_time)
        prediksi = model.predict(data)
        def cek_prediksi(prediksi):
            if prediksi == 0:
                st.write("Hasil prediksi, kemungkinan churn Sangat Rendah: Pertahankan dengan program loyalitas")
            elif prediksi == 1:
                st.write("Hasil prediksi, kemungkinan churn Sedikit di bawah rata-rata: Tawarkan promosi kecil")
            elif prediksi == 2:
                st.write("Hasil prediksi, kemungkinan churn Sedikit di atas rata-rata: Tingkatkan interaksi dengan pelanggan")
            elif prediksi == 3:
                st.write("Hasil prediksi, kemungkinan churn Sedang: Tawarkan penawaran khusus atau program referral")
            elif prediksi == 4:
                st.write("Hasil prediksi, kemungkinan churn Tinggi: Lakukan kontak langsung, tawarkan solusi yang dipersonalisasi")
            elif prediksi == 5:
                st.write("Hasil prediksi, kemungkinan churn Sangat Tinggi: Upayakan untuk menyelamatkan pelanggan dengan penawaran yang sangat menarik")
        cek_prediksi(prediksi)