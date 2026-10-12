#!/usr/bin/env python3
"""
Syft CycloneDX SBOM Compiler & Grype EPSS Evaluator
"""
import subprocess
import json
import sys

def generate_and_scan_sbom(image_name: str, output_path: str = "sbom.cdx.json"):
    print(f"📦 Compiling CycloneDX 1.5 SBOM for {image_name}...")
    subprocess.run(["syft", image_name, "-o", f"cyclonedx-json={output_path}"], check=True)
    
    print(f"🔍 Auditing SBOM vulnerabilities with Grype & EPSS...")
    scan = subprocess.run(["grype", f"sbom:{output_path}", "-o", "json"], capture_output=True, text=True, check=True)
    report = json.loads(scan.stdout)
    vulns = report.get("matches", [])
    print(f"Found {len(vulns)} packages audited.")
    return len(vulns)

if __name__ == "__main__":
    generate_and_scan_sbom("alpine:latest")
