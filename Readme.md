# Arjun

Arjun is a Python-based CLI log analysis tool built as a DevOps portfolio project. It parses web server access logs and provides useful insights for troubleshooting and monitoring server activity.

The goal of Arjun is to gradually evolve into a lightweight log analysis tool capable of assisting DevOps engineers with server monitoring, error detection, and traffic analysis.

---

## Features

Current features (v0.3)

- Parse web server access logs
- Top 5 IP address analysis
- HTTP Status Code distribution
- Error analysis (4xx & 5xx)
- Top IPs generating errors
- Top endpoints generating errors
- Clean CLI report generation

---

## Project Structure

```
Arjun/
│
├── main.py
├── parser.py
├── analyzer.py
├── report.py
│
├── sample_logs/
│   └── access.log
│
├── README.md
├── CHANGELOG.md
├── requirements.txt
└── .gitignore
```

---

## Technologies Used

- Python
- Pandas

---

## Installation

Clone the repository

```bash
git clone https://github.com/jatinthakur029/Arjun.git
cd Arjun
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run Arjun using

```bash
python main.py
```

---

## Sample Report

```
========================================
ARJUN v0.3 REPORT
========================================

Top IPs
----------------------------------------

Status Codes
----------------------------------------

Error Summary
----------------------------------------

Top Error IPs
----------------------------------------

Top Error Endpoints
----------------------------------------
```

---

## Roadmap

### v0.4

- HTTP Method Analysis
- Request Distribution
- Traffic Statistics

### v0.5

- Timestamp Analysis
- Traffic Timeline
- Peak Traffic Detection

### v0.6

- Suspicious IP Detection
- Security Analysis
- Brute Force Detection

### v1.0

- JSON Report Export
- HTML Report Export
- CLI Arguments
- Configuration File
- Unit Tests
- Documentation

---

## Purpose

Arjun is being developed incrementally as a portfolio project while learning DevOps, Python, and software engineering principles.

The focus is on writing clean, modular, maintainable code while solving practical log analysis problems.

---
## Current Limitations

As of **v0.3**, Arjun supports:

- Nginx access logs
- Log input through the `sample_logs/access.log` file
- CLI-based analysis only

To analyze logs:

1. Replace the contents of `sample_logs/access.log` with your own Nginx access log.
2. Run:

```bash
python main.py
```

Arjun will parse the log and generate a CLI report.

Future versions will support:

- Custom log file input
- Command-line arguments
- Multiple log formats
- Report export (JSON/HTML)

## Author

Jatin Thakur