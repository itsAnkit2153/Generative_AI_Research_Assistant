# 📚 Generative AI Research Assistant

A **Multi-Agent AI System** that automatically researches a topic from the internet, analyzes the collected information, and generates a structured research report.

Built using **CrewAI, Groq LLM, Serper Search API, and Streamlit**.

---

# 🚀 Project Overview

Researching a new topic usually requires:

- Searching multiple sources  
- Reading articles  
- Extracting key insights  
- Analyzing data  
- Writing reports  

This project **automates the entire research workflow** using **AI agents**.

The system works like a **virtual research team** where each AI agent has a specific role.

---


## 🧠 System Architecture

1. **User Input (Research Topic)**  
   The user enters a research topic through the Streamlit interface.

2. **Streamlit Interface**  
   The Streamlit web application collects the user input and sends it to the CrewAI system.

3. **CrewAI Multi-Agent System**  
   CrewAI coordinates multiple AI agents and manages the workflow between them.

4. **Research Specialist Agent**  
   This agent gathers information related to the research topic.

5. **Internet Search (Serper API)**  
   The research agent uses the Serper API to search the internet and collect relevant data, statistics, and expert opinions.

6. **Data Analyst Agent**  
   The analyst agent reviews the research findings and extracts patterns, trends, and key insights.

7. **Content Writer Agent**  
   The writer agent combines the research findings and analysis to create a well-structured research report.

8. **Final Research Report**  
   The system generates a complete research report including:
   - Executive Summary  
   - Introduction  
   - Main Findings  
   - Analysis and Insights  
   - Conclusions  
   - Sources



---

# 🤖 AI Agents

The system uses **three specialized agents**.

---

## 🔎 Research Specialist Agent

**Role:** Gather information from the internet.

**Responsibilities**

- Search for relevant information  
- Collect key facts and statistics  
- Identify expert opinions  
- Find recent developments  
- Organize research findings  

**Tool Used**
SerperDevTool (Google Search API)
**Output**
research_findings.md


---

## 📊 Data Analyst Agent

**Role:** Analyze research findings.

**Responsibilities**

- Identify patterns and trends  
- Extract key insights  
- Interpret research data  
- Provide analytical conclusions  

**Output**
analysis_report.md


---

## ✍ Content Writer Agent

**Role:** Generate the final professional report.

**Responsibilities**

- Combine research findings and analysis  
- Structure the report clearly  
- Write executive summary  
- Provide conclusions and recommendations  

**Output**
final_report.md


---

# ⚙️ Technologies Used

| Technology | Purpose |
|--------|--------|
| Python | Core programming language |
| CrewAI | Multi-agent orchestration |
| Groq | High-speed LLM inference |
| Serper API | Real-time internet search |
| Streamlit | Interactive web interface |

---

# 🌐 Streamlit Interface

The web interface allows users to:

- Enter a research topic  
- Start the research process  
- View results in structured tabs  

Tabs include:
Research Findings, 
 Analysis Report,
  Final Report,
