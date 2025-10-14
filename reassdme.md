# EsakoAPI

**EsakoAPI** is a free API that does **not require an API key** to use. It is designed to calculate **various types of Zakat** according to Islamic Shariah.

You can calculate Zakat on:

- **Gold**
- **Money**
- **Minerals**
- **Silver**
- **Crops**

And also on livestock:

- **Camels**
- **Sheep/Goats**
- **Cattle**

The API provides **fast responses** based on the Qur’an and Sunnah, using deep algorithms that comply with Zakat rulings.

---

## 🔍 Test the API

Visit: [https://esakoapi.org](https://esakoapi.org)

---

## 📌 Endpoints and Examples

### 1. Gold Zakat

**Endpoint:**

```bash
https://esakoapi.org/api/dahab/24,145
```

**Sharaxaad:**

inta hore ee *https://esakoapi.org/api/* mar walba waa loo bahan yahay

| Nooca Waxa Aad Xisaabinayso | Nooca Dahabka             | Xadiga                              |
| --------------------------- | ------------------------- | ----------------------------------- |
| dahab = `string`            | 24,21,22,20,18,16 = `int` | xadiga Dahabka giraam ahaan = `int` |

**Response Tusaale:**

```json
{
  "code": 200,
  "jawaab": 3.625,
  "Shuruudo": [
    "Waa Inuu Yahay Saafi 100%",
    "Waa Inaad Sanad Haysay",
    "Lacag Hadaad Ku Bixinayso Waa 468.3299$"
  ],
  "Qiyaas": "Giraam",
  "Taariikh": "Sunday 12-October-2025",
  "Wakhti": "05:29 PM"
}
```

### Sharaxaadda Response:-

**code: 200 → OK**, wax walba waa sax

**jawaab: 3.625** → inta giraam ee sakada ka baxaysa

**Shuruudo** → shuruudaha sakada (tusaale: saafi, sanad haysta, lacag haddii lagu bixiyo)

**Qiyaas** → qiyaasta jawaabta (Maadaama la xisaabinaya dahab qiyaastiisu waa: giraam)

_Taariikh iyo Wakhti_ → waqtiga jawaabta la helay, maadaama qiimaha dahabku isbeddeli karo

### 1. Xisaabinta Lacagta

**Endpoint:**

```bash
https://esakoapi.org/api/lacag/9920
```

**Sharaxaad:**

inta hore ee *https://esakoapi.org/api/* mar walba waa loo bahan yahay

| Nooca Waxa Aad Xisaabinayso | Xadiga                              |
| --------------------------- | ----------------------------------- |
| lacag = `string`            | 9920 xadiga lacagta $ ahaan = `int` |

**Response Tusaale:**

```json
{
  "code": 200,
  "jawaab": 248,
  "Shuruudo": [
    "Waa Inay Tahay Lacagtu Dollar 'Usd'",
    "Waa Inaad Sanad Haysay",
    "waxaa lagugu xisaabiyay sakadan qiimaha fidada oo maraysa 1.6426"
  ],
  "Qiyaas": "$",
  "Taariikh": "Monday 13-October-2025",
  "Wakhti": "10:33 AM"
}
```

### 1. Xisaabinta Fidada (dahabka cad ama qalin sida dadka qaar u yaqaanaan)

**Endpoint:**

```bash
https://esakoapi.org/api/fido/9920
```

**Sharaxaad:**

inta hore ee *https://esakoapi.org/api/* mar walba waa loo bahan yahay

| Nooca Waxa Aad Xisaabinayso | Xadiga                                  |
| --------------------------- | --------------------------------------- |
| fido = `string`             | 9920 xadiga fidada giraam ahaan = `int` |

**Response Tusaale:**

```json
{
  "code": 200,
  "jawaab": 248,
  "Shuruudo": [
    "Waa Inay Tahay Fido Saafi Ah 100%",
    "Waa Inaad Sanad Haysay",
    "Lacag Hadaad ku bixinayso waxay noqonaysaa 407.3679$"
  ],
  "Qiyaas": "Giraam",
  "Taariikh": "Monday 13-October-2025",
  "Wakhti": "10:33 AM"
}
```

### 1. Xisaabinta Dalag-yada(sida hadhuudhka Galayda bariiska iwm)

**Endpoint:**

```bash
https://esakoapi.org/api/dalag/9920?nooc=1
```

**Sharaxaad:**

inta hore ee *https://esakoapi.org/api/* mar walba waa loo bahan yahay

| Nooca Waxa Aad Xisaabinayso | Xadiga                                    | Query   |
| --------------------------- | ----------------------------------------- | ------- |
| dalag = `string`            | 9920 xadiga fidada dalag KG ahaan = `int` | ?nooc=1 |

**Fahanka query-ga:**
dalag yada marka la eego sida ay u baxeen waa sadex nooc sida kutubta fiqigana ku taal

- Nooc Ku Baxay Biyihii Dabiciga ahaa ilaahay Keenay wax Qarash Ahna Aanu Galin waraabitood
  noocan waxaan u soo qaadanay lanbarka-ka **`1`** sidaas darteed waxaad adeegsan doontaa `?nooc=1`
  hadii aad xisaabinayso sakada lagu leeyahay noocan 1aad

  ### Tusaale

  ```bash
  https://esakoapi.org/api/dalag/9920?nooc=1
  ```

- Nooca Labaad Kuwo ku Baxay Biyo Kharash Galay Sida in Loo IIbiyay Biyihii
  noocana waxaan u soo qaadanay Lanbarka **`2`** sidaas darteed hadii aad noocan xisaabinayso
  waxaad adeegsan doontaa sidan `?nooc=2`

  ### Tusaale

  ```bash
  https://esakoapi.org/api/dalag/9920?nooc=2
  ```

- Nooca Sadexaad Kuwo ku Baxay Biyo Kharash Galay Sida in Loo IIbiyay Biyihii iyo Biyo roob oo aan
  kharash galin oo isku jira
  noocana waxaan u soo qaadanay Lanbarka **`3`** sidaas darteed hadii aad noocan xisaabinayso
  waxaad adeegsan doontaa sidan `?nooc=3`

  ### Tusaale

  ```bash
  https://esakoapi.org/api/dalag/9920?nooc=3
  ```

---

**Response Tusaale:**

```json
{
  "code": 200,
  "jawaab": 90,
  "Shuruudo": [
    "Waa Inuu Yahay Dalag Roob Ku Baxay",
    "Waa In La Goostay Oo La Kaydsan Karro Sida Hadhuudh, Bariis, Ama Galley"
  ],
  "Qiyaas": "Kg",
  "Taariikh": "Monday 13-October-2025",
  "Wakhti": "10:33 AM"
}
```

### 1. Xisaabinta Geela

**Endpoint:**

```bash
https://esakoapi.org/api/geel/35
```

**Sharaxaad:**

inta hore ee *https://esakoapi.org/api/* mar walba waa loo bahan yahay

| Nooca Waxa Aad Xisaabinayso | Xadiga                 |
| --------------------------- | ---------------------- |
| geel = `string`             | 35 xadiga Geel = `int` |

**Response Tusaale:**

```json
{
  "code": 200,
  "jawaab": 1,
  "Shuruudo": [
    "Waxa La Bixinayaa Waa Geel",
    "Waa Inuu Galay Sanadkii 2Aad",
    "Waa Inuu Yahay Dhedig"
  ],
  "Qiyaas": "Neef",
  "Taariikh": "Monday 13-October-2025",
  "Wakhti": "10:33 AM"
}
```

### 1. Xisaabinta lo'a-da

**Endpoint:**

```bash
https://esakoapi.org/api/lo/35
```

**Sharaxaad:**

inta hore ee *https://esakoapi.org/api/* mar walba waa loo bahan yahay

| Nooca Waxa Aad Xisaabinayso | Xadiga                  |
| --------------------------- | ----------------------- |
| lo = `string`               | 35 xadiga Looda = `int` |

**Response Tusaale:**

```json
{
  "code": 200,
  "jawaab": 1,
  "Shuruudo": [
    "Waa Inuu Galay Sanadkii 2Aad (Tabiic Ama Tabiica)",
    "Inuu Dhedig Noqdo Ayaa Fiican Labna Waad Ku Bixin Kartaa",
    "waa inuu yahay neef Lo'a ah "
  ],
  "Qiyaas": "neef",
  "Taariikh": "Monday 13-October-2025",
  "Wakhti": "10:33 AM"
}
```

### 1. Xisaabinta Adhiga

**Endpoint:**

```bash
https://esakoapi.org/api/adhi/62
```

**Sharaxaad:**

inta hore ee *https://esakoapi.org/api/* mar walba waa loo bahan yahay

| Nooca Waxa Aad Xisaabinayso | Xadiga                   |
| --------------------------- | ------------------------ |
| adhi = `string`             | 62 xadiga adhiga = `int` |

**Response Tusaale:**

```json
{
  "code": 200,
  "jawaab": 1,
  "Shuruudo": [
    "Haduu Yahay Ido Waa In Sanad U Buuxsamay",
    "Haduu Yahay Riyo Waa In Uu Gaadhay 2 Sano "
  ],
  "Qiyaas": "neef",
  "Taariikh": "Monday 13-October-2025",
  "Wakhti": "10:33 AM"
}
```

## Programming Language

The API is built using Python, making it easy to integrate into both frontend and backend projects.
You can also use any language you prefer, such as:

- JavaScript
- Go
- Ruby
- C#
- C++
- Python

### JavaScript Example

```JavaScript
const sakoapi = "https://esakoapi.org/api/rikaas/100";
const sako = async () => {
  try {
    const respnse = await fetch(sakoapi);
    const data = await respnse.json();
    console.log(data);
    console.log(`waxaa lagaa doonayaa ${data.jawaab} ${data.Qiyaas}`); //waxaa lagaa doonayaa 20 Giraam
  } catch (Error) {
    console.log(Error);
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
    response.raise_for_status()  # hubi in request-ku uu guuleystay
    data = response.json()       # JSON-ka ka soo saar response
    print(data)
except requests.exceptions.RequestException as e:
    print("Error:", e)


```

## ⚠️ Note

This project is still under testing. If you notice any errors—legal, textual, or technical—you’re welcome to share feedback.

## 🤝 Contribute

This is an open-source project under the MIT License. Contributions are welcome!
📧 jumhuur123@hotmail.com
📞 +25263464519
