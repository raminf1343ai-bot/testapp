import streamlit as st
from google import genai
import os

# --- ۱. تنظیمات اولیه و امنیتی ---
# کلید API را از تنظیمات امنیتی Streamlit Cloud می‌گیرد
# این روش امن‌تر از گذاشتن کلید مستقیم در کد است
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except KeyError:
    st.error("کلید API در تنظیمات امنیتی (Secrets) موجود نیست.")
    st.stop()

# --- ۲. تنظیمات هوش مصنوعی ---
client = genai.Client(api_key=API_KEY)
model = "gemini-1.5-flash"  # یا مدل انتخابی شما

# --- ۳. رابط کاربری (Frontend) ---
st.title("🤖 دستیار هوشمند من")
st.write("سوال یا درخواست خود را وارد کنید تا هوش مصنوعی پاسخ دهد.")

user_prompt = st.text_input("اینجا بنویسید:", placeholder="مثلاً: سه روش برای یادگیری زبان جدید بگو.")

if st.button("پاسخ بگیر", type="primary"):
    if user_prompt:
        with st.spinner('در حال تولید پاسخ...'):
            # این قسمت باید با کد پرامپت شما از AI Studio جایگزین شود
            try:
                response = client.models.generate_content(
    model="gemini-2.5-flash", # <--- نام جدید جایگزین شده
    contents=contents
)
                
                st.info(response.text)
            except Exception as e:
                st.error(f"خطایی رخ داد: {e}")
    else:
        st.warning("لطفاً یک سوال وارد کنید.")
