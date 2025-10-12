# zakat_camels.py

def best_camel_zakat(n):
    if n < 5:
        return {"a":0,"b":0,"covered":0,"remainder":n,"note":"لا يصل للنصاب (أقل من 5)"}

    best = None
    max_a = n // 50
    max_b = n // 40

    for a in range(max_a + 1):
        for b in range(max_b + 1):
            covered = 50*a + 40*b
            # print("a", a)
            # print("b",b)
            # print(covered)
            if covered > n:
                continue
            remainder = n - covered
            cand = {"a":a, "b":b, "covered":covered, "remainder":remainder, "zakat_count": a+b}
            if best is None:
                best = cand
                continue
            print("best",best)
            print("cand", cand)

            if cand["remainder"] < best["remainder"]:
                best = cand
            elif cand["remainder"] == best["remainder"]:
                if cand["covered"] > best["covered"]:
                    best = cand
                elif cand["covered"] == best["covered"] and cand["zakat_count"] < best["zakat_count"]:
                    best = cand

    description = []
    if best["a"] > 0:
        description.append(f'{best["a"]} حِقّة{"ات" if best["a"]>1 else ""}')
    if best["b"] > 0:
        description.append(f'{best["b"]} بنت لبون{"ات" if best["b"]>1 else ""}')
    best["description"] = " + ".join(description) if description else "لا زكاة (أقل من النصاب أو لا يجتمع نصاب)"
    return best

print(best_camel_zakat(180))
