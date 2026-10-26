# Portfolio Website with Local Chat Assistant

A Python + Streamlit portfolio starter with a local Ollama-powered assistant.

## Requirements
- Python 3.14 (or a compatible Python version)
- Ollama installed and running
- A model available locally, e.g. `qwen2.5:1.5b`
- Packages installed in the project's `.venv`

## Run on Windows PowerShell
From the project folder:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Streamlit normally opens a browser at `http://localhost:8501`.

If the model is not available, check:

```powershell
ollama list
ollama run qwen2.5:1.5b "Reply with exactly: Local AI is working."
```

## Update portfolio content
Edit `knowledge/portfolio.md`. Replace placeholders with verified content approved for public display. Restart or refresh the app after editing.

## Local lead capture
Contact inquiries are saved in `data/leads.csv` on this computer. This starter does not send email. Treat inquiry data as private and protect the file.

## Important before public deployment
- Replace all placeholder profile details.
- Add a proper privacy notice and retention policy.
- Configure secure hosting, HTTPS, rate limiting and spam protection.
- Add email notifications only after configuring a legitimate email service.
- Test prompt-injection attempts and ensure the assistant does not invent profile facts.
- The local Ollama URL is intended for local development, not public hosting without a secure backend architecture.
