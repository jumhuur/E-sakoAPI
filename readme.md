# EsakoAPI

**EsakoAPI** waa API bilaash ah (free API) oo aadan u baahnayn **API key** si aad u isticmaasho. Waxaa loogu talagalay in lagu xisaabiyo **sakada noocyadeeda kala duwan** sida waafaqsan shareecada Islaamka.

Waxaad ku xisaabin kartaa waxyaabaha kala duwan ee sakada laga bixiyo sida:

- **Dahab**
- **Lacag**
- **Midhaha**
- **Rikaas** (macdanta dhulka)

Iyo sidoo kale **xoolaha** noocyadooda kala duwan sida:

- **Geela**
- **Adhiga**
- **Looda**

Waxaa kale oo lagu daray **midhaha baxa ee dadku beertaan** noocyadooda kala duwan.

API-ga waxaa loo qaabeeyay si uu u bixiyo **jawaabo degdeg ah** oo ku dhisan kitaabka Ilaahay iyo sunada Rasuulka (NNKH), iyadoo loo marayo algorithms qoto dheer oo u hoggaansamaya sharciga sakada.

---

## Tijaabinta API-ga

Si aad u tijaabiso EsakoAPI, booqo:  
[https://esakoapi.org](https://esakoapi.org)

Halkan waxaa ku yaal tusaalooyin **endpoint** iyo sharaxaad ku saabsan:

### 1. Xisaabinta Dahabka

**Endpoint:**

```bash
https://esakoapi.org/api/dahab/24,145
```

**Sharaxaad:**

- `dahab` → cadeynaya inaad xisaabinayso dahab
- `24` → nooca dahabka (waxaad badali kartaa: 22, 21, 20, 18, 16)
- `145` → xadiga dahabka aad doonayso inaad ogaato sakada lagu leeyahay

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

**Qiyaas** → qiyaasta jawaabta (halkan: giraam)

_Taariikh iyo Wakhti_ → waqtiga jawaabta la helay, maadaama qiimaha dahabku isbeddeli karo

## Luqadda Barnaamijka

API-ga waxaa lagu programiyay **Python**, taas oo fududaynaysa in lagu daro mashruucyada kala duwan oo backend ah.

laakiin waxaad u adeegsan kartaa luuqada aad aduu xiisanayso sida

- js
- go
- rupy
- c#
- c++
  iyo
- python lafteeda

### Tusaale JavaScript

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

### Tusaale JavaScript

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

Fiiro Gaar ah

Hadda mashruucan weli gacanta lagu hayaa , waxaad si ku meel gaadh ah ugu tijaabin kartaa endpoints-ka kor ku xusan.
