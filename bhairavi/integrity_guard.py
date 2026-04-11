"""
Module: IntegrityGuard (Bhairavi - Integrity Verification Layer)

Purpose:
- Detects unauthorized file modifications
- Maintains baseline hashes of critical system files
- Identifies tampering through hash comparison

NOTE:
- Passive detection only
- Does NOT take action
"""

import hashlib
import os
import logging


class IntegrityGuard:
    def __init__(self, target_dirs=None):
        if target_dirs is None:
            target_dirs = ["bhairava", "bhairavi", "config"]

        self.target_dirs = target_dirs
        self.baseline_hashes = {}

    # ---------------------------
    # Hash Calculation
    # ---------------------------
    def calculate_hash(self, filepath):
        sha256 = hashlib.sha256()

        try:
            with open(filepath, "rb") as f:
                while chunk := f.read(4096):
                    sha256.update(chunk)
            return sha256.hexdigest()

        except Exception as e:
            logging.error(f"[Integrity] Hashing failed for {filepath}: {e}")
            return None

    # ---------------------------
    # Baseline Creation
    # ---------------------------
    def create_baseline(self):
        self.baseline_hashes = {}

        for directory in self.target_dirs:
            for root, _, files in os.walk(directory):
                for file in files:

                    # Skip unnecessary files
                    if file.endswith(".pyc") or file.startswith("."):
                        continue

                    path = os.path.join(root, file)

                    file_hash = self.calculate_hash(path)
                    if file_hash:
                        self.baseline_hashes[path] = file_hash

        logging.info(f"[Integrity] Baseline created with {len(self.baseline_hashes)} files.")

    # ---------------------------
    # Integrity Verification
    # ---------------------------
    def verify_integrity(self):
        tampered_files = []

        for path, original_hash in self.baseline_hashes.items():

            # File deleted
            if not os.path.exists(path):
                logging.warning(f"[Integrity] File missing: {path}")
                tampered_files.append(path)
                continue

            current_hash = self.calculate_hash(path)

            # Skip if hashing failed
            if current_hash is None:
                continue

            # Hash mismatch
            if current_hash != original_hash:
                logging.warning(f"[Integrity] Tampered file detected: {path}")
                tampered_files.append(path)

        return tampered_files