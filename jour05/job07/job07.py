def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note >= 40 and note % 5 >= 3 and note % 5 != 0:
            note = note + 5 - (note % 5) 
        notes_arrondies.append(note)
    return notes_arrondies

liste_notes = [83, 72, 54, 39, 90]
notes_arrondies = arrondir_notes(liste_notes)
print("Notes originales :", liste_notes)
print("Notes arrondies :", notes_arrondies)
