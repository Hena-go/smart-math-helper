
import streamlit as st
import pandas as pd
import os

RESULTS_FILE = "/mnt/data/math_quiz_results.csv"

# --- تقييم الإجابات ---
def evaluate_score(answers):
    score = 0
    correct_answers = ["1/2", "3/4", "3/4"]
    for i in range(3):
        if answers[i] == correct_answers[i]:
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

# --- حفظ النتيجة ---
def save_result(name, score, level):
    df_new = pd.DataFrame([{"الاسم": name, "الدرجة": score, "المستوى": level}])
    if os.path.exists(RESULTS_FILE):
        df = pd.read_csv(RESULTS_FILE)
        df = pd.concat([df, df_new], ignore_index=True)
    else:
        df = df_new
    df.to_csv(RESULTS_FILE, index=False)

# --- نجوم التشجيع ---
def stars(score):
    return "⭐" * score + "☆" * (3 - score)

# --- الواجهة ---
st.set_page_config(page_title="مساعد الكسور", page_icon="🔢")
st.title("🔢 مساعد الرياضيات الذكي - درس الكسور")

name = st.text_input("أدخل اسمك:")

if name:
    st.write(f"أهلاً {name}! اختر الإجابات الصحيحة من الخيارات التالية:")

    st.markdown("### 1️⃣ ما هو نصف الواحد؟")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Fraction_1-2.svg/220px-Fraction_1-2.svg.png", width=100)
    q1 = st.radio("اختر الإجابة:", ["1/3", "1/2", "2/3"], key="q1")

    st.markdown("### 2️⃣ ما هو الكسر الذي يمثل ثلاثة أرباع؟")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Fraction_3-4.svg/220px-Fraction_3-4.svg.png", width=100)
    q2 = st.radio("اختر الإجابة:", ["1/4", "3/4", "2/4"], key="q2")

    st.markdown("### 3️⃣ ما ناتج: 1/2 + 1/4 = ؟")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Fraction_3-4.svg/220px-Fraction_3-4.svg.png", width=100)
    q3 = st.radio("اختر الإجابة:", ["2/4", "3/4", "4/4"], key="q3")

    if st.button("أرسل الإجابات"):
        answers = [q1, q2, q3]
        score = evaluate_score(answers)
        if score <= 1:
            level = "مبتدئ"
        elif score == 2:
            level = "متوسط"
        else:
            level = "متقدم"

        st.success(f"👍 مستواك: {level}  {stars(score)}")
        explanation = get_explanation(level)
        st.markdown("---")
        st.markdown(f"### الشرح المناسب ليك:")
        st.info(explanation)
        save_result(name, score, level)
        st.balloons()

    if st.button("إعادة المحاولة"):
        st.experimental_rerun()
else:
    st.info("يرجى إدخال الاسم للبدء بالاختبار.")

        
