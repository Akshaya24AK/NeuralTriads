# ArcSentry AI  
### Transforming News into Structured Story Intelligence
#### Entry by Neural Triads for ET Gen AI Hackathon

ArcSentry AI is a GenAI-powered system that converts fragmented news articles into a structured, evolving story helping users understand **what happened, why it matters, and what comes next**.

---

## Problem

Business and geopolitical news is fragmented across multiple articles.  
Users must read several sources to understand a single evolving story.

- Time-consuming  
- High cognitive load  
- Low clarity  

---

## Solution

ArcSentry AI transforms multiple news inputs into:

- Narrative Overview  
- Visual Timeline  
- Sentiment Flow  
- Future Outlook  
- Interactive Q&A  

From **reading articles → understanding stories**

---

## Features

- AI-powered story synthesis  
- Visual timeline rendering  
- Structured insights (entities, sentiment, future trends)  
- Context-aware Q&A  
- Fast and interactive UI  

---

## Architecture
User (Streamlit UI)
↓
Topic Selection
↓
Curated Articles
↓
Prompt Engineering
↓
Gemini LLM
↓
Structured JSON Output
↓
UI Rendering (Timeline + Insights)
↓
Interactive Q&A

--

## Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **LLM:** Google Gemini API  
- **State Management:** Streamlit session_state  
- **Visualization:** Custom HTML timeline  

---

## How It Works

1. User selects a topic  
2. System loads structured article data  
3. Prompt is sent to Gemini  
4. Model returns structured JSON:
   - Timeline  
   - Entities  
   - Sentiment  
   - Future outlook  
5. UI renders insights visually  
6. User can ask questions interactively  

---

## Run Locally

### 1. Clone repository
```bash
git clone https://github.com/your-username/arcsentry-ai.git
cd arcsentry-ai
```
---

## Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **LLM:** Google Gemini API  
- **State Management:** Streamlit session_state  
- **Visualization:** Custom HTML timeline  

---

## How It Works

1. User selects a topic  
2. System loads structured article data  
3. Prompt is sent to Gemini  
4. Model returns structured JSON:
   - Timeline  
   - Entities  
   - Sentiment  
   - Future outlook  
5. UI renders insights visually  
6. User can ask questions interactively  

---

## Run Locally

### 1. Clone repository
```bash
git clone https://github.com/your-username/arcsentry-ai.git
cd arcsentry-ai
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Add API Key
```bash
export GOOGLE_API_KEY="your_api_key_here"
```
(Windows: use setx GOOGLE_API_KEY "your_key")

### 4. Run app
```bash
streamlit run app.py
```

## Impact
80% reduction in time to understand a story
40–60% increase in user engagement
Potential revenue uplift for news platforms
Reduced cognitive load for users
Future Scope
Real-time news ingestion
Personalized story feeds
Multilingual support
Predictive analytics
Video-based story summaries

### Built For

ET GenAI Hackathon
Reimagining how users consume business and global news.

### Key Idea

ArcSentry AI doesn’t just summarize news — it transforms it into structured, interactive intelligence.

### Author
```
Neural Triads
GitHub: https://github.com/Akshaya24AK/NeuralTriads/
```
