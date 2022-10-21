
import sqlite3 as db
import pandas as pd
import streamlit as st

conn = db.connect('database_1.db')

c = conn.cursor()


#%%


telebeler = {'ad': 'Elnur', 'soyad': 'Shahbalayev', 'phone no': '0773061366'}

df = pd.DataFrame(telebeler, index=[0])
df.to_sql('users', con=conn, index=False)
#%%
