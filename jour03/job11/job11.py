def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0: 
        heures = minutes // 60 
        minutes_restantes = minutes % 60  

        if heures == 1:
            heure_texte = "heure"
        else:
            heure_texte = "heures"

        if minutes_restantes == 1:
            minute_texte = "minute"
        else:
            minute_texte = "minutes"

        print(f"{heures} {heure_texte} et {minutes_restantes} {minute_texte}")
    else:
        print("Veuillez entrer un nombre entier positif de minutes.")

time_to_text(112)
time_to_text(75)
time_to_text(90)
time_to_text(30)
time_to_text(-5)
time_to_text(0)
