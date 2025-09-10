import requests
import json
from datetime import datetime

class ComplianceAgent:
    def __init__(self):
        self.country_regulations = {
            "south_africa": {
                "data_protection": "POPIA",
                "requirements": ["data encryption", "user consent", "data breach notification"]
            },
            "namibia": {
                "data_protection": "Data Protection Act",
                "requirements": ["data security", "lawful processing", "data subject rights"]
            },
            "botswana": {
                "data_protection": "Data Protection Act",
                "requirements": ["data privacy", "consent", "secure storage"]
            }
        }
    
    def check_compliance(self, country, data_type):
        if country.lower() not in self.country_regulations:
            return {"status": "error", "message": "Country not supported"}
        
        regulations = self.country_regulations[country.lower()]
        return {
            "status": "success",
            "country": country,
            "data_type": data_type,
            "compliance": regulations,
            "timestamp": datetime.now().isoformat()
        }
    
    def generate_compliance_report(self, country):
        if country.lower() not in self.country_regulations:
            return {"status": "error", "message": "Country not supported"}
        
        regulations = self.country_regulations[country.lower()]
        report = f"""
        COMPLIANCE REPORT FOR {country.upper()}
        Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        Data Protection Legislation: {regulations['data_protection']}
        
        Key Requirements:
        """
        
        for i, requirement in enumerate(regulations['requirements'], 1):
            report += f"\n{i}. {requirement}"
        
        report += "\n\nSTATUS: COMPLIANT"
        return report
    
    def monitor_changes(self, country):
        # This would typically connect to a regulatory API to monitor for changes
        # For now, we'll return a mock response
        return {
            "country": country,
            "last_checked": datetime.now().isoformat(),
            "changes_detected": False,
            "message": "No recent changes to regulations detected"
        }
