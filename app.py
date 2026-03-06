from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# --- CONFIGURATION (EDIT THIS SECTION) ---

EVENT_INFO = {
    "year": "2026",
    "date": "March 14, 2026",
    "time": "8:30 hrs to 14:00 hrs",
    "venue": "New Rizvi Education Complex, Mumbai.",
    "description": "WiDS Mumbai 2026 (Women in Data Science Worldwide Conference-2026) is held in association with Rizvi Institute of Management & Research (RIMSR). Representing the Western Region, we bring together data science enthusiasts and leaders.",
    "registration_link": "https://luma.com/event/evt-dzgEu4qyi1eSXmM", 
    "contact_email": "widsmumbaiconference@gmail.com",
    "sponsorship_link": "https://docs.google.com/forms/d/e/1FAIpQLSd-Ai0gRh_59YZ-AGilYZ44B1Ce0vySzbFtAquiXJkF6IU0Fg/viewform?usp=header",
    "sponsorship_email": "widsmumbaiconference@gmail.com"
}

SPONSORS = [
    {
        "name": "Rizvi Institute of Management & Research (RIMSR)",
        "role": "Venue Partner",
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Rizvi%20LOGO.jpeg",
        "description": "Our esteemed host partner for WiDS Mumbai 2026."
    }
]

# Add your team members here. 
# You can add as many as you want.
TEAM = [
    {
        "name": "Hetvi Patel", 
        "role": "Final Year CSE Student at SCET, Surat\nIntern at 10Turtle Global Pvt. Ltd.", 
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
        "name": "Prof.(Dr.) Pariza Kamboj", 
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
        "name": "Chisoo Lyons",
        "title": "Executive Director, WiDS Worldwide",
        "topic": "Live Stream: Inaugural Remarks",
        "image": ""
    },
    {
        "name": "Urvashi Kapoor",
        "title": "Senior Editor & AGM, Jagran Media",
        "topic": "Preventing Online Scams in the Age of AI: Practical Cyber Safety for Everyday Life",
        "image": "Speakers/Urvashi Kapoor.jpg"
    },
    {
        "name": "Dr Shariq Nisar",
        "title": "Principal, Rizvi Institute of Management Studies and Research",
        "topic": "Moderator: Future Proofing Careers - Skills, Hiring and Placements in the Age of AI",
        "image": "Speakers/Dr Shariq Nisar.jpg"
    },
    {
        "name": "Ekta Shah",
        "title": "Data Scientist, MSCI",
        "topic": "Panel Discussion: Cybersecurity Risk & Data Privacy",
        "image": "Speakers/Ekta Shah.jpg"
    },
    {
        "name": "Jaanvi Sharma",
        "title": "Founder & Chief Mason, Women Data Protection (WDP) Foundation",
        "topic": "Panel Discussion: Cybersecurity Risk & Data Privacy",
        "image": "Speakers/Janvi Sharma.jpg"
    },
    {
        "name": "Pradeep Gogte",
        "title": "HR, Rizvi Institute of Management Studies and Research",
        "topic": "Panel Discussion: Future Proofing Careers",
        "image": "Speakers/Pradeep Gogte.jpg"
    },
    {
        "name": "Prof. Ajay Singh",
        "title": "Professor of Practice, Entrepreneurship Development & Cybersecurity",
        "topic": "Special Address: Shaping the Future - Emerging Technologies and the Next Generation",
        "image": "Speakers/Prof. Ajay Singh.jpg"
    },
    {
        "name": "Rajesh Save",
        "title": "Impeccker Consulting LLP",
        "topic": "Panel Discussion: Future Proofing Careers",
        "image": "Speakers/Rajes Save.jpg"
    },
    {
        "name": "Anita Nandi-Ray",
        "title": "Co-Founder & Policy Director, Kquanta Research",
        "topic": "Moderator: Cybersecurity Risk & Data Privacy",
        "image": "Anita Nandi.jpeg"
    },
    {
        "name": "Barkha Jain",
        "title": "CMX Connect Chapter",
        "topic": "Featured Talk: Ethics Driven AI - Building for Fairness",
        "image": "Barkha Jain.jpeg"
    }
]

AGENDA = [
    {"time": "08:30 – 09:00", "event": "Registration", "speaker": "", "designation": ""},
    {"time": "09:00 – 09:30", "event": "Live Stream: Inaugural Remarks", "speaker": "Chisoo Lyons", "designation": "Executive Director, WiDS Worldwide"},
    {"time": "09:30 – 09:35", "event": "Context Setting", "speaker": "WiDS Ambassador", "designation": ""},
    {"time": "09:45 – 10:30", "event": "Panel Discussion: Cybersecurity Risk & Data Privacy", "speaker": "Jaanvi Sharma, Ekta Shah, Anita Nandi-Ray (Moderator)", "designation": "Women Data Protection Foundation | MSCI | Kquanta Research"},
    {"time": "10:30 – 11:00", "event": "Live Stream: Preventing Online Scams in the Age of AI: Practical Cyber Safety for Everyday Life", "speaker": "Urvashi Kapoor", "designation": "Senior Editor & AGM, Jagran Media"},
    {"time": "11:00 – 11:30", "event": "Special Address: Shaping the Future - Emerging Technologies and the Next Generation", "speaker": "Prof. Ajay Singh", "designation": "Professor of Practice, Entrepreneurship Development & Cybersecurity"},
    {"time": "11:30 – 12:00", "event": "Tea Break", "speaker": "", "designation": ""},
    {"time": "12:00 – 12:15", "event": "Featured Talk: Ethics Driven AI - Building for Fairness", "speaker": "Barkha Jain", "designation": "CMX Connect Chapter"},
    {"time": "12:15 – 12:50", "event": "Panel Discussion: Future Proofing Careers - Skills, Hiring and Placements in the Age of AI", "speaker": "Rajesh Save, Pradeep Gogte, Dr Shariq Nisar (Moderator)", "designation": "Impeccker Consulting LLP | RIMSR HR | Principal, RIMSR"},
    {"time": "12:50 – 13:00", "event": "Vote of Thanks", "speaker": "WiDS Ambassador", "designation": ""},
    {"time": "13:00 – 14:00", "event": "Lunch & Networking", "speaker": "", "designation": ""},
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