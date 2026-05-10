import json
from pathlib import Path


KNOWLEDGE_PATH = Path(__file__).resolve().parent.parent / "knowledge"


def load_knowledge_domains():

    domains = {}

    if not KNOWLEDGE_PATH.exists():
        return domains

    for file in KNOWLEDGE_PATH.glob("*.json"):

        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

                domain_name = data.get("domain")

                if domain_name:
                    domains[domain_name] = data

        except Exception:
            continue

    return domains
