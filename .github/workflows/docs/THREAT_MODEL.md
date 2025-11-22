## STRIDE Analysis

| Threat          | Mitigation                          | Detection Rule |
|-----------------|-------------------------------------|----------------|
| Spoofing        | IP reputation checks                | T1194          |
| Tampering       | Log signing with SHA-256            | T1562          |
| Repudiation     | Immutable audit logs                | T1078          |
| Info Disclosure | Field-level encryption              | T1213          |
| DoS             | Rate limiting (iptables)            | T1498          |
| Elevation       | Least privilege service accounts    | T1068          |

## MITRE ATT&CK Coverage
![ATT&CK Matrix](artifacts/mitre_coverage.png)


