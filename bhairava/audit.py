import os
import json
import hashlib
from datetime import datetime


class Audit:
    def __init__(self, audit_file="logs/audit/audit_ledger.jsonl"):
        self.audit_file = audit_file
        os.makedirs(os.path.dirname(self.audit_file), exist_ok=True)

        if not os.path.exists(self.audit_file):
            open(self.audit_file, "w").close()

    def _get_last_hash(self):
        try:
            with open(self.audit_file, "r") as f:
                lines = f.readlines()
                if not lines:
                    return "GENESIS"
                last_entry = json.loads(lines[-1])
                return last_entry["entry_hash"]
        except Exception:
            return "GENESIS"

    def _compute_hash(self, entry_data):
        serialized = json.dumps(entry_data, sort_keys=True).encode()
        return hashlib.sha256(serialized).hexdigest()

    def log_event(self, event_type, details):
        timestamp = datetime.utcnow().isoformat()
        previous_hash = self._get_last_hash()

        entry = {
            "timestamp": timestamp,
            "event_type": event_type,
            "details": details,
            "previous_hash": previous_hash
        }

        entry_hash = self._compute_hash(entry)
        entry["entry_hash"] = entry_hash

        with open(self.audit_file, "a") as f:
            f.write(json.dumps(entry) + "\n")

    def verify_chain(self):
        try:
            with open(self.audit_file, "r") as f:
                lines = f.readlines()

            previous_hash = "GENESIS"

            for line in lines:
                entry = json.loads(line)

                expected_hash = entry["entry_hash"]

                temp_entry = dict(entry)
                del temp_entry["entry_hash"]

                recalculated_hash = self._compute_hash(temp_entry)

                if recalculated_hash != expected_hash:
                    return False

                if entry["previous_hash"] != previous_hash:
                    return False

                previous_hash = expected_hash

            return True

        except Exception:
            return False