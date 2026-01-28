from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# --- CONFIGURATION (EDIT THIS SECTION) ---

EVENT_INFO = {
    "year": "2026",
    "date": "March 14, 2026",
    "time": "9:00 AM - 5:00 PM IST",
    "venue": "To Be Announced, Mumbai",
    "description": "WiDS Mumbai is a flagship location for the WiDS India Conference 2026, alongside Delhi and Bangalore. Representing the Western Region, we bring together Ambassadors from Mumbai, Pune, and Surat.",
    "registration_link": "https://docs.google.com/forms/d/e/1FAIpQLSeg45Skd91dYkGdhle1ycfzV8a3-1xFl-VZlEnKddA4tmIDJw/viewform", 
    "contact_email": "wids.surat@example.com"
}

# Add your team members here. 
# You can add as many as you want.
TEAM = [
    {
        "name": "Hetvi Patel", 
        "role": "Final Year CSE Student at SCET Surat", 
        "city": "Surat", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Hetvi%20Patel.png",
        "email": "hetvi1655@example.com",
        "linkedin": "https://www.linkedin.com/in/hetvi-patel-5a6467275/"
    },
    {
        "name": "Shradhha Joshi", 
        "role": "Co-Founder & Head Of Marketing at Kquanta Research ", 
        "city": "Mumbai", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Shraddha%20Joshi.jpeg",
        "email": "Shraddha.joshi@kquantaresearch.com",
        "linkedin": "https://www.linkedin.com/in/shraddha-joshi-14285461/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
    },
    {
        "name": "Barkha Jain", 
        "role": "International Speaker and Community Lead", 
        "city": "Pune", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Barkha%20Jain.jpeg",
        "email": "barkhajain15sep@gmail.com",
        "linkedin": " https://www.linkedin.com/in/jbarkha/"
    },
    {
        "name": "Prof.(Dr.)Pariza Kamboj", 
        "role": "Professor at Sarvajanik College of Engineering and Technology(SCET), Surat", 
        "city": "Surat", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Pariza%20Kamboj.jpeg",
        "email": "pariza.kamboj@scet.ac.in",
        "linkedin": "https://www.linkedin.com/in/prof-dr-pariza-kamboj-37617616/"
    },
    {
        "name": "Anita Nandi-Ray", 
        "role": "Co-founder & Policy Director at Kquanta Research", 
        "city": "Mumbai", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Anita%20Nandi.jpeg",
        "email": "Anita.nandi-ray@kquantaresearch.com",
        "linkedin": "https://www.linkedin.com/in/anitanandi/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
    }
]

SPEAKERS = [
    {
        "name": "Urvashi Kapoor",
        "title": "Head of AI, Tech Corp",
        "topic": "Generative AI in Healthcare",
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Urvashi%20Kapoor.jpg"
    },
    {
        "name": "Sarah Johnson",
        "title": "Lead Data Scientist",
        "topic": "Ethics in Machine Learning",
        "image": "speaker2.jpg"
    },
]

AGENDA = [
    {"time": "9:15 AM", "event": "Welcome & Opening Remarks", "speaker": "[WiDS Ambassador]", "designation": "[Designation]"},
    {"time": "9:00 - 9:30 AM", "event": "Opening Remarks", "speaker": "[Chisoo Lyons]", "designation": "[WiDS Wordwide Executive Director, WiDS Worldwide]"},
    {"time": "9:30 - 10:00 AM", "event": "Technology Vision Talks 1", "speaker": "[Speaker Name]", "designation": "[Designation]"},
    {"time": "10:00 - 10:30 AM", "event": "Technology Vision Talks 2", "speaker": "[Speaker Name]", "designation": "[Designation]"},
    {"time": "10:30 - 11:00 AM", "event": "Technology Vision Talks 3", "speaker": "[Speaker Name]", "designation": "[Designation]"},
    {"time": "11:00 - 11:30 AM", "event": "Break", "speaker": "", "designation": ""},
    {"time": "11:30 - 12:00 PM", "event": "Technology Vision Talks 4", "speaker": "[Speaker Name]", "designation": "[Designation]"},
    {"time": "12:00 - 12:30 PM", "event": "Technology Vision Talks 5", "speaker": "[Speaker Name]", "designation": "[Designation]"},
    {"time": "12:30 - 1:00 PM", "event": "Technology Vision Talks 6", "speaker": "[Speaker Name]", "designation": "[Designation]"},
    {"time": "1:00 - 2:00 PM", "event": "Lunch Break", "speaker": "", "designation": ""},
    {"time": "2:00 - 3:00 PM", "event": "Panel Discussion - Is AI making us better or just faster?", "speaker": "[Speaker 1], [Speaker 2], [Speaker 3]", "designation": "[Designations]"},
    {"time": "3:00 - 3:30 PM", "event": "Technology Vision Talks 7", "speaker": "[Speaker Name]", "designation": "[Designation]"},
    {"time": "3:30 - 4:00 PM", "event": "Break", "speaker": "", "designation": ""},
    {"time": "4:00 - 4:30 PM", "event": "Technology Vision Talks 8", "speaker": "[Urvashi Kapoor]", "designation": "[Senior Editor and AGM, Jagran Media]"},
    {"time": "4:30 - 5:00 PM", "event": "Closing Remarks", "speaker": "[Speaker Name]", "designation": "[Designation]"},
    {"time": "5:00 - 5:15 PM", "event": "Group Photo and Tea", "speaker": "", "designation": ""},
]

# -----------------------------------------

@app.route('/')
def home():
    return render_template(
        'index.html', 
        info=EVENT_INFO, 
        speakers=SPEAKERS, 
        agenda=AGENDA,
        team=TEAM
    )

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')

if __name__ == '__main__':
    app.run(debug=True)