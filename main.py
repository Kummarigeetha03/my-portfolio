import streamlit as st
import pandas as pd
from PIL import Image

# Set page configuration with title and icon
st.set_page_config(page_title="My Portfolio", page_icon=":rocket:", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
        }
        .content-section {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        .header-img {
            text-align: center;
            margin-top: 20px;
            position: relative;
        }
        .header-img img {
            border-radius: 50%;
            width: 120px;
            height: 120px;
        }
        .header-text {
            font-size: 24px;
            font-weight: bold;
            color: white;
            background-color: #2c3e50;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 20px;
        }
        .flip-card {
            background-color: transparent;
            width: 300px;
            height: 200px;
            perspective: 1000px;
            display: inline-block;
            margin: 20px;
        }
        .flip-card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.6s;
            transform-style: preserve-3d;
        }
        .flip-card:hover .flip-card-inner {
            transform: rotateY(180deg);
        }
        .flip-card-front, .flip-card-back {
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
        }
        .flip-card-front {
            background-color: #bbb;
            color: black;
        }
        .flip-card-back {
            background-color: #2980b9;
            color: white;
            transform: rotateY(180deg);
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        .achievement-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
        }
        .achievement-card {
            background-color: #f1f1f1;
            padding: 20px;
            margin: 10px;
            border-radius: 10px;
            width: 300px;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2);
        }
        .achievement-card h4 {
            margin-bottom: 15px;
            color: #333;
        }
        .achievement-card p {
            font-size: 14px;
            color: #666;
        }
        .error-message {
            color: red;
            font-size: 14px;
            margin-top: -10px;
        }
            
        .footer {
            font-size: 10px; /* Small font size */
            text-align: center; /* Center the text */
            margin-top: 20px; /* Margin for separation from the content */
            padding: 10px 0; /* Padding for better spacing */
            background-color: #f0f2f6; /* Background color for the footer */
            color : #333;
        }
        .footer a {
            color: #2980b9; /* Link color */
            text-decoration: none; /* Remove underline from links */
        }
    </style>
""", unsafe_allow_html=True)

# Load the profile image
profile_image = Image.open("geetha.jpg")

# Display "My Portfolio" text in the sidebar
st.sidebar.markdown("""
    <div class="header-text">My Portfolio</div>
""", unsafe_allow_html=True)

# Display profile image below "My Portfolio" heading
st.sidebar.image(profile_image, use_column_width=True)

# Sidebar menu 
menu = st.sidebar.selectbox('Menu', [
    '🧑 About Me', 
    '📜 Certifications', 
    '🎓 Education', 
    '🏆 Achievements', 
    '💼 Projects', 
    '📧 Contact Me'  
])

# Content section based on menu selection
if menu == '🧑 About Me':
    st.markdown("""
    <div class='content-section'>
        <h2>About Me</h2>
        <p>Hello! I am Geetha, a motivated Computer Science Engineering student with a passion for exploring various technologies. I have strong technical skills, particularly in Python and Machine Learning, and am eager to apply these in real-world projects to gain practical experience.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == '📜 Certifications':
    st.markdown("<div class='content-section'><h2>Certifications</h2></div>", unsafe_allow_html=True)
    
    # Dropdown for certificates
    with st.expander("HTML, CSS, Bootstrap"):
        st.write("Certified in static website development, responsive web design with Bootstrap and Flexbox.")
    
    with st.expander("Python Programming,Machine Learning"):
        st.write("Certified in Python programming, focusing on foundational and advanced programming concepts with machine learning algorithms.")
    
    with st.expander("Dynamic Website Design with JavaScript"):
        st.write("Certified in designing dynamic websites using JavaScript.")

