import asyncio
from service import EnterpriseDatabase, AutomatRContext
from agent import invoice_agent

async def run_enterprise_pipeline():
    db_client = EnterpriseDatabase()
    context_locker = AutomatRContext(db=db_client, current_department="Finance Operations", account_id="ACCT-889")

    unstructured_invoice_text = """
    Please process this billing statement under account scope. 
    Vendor: Navayuga Infotech. Invoice Identifier: INV-2026-X8.
    Items:
    - Cloud Computing Core Migration Specialist: 45000.00
    - Automated Infrastructure Playbooks: 5000.00
    The grand total calculated is 50000.00.
    """

    print("🚀 Passing unstructured text to Groq Agent Pipeline...")
    response = await invoice_agent.run(unstructured_invoice_text, deps=context_locker)

    print("\n✅ Extraction Successful! Structured Result Data:")
    print(f"Vendor Name: {response.output.vendor_name}")
    print(f"Invoice ID:  {response.output.invoice_id}")
    print(f"Line Items:  {response.output.line_items}")
    print(f"Grand Total: {response.output.total_amount} INR")

if __name__ == "__main__":
    asyncio.run(run_enterprise_pipeline())