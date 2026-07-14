"""Streamlit UI for Agentic RAG"""

import sys
import time
from pathlib import Path


import streamlit as st
import streamlit.components.v1 as components

# Add src to path
sys.path.append(str(Path(__file__).parent))

from src.config.config import Config
from src.document_ingestion.document_processor import DocumentProcessor
from src.vectorstore.vectorstore import VectorStore
from src.graph_builder.graph_builder import GraphBuilder

# -------------------------------
# Mermaid Renderer
# -------------------------------

def st_mermaid(code: str):

    components.html(
        f"""
        <pre class="mermaid">
{code}
        </pre>

        <script type="module">
            import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";

            mermaid.initialize({{
                startOnLoad: true,
                theme: "default"
            }});
        </script>
        """,
        height=700,
        scrolling=True,
    )
# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="🤖 Agentic RAG",
    page_icon="🤖",
    layout="wide"
)


# -------------------------------
# CSS
# -------------------------------

st.markdown("""
<style>

.stButton>button{
    width:100%;
    background:#2563eb;
    color:white;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------
# Session State
# -------------------------------

def init_session():
    if "graph" not in st.session_state:
        st.session_state.graph = None

    if "history" not in st.session_state:
        st.session_state.history = []

    if "ready" not in st.session_state:
        st.session_state.ready = False

    if "api_key" not in st.session_state:
        st.session_state.api_key = ""

    if "model_name" not in st.session_state:
        st.session_state.model_name = Config.DEFAULT_MODEL


# -------------------------------
# Initialize RAG
# -------------------------------

@st.cache_resource
def initialize_system(api_key, model_name):

    llm = Config.get_llm(
        api_key=api_key,
        model_name=model_name
    )

    processor = DocumentProcessor(
        chunk_size=Config.CHUNK_SIZE,
        chunk_overlap=Config.CHUNK_OVERLAP
    )

    vector_store = VectorStore()

    documents = processor.load_documents(
        Config.DEFAULT_URLS
    )

    chunks = processor.split_documents(documents)

    vector_store.create_vectorstore(chunks)

    graph = GraphBuilder(
        retriever=vector_store.get_retriever(),
        llm=llm
    )

    graph.build()

    return graph, len(chunks)


# -------------------------------
# UI
# -------------------------------

def main():

    init_session()

    st.title("🤖 Agentic RAG")
    st.caption(
        "Groq + LangGraph + HuggingFace + FAISS"
    )
    with st.sidebar:

      st.header("🔑 LLM Configuration")

      groq_api_key = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="gsk_..."
    )

      model_name = st.selectbox(
        "Select Model",
        [
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
            "deepseek-r1-distill-llama-70b",
            "qwen/qwen3-32b",
        ],
        index=0
      )

      st.link_button(
    "🔑 Get a Groq API Key",
    "https://console.groq.com/keys"
     )

      initialize = st.button(
        "🚀 Initialize Agent"
      )

    if initialize:

      if groq_api_key.strip() == "":
         st.error("Please enter your Groq API Key.")
         st.stop()

      with st.spinner("Initializing Agent..."):

         graph, chunks = initialize_system(
            groq_api_key,
            model_name
         )

         st.session_state.graph = graph
         st.session_state.ready = True
         st.session_state.api_key = groq_api_key
         st.session_state.model_name = model_name

      st.success(
        f"✅ Loaded {chunks} document chunks."
       )
    if not st.session_state.ready:

       st.info(
        "👈 Enter your Groq API Key and click 'Initialize Agent' to begin."
    )

       st.stop()

    st.divider()

    question = st.text_input(
        "Ask your question",
        placeholder="What is an LLM Agent?"
    )

    if st.button("Search"):

        if question.strip() == "":
            st.warning("Please enter a question.")
            return

        with st.spinner("Thinking..."):

            start = time.time()

            result = st.session_state.graph.run(question)

            elapsed = time.time() - start

            answer = result.get(
                "answer",
                "No answer generated."
            )

            st.session_state.history.insert(
                0,
                {
                    "question": question,
                    "answer": answer,
                    "time": elapsed
                }
            )

        st.subheader("Answer")

        # Remove markdown if LLM returns ```mermaid
        answer = (
            answer.replace("```mermaid", "")
                  .replace("```", "")
                  .strip()
        )

        diagram_types = [
         "graph",
        "flowchart",
        "sequenceDiagram",
    "classDiagram",
        "erDiagram",
    "stateDiagram",
    "journey",
    "gantt",
    "pie",
    "mindmap",
    "timeline",
     ]

        if any(answer.startswith(t) for t in diagram_types):

            st_mermaid(answer)

            with st.expander("📄 Mermaid Code"):
                st.code(answer)

        else:

            st.write(answer)

        st.caption(
            f"⏱ Response Time : {elapsed:.2f} sec"
        ) 


if __name__ == "__main__":
    main()