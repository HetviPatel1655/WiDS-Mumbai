from flask import Flask, render_template

app = Flask(__name__)

# --- CONFIGURATION (EDIT THIS SECTION) ---

EVENT_INFO = {
    "year": "2026",
    "date": "March 14, 2026",
    "time": "9:00 AM - 5:00 PM IST",
    "venue": "To Be Announced, Mumbai",
    "description": "WiDS Mumbai is a flagship location for the WiDS India Conference 2026, alongside Delhi and Bangalore. Representing the Western Region, we bring together Ambassadors from Mumbai, Pune, and Surat.",
    "registration_link": "https://docs.google.com/forms/d/e/1FAIpQLSeg45Skd91dYkGdhle1ycfzV8a3-1xFl-VZlEnKddA4tmIDJw/viewform", 
    "contact_email": "wids.mumbai@example.com"
}

# Add your team members here. 
# You can add as many as you want.
TEAM = [
    {"name": "Ambassador Name 1", "role": "Lead Ambassador", "city": "Mumbai", "image": "team1.jpg"},
    {"name": "Ambassador Name 2", "role": "Co-Organizer", "city": "Pune", "image": "team2.jpg"},
    {"name": "Ambassador Name 3", "role": "Co-Organizer", "city": "Surat", "image": "team3.jpg"},
    {"name": "Ambassador Name 4", "role": "Program Chair", "city": "Mumbai", "image": "team4.jpg"},
]

SPEAKERS = [
    {
        "name": "Dr. Aditi Sharma",
        "title": "Head of AI, Tech Corp",
        "topic": "Generative AI in Healthcare",
        "image": "speaker1.jpg"
    },
    {
        "name": "Sarah Johnson",
        "title": "Lead Data Scientist",
        "topic": "Ethics in Machine Learning",
        "image": "speaker2.jpg"
    },
]

AGENDA = [
    {"time": "09:00 AM", "event": "Registration & Networking"},
    {"time": "10:00 AM", "event": "Welcome Note: WiDS India Western Region"},
    {"time": "10:30 AM", "event": "Keynote Speech"},
    {"time": "01:00 PM", "event": "Lunch Break"},
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

if __name__ == '__main__':
    app.run(debug=True)