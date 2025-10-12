from Nisaabyo import Sako , selfinfo
import re
from Errors import Errors
from jawaabo import jawaab
def saafi(nooc:int,xadiga:int)-> int:
    result = (xadiga * nooc) / Sako.Noocyo["24"]
    return result
def xisaab_Dahab(nooc:int,xadiga:float):
    reg = r"^\d{2}$"
    # Hubin in Tiradu tahay laba lanbar oo kaliya sida 24 - 16
    if re.match(reg, str(nooc)):
        grams = []
        # noocyadii dahabka ahaa ee dict ahaan aan kaga soo qaatay class-ka Sako
        # ayaan waxaan u badashay list si aan u hubiyo in noocu yahay mid kamid kuwaas
        for n_key , n_value in Sako.Noocyo.items():
            grams.append(n_value)
        if nooc in grams: # waxaa la hubinayaa in grams-ka nooca user-ka qoray kamid yahay 
                if type(xadiga) == float:
                    if xadiga >= Sako.Nisaab_dahab:
                        # xisaabinta rasmiga ah waa halkan
                        if nooc == Sako.Noocyo["24"]:
                            jw = round(xadiga / Sako.Dahab_40, 4)
                            usd_price = round(jw  * selfinfo.qiimaha_dahab_24, 4)
                            return jawaab(jw, ["waa inuu yahay saafi 100%".title(), "waa inaad sanad haysay".title(), f"lacag hadaad ku bixinayso waa {usd_price}$".title()], "Giraam")
                        elif nooc == Sako.Noocyo["22"]:
                            d_saafi = saafi(nooc,xadiga)
                            if d_saafi >= Sako.Nisaab_dahab:
                                jw = round(d_saafi / Sako.Dahab_40 , 4)
                                usd_price = round(jw  * selfinfo.qiimaha_dahab_24, 4)
                                return jawaab(jw, [f"waa inuu yahay nooca {nooc}".title(), "waa inaad sanad haysay".title(), f"lacag hadaad ku bixinayso waa {usd_price}$".title()], "Giraam")
                            else:
                                return Errors(466, True)
                        elif nooc == Sako.Noocyo["21"]:
                            d_saafi = saafi(nooc,xadiga)
                            if d_saafi >= Sako.Nisaab_dahab:
                                jw = round(d_saafi / Sako.Dahab_40 , 4)
                                usd_price = round(jw  * selfinfo.qiimaha_dahab_24, 4)
                                return jawaab(jw, [f"waa inuu yahay nooca {nooc}".title(),"waa inaad sanad haysay".title()], f"lacag hadaad ku bixinayso waa {usd_price}$".title(), "Giraam")
                            else:
                                return Errors(466, True)
                        elif nooc == Sako.Noocyo["20"]:
                            d_saafi = saafi(nooc,xadiga)
                            if d_saafi >= Sako.Nisaab_dahab:
                                jw = round(d_saafi / Sako.Dahab_40 , 4)
                                usd_price = round(jw  * selfinfo.qiimaha_dahab_24, 4)
                                return jawaab(jw, [f"waa inuu yahay nooca {nooc}".title(), "waa inaad sanad haysay".title(), f"lacag hadaad ku bixinayso waa {usd_price}$".title()], "Giraam")
                            else:
                                return Errors(466, True)
                        elif nooc == Sako.Noocyo["18"]:
                            d_saafi = saafi(nooc,xadiga)
                            if d_saafi >= Sako.Nisaab_dahab:
                                jw = round(d_saafi / Sako.Dahab_40 , 4)
                                usd_price = round(jw  * selfinfo.qiimaha_dahab_24, 4)
                                return jawaab(jw, [f"waa inuu yahay nooca {nooc}".title(), "waa inaad sanad haysay".title(), f"lacag hadaad ku bixinayso waa {usd_price}$".title()], "Giraam")
                            else:
                                return Errors(466, True)
                        elif nooc == Sako.Noocyo["16"]:
                            d_saafi = saafi(nooc,xadiga)
                            if d_saafi >= Sako.Nisaab_dahab:
                                jw = round(d_saafi / Sako.Dahab_40 , 4)
                                usd_price = round(jw  * selfinfo.qiimaha_dahab_24, 4)
                                return jawaab(jw, [f"waa inuu yahay nooca {nooc}".title(), "waa inaad sanad haysay".title(), f"lacag hadaad ku bixinayso waa {usd_price}$".title()], "Giraam")
                            else:
                                return Errors(466, True)
                        else:
                            return Errors(463)
                    else:
                        return Errors(320,True)
                else:
                    return Errors(461)
        else:
            return Errors(463)
    else:
        return f"{Errors(465)}"