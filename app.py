
import streamlit as st

from generator import generate_interview


st.set_page_config(
    page_title="AI Placement Assistant",
   page_icon="🎯",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title(" AI Placement Preparation Assistant ")

st.write(
    "Prepare for your technical interviews with "
    "AI-powered questions, practical examples and "
    "interview-ready answers."
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("Interview Configuration")


job_role = st.sidebar.selectbox(
    "Select Job Role",
    [
        "Python Developer",
        "Java Developer",
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Analyst",
        "Data Scientist",
        "GenAI Engineer",
        "Backend Developer"
    ]
)


experience_level = st.sidebar.selectbox(
    "Experience Level",
    [
        "Fresher",
        "0-1 Years",
        "1-3 Years",
        "3-5 Years"
    ]
)


difficulty = st.sidebar.selectbox(
    "Difficulty Level",
    [
        "Easy",
        "Medium",
        "Hard"
    ],
    index=1
)


num_questions = st.sidebar.slider(
    "Number of Questions",
    min_value=3,
    max_value=15,
    value=5
)


st.sidebar.divider()


# --------------------------------------------------
# GENERATE QUESTIONS
# --------------------------------------------------

if st.sidebar.button(
    "🚀 Generate Interview Questions",
    type="primary",
    use_container_width=True
):

    with st.spinner("Generating interview questions..."):

        try:

            result = generate_interview(
                job_role,
                experience_level,
                difficulty,
                num_questions
            )

            st.session_state["result"] = result

        except Exception as e:

            st.error(
                f"Something went wrong: {str(e)}"
            )


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

if "result" in st.session_state:

    result = st.session_state["result"]

    st.success("Interview preparation generated!")

    st.subheader(
        f"{result.job_role} | {result.experience_level}"
    )

    st.caption(
        f"Total Questions: {len(result.questions)}"
    )

    st.divider()


    for index, question in enumerate(
        result.questions,
        start=1
    ):

        # Bold question title in expander

        with st.expander(
            f"**Q{index}. {question.question}**",
            expanded=(index == 1)
        ):

            # Question metadata

            col1, col2 = st.columns(2)

            with col1:
                st.caption(
                    f"📌 Question Type: {question.question_type}"
                )

            with col2:
                st.caption(
                    f"🎯 Difficulty: {question.difficulty}"
                )


            st.divider()


            # Model Answer

            st.markdown("### 📝 Model Answer")

            st.markdown(
                question.model_answer
            )


            st.divider()


            # Simple Explanation

            st.markdown("### 💡 Understand It Simply")

            st.info(
                question.explanation
            )


            # Practical Example

            st.markdown("### 💻 Practical Example")

            st.markdown(
                question.practical_example
            )


            st.divider()


            # Important Keywords

            st.markdown("### 🔑 Important Keywords")

            st.markdown(
                "  |  ".join(
                    [f"`{keyword}`" for keyword in question.keywords]
                )
            )


            st.divider()


            # Follow-up Question

            st.markdown("### 🎤 Interviewer's Follow-up")

            st.warning(
                f"**{question.follow_up}**"
            )


else:

    st.info(
        "Select your job role and click "
        "'Generate Interview Questions' to begin."
    )
