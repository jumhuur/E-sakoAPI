from Nisaabyo import Sako , selfinfo
URL_DOC = "https:esakoapi.com/docs"
Errors_Code_messages = {
    # Errors
    460:"Fadlan Markale isku day".title(),
    461 :"Qaab Tiro Ahaan Ah U qor Xadiga aad Xisaabinayso".title(),
    462:"Lama Ogola Waxa Aad Dooratay".title(),
    463: "Nooca Aad dooratay kama mid ah noocyada Dahabka".title(),
    464: "Fadlan adeegso Tiro Kaliya".title(),
    465: "Fadlan Adeegso Tiro Ka kooban laba Lanbar".title(),
    466: "Sako Laguma laha xadiga aad qortay Ee Ka tirsan nooca dahabka aad dooratay".title(),
    467: f"Waxaa Qaldan URL-KA Halkan Ka Akhriso Faah Faahinta {URL_DOC}",


    # warbixin
    320: "dahabka aad xisabinaysaa sako(nisaab) ma gaadhin waxa uu ku gaadhaa sako(nisaab) 85-g".title(),
    325: F"Qiimaha lacagtu sako ma gaadhin lacagtu waxay sako ku gaadhaa {round(selfinfo.Nisaab_lacag_d, 4)}$ marka lagu xisaabiyo Dahab ama {round(selfinfo.Nisaab_Lacag_f, 4)}$ marka lagu xisaabiyo Fido".title(),
}

def Errors(code,succsess=False):
    return {"code": code, "Fariin": Errors_Code_messages.get(code), "ok": succsess}