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
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Rizvi%20Institute%20Logo.jpeg",
        "description": "Our esteemed host partner for WiDS Mumbai 2026."
    }
]

# Add your team members here. 
# You can add as many as you want.
TEAM = [
    {
        "name": "Hetvi Patel", 
        "role": "Final Year CSE Student at SCET, Surat\nIntern at 10 Turtle Global Pvt. Ltd.", 
        "city": "Surat", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Organizers/Hetvi%20Patel.png",
        "email": "hetvi1655@gmail.com",
        "linkedin": "https://www.linkedin.com/in/hetvi-patel-5a6467275/"
    },
    {
        "name": "Anita Nandi-Ray", 
        "role": "Co-founder & Policy Director at Kquanta Research", 
        "city": "Mumbai", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Organizers/Anita%20Nandi.jpeg",
        "email": "Anita.nandi-ray@kquantaresearch.com",
        "linkedin": "https://www.linkedin.com/in/anitanandi/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
    },
    {
        "name": "Barkha Jain", 
        "role": "International Speaker and Community Lead", 
        "city": "Pune", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Organizers/Barkha%20Jain.jpeg",
        "email": "barkhajain15sep@gmail.com",
        "linkedin": "https://www.linkedin.com/in/jbarkha/"
    },
    {
        "name": "Prof.(Dr.) Dhatri Pandya", 
        "role": "Professor at Sarvajanik College of Engineering and Technology(SCET), Surat", 
        "city": "Surat", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Organizers/Dhatri%20Pandya.jpeg",
        "email": "dhatri.pandya@scet.ac.in",
        "linkedin": "https://www.linkedin.com/in/dr-dhatri-pandya-a76569a8/"
    },
    {
        "name": "Prof.(Dr.) Pariza Kamboj", 
        "role": "Professor at Sarvajanik College of Engineering and Technology(SCET), Surat", 
        "city": "Surat", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Organizers/Pariza%20Kamboj.jpeg",
        "email": "pariza.kamboj@scet.ac.in",
        "linkedin": "https://www.linkedin.com/in/prof-dr-pariza-kamboj-37617616/"
    },
    {
        "name": "Shradhha Joshi", 
        "role": "Co-Founder & Head Of Marketing at Kquanta Research ", 
        "city": "Mumbai", 
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Organizers/Shraddha%20Joshi.jpeg",
        "email": "Shraddha.joshi@kquantaresearch.com",
        "linkedin": "https://www.linkedin.com/in/shraddha-joshi-14285461/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
    }
]

