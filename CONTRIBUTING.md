# Contributing to EsakoAPI

Thank you for your interest in contributing to EsakoAPI. Contributions are welcome from developers, documentation writers, testers, translators, and people who can help review Zakat calculation rules.

## Ways to Contribute

You can help by:

- Fixing bugs
- Improving API documentation
- Adding or improving tests
- Improving the static website UI/UX
- Refactoring code for readability and maintainability
- Reviewing Zakat formulas and requirements
- Translating documentation
- Reporting unclear behavior or edge cases

## Before You Start

If your contribution changes a Zakat rule, nisab value, calculation formula, or requirement text, please include a clear reference or explanation for the source used.

For security issues, do not open a public issue. Follow the instructions in [SECURITY.md](SECURITY.md).

## Local Setup

Clone the repository:

```bash
git clone https://github.com/jumhuur/E-sakoAPI.git
cd E-sakoAPI
```

Create and activate a virtual environment:

```bash
python -m venv env
```

Windows PowerShell:

```bash
.\env\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
URL_DAHAB=https://example.com/gold-price-api
URL_FIDO=https://example.com/silver-price-api
```

Run the local server:

```bash
uvicorn app.main:app --reload
```

Open the app:

```text
http://127.0.0.1:8000
```

## Running Tests

Run the full test suite:

```bash
pytest
```

Run one test file:

```bash
pytest tests/test_gold.py
```

Please run tests before opening a pull request. If tests fail because external price APIs are unavailable, mention that in your pull request.

## Development Guidelines

- Keep changes focused and easy to review.
- Follow the existing project style where possible.
- Use clear function and variable names.
- Avoid unrelated refactors in the same pull request.
- Add or update tests when calculation logic changes.
- Keep public API responses stable unless the change is intentional.
- Do not commit secrets, API keys, local virtual environments, or generated cache files.

## API and Calculation Changes

For changes to calculation modules, include:

- The endpoint affected
- The reason for the change
- Before and after behavior
- Tests that cover the change
- Source or explanation if the change relates to Islamic rulings

Examples of calculation modules:

- `app/calculators/gold.py` for gold
- `app/calculators/money.py` for money
- `app/calculators/silver.py` for silver
- `app/calculators/crops.py` for crops
- `app/calculators/camels.py` for camels
- `app/calculators/cows.py` for cows
- `app/calculators/sheep.py` for sheep/goats
- `app/calculators/rikaas.py` for rikaas

## Documentation Changes

Documentation improvements are very welcome. Please keep examples accurate and use the live base URL:

```text
https://esakoapi.org/api
```

If you add a new endpoint or change an existing one, update:

- `Readme.md`
- `static/docs.html`
- Tests, if behavior changed

## Commit Messages

Use short, clear commit messages.

Good examples:

```text
fix gold nisab validation
add copy buttons to docs page
document local development setup
```

## Pull Request Checklist

Before submitting a pull request, please check:

- The change is focused and clearly described.
- Tests pass locally, or failures are explained.
- Documentation is updated if behavior changed.
- No secrets or local files are committed.
- Zakat rule changes include a source or explanation.

## Opening Issues

When opening an issue, include:

- What you expected to happen
- What actually happened
- The endpoint or file involved
- Steps to reproduce
- Example request/response, if available

For feature requests, explain the use case and why it would help users or contributors.

## Code of Conduct

Please be respectful and constructive. This project welcomes contributors from different backgrounds, languages, and levels of experience.

## License

By contributing, you agree that your contributions will be licensed under the MIT License used by this project.
