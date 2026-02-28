from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# --- CONFIGURATION (EDIT THIS SECTION) ---

EVENT_INFO = {
    "year": "2026",
    "date": "March 14, 2026",
    "time": "8:30 hrs to 13:30 hrs",
    "venue": "New Rizvi Education Complex, Mumbai.",
    "description": "WiDS Mumbai 2026 (Women in Data Science Worldwide Conference-2026) is held in association with Rizvi Institute of Management & Research (RIMSR). Representing the Western Region, we bring together data science enthusiasts and leaders.",
    "registration_link": "https://docs.google.com/forms/d/e/1FAIpQLSeg45Skd91dYkGdhle1ycfzV8a3-1xFl-VZlEnKddA4tmIDJw/viewform", 
    "contact_email": "widsmumbaiconference@gmail.com",
    "sponsorship_link": "https://docs.google.com/forms/d/e/1FAIpQLSd-Ai0gRh_59YZ-AGilYZ44B1Ce0vySzbFtAquiXJkF6IU0Fg/viewform?usp=header",
    "sponsorship_email": "widsmumbaiconference@gmail.com"
}

SPONSORS = [
    {
        "name": "Rizvi Institute of Management & Research (RIMSR)",
        "role": "Venue Partner",
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/RIMSR%20Logo.png",
        "description": "Our esteemed host partner for WiDS Mumbai 2026."
    }
]

# Add your team members here. 
# You can add as many as you want.
TEAM = [
    {
        "name": "Hetvi Patel", 
        "role": "Final Year CSE Student at SCET Surat", 
        "city": "Surat", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Hetvi%20Patel.png",
        "email": "hetvi1655@gmail.com",
        "linkedin": "https://www.linkedin.com/in/hetvi-patel-5a6467275/"
    },
    {
        "name": "Anita Nandi-Ray", 
        "role": "Co-founder & Policy Director at Kquanta Research", 
        "city": "Mumbai", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Anita%20Nandi.jpeg",
        "email": "Anita.nandi-ray@kquantaresearch.com",
        "linkedin": "https://www.linkedin.com/in/anitanandi/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
    },
    {
        "name": "Barkha Jain", 
        "role": "International Speaker and Community Lead", 
        "city": "Pune", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Barkha%20Jain.jpeg",
        "email": "barkhajain15sep@gmail.com",
        "linkedin": "https://www.linkedin.com/in/jbarkha/"
    },
    {
        "name": "Prof.(Dr.) Dhatri Pandya", 
        "role": "Professor at Sarvajanik College of Engineering and Technology(SCET), Surat", 
        "city": "Surat", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Dhatri%20Pandya.jpeg",
        "email": "dhatri.pandya@scet.ac.in",
        "linkedin": "https://www.linkedin.com/in/dr-dhatri-pandya-a76569a8/"
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
        "name": "Shradhha Joshi", 
        "role": "Co-Founder & Head Of Marketing at Kquanta Research ", 
        "city": "Mumbai", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Shraddha%20Joshi.jpeg",
        "email": "Shraddha.joshi@kquantaresearch.com",
        "linkedin": "https://www.linkedin.com/in/shraddha-joshi-14285461/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
    }
]

SPEAKERS = [
    {
        "name": "Urvashi Kapoor",
        "title": "Senior Editor & AGM at Jagran New Media",
        "topic": "The AI Safety Blueprint: Preventing Online Scams through Ethical and Responsible Use of AI",
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Urvashi%20Kapoor.jpg"
    }
]

AGENDA = [
    {"time": "08:30 – 09:00", "event": "Registrations", "speaker": "", "designation": ""},
    {"time": "09:00 – 09:30", "event": "Live Stream: Inaugural Remarks", "speaker": "", "designation": ""},
    {"time": "09:30 – 09:40", "event": "Opening Address & Context Setting", "speaker": "", "designation": ""},
    {"time": "09:40 – 09:50", "event": "Special Address", "speaker": "", "designation": ""},
    {"time": "09:50 – 10:10", "event": "Keynote: Future of AI & Data for Impact", "speaker": "Focus: Generative AI, responsible innovation, and inclusive AI & analytics", "designation": "Takeaways: Industry demands and ethical considerations"},
    {"time": "10:10 – 10:35", "event": "Panel: Women Leaders in Tech & STEM", "speaker": "Breaking barriers, Leadership lessons, Building influence", "designation": ""},
    {"time": "10:35 – 10:55", "event": "Tea Break & Networking", "speaker": "", "designation": ""},
    {"time": "10:55 – 11:20", "event": "Technology Horizons: AI, Cybersecurity & Quantum Technology", "speaker": "", "designation": ""},
    {"time": "11:20 – 11:45", "event": "Cybersecurity, Data Privacy & Trust", "speaker": "", "designation": ""},
    {"time": "11:45 – 12:15", "event": "Rising Voices: Student Journeys in Data & AI", "speaker": "Up to 3 student speakers (subject to registrations)", "designation": ""},
    {"time": "12:15 – 12:40", "event": "Featured Talk", "speaker": "Topic to be Confirmed", "designation": ""},
    {"time": "12:40 – 13:00", "event": "Decode Your Career Path: Interactive Quiz", "speaker": "", "designation": ""},
    {"time": "13:00 – 13:30", "event": "Lunch Break & Networking", "speaker": "", "designation": ""},
]

# -----------------------------------------

@app.route('/')
def home():
    return render_template(
        'index.html', 
        info=EVENT_INFO, 
        speakers=SPEAKERS, 
        agenda=AGENDA,
        team=TEAM,
        sponsors=SPONSORS
    )

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')

if __name__ == '__main__':
    app.run(debug=True)