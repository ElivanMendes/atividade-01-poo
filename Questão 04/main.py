note_1 = float(input("Informe a Primeiro Nota: "))
note_2 = float(input("Informe a Segundo Nota: "))

if note_1 < 0.0 or note_1 > 10.0 or note_2 < 0.0 or note_2 >10.0:
    print("Notas Invalidas! Informe uma Nota Entre 0 a 10.")
else:
    average = (note_1 + note_2) / 2
    print("Media: %.2f" % average)
