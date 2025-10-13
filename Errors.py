from Nisaabyo import Sako , selfinfo
URL_DOC = "https://esakoapi.org/docs"
Errors_Code_messages = {
    # blobal
    404: "Ma jiro URL-Kani",
    # Errors
    460:"Fadlan Markale isku day".title(),
    461 :"Qaab Tiro Ahaan Ah U qor Xadiga aad Xisaabinayso".title(),
    462:"Lama Ogola Waxa Aad Dooratay".title(),
    463: "Nooca Aad dooratay kama mid ah noocyada Dahabka".title(),
    464: "Fadlan adeegso Tiro Kaliya".title(),
    465: "Fadlan Adeegso Tiro Ka kooban laba Lanbar".title(),
    466: "Sako Laguma laha xadiga aad qortay Ee Ka tirsan nooca dahabka aad dooratay".title(),
    467: f"Waxaa Qaldan URL-KA Halkan Ka Akhriso Faah Faahinta {URL_DOC}".title(),
    468: f"Qaabka aad u dalbatay in loo xisaabiyo dalagan wa qalada ha noqdo qaabku mid ah 1,2,3 waxii faah faahin ah ka akriso {URL_DOC}".title(),


    # warbixin
    320: "dahabka aad xisabinaysaa sako(nisaab) ma gaadhin waxa uu ku gaadhaa sako(nisaab) 85-g".title(),
    321: F"Qiimaha Fidada sako ma gaadhin Fidada waxay sako ku gaadhaa {round(Sako.Nisaab_Fidada, 4)} Giraam".title(),
    322: f"Xadiga Adhiga aad Qoratay Sako Ma gaadhin Adhigu wax uu ku sako gaadhaa {Sako.Nisaab_adhi} Neet".title(),
    323: F"Qiimaha Rikaaska sako ma gaadhin rikaasku waxu  sako ku gaadhaa {round(Sako.Nisaab_Rikaas, 4)} Giraam".title(),
    324: f"Sako Ma gaadhin Xadiga looda aad qoratay Looda waxay ku sako Gaadhaa {Sako.Nisaab_lo} Neef".title(),
    325: F"Qiimaha lacagtu sako ma gaadhin lacagtu waxay sako ku gaadhaa {round(selfinfo.Nisaab_lacag_d, 4)}$ marka lagu xisaabiyo Dahab ama {round(selfinfo.Nisaab_Lacag_f, 4)}$ marka lagu xisaabiyo Fido".title(),
    326: f"Sako laguma laha xadiga aad qortay Geelu Waxa uu Ku sako Gaadhaa {Sako.Nisaab_Geel} Neef".title(),
    327: f"Sako laguma laha xadiga aad qortay dalagu  Waxa uu Ku sako Gaadhaa {Sako.Nisaab_Midhaha} kg".title()
}

def Errors(code,succsess=False):
    return {"code": code, "Fariin": Errors_Code_messages.get(code), "ok": succsess}