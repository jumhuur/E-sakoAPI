from Nisaabyo import Sako, selfinfo

URL_DOC = "https://esakoapi.org/doc"

Errors_Code_messages = {
    # global
    404: f"This URL does not exist Read more details here: {URL_DOC}.",

    # Errors
    460: f"Please try again later.",
    461: f"Please enter a valid numeric amount Read more details this URL: {URL_DOC}.",
    462: "The option you selected is not allowed.",
    463: f"The selected type is not among the recognized gold types Read more details this URL: {URL_DOC}.",
    464: f"Please use numbers only Read more details this URL: {URL_DOC} .",
    465: f"Please use a number that contains at least two digits.",
    466: f"Zakat is not applicable to the amount you entered for this gold type Read more details this URL: {URL_DOC}.",
    467: f"Invalid URL. Read more details this URL: {URL_DOC}",
    468: f"The calculation type you requested is invalid. Accepted types are 1, 2, or 3. Read more details here: {URL_DOC}",

    # Info messages
    320: "The amount of gold you entered has not reached the Zakat threshold (Nisaab). The Nisaab for gold is 85 grams.",
    321: f"The amount of silver has not reached the Zakat threshold. The Nisaab for silver is {round(Sako.Nisaab_Fidada, 4)} grams.",
    322: f"The number of sheep you entered has not reached the Zakat threshold. The Nisaab for sheep is {Sako.Nisaab_adhi} heads.",
    323: f"The amount of rikaas has not reached the Zakat threshold. The Nisaab for rikaas is {round(Sako.Nisaab_Rikaas, 4)} grams.",
    324: f"The number of cows you entered has not reached the Zakat threshold. The Nisaab for cows is {Sako.Nisaab_lo} heads.",
    325: f"The amount of money has not reached the Zakat threshold. The Nisaab for money is {round(selfinfo.Nisaab_lacag_d, 4)} USD (based on gold) or {round(selfinfo.Nisaab_Lacag_f, 4)} USD (based on silver).",
    326: f"The number of camels you entered has not reached the Zakat threshold. The Nisaab for camels is {Sako.Nisaab_Geel} heads.",
    327: f"The amount of crops you entered has not reached the Zakat threshold. The Nisaab for crops is {Sako.Nisaab_Midhaha} kg."
}

def Errors(code, success=False):
    return {"code": code, "message": Errors_Code_messages.get(code), "ok": success}
