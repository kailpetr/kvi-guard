# OpenAI Setup

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Set API key

Windows:

```bash
set OPENAI_API_KEY=your_api_key
```

Linux/macOS:

```bash
export OPENAI_API_KEY=your_api_key
```

---

## 3. Start KVI Guard

```bash
uvicorn app.main:app --reload
```

---

## 4. Open API docs

```text
http://127.0.0.1:8000/docs
```

---

## 5. Test /safe-generate

Example request:

```json
{
  "prompt": "Explain why the sky is blue."
}
```

KVI Guard will:

- generate multiple responses
- compare semantic similarity
- estimate response risk
- compute confidence
- return a verified output
