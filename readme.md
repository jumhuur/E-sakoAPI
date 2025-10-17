# EsakoAPI

**EsakoAPI** is a free API that **does not require an API key** to use. It is designed to calculate **different types of Zakat** according to Islamic Shariah.

You can calculate Zakat on:

- **Gold**
- **Money**
- **Minerals (Rikas)**
- **Silver**
- **Crops**

And also on livestock:

- **Camels**
- **Sheep/Goats**
- **Cattle**

The API provides **fast and reliable responses** based on the Qur’an and Sunnah, using advanced algorithms that comply with Islamic Zakat rulings.

---

## 🔍 Documentation

Visit: [https://esakoapi.org](https://esakoapi.org)

---

## 📌 Endpoints and Examples

### 1. Gold Zakat

**Endpoint:**

```bash
https://esakoapi.org/api/gold/145?Type=24
```

**Description:**

The prefix *https://esakoapi.org/api/* is always required.

| Type of Calculation | Gold Karat Type           | Weight (in grams)               |
| ------------------- | ------------------------- | ------------------------------- |
| gold = `string`     | 24,21,22,20,18,16 = `int` | amount of gold in grams = `int` |

the default Type is 24

**Sample Response:**

```json
{
  "code": 200,
  "response": 3.625,
  "requirements": [
    "It must be 100% pure gold.",
    "You must have possessed it for one full year.",
    "If paying in cash, the amount is 468.3299$."
  ],
  "unit": "Grams",
  "date": "Sunday 12-October-2025",
  "time": "05:29 PM"
}
```

**Response Explanation:**

- **code: 200 → OK** → Everything is correct
- **response: 3.625** → The amount of Zakat due in grams
- **requirements** → Conditions of Zakat (e.g., purity, one-year possession, cash equivalent)
- **unit** → The unit of measurement (since it’s gold, the unit is grams)
- **date** and **time** → The response timestamp (gold prices may fluctuate daily)

---

### 2. Money Zakat

**Endpoint:**

```bash
https://esakoapi.org/api/money/9920
```

**Description:**

The prefix *https://esakoapi.org/api/* is always required.

| Type of Calculation | Amount ($)                 |
| ------------------- | -------------------------- |
| money = `string`    | 9920 amount in USD = `int` |

**Sample Response:**

```json
{
  "code": 200,
  "response": 248,
  "requirements": [
    "The amount must be in US dollars (USD).",
    "You must have possessed it for one full year.",
    "The Zakat has been calculated based on the silver price, currently 1.6426."
  ],
  "unit": "$",
  "date": "Monday 13-October-2025",
  "time": "10:33 AM"
}
```

---

### 3. Silver Zakat (also known as white gold)

**Endpoint:**

```bash
https://esakoapi.org/api/silver/9920
```

**Description:**

The prefix *https://esakoapi.org/api/* is always required.

| Type of Calculation | Weight (grams)                         |
| ------------------- | -------------------------------------- |
| silver = `string`   | 9920 amount of silver in grams = `int` |

**Sample Response:**

```json
{
  "code": 200,
  "response": 248,
  "requirements": [
    "Must be 100% pure silver.",
    "You must have possessed it for one full year.",
    "If paying in cash, the amount is 407.3679$."
  ],
  "unit": "Grams",
  "date": "Monday 13-October-2025",
  "time": "10:33 AM"
}
```

---

### 4. Crops Zakat (e.g., wheat, corn, rice, etc.)

**Endpoint:**

```bash
https://esakoapi.org/api/crops/9920?Type=1
```

**Description:**

The prefix *https://esakoapi.org/api/* is always required.

| Type of Calculation | Amount (KG)                              | Query   |
| ------------------- | ---------------------------------------- | ------- |
| crops = `string`    | 9920 amount of crop in kilograms = `int` | ?Type=1 |

the default Type is 1

**Understanding the Query:**

There are **three crop types** based on their irrigation method:

- **Type 1:** Naturally rain-fed crops, without human irrigation costs.  
  Use `?nooc=1`

- **Type 2:** Crops irrigated with paid water (e.g., purchased or artificial irrigation).  
  Use `?nooc=2`

- **Type 3:** Crops irrigated with both rain and paid water combined.  
  Use `?nooc=3`

**Sample Response:**

```json
{
  "code": 200,
  "response": 90,
  "requirements": [
    "Must be rain-fed crops.",
    "Must be harvested and storable (e.g., wheat, rice, or maize)."
  ],
  "unit": "Kg",
  "date": "Monday 13-October-2025",
  "time": "10:33 AM"
}
```

---

### 5. Camel Zakat

**Endpoint:**

```bash
https://esakoapi.org/api/camels/35
```

**Description:**

The prefix *https://esakoapi.org/api/* is always required.

| Type of Calculation | Quantity of Camels          |
| ------------------- | --------------------------- |
| camels = `string`   | 35 number of camels = `int` |

**Sample Response:**

```json
{
  "code": 200,
  "response": 1,
  "requirements": [
    "To be paid as a camel.",
    "Must have entered its second year.",
    "Must be female."
  ],
  "unit": "Heads",
  "date": "Monday 13-October-2025",
  "time": "10:33 AM"
}
```

---

### 6. cows Zakat

**Endpoint:**

```bash
https://esakoapi.org/api/cows/35
```

**Description:**

The prefix *https://esakoapi.org/api/* is always required.

| Type of Calculation | Quantity of cows            |
| ------------------- | --------------------------- |
| cows = `string`     | 35 number of cattle = `int` |

**Sample Response:**

```json
{
  "code": 200,
  "response": 1,
  "requirements": [
    "Must have entered its second year (natural or domestic).",
    "It is preferable to offer a female, but a male is also acceptable.",
    "Must be a cattle species."
  ],
  "unit": "Heads",
  "date": "Monday 13-October-2025",
  "time": "10:33 AM"
}
```

---

### 7. Sheep/Goat Zakat

**Endpoint:**

```bash
https://esakoapi.org/api/sheep/62
```

**Description:**

The prefix *https://esakoapi.org/api/* is always required.

| Type of Calculation | Quantity of Sheep/Goats          |
| ------------------- | -------------------------------- |
| sheep = `string`    | 62 number of sheep/goats = `int` |

**Sample Response:**

```json
{
  "code": 200,
  "response": 1,
  "requirements": [
    "If they are lambs, they must be one year old.",
    "If they are goats, they must be at least two years old."
  ],
  "unit": "Heads",
  "date": "Monday 13-October-2025",
  "time": "10:33 AM"
}
```

---

## Programming Language

The API is built using **Python**, making it easy to integrate into both frontend and backend projects.  
You can also use any programming language, such as:

- JavaScript
- Go
- Ruby
- C#
- C++
- Python

### JavaScript Example

```js
const sakoapi = "https://esakoapi.org/api/rikaas/100";
const sako = async () => {
  try {
    const response = await fetch(sakoapi);
    const data = await response.json();
    console.log(data);
    console.log(`You owe ${data.response} ${data.unit}`); // Example: You owe 20 Grams
  } catch (error) {
    console.log(error);
  }
};

sako();
```

### Python Example

```py
import requests

url = "https://esakoapi.org/api/rikaas/100"

try:
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    data = response.json()       # Extract JSON response
    print(data)
except requests.exceptions.RequestException as e:
    print("Error:", e)
```

## 🤝 Contribute

This is an open-source project licensed under **MIT**.  
Contributions are welcome!

---

## ⚠️ Note

This project is still under testing.  
If you find any **legal, textual, or technical errors**, feel free to report them.

---

📧 **Email:** jumhuur123@hotmail.com  
📞 **Phone:** +252634645195
