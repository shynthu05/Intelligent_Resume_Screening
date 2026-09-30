import streamlit as st

from resume_parser import extract_resume_text

from nlp_processor import (
    extract_entities,
    extract_email,
    extract_phone,
    extract_skills
)

from classifier import (
    calculate_match_score,
    classify_candidate
)


# Page configuration

st.set_page_config(
    page_title="Intelligent Resume Screening System",
    page_icon="📄",
    layout="wide"
)


# Title

st.title(
    "📄 Intelligent Resume Screening System"
)

st.write(
    "AI-powered resume screening using NLP, NER and Machine Learning."
)


# Job Description

st.sidebar.header(
    "Job Description"
)

job_description = st.sidebar.text_area(
    "Enter the Job Description",
    height=300
)


# Resume Upload

st.header(
    "📤 Upload Resume"
)

uploaded_file = st.file_uploader(
    "Upload PDF or DOCX Resume",
    type=["pdf", "docx"]
)


if uploaded_file is not None:

    # Check Job Description

    if not job_description.strip():

        st.warning(
            "Please enter a Job Description."
        )

    else:

        # Extract resume text

        resume_text = extract_resume_text(
            uploaded_file
        )


        # Extract candidate information

        email = extract_email(
            resume_text
        )

        phone = extract_phone(
            resume_text
        )

        skills = extract_skills(
            resume_text
        )

        entities = extract_entities(
            resume_text
        )


        # Calculate score

        score = calculate_match_score(
            resume_text,
            job_description
        )


        classification = classify_candidate(
            score
        )


        # Candidate Information

        st.header(
            "👤 Candidate Information"
        )

        col1, col2 = st.columns(2)


        with col1:

            st.write(
                "**Email:**",
                email
            )

            st.write(
                "**Phone:**",
                phone
            )


        with col2:

            st.write(
                "**Skills:**",
                ", ".join(skills)
            )


        # Resume text

        with st.expander(
            "📃 View Extracted Resume Text"
        ):

            st.write(
                resume_text
            )


        # Match Score

        st.header(
            "🎯 Resume–Job Match"
        )

        st.metric(
            "Match Score",
            f"{score}%"
        )


        st.subheader(
            "Classification"
        )

        st.info(
            classification
        )


        # Matching keywords

        job_lower = job_description.lower()

        matching_skills = []

        for skill in skills:

            if skill.lower() in job_lower:

                matching_skills.append(skill)


        # Missing skills

        common_skills = [

            "python",
            "java",
            "sql",
            "machine learning",
            "deep learning",
            "artificial intelligence",
            "data science",
            "pandas",
            "numpy",
            "scikit-learn",
            "tensorflow",
            "pytorch",
            "aws",
            "azure",
            "docker",
            "git"

        ]


        missing_skills = []

        for skill in common_skills:

            if skill.lower() in job_lower:

                if skill.lower() not in [
                    x.lower()
                    for x in skills
                ]:

                    missing_skills.append(
                        skill
                    )


        # Skills display

        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "✅ Matching Skills"
            )

            if matching_skills:

                for skill in matching_skills:

                    st.write(
                        "✓",
                        skill
                    )

            else:

                st.write(
                    "No matching skills found."
                )


        with col2:

            st.subheader(
                "❌ Missing Skills"
            )

            if missing_skills:

                for skill in missing_skills:

                    st.write(
                        "•",
                        skill
                    )

            else:

                st.write(
                    "No major missing skills detected."
                )


        # Named Entities

        st.header(
            "🔎 Named Entity Recognition"
        )


        if entities:

            for entity in entities:

                st.write(
                    f"**{entity['text']}** → "
                    f"{entity['label']}"
                )

        else:

            st.write(
                "No entities detected."
            )