import streamlit as st
import pandas as pd
import os

# استخدم ملف تخزين محلي مناسب لمكان Streamlit Cloud
RESULTS_FILE = "math_quiz_results.csv"

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

# --- نصائح ---
def get_tips(level):
    if level == "مبتدئ":
        return (
            "👨‍🏫 **نصائح للمربي:** استخدم أدوات بصرية مثل قطع الكسور أو الفواكه.",
            "👦 **نصائح للطالب:** حاول تقسيم أشياء حولك إلى أنصاف وأرباع لتفهم الكسر عمليًا."
        )
    elif level == "متوسط":
        return (
            "👨‍🏫 **نصائح للمربي:** شجع الطالب على إجراء عمليات جمع وطرح بسيطة للكسور.",
            "👦 **نصائح للطالب:** تدرب على مقارنة الكسور وتبسيطها."
        )
    else:
        return (
            "👨‍🏫 **نصائح للمربي:** شجع الطالب على ربط الكسور بالحياة اليومية (مثل الطهي أو الوقت).",
            "👦 **نصائح للطالب:** جرب حل مسائل منوعة تشمل ضرب وطرح الكسور وتطبيقها في مواقف حقيقية."
        )

# --- فيديو توضيحي ---
def get_video_url(level):
    if level == "مبتدئ":
        return "https://www.youtube.com/embed/At6VjUqah6A"
    elif level == "متوسط":
        return "https://www.youtube.com/embed/3v6tw7v2D7Q"
    else:
        return "https://www.youtube.com/embed/YJPl1v9aL2k"

# --- حفظ النتيجة ---
def save_result(name, score, level):
    df_new = pd.DataFrame([{"الاسم": name, "الدرجة": score, "المستوى": level}])
    try:
        parent_dir = os.path.dirname(RESULTS_FILE)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        if os.path.exists(RESULTS_FILE):
            df = pd.read_csv(RESULTS_FILE)
            df = pd.concat([df, df_new], ignore_index=True)
        else:
            df = df_new
        df.to_csv(RESULTS_FILE, index=False)
    except Exception as e:
        st.warning("لم نتمكن من حفظ النتيجة. تأكد من صلاحيات الكتابة في بيئة التشغيل.")

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
        tips_teacher, tips_student = get_tips(level)
        video_url = get_video_url(level)

        st.markdown("---")
        st.markdown("### الشرح المناسب ليك:")
        st.info(explanation)

        st.markdown("### 📘 نصائح:")
        st.markdown(tips_teacher)
        st.markdown(tips_student)

        st.markdown("### 🎬 فيديو توضيحي:")
        st.video(video_url)

        save_result(name, score, level)
        st.balloons()

    if st.button("إعادة المحاولة"):
        st.experimental_rerun()
else:
    st.info("يرجى إدخال الاسم للبدء بالاختبار.")
