import requests
import json
from typing import Dict

class SlackNotifier:
    def __init__(self, webhook_url: str, channel: str = "#alerts"):
        self.webhook_url = webhook_url
        self.channel = channel

    def send_alert(self, alert: Dict) -> bool:
        """Sends formatted Slack alert with MITRE details"""
        payload = {
            "channel": self.channel,
            "attachments": [{
                "color": "#ff0000",
                "title": alert.get("title"),
                "fields": [
                    {"title": "MITRE Tactic", "value": alert.get("mitre_tactic"), "short": True},
                    {"title": "Technique", "value": alert.get("mitre_technique"), "short": True},
                    {"title": "Source IP", "value": alert.get("source_ip"), "short": False}
                ]
            }]
        }
         
        try:
            response = requests.post(
                self.webhook_url,
                data=json.dumps(payload),
                headers={"Content-Type": "application/json"}
            )
            return response.status_code == 200
        except Exception as e:
            logging.error(f"Slack notification failed: {e}")
            return False      

            

            