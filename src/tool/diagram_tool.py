from langchain_core.tools import tool


def create_diagram_tool(llm):

    @tool
    def diagram_generator(prompt: str) -> str:
        """
        Generate Mermaid diagrams.

        Use whenever the user asks for:
        - architecture
        - flowchart
        - sequence diagram
        - ER diagram
        - class diagram
        - UML
        """

        response = llm.invoke(
            f"""
You are a software architect.

Generate ONLY Mermaid code.

Rules:
- Return ONLY valid Mermaid syntax.
- Do NOT explain.
- Do NOT wrap inside ```mermaid.
- Do NOT wrap inside ```.

Request:
{prompt}
"""
        )

        diagram = response.content

        diagram = (
            diagram.replace("```mermaid", "")
                   .replace("```", "")
                   .strip()
        )

        return diagram

    return diagram_generator