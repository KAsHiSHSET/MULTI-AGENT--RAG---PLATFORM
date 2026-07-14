# 🤖 Multi-Tool Agentic RAG Assistant

An intelligent **Agentic Retrieval-Augmented Generation (RAG)** system built using **LangGraph**, **Groq Llama 3.3**, **FAISS**, and **HuggingFace Embeddings**.

Unlike traditional RAG chatbots, this project uses a **ReAct-based AI Agent** capable of selecting specialized tools autonomously to answer different categories of user queries, including document retrieval, GitHub repository analysis, research paper search, SQL generation, Python code generation, architecture diagram generation, and mathematical reasoning.

<img width="1284" height="822" alt="image" src="https://github.com/user-attachments/assets/2de76ce6-fbda-4b19-bcd9-c87871c639de" />


Deployed link for project:- [link](https://multi-agent--rag---platformkashish.streamlit.app/)
---

# ✨ Features

- 🤖 LangGraph ReAct Agent
- 🧠 Smart Keyword-Based Tool Routing
- 🔑 User Provided Groq API Key
- 🎛 Runtime Model Selection
- 📄 Retrieval-Augmented Generation (RAG)
- 📚 HuggingFace Sentence Transformer Embeddings
- ⚡ Groq Llama Models
- 🔍 FAISS Vector Search
- 🐍 Python Code Generation & Execution
- 🗄 SQL Query Generator
- 📊 Mermaid Diagram Generator
- 🐙 GitHub Repository Search
- 📚 ArXiv Research Paper Search
- 🧮 Calculator Tool
- 💬 Streamlit Interactive UI
- 📂 PDF & Web Document Ingestion

---

# 🔑 Bring Your Own API Key

Instead of hardcoding an API key, the application allows every user to configure their own LLM.

Users can:

- Enter their own Groq API Key
- Select the preferred Groq model
- Initialize the Agent
- Start asking questions

This makes the application deployment-friendly and keeps API credentials private.

---


# 🏗 System Architecture

```

                         User Query
                              │
                              ▼
                 Smart Tool Router (Keyword Detection)
                              │
      ┌──────────────┬───────────────┬──────────────┐
      ▼              ▼               ▼              ▼
 Python Tool     SQL Generator   Diagram Tool   Calculator
      │
      ├──────────────┬───────────────┐
      ▼              ▼               ▼
 GitHub Tool    ArXiv Tool     Document Retriever
                                      │
                                      ▼
                               FAISS Vector Store
                                      │
                                      ▼
                              LangGraph ReAct Agent
                                      │
                                      ▼
                               Final AI Response
```

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Framework | LangGraph |
| LLM | Groq Llama 3.3 70B |
| Embeddings | HuggingFace MiniLM |
| Vector Database | FAISS |
| Frontend | Streamlit |
| Language | Python |
| Retrieval | LangChain Retriever |
| Agent | ReAct Agent |
| Diagrams | Mermaid |
| Research | ArXiv API |
| Repository Search | GitHub API |

---

# 🧰 Integrated AI Tools

The agent intelligently chooses among multiple tools depending on the user's query.

---

## 📄 1. Document Retriever Tool

Uses semantic search over indexed documents stored inside a FAISS Vector Database.

### Capabilities

- PDF Question Answering
- Semantic Search
- Context Retrieval
- Knowledge Grounding

### Example

> Explain the concept of autonomous agents from my uploaded PDF.

---

## 🧮 2. Calculator Tool

Performs mathematical reasoning and arithmetic operations.

### Example

```
Calculate (245 × 17) + 982
```

---

## 🐙 3. GitHub Repository Search Tool

Searches GitHub repositories and retrieves repository information.

### Retrieves

- Repository Description
- Stars
- Forks
- Language
- URL

### Example

```
Find popular LangGraph repositories.
```

---

## 📚 4. ArXiv Research Tool

Searches academic papers from ArXiv.

### Retrieves

- Paper Title
- Authors
- Published Date
- Abstract
- PDF Link

### Example

```
Latest research papers on LLM Agents.
```

---

## 🐍 5. Python Code Generator

Generates Python solutions using the LLM.

### Supports

- DSA
- Algorithms
- Pandas
- NumPy
- Matplotlib
- CSV Processing
- Data Analysis
- Visualization

### Example

```
Write Python code to implement BFS.
```

---

## 🗄 6. SQL Generator

Generates SQL queries.

### Supports

- SELECT
- JOIN
- GROUP BY
- Window Functions
- CTE
- Stored Procedures

### Example

```
Write SQL to find the second highest salary.
```

---

## 📊 7. Mermaid Diagram Generator

Generates software architecture diagrams using Mermaid.

### Supports

- Flowcharts
- System Design
- UML
- Sequence Diagram
- Class Diagram
- ER Diagram
- API Flow
- Microservice Architecture

### Example

```
Generate Netflix microservice architecture.
```

---

# 📸 Demo

## Home Page

### User has to enter their own api key 
<img width="833" height="603" alt="image" src="https://github.com/user-attachments/assets/6e906575-fc75-4489-b15a-2c773399f320" />

<img width="934" height="613" alt="image" src="https://github.com/user-attachments/assets/b9d6bca2-82da-4d1c-a7cd-b97713108ce4" />

<img width="939" height="673" alt="image" src="https://github.com/user-attachments/assets/eb3b7b90-fd75-4e63-b4a5-d7a984466d7d" />


---

## Question Answering

<img width="909" height="634" alt="image" src="https://github.com/user-attachments/assets/1b3f7213-c920-4f95-98d1-da6b9a149840" />
<img width="933" height="751" alt="image" src="https://github.com/user-attachments/assets/7884dfd7-049a-4e7c-b46e-d6e5fa037426" />

---

## GitHub Tool

<img width="859" height="690" alt="image" src="https://github.com/user-attachments/assets/6eda1e90-705e-4830-989a-baa1077941e1" />

## It opens desired gitub repository in another tab.

<img width="755" height="534" alt="image" src="https://github.com/user-attachments/assets/dce6799b-0428-4505-a8f0-70d716416195" />

---

## ArXiv Tool

<img width="1917" height="784" alt="image" src="https://github.com/user-attachments/assets/ed36fa72-5640-449c-86e2-8f23057a9a27" />



---

## SQL Generator

<img width="917" height="624" alt="image" src="https://github.com/user-attachments/assets/56178d46-8194-4ded-9da3-d0b3215b41ec" />

---
## Calculator

<img width="663" height="490" alt="image" src="https://github.com/user-attachments/assets/ac775af6-ccc2-4611-86ab-a91b2d1eda6e" />

---

## Python Generator

<img width="649" height="565" alt="image" src="https://github.com/user-attachments/assets/8cb656f3-6491-4ab5-b211-d6a0855b7224" />
<img width="918" height="756" alt="image" src="https://github.com/user-attachments/assets/045ba707-e09d-4319-a966-fe6ebf923a62" />
<img width="615" height="565" alt="image" src="https://github.com/user-attachments/assets/cc5559c3-92bd-4241-b9ef-26e70ea87b5a" />



---

## Diagram Generator

<img width="864" height="766" alt="image" src="https://github.com/user-attachments/assets/631e30e8-177e-46e5-9149-f94ba6967a98" />

<img width="633" height="805" alt="image" src="https://github.com/user-attachments/assets/15a2a197-4957-469f-9b5a-f5ef5cf82a6f" />

## Generates Mermaid code as well

<img width="942" height="794" alt="image" src="https://github.com/user-attachments/assets/737ee95e-391a-4ba1-bf1c-12ff2ae20411" />

---

 # Tool Routing Demo
 ## Arxiv tool 
<img width="454" height="285" alt="image" src="https://github.com/user-attachments/assets/e0be9f4d-6f63-43aa-83d0-76c1cd08c030" />

## Python tool
<img width="397" height="111" alt="image" src="https://github.com/user-attachments/assets/5c520c1e-09f4-4333-bf47-ea7f520552e6" />


## reAct Agent
<img width="450" height="216" alt="image" src="https://github.com/user-attachments/assets/7937ab0e-74ac-456c-81ad-041558c97c6d" />


# 📂 Project Structure

```
multi-tool-agentic-rag/

│── src/
│   ├── config/
│   ├── document_ingestion/
│   ├── graph_builder/
│   ├── node/
│   ├── state/
│   ├── tool/
│   │    ├── calculator_tool.py
│   │    ├── github_tool.py
│   │    ├── arxiv_tool.py
│   │    ├── python_tool.py
│   │    ├── sql_tool.py
│   │    ├── diagram_tool.py
│   ├── vectorstore/
│
│── assets/
│── streamlit_app.py
│── main.py
│── requirements.txt
│── README.md
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/KAsHiSHSET/multi-tool-agentic-rag.git
```

Move into the project

```bash
cd multi-tool-agentic-rag
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
GITHUB_TOKEN=your_github_token
```

Run the application

```bash
streamlit run streamlit_app.py
```

---

# 💡 Sample Questions

### Retrieval

- Explain LangGraph.
- What are autonomous agents?

### GitHub

- Find popular LangGraph repositories.

### Research

- Latest papers on RAG.

### SQL

- Find duplicate email addresses.

### Python

- Write Merge Sort in Python.

### Diagram

- Generate Swiggy microservice architecture.

---

# 🎯 Future Improvements

- Docker Deployment
- Kubernetes Deployment
- AWS Architecture Generator
- Memory-enabled Agents
- Multi-Agent Collaboration
- Voice Assistant
- Image Understanding
- Web Search Integration
- Tool Usage Analytics

---

# 👨‍💻 Author

**Kashish Seth**

- LinkedIn: https://www.linkedin.com/in/kashish-seth-6097182bb
- GitHub: https://github.com/KAsHiSHSET

---

# ⭐ If you found this project useful, consider giving it a star!
