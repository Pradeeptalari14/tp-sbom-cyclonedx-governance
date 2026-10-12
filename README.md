# SBOM & CycloneDX Vulnerability Governance Studio

> **Production Repository:** `Pradeeptalari14/tp-sbom-cyclonedx-governance`  
> **Interactive Studio Workspace:** [https://talaripradeep.info/tools/sbom-cyclonedx-governance/](https://talaripradeep.info/tools/sbom-cyclonedx-governance/)  
> **Visual Flow Canvas:** [https://talaripradeep.info/studios/flow/?studio=sbom-cyclonedx-governance](https://talaripradeep.info/studios/flow/?studio=sbom-cyclonedx-governance)

## Overview
Generate CycloneDX and SPDX Software Bill of Materials (SBOM) using Syft, enforce Grype vulnerability gates with EPSS scoring, and verify licensing compliance.

## Primary Specification Manifest: `sbom-policy.yaml`
```yaml
apiVersion: governance.cyclonedx.org/v1
kind: SBOMAuditPolicy
metadata:
  name: cyclonedx-governance
spec:
  specVersion: "1.5"
  formats: ["cyclonedx-json", "spdx-json"]
  scanner:
    engine: "syft"
    vulnerabilityMatcher: "grype"
    epssThreshold: 0.05
    maxCvssScore: 7.0
  failOnSeverity: ["CRITICAL", "HIGH"]
```

## Verification & Execution
```bash
# Run local verification
git verify-commit HEAD
```

## License
MIT License. Copyright (c) 2026 Talari Pradeep.
