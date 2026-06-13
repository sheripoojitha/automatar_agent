from dataclasses import dataclass

class EnterpriseDatabase:
    def verify_vendor_exists(self, vendor_name: str) -> bool:
        approved_vendors = ["Navayuga Infotech", "RKS Infra Solutions", "OpenAI"]
        return vendor_name in approved_vendors

@dataclass
class AutomatRContext:
    db: EnterpriseDatabase
    current_department: str
    account_id: str