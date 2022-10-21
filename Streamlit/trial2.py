import pandas as pd
import sqlite3 as db
import streamlit as st


conn = db.connect('database_1.db')
c = conn.cursor()

df = pd.read_sql_query('select * from users', conn)

st.markdown('# Telebeler databasina xos gelmisiniz')

if st.checkbox(label='Databasani goster'):
    st.dataframe(df)

if st.checkbox(label='Teze telebe elave et'):
    st.

# ad = 'Hesen'
# soyad = 'Cemil'
# phone = '0283923894'
#
# df = df.append({'ad':ad, 'soyad':soyad,'phone no':phone}, ignore_index=True)

# df.to_sql('users',conn, index=False, if_exists='replace')