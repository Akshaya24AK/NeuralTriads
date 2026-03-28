import streamlit as st
import json
import google.generativeai as genai
import streamlit.components.v1 as components

# --- Page Setup ---
st.set_page_config(page_title="ArcSentry AI", layout="wide")

# --- Styling ---
st.markdown("""
<style>
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #1c1f26;
    margin-bottom: 15px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.3);
    color: #00ffae;
}
.badge-positive { color: #00ffae; font-weight: bold; }
.badge-negative { color: #ff4b4b; font-weight: bold; }
.badge-neutral { color: #ffaa00; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.title("ArcSentry AI")
st.subheader("Turn fragmented news into a living story")

# --- Sidebar ---
st.sidebar.header("Select Story")
topic = st.sidebar.selectbox(
    "Choose a topic",
    [
        "AI Industry Boom",
        "ETGenAI Hackathon",
        "Strait of Hormuz Crisis",
        "IPL T20 2026",
        "Search for Life in Exoplanets"
    ]
)

# --- Articles ---
ARTICLES = {

"AI Industry Boom": """
STORY OVERVIEW:
The AI industry has rapidly evolved from experimental research into a global technological revolution.
What began with niche applications has now expanded into enterprise-scale adoption across industries such as finance, healthcare, and education.
Tech giants and startups are competing aggressively, investing billions into building advanced AI models and infrastructure.
At the same time, concerns around ethics, bias, and governance are shaping regulatory frameworks worldwide.
AI is no longer a supporting tool—it is becoming the backbone of digital transformation and economic growth.
This shift is redefining productivity, innovation cycles, and competitive advantage across global markets.

TIMELINE:
Jan 2023 | ChatGPT adoption surge
ChatGPT reached millions of users within months, showcasing the real-world power of generative AI.
This milestone marked the transition of AI from research labs into mainstream consumer and enterprise use.

Mar 2023 | Big Tech AI race intensifies
Companies like Google, Microsoft, and OpenAI accelerated investments in AI development.
This triggered a competitive race to dominate the AI ecosystem and redefine digital platforms.

Sep 2024 | Enterprise AI adoption rises
Organizations began embedding AI copilots into workflows, improving efficiency and decision-making.
AI started delivering measurable business value across sectors.

Jan 2025 | Regulatory frameworks emerge
Governments introduced AI regulations focusing on transparency, safety, and data privacy.
This marked the beginning of structured governance for AI technologies.

2026 | AI becomes core infrastructure
AI transitioned into a foundational layer powering products, services, and operations globally.
Businesses now rely on AI as a strategic necessity rather than an optional capability.
""",

"ETGenAI Hackathon": """
STORY OVERVIEW:
The ET GenAI Hackathon represents a major initiative to democratize artificial intelligence innovation.
It brings together developers, students, and professionals to build real-world solutions using generative AI.
The competition spans multiple domains including fintech, healthcare, and media.
Participants are encouraged to move beyond theoretical ideas and create scalable, impactful prototypes.
The hackathon reflects the broader shift of AI from experimentation to practical implementation.
It also highlights the growing importance of collaborative innovation in solving complex real-world problems.

TIMELINE:
Dec 2025 | Hackathon announced
The Economic Times launched a nationwide GenAI hackathon to foster innovation.
This created a platform for diverse participants to engage with cutting-edge AI technologies.

Jan 2026 | Registrations surge
Thousands of participants registered across domains, showing strong interest in GenAI.
The scale of participation highlighted the growing demand for AI-driven innovation.

Feb 2026 | Idea submission phase
Teams submitted solutions addressing real-world problems across industries.
Ideas ranged from fintech solutions to healthcare assistants and media intelligence tools.

Mar 2026 | Shortlisting of teams
Top teams were selected based on originality, feasibility, and potential impact.
This stage filtered high-quality ideas for deeper development.

Apr 2026 | Prototype development phase
Finalists began building working prototypes and preparing for evaluation.
This phase emphasized execution, usability, and real-world applicability.
""",

"Strait of Hormuz Crisis": """
STORY OVERVIEW:
The Strait of Hormuz is one of the world’s most critical oil transit chokepoints, carrying a significant portion of global energy supply.
Rising geopolitical tensions in the Middle East have made the region increasingly unstable.
Any disruption in this narrow waterway has immediate ripple effects on global markets and energy security.
The crisis highlights the vulnerability of global supply chains and overdependence on specific trade routes.
Governments and organizations are forced to balance diplomacy, security, and economic stability.
This situation underscores the importance of diversification and resilience in global trade infrastructure.

TIMELINE:
Jun 2025 | Geopolitical tensions escalate
Conflicts in the region increased instability around the Strait of Hormuz.
This raised concerns about the safety of global oil shipments.

Aug 2025 | Oil shipment disruptions begin
Tanker movements slowed due to security threats and uncertainty.
Supply chain disruptions began affecting global energy markets.

Sep 2025 | Oil prices surge globally
Reduced supply and uncertainty led to a sharp increase in crude oil prices.
Markets reacted strongly, impacting inflation and economic outlooks.

Oct 2025 | Diplomatic negotiations initiated
Global powers began diplomatic talks to stabilize the region.
Efforts focused on ensuring safe passage for oil shipments.

2026 | Trade route diversification
Countries explored alternative routes and energy strategies.
This reduced dependency on the Strait and improved resilience.
""",

"IPL T20 2026": """
STORY OVERVIEW:
IPL 2026 continues to establish itself as one of the most valuable and widely followed sports leagues globally.
The tournament combines high-quality cricket with massive commercial and entertainment value.
Emerging players are gaining prominence alongside established stars, reshaping team dynamics.
Digital platforms and streaming services are driving record-breaking viewership numbers.
Sponsorship deals and media rights are reaching unprecedented levels.
IPL is not just a sporting event—it is a global business and entertainment phenomenon.

TIMELINE:
Dec 2025 | IPL auction sets new benchmarks
Franchises invested heavily in emerging and international talent.
This shaped team strategies and increased competition levels.

Mar 2026 | Tournament kickoff
IPL 2026 began with high fan engagement and global attention.
Opening matches set the tone for an exciting season.

Apr 2026 | Breakout performances by new players
Young players delivered match-winning performances under pressure.
This marked a shift in team dynamics and future talent recognition.

May 2026 | Record-breaking viewership
Streaming platforms reported the highest-ever audience numbers.
Digital engagement significantly boosted league value.

Jun 2026 | Finals and commercial success
The season concluded with record sponsorship and revenue figures.
IPL reinforced its position as a global sports powerhouse.
""",

"Search for Life in Exoplanets": """
STORY OVERVIEW:
The search for life beyond Earth has entered a transformative phase with advancements in space exploration technology.
Scientists are identifying potentially habitable exoplanets using powerful telescopes and data analysis tools.
Organizations like NASA and ESA are focusing on detecting biosignatures in distant atmospheres.
Artificial intelligence is playing a key role in analyzing massive datasets from space missions.
These discoveries are bringing humanity closer to answering fundamental questions about life beyond Earth.
Global collaboration is accelerating research and expanding our understanding of the universe.

TIMELINE:
2023 | Discovery of habitable exoplanets
Scientists identified Earth-like planets within habitable zones.
This increased the possibility of finding life beyond Earth.

2024 | Breakthroughs using James Webb Telescope
Advanced atmospheric analysis revealed potential biosignatures.
This marked a major leap in space observation capabilities.

2025 | Expansion of space missions
NASA and ESA launched new missions focused on detecting life.
Research efforts became more targeted and advanced.

Early 2026 | AI-driven detection improves accuracy
AI models enhanced the identification of habitable environments.
This improved efficiency in analyzing vast space data.

2026 | Global collaboration accelerates research
International agencies began sharing data and insights.
This boosted collective progress in space exploration.
"""
}

articles = ARTICLES[topic]

# --- Gemini Setup ---
genai.configure(api_key="ADD API KEY HERE")
model = genai.GenerativeModel("gemini-2.5-flash")

# --- Initialize Session ---
if "data" not in st.session_state:
    st.session_state["data"] = None

# --- Generate Function ---
def generate_story_arc(text):
    prompt = f"""
    You are an expert analyst.

    Use STORY OVERVIEW for context.
    Extract timeline from TIMELINE.

    Return STRICT JSON:

    {{
      "timeline": [{{"date":"","event":"","impact":""}}],
      "entities": [{{"name":"","role":"","type":""}}],
      "sentiment_flow": [{{"phase":"","sentiment":"","reason":""}}],
      "future_outlook": [{{"prediction":""}}]
    }}

    Articles:
    {text}
    """
    return model.generate_content(prompt).text

# --- Generate Button ---
if st.button("🚀 Generate Story Arc"):
    with st.spinner("Analyzing story..."):
        output = generate_story_arc(articles)

    try:
        output = output.replace("```json", "").replace("```", "").strip()
        data = json.loads(output)

        st.session_state["data"] = data
        st.session_state["articles"] = articles
        st.session_state["topic"] = topic

    except:
        st.error("Parsing failed")
        st.text(output)

# --- Display ---
if st.session_state["data"]:
    data = st.session_state["data"]
    articles = st.session_state["articles"]
    topic = st.session_state["topic"]

    # --- Story Overview ---
    story_text = articles.split("TIMELINE:")[0].replace("STORY OVERVIEW:", "").strip()

    st.markdown("## 📖 Story Overview")
    st.markdown(f'<div class="card">{story_text}</div>', unsafe_allow_html=True)

    # --- Timeline ---
    st.markdown("## 🕰️ Timeline")

    timeline_items = ""
    for item in data["timeline"]:
        timeline_items += f"""
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <div class="timeline-date">{item['date']}</div>
                <div class="timeline-event">{item['event']}</div>
                <div class="timeline-impact">{item['impact']}</div>
            </div>
        </div>
        """

    timeline_html = f"""
    <html>
    <head>
    <style>
    body {{ background-color:#0e1117; color:white; font-family:Arial; }}
    .timeline {{ padding-left:40px; }}
    .timeline::before {{
        content:''; position:absolute; left:15px; width:3px; height:100%; background:#444;
    }}
    .timeline-item {{ margin-bottom:25px; position:relative; }}
    .timeline-dot {{
        position:absolute; left:-2px; top:5px; width:12px; height:12px;
        background:#00ffae; border-radius:50%;
    }}
    .timeline-content {{
        background:#1c1f26; padding:15px; border-radius:10px; margin-left:20px;
    }}
    .timeline-date {{ color:#00ffae; font-weight:bold; }}
    .timeline-event {{ font-weight:bold; margin-top:5px; }}
    .timeline-impact {{ color:#ccc; font-style:italic; margin-top:5px; }}
    </style>
    </head>
    <body>
    <div class="timeline">
    {timeline_items}
    </div>
    </body>
    </html>
    """

    components.html(timeline_html, height=400, scrolling=True)

    # --- Future ---
    st.markdown("## 🔮 What to Watch Next")
    future_html = "<div class='card'>"
    for f in data["future_outlook"]:
        future_html += f"<p>• {f['prediction']}</p>"
    future_html += "</div>"
    st.markdown(future_html, unsafe_allow_html=True)

# --- Q&A ---
st.markdown("---")
st.markdown("## 💬 Ask About This Story")

user_q = st.text_input("Ask a question")

if st.button("Ask"):
    if user_q and st.session_state["data"]:
        q_prompt = f"""
You are analyzing the story: "{st.session_state['topic']}"

Use ONLY this:
{st.session_state['articles']}

Question: {user_q}
"""

        res = model.generate_content(q_prompt)
        st.session_state["answer"] = res.text

if "answer" in st.session_state:
    st.markdown(f'<div class="card">{st.session_state["answer"]}</div>', unsafe_allow_html=True)