elif menu == '🎓 Education':
    st.markdown("<div class='content-section'><h2>Education</h2></div>", unsafe_allow_html=True)
    
    # DataFrame for Education
    education_data = {
        'Education': ['B. Tech, HITAM - CSE', '12th, Narayana Junior College', '10th, PNM High School'],
        'Board': ['Jntuh', 'TSBIE', 'SSC'],
        'Year of Passing': [2025, 2021, 2019],
        'Score': ['8.5 CGPA', '96%', '9.5 CGPA']
    }
    df = pd.DataFrame(education_data)
    
    # Display DataFrame as a table
    st.write(df)

elif menu == '🏆 Achievements':
    st.markdown("<div class='content-section'><h2>Achievements</h2></div>", unsafe_allow_html=True)
    
    # Achievement cards
    st.markdown("""
    <div class="achievement-container">
        <div class="achievement-card">
            <h4>Sports</h4>
            <p>Honored for accomplishments in inter and intra-school badminton, kho-kho, and Bhagavad Gita chanting competitions.</p>
        </div>
        <div class="achievement-card">
            <h4>Hindi Proficiency</h4>
            <p>Completed Hindi exams up to Madhyama level with Dakshina Bharat Hindi Prachar Sabha.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif menu == '💼 Projects':
    st.markdown("<div class='content-section'><h2>Projects</h2></div>", unsafe_allow_html=True)

    # Flip card for project 1
    st.markdown("""
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front">
                <h3>Password Strength Checker</h3>
                <img src="https://res.cloudinary.com/bw-com/image/upload/f_auto/v1/ctf/7rncvj1f8mw7/7yYK16b2bBdsWbkG9cvijf/6dbf8bc9fefffa54d27a43f774f3d7ec/pw-strength-test-chart.png?_a=DAJAUVWIZAAB" alt="Project Image" style="width:100%; height:100%;">
            </div>
            <div class="flip-card-back">
                <h3>Details</h3>
                <p>Developed a password strength checker application to enhance security measures using Python.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Flip card for project 2
    st.markdown("""
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front">
                <h3>Sonar-Based Mineral Detection</h3>
                <img src="https://media.licdn.com/dms/image/D5622AQHsNd5ewLgCbg/feedshare-shrink_2048_1536/0/1711302316802?e=2147483647&v=beta&t=N6ywSOBQGRhFE0LdwU0s5Z1LsOtpooVQzn199EXvEhU" alt="Project Image" style="width:100%; height:100%;">
            </div>
            <div class="flip-card-back">
                <h3>Details</h3>
                <p>Developed a sonar-based system for mineral and rock detection, optimizing exploration processes using Machine Learning.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Flip card for project 3
    st.markdown("""
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front">
                <h3>Mini Voting System</h3>
                <img src="https://media.geeksforgeeks.org/wp-content/uploads/20230803111937/Online-Voting-System.webp" alt="Project Image" style="width:100%; height:100%;">
            </div>
            <div class="flip-card-back">
                <h3>Details</h3>
                <p>Designed and implemented a mini voting system tailored for small-scale elections using Python.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif menu == '📧 Contact Me':
    st.markdown("<div class='content-section'><h2>Contact Me</h2></div>", unsafe_allow_html=True)
    
    # Contact form with placeholders and validation
    with st.form("contact_form"):
        name = st.text_input("Your Name", placeholder="Enter your name")
        email = st.text_input("Your Email", placeholder="Enter your email address")
        submitted = st.form_submit_button("Contact Me")

    # Validation
    if submitted:
        if not name:
            st.markdown("<p class='error-message'>Name is mandatory!</p>", unsafe_allow_html=True)
        elif not email:
            st.markdown("<p class='error-message'>Email is mandatory!</p>", unsafe_allow_html=True)
        else:
            st.success(f"Thank you {name}! We will contact you soon.")

# Footer with contact information
st.markdown("""
    <div class='footer'>
        Connect with me on <a href="http://www.linkedin.com/in/kummari-geetha-a781a7229" target="_blank">LinkedIn</a> | 
        Email: kummarigeetha03@gmail.com
    </div>
""", unsafe_allow_html=True)
