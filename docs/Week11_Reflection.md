# Week 11 Reflection - Weather Dashboard Project

## 🔖 Section 0: Fellow Details

| Field | Your Entry |
|-------|------------|
| Name | Mindy Stricklin |
| GitHub Username | mstricklin6400 |
| Preferred Feature Track | Interactive |
| Team Interest | Yes - Project Owner |

## ✍️ Section 1: Week 11 Reflection

### Key Takeaways: What did you learn about capstone goals and expectations?
- Honestly, this capstone feels way bigger than I expected at first - it's not just about writing code that works, but making something I'm actually proud to show off
- The instructors keep emphasizing that it's better to have a simple app that works really well than something complicated that's half-broken
- I'm realizing documentation matters more than I thought - future me will thank present me for writing good comments!
- This project is basically my chance to prove I've actually learned something over these past 10 weeks
- Time management is going to be everything... I have a tendency to overthink things and get stuck in rabbit holes

### Concept Connections: Which Week 1–10 skills feel strongest? Which need more practice?
**Strongest Skills:**
- I'm pretty comfortable with basic Python stuff now - lists, dictionaries, loops don't make me panic anymore
- File operations are clicking for me, especially after all those practice exercises
- Writing functions feels natural now, and I'm getting better at breaking problems down into smaller pieces
- Try/except blocks saved my butt so many times, I actually remember to use them now!

**Need More Practice:**
- APIs still feel intimidating - like what if I break the internet? (I know that's not how it works but still...)
- Making pretty charts and graphs - my visualizations look like they're from 1995
- Tkinter makes my brain hurt sometimes, especially getting the layout to look decent
- I'm terrible at testing my own code properly - I usually just run it and hope for the best
- Object-oriented programming still feels like speaking a foreign language

### Early Challenges: Any blockers (e.g., API keys, folder setup)?
- The whole API key thing has me nervous - I've watched too many horror stories about people accidentally committing secrets to GitHub
- I'm second-guessing my folder structure constantly. Is this the "right" way to organize things? Who decides these things anyway?
- My GUI skills are... let's just say if this was a dating profile, I'd swipe left on my own interfaces
- Balancing this project with my other classes is gonna be tough - I tend to hyperfocus on one thing and forget everything else exists
- Data caching sounds fancy but I have no idea how to do it without making everything slower instead of faster

### Support Strategies: Which office hours or resources can help you move forward?
- Definitely need to hit up office hours for the API setup - I'd rather ask a "dumb" question than spend hours stuck
- The Slack channel has been super helpful for quick questions, especially when I'm coding at weird hours
- I should probably revisit some of the earlier course materials instead of just googling everything
- YouTube tutorials for Tkinter might be my saving grace - sometimes seeing someone else do it helps more than reading docs
- I'm going to try to schedule regular check-ins so I don't disappear into a coding cave for three days straight

## 🧠 Section 2: Feature Selection Rationale

| # | Feature Name | Difficulty (1–3) | Why You Chose It / Learning Goal |
|---|--------------|------------------|-----------------------------------|
| 1 | Current Weather Display | 2 | Gotta start somewhere! This is the bread and butter of any weather app |
| 2 | Weather History Tracking | 2 | I'm curious if I can spot patterns in my local weather - plus it's good practice with files |
| 3 | Weather Alerts System | 3 | This one scares me a little, but I want to challenge myself with some real logic |
| Enhancement | Weather Journal | - | Because sometimes you need to remember that rainy Tuesday when you felt amazing |

## 🗂️ Section 3: High-Level Architecture Sketch

```
weather-dashboard-mindy/
├── main.py                 # Entry point and main GUI
├── config.py              # Configuration and API settings
├── .env                   # Environment variables (API keys)
├── data/                  # Data storage
│   ├── weather_history.txt
│   └── journal_entries.json
├── features/              # Feature modules
│   ├── weather_display.py
│   ├── weather_history.py
│   ├── weather_alerts.py
│   └── weather_journal.py
├── utils/                 # Utility functions
│   ├── api_client.py
│   └── data_manager.py
└── docs/                  # Documentation
    └── Week11_Reflection.md
```

**Data Flow:**
1. User types in a location → My API client goes and fetches the weather data
2. The app processes all that JSON mess → Shows something readable on screen
3. Everything gets saved to files → So I can look back at the data later
4. User clicks on alerts or journal stuff → App responds accordingly (hopefully!)

## 📊 Section 4: Data Model Plan

| File/Table Name | Format | Example Row |
|-----------------|--------|-------------|
| weather_history.txt | txt | 2025-07-07,New Brunswick,NJ,75,Partly Cloudy,1015.2 |
| journal_entries.json | json | {"date": "2025-07-07", "mood": "Happy", "notes": "Beautiful weather today!"} |
| alert_preferences.json | json | {"temperature_threshold": 80, "condition_alerts": ["rain", "snow"]} |

## 📆 Section 5: Personal Project Timeline (Weeks 12–17)

| Week | Monday | Tuesday | Wednesday | Thursday | Key Milestone |
|------|--------|---------|-----------|----------|---------------|
| 12 | API setup & testing | Error handling implementation | Basic Tkinter GUI | Buffer/debugging day | Basic working app |
| 13 | Weather display feature | Data persistence setup | History tracking | Integration testing | Feature 1 complete |
| 14 | Weather alerts start | Alert logic implementation | User preferences | Testing & refinement | Feature 2 complete |
| 15 | Weather journal feature | GUI polish & UX | Error handling review | Code refactoring | All features complete |
| 16 | Enhancement completion | Documentation writing | Unit tests creation | Final packaging | Ready-to-ship app |
| 17 | Demo preparation | Buffer time | Final showcase | Reflection | Demo Day |

## ⚠️ Section 6: Risk Assessment

| Risk | Likelihood | Impact | Mitigation Plan |
|------|------------|--------|-----------------|
| API Rate Limit | Medium | Medium | Cache stuff so I'm not hitting the API constantly, maybe add some delays |
| GUI Looking Terrible | High | Medium | Start simple and ugly, make it work first, pretty later |
| Running Out of Time | High | High | Set daily goals and actually stick to them, cut features if I have to |
| Accidentally Deleting Data | Low | High | Backup everything, maybe validate data before saving it |
| Commiting API Keys | Medium | High | Use .env files religiously, double-check before every commit |

## 🤝 Section 7: Support Requests

**Specific help I'll ask for in office hours or on Slack:**
- How to set up APIs without breaking everything (seriously, I'm paranoid about this)
- Is my project structure decent or am I doing it completely wrong?
- Tkinter layout tips - why does everything look so cramped?
- Best practices for handling errors gracefully instead of just crashing
- Can someone review my code and tell me if it's terrible before I submit it?
- How to test API-dependent code when I don't want to use up my API calls
- Any tips for presenting without having a panic attack?

## ✅ Section 8: Before Monday (Start of Week 12)

**Setup steps to complete before Monday:**
- [x] Create project structure with main.py, config.py, and /data/ folder
- [x] Get that OpenWeatherMap API key set up (and NOT commit it to GitHub!)
- [x] Create basic skeleton files for my features so I have something to work with
- [x] Write a decent README that explains what this thing is supposed to do
- [ ] Maybe book office hours if the API setup goes sideways
- [ ] Test that I can actually connect to the API without everything exploding

## 📤 Final Submission Checklist:
- [x] Week11_Reflection.md completed
- [x] File uploaded to GitHub repo /docs/
- [ ] Repo link submitted on Canvas
