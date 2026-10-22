student = {'imie': 'Kamil', 'nazwisko': 'Nowak', 'wiek': 22, 'kierunek': 'Informatyka'}
student['email'] = 'kamil.nowak@edu.pl'
student['wiek'] = 23
print(f"Student: {student['imie']} {student['nazwisko']} ({student['wiek']} lata), kierunek: {student['kierunek']}, email: {student['email']}")
print(list(student.keys()))
print(list(student.values()))
