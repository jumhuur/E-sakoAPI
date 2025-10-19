from Errors import Errors
from Nisaabyo import Sako , selfinfo
from jawaabo import jawaab
from fastapi.responses import JSONResponse
import re

def Loa(xadi):
    Sako.data_collection(xadi)
    nisaab = {
        1: 40,
        2: 60,
    }

    reg_exp = r"^\d+$"
    if not re.match(reg_exp, str(xadi)):
        return JSONResponse(status_code=464, content=Errors(464))
    if int(xadi) > Sako.Nisaab_lo and int(xadi) < nisaab[1]:
        jw = 1
        shuruudo = [
            "It must have entered its second year (Tabiic or Tabiica)".title(),
            "Female is preferred, but male is also acceptable".title(),
            "It must be a cow".title()
        ]
        return JSONResponse(status_code=200, content=jawaab(jw, shuruudo, "heads"))

    if int(xadi) >= nisaab[1] and int(xadi) < nisaab[2]:
        jw = 1
        shuruudo = [
            "It must have entered its third year (Musina or similar)".title(),
            "Female is preferred, but male is also acceptable".title(),
            "It must be a cow".title()
        ]
        return JSONResponse(status_code=200, content=jawaab(jw, shuruudo, "heads"))

    if int(xadi) >= nisaab[1]:
        best_option = None
        tabiic_count = int(xadi) // 30
        musina_count = int(xadi) // 40

        for tabiic in range(tabiic_count + 1):
            for musina in range(musina_count + 1):
                total_covered = 30 * tabiic + 40 * musina
                if total_covered > int(xadi):
                    continue
                remainder = int(xadi) - total_covered
                candidate = {
                    "Tabiic": tabiic,
                    "Musina": musina,
                    "la_daboolay": total_covered,
                    "Hadhaa": remainder,
                    "Sako": tabiic + musina
                }

                if best_option is None:
                    best_option = candidate
                if candidate["Hadhaa"] < best_option["Hadhaa"]:
                    best_option = candidate
                elif candidate["Hadhaa"] == best_option["Hadhaa"]:
                    if candidate["la_daboolay"] > best_option["la_daboolay"]:
                        best_option = candidate
                    elif candidate["la_daboolay"] == best_option["la_daboolay"] and candidate["Sako"] < best_option["Sako"]:
                        best_option = candidate

        if best_option["Tabiic"] > 0 and best_option["Musina"] > 0:
            jw = best_option["Sako"]
            shuruudo = [
                f"{best_option['Tabiic']} cows must be at least one year old".title(),
                f"{best_option['Musina']} cows must be at least two years old".title(),
                "They must be cows, male or female both are acceptable".title()
            ]
            return JSONResponse(status_code=200, content=jawaab(jw, shuruudo, "heads"))

        if best_option["Tabiic"] > 0 and best_option["Musina"] < 1:
            jw = best_option["Tabiic"]
            shuruudo = [
                f"{best_option['Tabiic']} cows must be at least one year old".title(),
                "They must be cows, male or female both are acceptable".title()
            ]
            return JSONResponse(status_code=200, content=jawaab(jw, shuruudo, "heads"))

        if best_option["Tabiic"] < 1 and best_option["Musina"] > 0:
            jw = best_option["Musina"]
            shuruudo = [
                f"{best_option['Musina']} cows must be at least two years old".title(),
                "They must be cows, male or female both are acceptable".title()
            ]
            return JSONResponse(status_code=200, content=jawaab(jw, shuruudo, "heads"))
    else:
        return JSONResponse(status_code=324, content=Errors(324))