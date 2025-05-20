# هذا الكود مُصمم ليُشغّل باستخدام Streamlit محليًا على جهازك
# تأكد أنك لا تستخدم Google Colab لأن Streamlit لا يعمل عليه مباشرة

# لتشغيل الكود:
# 1. انسخه في ملف اسمه app.py
# 2. من الطرفية (Terminal) شغل الأمر: streamlit run app.py

import streamlit as st

# --- تقييم الإجابات ---
def evaluate_score(answers):
    score = 0
    correct_answers = ["1/2", "3/4", "3/4"]
    for i in range(3):
        if answers[i].strip().replace(" ", "") == correct_answers[i]:
            score += 1
    return score

# --- توليد الشرح ---
def get_explanation(level):
    if level == "مبتدئ":
        return "الكسور هي أجزاء من شيء كامل. مثلًا: لو قسمنا تفاحة إلى نصفين، كل جزء هو 1/2."
    elif level == "متوسط":
        return "الكسور تمثل جزءًا من عدد صحيح. مثلًا: 3/4 يعني ثلاثة أجزاء من أربعة. ويمكنك جمع الكسور أو طرحها بسهولة عندما يكون المقام متساوي."
    else:
        return "يمكنك جمع وطرح وضرب الكسور. مثلًا: 1/2 + 1/4 = 3/4. وعند ضرب الكسور: 1/2 × 4 = 2."

# --- واجهة Streamlit ---
st.set_page_config(page_title="مساعد الكسور", page_icon="🔢")
st.title("🔢 مساعد الرياضيات الذكي - درس الكسور")

st.write("أدخل اسمك أولاً:")
name = st.text_input("الاسم")

if name:
    st.write(f"أهلاً {name}! هنسألك 3 أسئلة بسيطة علشان نعرف مستواك في الكسور:")

    with st.form("quiz_form"):
        q1 = st.text_input("1️⃣ ما هو نصف الواحد؟ (اكتب الكسر)")
        q2 = st.text_input("2️⃣ ما هو الكسر الذي يمثل ثلاثة أرباع؟ (اكتب الكسر)")
        q3 = st.text_input("3️⃣ ما ناتج: 1/2 + 1/4 = ؟ (اكتب الناتج على شكل كسر مثل 3/4)")
        submitted = st.form_submit_button("أرسل الإجابات")

    if submitted:
        score = evaluate_score([q1, q2, q3])

        if score <= 1:
            level = "مبتدئ"
        elif score == 2:
            level = "متوسط"
        else:
            level = "متقدم"

        st.success(f"👍 مستواك: {level}")
        explanation = get_explanation(level)
        st.markdown("---")
        st.markdown(f"### الشرح المناسب ليك:")
        st.info(explanation)
        st.balloons()
