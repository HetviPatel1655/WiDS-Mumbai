from flask import Flask, render_template

app = Flask(__name__)

# --- CONFIGURATION (EDIT THIS SECTION) ---
# As a Python user, you can just update these dictionaries to change the website!

EVENT_INFO = {
    "year": "2026",
    "date": "March 8, 2026",
    "time": "9:00 AM - 5:00 PM IST",
    "venue": "To Be Announced, Mumbai",
    "gmap_link": "#",  # Add Google Maps link later
    "registration_link": "https://forms.google.com/...", # YOUR REGISTRATION LINK
    "contact_email": "wids.mumbai@example.com",
    "hero_image": "hero.jpg" # Name of image in static folder
}

SPEAKERS = [
    {
        "name": "Dr. Aditi Sharma",
        "title": "Head of AI, Tech Corp",
        "topic": "Generative AI in Healthcare",
        "image": "speaker1.jpg" # Name of image in static folder
    },
    {
        "name": "Sarah Johnson",
        "title": "Lead Data Scientist",
        "topic": "Ethics in Machine Learning",
        "image": "speaker2.jpg"
    },
    # Copy/Paste to add more speakers...
]

AGENDA = [
    {"time": "09:00 AM", "event": "Registration & Breakfast"},
    {"time": "10:00 AM", "event": "Keynote Speech"},
    {"time": "11:30 AM", "event": "Panel Discussion: Women in AI"},
    {"time": "01:00 PM", "event": "Lunch & Networking"},
]

# -----------------------------------------

@app.route('/')
def home():
    return render_template(
        'index.html', 
        info=EVENT_INFO, 
        speakers=SPEAKERS, 
        agenda=AGENDA
    )

if __name__ == '__main__':
    app.run(debug=True)