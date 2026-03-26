# Veterinary Case Simulator

AI chatbot developed with Chainlit.

## Prerequisites

- pyenv (recommended) — required Python version is pinned in `.python-version`
- pip

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd vet_simulator
   ```

2. **Install the pinned Python version:**

   ```bash
   pyenv install $(cat .python-version)
   ```

3. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   ```

4. **Activate the virtual environment:**

   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

5. **Install dependencies:**

   ```bash
   pip install -r requirements.lock -r requirements-dev.lock
   ```

6. **Create environment variables file:**

   ```bash
   # copy .env.example content and paste to .env while creating it
   cp .env.example .env
   ```

   Then edit `.env` and add your API keys:

   ```bash
   # Edit with your preferred editor
   vim .env  # or nvim, nano, code, etc.
   ```

7. **Start the app:**

   ```bash
   chainlit run app.py -w
   ```

   The UI will open in your browser at `http://localhost:8000`

## When Adding or Removing Dependencies

1. **Add or remove them from** `pyproject.toml`

   Then run:

   ```bash
   pip install -e .[dev]
   ```

2. **Regenerate lock files**

   ```bash
   pip-compile -o requirements.lock pyproject.toml
   pip-compile --extra dev -o requirements-dev.lock pyproject.toml
   ```

3. **Ensure your environment exactly matches both lock files**

   ```bash
   pip-sync requirements.lock requirements-dev.lock
   ```

## Deactivating Virtual Environment

When done working on the project:

```bash
deactivate
```

## Troubleshooting

- If you encounter module import errors, ensure the virtual environment is activated
- For "command not found" errors, verify all dependencies are installed
- Check that your Python version matches .python-version: `python --version`