SPEAKERS = [
    {
        "name": "Chisoo Lyons",
        "title": "Executive Director, WiDS Worldwide",
        "topic": "Live Stream: Inaugural Remarks",
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Speakers/Chisoo%20Lyons.jpg",
        "bio": "Chisoo Lyons leads Women in Data Science Worldwide, a global non-profit dedicated to advancing women in data science. With strong academic credentials in Industrial Engineering from UC Berkeley and a leadership background driving analytics innovation at FICO, she now guides WiDS programs and global impact initiatives that expand access, opportunity, and community for underrepresented data professionals."
    },
    {
        "name": "Urvashi Kapoor",
        "title": "Senior Editor & AGM, Jagran Media",
        "topic": "Preventing Online Scams in the Age of AI: Practical Cyber Safety for Everyday Life",
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Speakers/Urvashi%20Kapoor.jpg",
        "bio": "Urvashi Kapoor is an award-winning journalist specializing in AI literacy, digital safety, and responsible technology use. She leads large-scale media literacy initiatives at Jagran New Media in collaboration with global organizations including Google and Meta. Through nationwide programs combating misinformation and promoting cyber awareness, she has emerged as a leading voice advancing ethical AI adoption and digital trust."
    },
    {
        "name": "Jaanvi Sharma",
        "title": "Founder & Chief Mason, Women Data Protection (WDP) Foundation",
        "topic": "Panel Discussion: Cybersecurity Risk & Data Privacy",
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Speakers/Janvi%20Sharma.jpg",
        "bio": "Advocate Jaanvi Sharma is a data protection lawyer specializing in global privacy regulations including GDPR and India’s DPDPA. She advises organizations on compliance strategy, privacy governance, and ethical data practices. Through her foundation, she promotes gender inclusion in cybersecurity and mentors aspiring privacy professionals, contributing to stronger and more responsible data governance ecosystems."
    },
    {
        "name": "Ekta Shah",
        "title": "Data Scientist, MSCI",
        "topic": "Panel Discussion: Cybersecurity Risk & Data Privacy",
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Speakers/Ekta%20Shah.jpg",
        "bio": "Ekta Shah is a data science professional with expertise in machine learning, artificial intelligence, and advanced analytics. She has hands-on experience across predictive modeling, NLP, reinforcement learning, and large-scale data systems. Passionate about applying analytics to real-world challenges, she also mentors emerging professionals and actively contributes to the data science community."
    },
    {
        "name": "Nirali Bhatia",
        "title": "Cyber Psychologist & Psychotherapist | Director - V4WEB | Founder - CyberB.A.A.P.",
        "topic": "Digital Safety Awareness, Mental Wellness, and Responsible Online Behaviour",
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Speakers/Nirali%20Bhatia.jpg",
        "bio": "Nirali Bhatia is a cyber psychologist and user behaviour expert with over two decades of experience studying the intersection of human behaviour and technology. She leads CyberB.A.A.P., India’s pioneering anti-cyberbullying initiative, and works with schools, corporates, and law enforcement to promote safer digital ecosystems. A TEDx speaker and counsellor, she specializes in digital safety awareness, mental wellness, and responsible online behaviour."
    },
    {
        "name": "Barkha Jain",
        "title": "CMX Connect Chapter",
        "topic": "Featured Talk: Ethics Driven AI - Building for Fairness",
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Organizers/Barkha%20Jain.jpeg",
        "bio": ""
    },
    {
        "name": "Anita Nandi-Ray",
        "title": "Co-Founder & Policy Director, Kquanta Research",
        "topic": "Moderator: Cybersecurity Risk & Data Privacy",
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Organizers/Anita%20Nandi.jpeg",
        "bio": ""
    },
    {
        "name": "Prof. Ajay Singh",
        "title": "Professor of Practice, Entrepreneurship Development & Cybersecurity",
        "topic": "Special Address: Shaping the Future - Emerging Technologies and the Next Generation",
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Speakers/Prof.%20Ajay%20Singh.jpg",
        "bio": "Prof. Ajay Singh is a veteran technology leader with 35+ years of experience in IT leadership, fintech innovation, and corporate governance. He has led global technology transformations across banking, telecom, and government sectors. A certified corporate director and academic, his expertise includes cyber risk management, digital governance, cyber forensics, and technology law."
    },
    {
        "name": "Pradeep Gogte",
        "title": "HR, Rizvi Institute of Management Studies and Research",
        "topic": "Panel Discussion: Future Proofing Careers",
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Speakers/Pradeep%20Gogte.jpg",
        "bio": "Pradeep Gogte is a seasoned HR leader with extensive experience across global corporations, premier academic institutions, and nonprofit organizations. He has led senior roles in talent strategy, corporate relations, and career services. As an academician, he focuses on mentoring future management professionals and strengthening industry readiness through practical human resource education."
    },
    {
        "name": "Rajesh Save",
        "title": "Impeccker Consulting LLP",
        "topic": "Panel Discussion: Future Proofing Careers",
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Speakers/Rajes%20Save.jpg",
        "bio": "Dr. Rajesh Save brings over three decades of experience spanning behavioral science, psychometrics, human resource strategy, and advanced analytics. He specializes in applying AI and machine learning to workforce transformation and people analytics. His work focuses on building intelligent, data-driven talent systems that help organizations enhance performance and future readiness."
    },
    {
        "name": "Dr. Shariq Nisar",
        "title": "Principal, Rizvi Institute of Management Studies and Research",
        "topic": "Moderator: Future Proofing Careers - Skills, Hiring and Placements in the Age of AI",
        "image": "https://raw.githubusercontent.com/HetviPatel1655/WiDS-Mumbai/main/static/Speakers/Dr%20Shariq%20Nisar.jpg",
        "bio": "Dr. Shariq Nisar is an economist and academic specializing in ethical finance and financial inclusion. He has advised leading financial institutions and government bodies while pioneering ethical investment frameworks in India. A globally recognized scholar and former Visiting Fellow at Harvard Law School, he contributes extensively to research, policy dialogue, and international academic forums."
    }
]

AGENDA = [
    {"time": "08:30 – 09:00", "event": "Registration", "speaker": "", "designation": ""},
    {"time": "09:00 – 09:30", "event": "Live Stream: Inaugural Remarks", "speaker": "Chisoo Lyons", "designation": "Executive Director, WiDS Worldwide"},
    {"time": "09:30 – 09:35", "event": "Context Setting", "speaker": "WiDS Ambassador", "designation": ""},
    {"time": "09:45 – 10:30", "event": "Panel Discussion: Cybersecurity Risk & Data Privacy", 
     "speaker": ["Jaanvi Sharma", "Ekta Shah", "Anita Nandi-Ray (Moderator)"], 
     "designation": ["Founder & Chief Mason, Women Data Protection Foundation", "Data Scientist, MSCI", "Co-Founder & Policy Director, Kquanta Research"]},
    {"time": "10:30 – 11:00", "event": "Livestream: Preventing Online Scams in the age of AI: Practical Cyber Safety for Everyday life", "speaker": "Urvashi Kapoor", "designation": "Senior Editor & AGM, Jagran Media"},
    {"time": "11:00 – 11:30", "event": "Special Address: Quantum Computing: Preparing for the Next Frontier of Technology", "speaker": "Prof. Ajay Singh", "designation": "Professor of Practice/Author/Fellow Institute of Directors <br> Former CEO/Advisory Board Member"},
    {"time": "11:30 – 12:00", "event": "TEA BREAK", "speaker": "", "designation": ""},
    {"time": "12:00 – 12:15", "event": "Featured Talk: Ethics Driven AI: Building for Fairness", "speaker": "Barkha Jain", "designation": "CMX Connect Chapter"},
    {"time": "12:15 – 12:50", "event": "Panel Discussion: Future Proofing careers: Skills, Hiring and Placements in the age of AI", 
     "speaker": ["Rajesh Save", "Pradeep Gogte", "Dr Shariq Nisar (Moderator)"], 
     "designation": ["Impeccker Consulting LLP", "HR, Rizvi Institute of Management Studies and Research", "Principal, RIMSR / Former Visiting Fellow, Harvard Law School"]},
    {"time": "12:50 – 13:00", "event": "Vote of thanks", "speaker": "WiDS Ambassador", "designation": ""},
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