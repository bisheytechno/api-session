# API Session

Learning how to work with APIs using Python's requests library — foundation for calling AI APIs like Claude and OpenAI.

---

## What This Covers

- GET requests — fetching data
- Query parameters — filtering data
- Headers & Auth — API key authentication
- Error handling — timeout, connection errors
- JSON handling — parse, save, load

---

## Tech Stack

- Python 3.x
- requests library

---

## Project Structure

```
api-session/
│
├── basic.py          → GET request basics
├── params.py          → Query parameters
├── headers.py         → Headers & Auth
├── error_handling.py  → try/except
├── jsontry.py            → JSON handle
├── requirements.txt      → Dependencies
└── README.md
```

---

## How to Run

**1. Clone:**
```bash
git clone https://github.com/bisheytechno/api-session.git
cd api-session
```

**2. Virtual Environment:**
```bash
python -m venv myvenv
myvenv\Scripts\activate
```

**3. Install:**
```bash
pip install -r requirements.txt
```

**4. Run any file:**
```bash
python 01_basics.py
```

---

## Topics Covered

| File | Topic | Status |
|------|-------|--------|
| 01_basics.py | GET request | ✅ |
| 02_params.py | Query parameters | ✅ |
| 03_headers.py | Headers & Auth | ✅ |
| 04_error_handling.py | Error handling | ✅ |
| 05_json.py | JSON handle | ✅ |

---

## Why This Matters

```
requests library =
→ Foundation for all AI API calls
→ Claude API
→ OpenAI API
→ Hugging Face API
```

---

## Requirements

```
requests
```

---

## Author

**Bishal KC** — Aspiring AI Engineer

---

## License

MIT License