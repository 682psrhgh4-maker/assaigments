def bayes(p_hazard, p_alarm_if_hazard, p_alarm_if_safe):
    """Байес формуласы бойынша P(HAZARD | ALARM) есептеу"""
    score_hazard = p_hazard * p_alarm_if_hazard
    score_safe = (1.0 - p_hazard) * p_alarm_if_safe
    denominator = score_hazard + score_safe
    return score_hazard / denominator



# A 
p_h0 = 0.20  # Априорлық ықтималдық P(HAZARD)

# ALARM және NORMAL сигналы үшін есептеу
p_h_alarm = bayes(p_h0, p_alarm_if_hazard=0.90, p_alarm_if_safe=0.10)
p_h_normal = bayes(p_h0, p_alarm_if_hazard=0.10, p_alarm_if_safe=0.90)

print(f"P(HAZARD | ALARM)  = {p_h_alarm:.4f} ({p_h_alarm * 100:.2f}%)")
print(f"P(HAZARD | NORMAL) = {p_h_normal:.4f} ({p_h_normal * 100:.2f}%)")



# C 
observations = ["ALARM", "NORMAL", "ALARM", "ALARM"]
p_h = 0.20  # t0 сәтіндегі бастапқы сенім

print("t  Сигнал    Болжам P(H)  Жаңартылған P(H)  Жаңартылған P(S)")
print("-" * 60)

for t, obs in enumerate(observations, start=1):
    # 1-қадам: Болжау (Predict)
    if t == 1:
        pred_h = p_h  # t1 сәтінде ауысу қолданылмайды
    else:
        # Ауысу моделі: P(Ht|Ht-1) = 0.80, P(Ht|St-1) = 0.10
        pred_h = 0.80 * p_h + 0.10 * (1.0 - p_h)

    # 2-қадам: Эмиссия (Сенсор шартты ықтималдықтары)
    p_e_h = 0.90 if obs == "ALARM" else 0.10
    p_e_s = 0.10 if obs == "ALARM" else 0.90

    # 3-қадам: Жаңарту (Update)
    p_h = bayes(pred_h, p_e_h, p_e_s)
    p_s = 1.0 - p_h

    print(f"t{t} {obs:<9} {pred_h:.4f}       {p_h:.4f}            {p_s:.4f}")



# D 

priors = [0.05, 0.20, 0.50, 0.80]

print("Бастапқы P(H)  ->  Соңғы P(HAZARD | ALARM)")
print("-" * 45)
for p in priors:
    res = bayes(p, p_alarm_if_hazard=0.90, p_alarm_if_safe=0.10)
    print(f"P(H) = {p:.2f}      ->  P(HAZARD | ALARM) = {res:.4f} ({res * 100:.2f}%)")
