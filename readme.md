# EsakoAPI

EsakoAPI is a free, open-source Zakat calculation API built with Python and FastAPI. It does not require an API key for public use and is designed to help developers calculate common types of Zakat through simple HTTP endpoints.

The API currently supports Zakat calculations for:

- Gold
- Money
- Silver
- Crops
- Rikaas, also known as buried treasure or minerals
- Camels
- Cows
- Sheep and goats

EsakoAPI aims to provide fast, clear, and reliable responses based on Islamic Zakat rulings from the Qur'an and Sunnah. The project is still under active testing, so scholarly, textual, and technical reviews are welcome.

## Documentation

Live documentation: [https://esakoapi.org/doc](https://esakoapi.org/doc)

Base API URL:

```text
https://esakoapi.org/api
```

## Quick Start

Use any HTTP client or programming language that can make GET requests.

```bash
curl https://esakoapi.org/api/money/9920
```

Example response:

```json
{
  "code": 200,
  "response": 248,
  "requirements": [
    "The amount must be in US dollars 'USD'.",
    "You must have possessed it for one full year.",
    "The Zakat has been calculated based on the gold price of 129.1985 USD per gram."
  ],
  "unit": "$",
  "date": "Monday-13-October-2025",
  "time": "10:33 AM"
}
```

## Endpoints

| Category    | Method | Endpoint                         | Description                                             |
| ----------- | ------ | -------------------------------- | ------------------------------------------------------- |
| Gold        | GET    | `/api/gold/{grams}?Type={karat}` | Calculates Zakat on gold by weight and karat.           |
| Money       | GET    | `/api/money/{amount}`            | Calculates Zakat on money in USD.                       |
| Silver      | GET    | `/api/silver/{grams}`            | Calculates Zakat on silver by weight.                   |
| Rikaas      | GET    | `/api/rikaas/{amount}`           | Calculates Zakat on rikaas/minerals.                    |
| Crops       | GET    | `/api/crops/{kg}?Type={method}`  | Calculates Zakat on crops by irrigation method.         |
| Camels      | GET    | `/api/camels/{count}`            | Calculates livestock Zakat for camels.                  |
| Cows        | GET    | `/api/cows/{count}`              | Calculates livestock Zakat for cattle.                  |
| Sheep/Goats | GET    | `/api/sheep/{count}`             | Calculates livestock Zakat for sheep or goats.          |
| Prices      | GET    | `/api/price`                     | Returns current gold and silver prices used by the API. |
| Info        | GET    | `/api/info`                      | Returns API metadata and request count.                 |

## Endpoint Examples

### Gold Zakat

```text
GET https://esakoapi.org/api/gold/145?Type=24
```

Gold karat types supported:

| Type | Meaning                                   |
| ---- | ----------------------------------------- |
| `24` | 24K gold, pure gold. This is the default. |
| `22` | 22K gold                                  |
| `21` | 21K gold                                  |
| `20` | 20K gold                                  |
| `18` | 18K gold                                  |
| `16` | 16K gold                                  |

Sample response:

```json
{
  "code": 200,
  "response": 3.625,
  "requirements": [
    "It must be 100% pure gold.",
    "You must have possessed it for one full year.",
    "If you are paying in cash, the amount is 468.3299$."
  ],
  "unit": "Grams",
  "date": "Sunday-12-October-2025",
  "time": "05:29 PM"
}
```

### Money Zakat

```text
GET https://esakoapi.org/api/money/9920
```

The amount is expected to be in USD.

### Silver Zakat

```text
GET https://esakoapi.org/api/silver/9920
```

The amount is expected to be silver weight in grams.

### Crops Zakat

```text
GET https://esakoapi.org/api/crops/9920?Type=1
```

Crop irrigation types:

| Type | Meaning                                       | Rate |
| ---- | --------------------------------------------- | ---- |
| `1`  | Rain-fed or naturally irrigated crops         | 10%  |
| `2`  | Crops irrigated with paid/artificial water    | 5%   |
| `3`  | Mixed rain-fed and paid/artificial irrigation | 7.5% |

### Livestock Zakat

```text
GET https://esakoapi.org/api/camels/35
GET https://esakoapi.org/api/cows/35
GET https://esakoapi.org/api/sheep/62
```

Livestock responses include the amount due and the requirements for the animal to be given.

### Rikaas Zakat

```text
GET https://esakoapi.org/api/rikaas/100
```

### Gold and Silver Prices

```text
GET https://esakoapi.org/api/price
```

Sample response:

```json
{
  "XAU": 4018.399902,
  "XAG": 50.008999
}
```

## Response Format

Most successful calculation responses follow this shape:

```json
{
  "code": 200,
  "response": 0,
  "requirements": [],
  "unit": "unit",
  "date": "Day-Date-Month-Year",
  "time": "HH:MM AM"
}
```

Common fields:

| Field           | Description                                                                |
| --------------- | -------------------------------------------------------------------------- |
| `code`          | API status or domain-specific code.                                        |
| `response`      | The calculated Zakat amount.                                               |
| `requirements`  | Conditions and notes for the calculation.                                  |
| `unit`          | Unit of the returned amount, such as `$`, `Grams`, `Kg`, or `Heads`.       |
| `date` / `time` | Timestamp for the response. Price-based calculations can change over time. |

## Error Codes

| Code  | Meaning                                                              |
| ----- | -------------------------------------------------------------------- |
| `404` | The requested URL does not exist.                                    |
| `403` | Required file or resource was not found.                             |
| `460` | Please try again later.                                              |
| `461` | Please enter a valid numeric amount.                                 |
| `462` | The selected option is not allowed.                                  |
| `463` | The selected gold type is not recognized.                            |
| `464` | Please use numbers only.                                             |
| `465` | Please use a number that contains at least two digits.               |
| `466` | Zakat is not applicable to the entered gold amount/type.             |
| `467` | Invalid URL.                                                         |
| `468` | Invalid crop calculation type. Accepted values are `1`, `2`, or `3`. |

## Usage Examples

### JavaScript

```js
const url = "https://esakoapi.org/api/rikaas/100";

async function calculateZakat() {
  try {
    const response = await fetch(url);
    const data = await response.json();

    console.log(data);
    console.log(`You owe ${data.response} ${data.unit}`);
  } catch (error) {
    console.error("Request failed:", error);
  }
}

calculateZakat();
```

### Python

```py
import requests

url = "https://esakoapi.org/api/rikaas/100"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.RequestException as error:
    print("Request failed:", error)
```

## Local Development

### Requirements

- Python 3.10 or newer
- `pip`
- A working internet connection for gold and silver price requests

### Setup

```bash
git clone https://github.com/jumhuur/E-sakoAPI.git
cd E-sakoAPI
python -m venv env
```

Activate the virtual environment:

```bash
# Windows PowerShell
.\env\Scripts\Activate.ps1
```

```bash
# macOS/Linux
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

Run the development server:

```bash
uvicorn app.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000
```

API docs generated by FastAPI are available at:

```text
http://127.0.0.1:8000/docs
```

## Testing

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_gold.py
```

If tests fail because price APIs are unavailable, check your `.env` values and network connection.

## Project Structure

```text
.
|-- app/
|   |-- main.py             # FastAPI application and routes
|   |-- calculators/        # Zakat calculation modules
|   |-- services/           # Price, info, and external service helpers
|   |-- utils/              # Shared constants, responses, and errors
|   `-- schemas/            # Future request/response schemas
|-- tests/                  # Test suite
|-- docs/                   # Contributor-facing documentation
|-- static/                 # Public website and documentation pages
|-- files/                  # Local JSON data files
|-- requirements.txt
`-- Readme.md
```

## Contributing

Contributions are welcome. You can help by:

- Fixing bugs
- Improving documentation
- Adding tests
- Reviewing Zakat rules and calculation logic
- Improving UI/UX for the static website
- Translating documentation

Before opening a pull request:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Run the tests.
5. Open a pull request with a clear description.

For changes related to Islamic rulings, please include references or a clear explanation of the source used.

## Roadmap Ideas

- Add formal contribution guidelines.
- Add GitHub issue and pull request templates.
- Add GitHub Actions CI for automated testing.
- Add more detailed Zakat rule documentation.
- Improve API versioning.
- Add multi-language documentation.

## License

This project is open source and licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Maintainer

Created and maintained by Jumhuur.

- GitHub: [jumhuur](https://github.com/jumhuur)
- Email: jumhuur123@hotmail.com

## Note

This project is still under testing. If you find a legal, textual, scholarly, or technical issue, please open an issue or submit a pull request.
