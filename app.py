import streamlit as st
from google import genai
# import os # این کتابخانه در این کد کاربردی ندارد و حذف شده است

# --- ۱. تنظیمات اولیه و امنیتی ---
# کلید API را از تنظیمات امنیتی Streamlit Cloud می‌گیرد
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except KeyError:
    st.error("کلید API در تنظیمات امنیتی (Secrets) موجود نیست.")
    st.stop()

# --- ۲. تنظیمات هوش مصنوعی ---
client = genai.Client(api_key=API_KEY)

# استفاده از مدل پایدار و جدید برای جلوگیری از خطای 404
MODEL_NAME = "gemini-2.5-flash"

# --- ۳. رابط کاربری (Frontend) ---
st.title("🤖 دستیار هوشمند من")
st.write("سوال یا درخواست خود را وارد کنید تا هوش مصنوعی پاسخ دهد.")

user_prompt = st.text_input("اینجا بنویسید:", placeholder="مثلاً: سه روش برای یادگیری زبان جدید بگو.")

if st.button("پاسخ بگیر", type="primary"):
    if user_prompt:
        with st.spinner('در حال تولید پاسخ...'):
            # --- ۴. منطق فراخوانی هوش مصنوعی (اصلاح شده) ---
            try:
                # متغیر contents حذف و به جای آن مستقیماً از user_prompt استفاده می‌شود.
                response = client.models.generate_content(
                    model=MODEL_NAME, 
                    contents=user_prompt # <--- متغیر contents حذف شد و از ورودی متنی کاربر استفاده شد
                )
                
                st.info(response.text)
            except Exception as e:
                st.error(f"خطایی رخ داد: {e}")
    else:
        st.warning("لطفاً یک سوال وارد کنید.")
