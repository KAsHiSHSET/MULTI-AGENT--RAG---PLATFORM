"""LangGraph ReAct Agent Node"""

from typing import List
import re
from src.state.rag_state import RAGState

from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

from src.tool.calculator_tool import calculator
from src.tool.github_tool import github_repository
from src.tool.arxiv_tool import arxiv_search
from src.tool.python_tool import create_python_tool
from src.tool.diagram_tool import create_diagram_tool
from src.tool.sql_tool import create_sql_tool


class RAGNodes:

    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm
        self.agent = None

    def _build_agent(self):

        retriever = self.retriever

        @tool
        def retriever_tool(query: str) -> str:
            """
            Search uploaded documents.
            """

            docs: List[Document] = retriever.invoke(query)

            if not docs:
                return "No relevant documents found."

            output = []

            for i, doc in enumerate(docs[:5], start=1):

                source = doc.metadata.get("source", "Unknown")

                output.append(
                    f"""
Document {i}

Source:
{source}

Content:
{doc.page_content}
"""
                )

            return "\n\n".join(output)
        self.python_executor = create_python_tool(self.llm)
        self.sql_generator = create_sql_tool(self.llm)
        self.diagram_generator = create_diagram_tool(self.llm)
        tools = [
            retriever_tool,
            calculator,
            github_repository,
            arxiv_search,
            self.python_executor,
            self.diagram_generator,
            self.sql_generator,
        ]

        prompt = """
You are an intelligent Agentic AI Assistant.

You have access to the following tools.

1. retriever_tool
Use for uploaded PDFs and indexed documents.

2. calculator
Use for mathematical calculations.

3. github_repository
Use for GitHub repositories and open-source projects.

4. arxiv_search
Use for research papers and academic publications.

5. python_executor
Use whenever Python code, algorithms, DSA, pandas, numpy,
matplotlib, statistics, visualization or CSV processing
is requested.

6. diagram_generator
You are an expert software architect.

Generate ONLY valid Mermaid syntax.

Rules:

1. Never write explanations.
2. Never wrap the output inside ```mermaid.
3. Never wrap the output inside ```.

Choose the correct Mermaid syntax:

- Architecture / Workflow -> flowchart LR
- Sequence -> sequenceDiagram
- Class -> classDiagram
- ER -> erDiagram
- State Machine -> stateDiagram-v2

For flowcharts:
- Use only:
A[User]
B[API Gateway]
A --> B

Never use:
participant
activate
deactivate

Return ONLY valid Mermaid code.

7. sql_generator

Purpose:
Generate SQL queries.

Always use when user asks for:

- SQL
- MySQL
- PostgreSQL
- SQLite
- Database
- Joins
- GROUP BY
- Window Functions
- CTE
- Triggers
- Stored Procedures

Always choose the most suitable tool.

Return only the final answer.
"""

        self.agent = create_react_agent(
            model=self.llm,
            tools=tools,
            prompt=prompt,
        )

    def generate_answer(self, state: RAGState):

        # ----------------------------------------
        # Build agent only once
        # ----------------------------------------

        if self.agent is None:
            self._build_agent()

        question = state.question.lower()

        # ----------------------------------------
        # Python Router
        # ----------------------------------------

        python_keywords = [
            "python",
    "code",
    "coding",
    "program",
    "script",
    "algorithm",
    "implement",
    "implementation",
    "generate code",
    "write code",
    "python function",
    "function",
    "class",
    "object",
    "oop",
    "recursion",
    "dynamic programming",
    "dp",
    "dfs",
    "bfs",
    "tree",
    "binary tree",
    "bst",
    "graph",
    "linked list",
    "stack",
    "queue",
    "heap",
    "trie",
    "segment tree",
    "hashmap",
    "dictionary",
    "set",
    "binary search",
    "merge sort",
    "quick sort",
    "selection sort",
    "bubble sort",
    "dijkstra",
    "kruskal",
    "prim",
    "bellman ford",
    "floyd warshall",
    "topological sort",
    "backtracking",
    "sliding window",
    "two pointers",
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "csv",
    "dataframe",
    "visualization",
    "plot",
    "automation",
        ]
          
        if any(k in question for k in python_keywords):

            print("\n========== PYTHON TOOL ==========\n")

            answer = self.python_executor.invoke(
                {"task": state.question}
            )

            return RAGState(
                question=state.question,
                retrieved_docs=[],
                answer=answer,
            )
        sql_keywords = [
             "sql",
    "mysql",
    "postgres",
    "postgresql",
    "sqlite",
    "database",
    "query",
    "table",
    "schema",
    "primary key",
    "foreign key",
    "normalization",
    "select",
    "insert",
    "update",
    "delete",
    "create table",
    "drop table",
    "alter table",
    "join",
    "left join",
    "right join",
    "inner join",
    "full join",
    "group by",
    "having",
    "order by",
    "distinct",
    "count",
    "sum",
    "avg",
    "min",
    "max",
    "cte",
    "window function",
    "row_number",
    "rank",
    "dense_rank",
    "lead",
    "lag",
    "trigger",
    "view",
    "stored procedure",
        ]

        if any(k in question for k in sql_keywords):

           print("\n========== SQL TOOL ==========\n")

           answer = self.sql_generator.invoke(
             {"task": state.question}
            )

           return RAGState(
             question=state.question,
             retrieved_docs=[],
            answer=answer,
            )
        # ----------------------------------------
        # Diagram Router
        # ----------------------------------------

        diagram_keywords = [
            "diagram",
    "architecture",
    "flowchart",
    "workflow",
    "sequence",
    "sequence diagram",
    "class diagram",
    "er diagram",
    "uml",
    "state diagram",
    "system design",
    "microservice",
    "network architecture",
    "api flow",
    "hld",
    "lld",
    "design",
        ]

        if any(k in question for k in diagram_keywords):

            print("\n========== DIAGRAM TOOL ==========\n")

            answer = self.diagram_generator.invoke(
                {"prompt": state.question}
            )

            return RAGState(
                question=state.question,
                retrieved_docs=[],
                answer=answer,
            )
        github_keywords = [
    "github",
    "repository",
    "repo",
    "open source",
]

        if any(k in question for k in github_keywords):

            print("\n========== GITHUB TOOL ==========\n")

            answer = github_repository.invoke(
            {"repo": state.question}
    )

            return RAGState(
        question=state.question,
        retrieved_docs=[],
        answer=answer,
            )
        # ----------------------------------------
        # Otherwise let ReAct decide
        # ----------------------------------------
        paper_keywords = [
    "paper",
    "papers",
    "research",
    "research paper",
    "survey",
    "publication",
    "arxiv",
]

        if any(k in question for k in paper_keywords):

           print("\n========== ARXIV TOOL ==========\n")

           answer = arxiv_search.invoke(
          {"query": state.question}
           )

           return RAGState(
        question=state.question,
        retrieved_docs=[],
        answer=answer,
         )
        
        math_pattern = r"^[0-9+\-*/(). ]+$"

        if re.fullmatch(math_pattern, state.question):

           print("\n========== CALCULATOR TOOL ==========\n")
 
           answer = calculator.invoke(
        {"expression": state.question}
    )

           return RAGState(
        question=state.question,
        retrieved_docs=[],
        answer=answer,
    )
        
        print("\n========== REACT AGENT ==========\n")

        result = self.agent.invoke(
            {
                "messages": [
                    HumanMessage(
                        content=state.question
                    )
                ]
            }
        )

        answer = result["messages"][-1].content

        return RAGState(
            question=state.question,
            retrieved_docs=[],
            answer=answer,
        )