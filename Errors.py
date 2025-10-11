Errors_Code_messages = {
    # Errors
    460:"Fadlan Markale isku day".title(),
    461 :"Qaab Tiro Ahaan Ah U qor Xadiga aad Xisaabinayso".title(),
    462:"Lama Ogola Waxa Aad Dooratay".title(),
    463: "Nooca Aad dooratay kama mid ah noocyada Dahabka".title(),
    464: "Fadlan adeegso Tiro Kaliya".title(),
    465: "Fadlan Adeegso Tiro Ka kooban laba Lanbar".title(),
    466: "Sako Laguma laha xadiga aad qortay Ee Ka tirsan nooca dahabka aad dooratay".title(),


    # warbixin
    320: "dahabka aad xisabinaysaa sako(nisaab) ma gaadhin waxa uu ku gaadhaa sako(nisaab) 85-g".title(),
}

def Errors(code,succsess=False):
    return {"code": code, "msg": Errors_Code_messages.get(code), "ok": succsess}