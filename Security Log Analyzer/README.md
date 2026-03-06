# Security Log Analyzer

## Overview
The Security Log Analyzer is a Python-based project designed to read log files, analyze network activity, and detect suspicious behavior. This tool simulates how security engineers monitor and analyze server logs to identify potentially malicious activity.

---

## Features
- Reads log files containing network requests
- Extracts IP addresses from logs
- Counts the number of requests per IP
- Detects suspicious IPs exceeding a configurable threshold
- Displays a user-friendly report with summaries and warnings

---

## Requirements
- Python 3.x
- No external libraries required

---

## How to Run
1. Place your log file in the same directory as the script and name it `file.log`.
2. Run the Python script:

```bash
python log_analyzer.py
```

3. View the output in the console.

---

## Example Log File (`file.log`)
```
192.168.1.5 - GET /index.html
192.168.1.5 - GET /login
192.168.1.5 - GET /admin
10.0.0.4 - GET /index.html
```

## Example Output
```
========================================
SECURITY LOG ANALYSIS REPORT
========================================

Total log entries analyzed: 4
Unique IP addresses found: 2

Activity Summary:
- 192.168.1.5 → 3 requests
- 10.0.0.4 → 1 request

Suspicious Activity:
None detected

Analysis Complete.
========================================
```

---

## How it Helps You Learn
- Practice file handling in Python
- Work with string manipulation and dictionaries
- Gain early exposure to security concepts and log analysis
- Build foundational skills for red teaming and cybersecurity

---

## Future Enhancements
- Add sorting by number of requests
- Categorize suspicious activity by severity
- Visualize results using a frontend dashboard
- Extend detection rules for advanced security scenarios

---

## Author
[Muhammad Uzair] - Python & Cybersecurity Enthusiast

