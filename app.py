import streamlit as st
from PIL import Image
from backend.caption_generator import generate_caption

# Set page config
st.set_page_config(page_title="X-ray Diagnosis Generator", layout="centered")

# Sidebar for navigation
page = st.sidebar.selectbox(
    "Navigate",
    ("Project Description", "X-ray Diagnosis")
)

if page == "Project Description":
    st.title("🩻 X-ray Image Diagnosis Generator")
    st.header("Project Overview")
    st.write("""
    Welcome to the X-ray Image Diagnosis Generator project!
    
    **Purpose:**  
    This tool uses artificial intelligence to analyze X-ray images and generate a description of the findings, assisting healthcare professionals and students in understanding radiological images.

    **How it works:**  
    - You upload an X-ray image.
    - The AI model analyzes the image.
    - A diagnostic description is generated and displayed.

    **Note:**  
    This tool is for educational and research purposes only, and not for clinical diagnosis.
    """)

elif page == "X-ray Diagnosis":
    st.title("📤 Upload & Analyze X-ray Image")
    st.write("Upload an X-ray image, and the model will generate a description of the findings.")

    uploaded_file = st.file_uploader("Upload an X-ray image", type=["png", "jpg", "jpeg", "avif"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded X-ray", use_column_width=True)

        with st.spinner("Analyzing X-ray..."):
            caption = generate_caption(image)
            st.success("Diagnosis Result:")
            st.markdown(f"**{caption}**")
