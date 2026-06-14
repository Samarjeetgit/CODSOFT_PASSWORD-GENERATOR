# Cryptographically Secure Password Generator

An industry-grade, compliance-driven Command Line Interface (CLI) security tool engineered for the CodSoft Python Programming internship. This application bypasses standard pseudo-random number limitations by implementing high-entropy cryptographic generation routines, proactive resource boundary safeguards, and structured data execution reporting.

## Architectural & Security Standards

### 1. Cryptographically Secure Pseudo-Random Number Generation (CSPRNG)
Standard random string generation utilities in Python utilize the Mersenne Twister algorithm via the default `random` module, which is completely predictable via state-reconstruction attacks. This system mandates the use of the native `secrets` module, leveraging operating-system-sourced entropy (e.g., `/dev/urandom` or `CryptGenRandom`) to ensure maximum bit-unpredictability for true production environments.

### 2. Shannon Entropy Evaluation Metrics
To provide real-world administrative insights, the platform evaluates the generated key space using classical Information Theory. The total theoretical entropy ($E$) in bits is dynamically derived using:

$$E = \log_2(R^L)$$

Where:
- $R$ represents the total character pool radius (base cardinality determined by policy configurations).
- $L$ represents the absolute length of the generated key array.

The system enforces standard cybersecurity tier classifications based on the output bits:
- **Weak:** $< 50 \text{ bits}$
- **Moderate:** $50 - 79 \text{ bits}$
- **Strong:** $\ge 80 \text{ bits}$

### 3. Rate-Limiting & Injection Control
To insulate the processing thread against self-inflicted Denial of Service (DoS) constraints or heap-memory saturation failures, the execution loop enforces strict logical boundaries (Minimum: 8 characters, Maximum: 2048 characters) at the entry point.

### 4. Zero-Knowledge Compliance Logging
The transaction system supports optional storage logging to a localized secure ledger file (`vault_manifest.json`). Adhering to zero-knowledge architectural principles, the actual plaintext keys are strictly retained in volatile memory and never committed to disk storage; only statistical metadata, length matrices, and entropy scores are permanently written.

---

## File System Structure

```text
CODSOFT_PASSWORD-GENERATOR/
├── chai.py               # Active secure core implementation logic
├── passwordgenerator.py  # Environment execution runtime
└── README.md             # Systems documentation deployment ledger
Installation & Environment Verification
Prerequisites
Python 3.13.x Environment Runtime

Native CLI Shell (PowerShell 7+, Bash, or zsh)

Step 1: Clone the Version-Controlled Repository
git clone [https://github.com/Samarjeetgit/CODSOFT_PASSWORD-GENERATOR.git](https://github.com/Samarjeetgit/CODSOFT_PASSWORD-GENERATOR.git)
cd CODSOFT_PASSWORD-GENERATOR
Step 2: System Execution
To launch the core engine, run either localized entry point script within your VS Code Terminal environment:
python passwordgenerator.py
