from pydantic import BaseModel

class LineItem(BaseModel):
    description: str
    amount: float

class ProcessedInvoice(BaseModel):
    vendor_name: str
    invoice_id: str
    line_items: list[LineItem]
    total_amount: float