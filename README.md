# Prospera

**Find businesses without websites , sorted by urgency.**

Prospera is a lead-generation tool that helps consultants, freelancers, and service providers identify high-potential business prospects who don't yet have an online presence.

## Overview

Prospera uses the Google Maps API to search for businesses in a specific location and business type, then filters for those without websites. It ranks them by urgency based on review count, rating, and business category—helping you prioritize which leads to reach out to first.

## Features

- **Location-based search** — Find businesses in any area using Google Maps
- **Website detection** — Automatically identifies businesses without websites
- **Urgency scoring** — Ranks leads by:
  - Review count (popularity signal)
  - Rating (quality signal)
  - Business type (trust categories like doctors, lawyers, hotels rank higher)
  - Contact availability (phone number presence)
- **Export to CSV** — Download your results for outreach campaigns
- **Direct Google Maps links** — Quick access to view each business on Google Maps

## How It Works

1. **Enter a location** — Be specific (e.g., "Ramankulangara, Kollam" instead of just "Kollam")
2. **Select business type** — Choose from restaurant, doctor, dentist, gym, lawyer, hotel, beauty_salon, school
3. **Search** — Prospera fetches all businesses matching your criteria
4. **Review results** — See urgency ratings and key metrics
5. **Export and outreach** — Download CSV and start your sales process

## Urgency Labels

- 🔴 **URGENT** (score ≥ 80) — High-priority leads with strong signals
- 🟡 **MEDIUM** (score ≥ 50) — Moderate priority, worth reaching out to
- 🟢 **LOW** (score < 50) — Lower priority, but still potential

## Real-World Validation

Prospera was validated with a real user , a consultant building QR-code ordering solutions for restaurants. He used Prospera to:
- Identify restaurants without websites in his target area
- Reach out to 50+ restaurants
- Close 2 paying customers in initial outreach

**Key insight from validation:** Businesses don't need websites; they need operational solutions. Prospera helps identify which businesses have problems you can solve.

## Tech Stack

- **Frontend** — Streamlit (Python-based UI)
- **Backend** — FastAPI/Python
- **APIs** — Google Maps Places API
- **Deployment** — Streamlit Cloud

## Setup

### Requirements

- Python 3.8+
- Google Maps API key
- `.env` file with:
  ```
  API_KEY=your_google_maps_api_key
  ```

### Installation

```bash
git clone https://github.com/MaAs0706/maps-scrapper.git
cd maps-scrapper
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Running Locally

```bash
streamlit run app.py
```

Then visit `http://localhost:8502` in your browser.

### Deploying to Streamlit Cloud

1. Push to GitHub
2. Connect your repo to Streamlit Cloud
3. Add secrets in Streamlit Cloud settings:
   ```
   API_KEY=your_google_maps_api_key
   ```
4. Deploy

## Project Journey

### Initial Concept
Started as a way to help web designers find potential clients (restaurants without websites). Built with Streamlit to get an MVP out quickly.

### Validation
Shared with a friend who was building QR-code ordering solutions for restaurants. He used it to:
- Validate the tool was useful
- Identify target restaurants
- Close initial customers

### Learnings
- **Websites aren't the pain point** — Restaurants care about operational efficiency, not digital presence
- **Lead-gen tools need context** — Raw data is less useful than ranked, prioritized leads
- **Real users beat hypothetical ones** — One actual user testing the tool taught us more than months of theorizing

### Evolution
Initially explored adding AI-powered pain point extraction from reviews (using Groq API), but discovered:
- Review-based inference isn't reliable for operational needs
- You need to talk to businesses directly
- The tool's value is in finding leads quickly, not predicting their problems

## Current Status

Prospera is a **working tool**, not a startup. It solves a real problem for consultants and service providers looking to identify and prioritize business prospects.

**What it does well:**
- Finds businesses without websites
- Ranks by urgency signals
- Exports data for outreach

**What it doesn't do:**
- Guarantee specific pain points from reviews
- Automate the actual sales process
- Predict revenue potential

## Future Directions

Possible enhancements (not planned, just possibilities):
- Industry-specific urgency scoring
- Integration with CRM tools
- Automated outreach templates
- A/B testing of outreach messages
- Conversion tracking dashboard

However, these would only be built if:
1. Real users asked for them
2. They solved a concrete problem
3. There was willingness to pay

## Conclusion

**This project concludes here.** Prospera works, solves a real problem for real users, and serves as a proof point that you can validate ideas by shipping quickly and getting user feedback.

The biggest lesson: Don't overthink it. Build something, test it with real people, learn from their usage, then decide what's next. Prospera did that successfully.

---

**Built by:** Aswanth Madhav  
**GitHub:** [@MaAs0706](https://github.com/MaAs0706)  
**Status:** Completed MVP, actively used by at least one consultant  
**License:** MIT
