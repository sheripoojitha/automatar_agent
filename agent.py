from pydantic_ai import Agent, RunContext
from models import ProcessedInvoice
from service import AutomatRContext

invoice_agent = Agent(
    "groq:llama-3.3-70b-versatile",  
    output_type=ProcessedInvoice,  
    deps_type=AutomatRContext     
)

@invoice_agent.system_prompt
def dynamic_enterprise_rules(ctx: RunContext[AutomatRContext]) -> str:
    return f"""
    You are an automated intelligence worker operating within the AutomatR platform.
    Active Processing Department: {ctx.deps.current_department}
    Target Account Scope: {ctx.deps.account_id}
    
    Strict rule: Return ONLY raw, valid JSON text that complies perfectly with the schema. 
    Do NOT wrap your output in any XML tags, markdown blocks, code blocks, or function brackets.
    """