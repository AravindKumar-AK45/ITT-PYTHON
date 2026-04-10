         
    1. Course.py


user_a = {"Python", "Data Science", "Web Design", "AI"}
user_b = {"Web Design", "AI", "Graphic Design", "Marketing"}


common = user_a.intersection(user_b)


a = user_b.difference(user_a)


b = user_a.difference(user_b)


print("Common Interests:", common)
print("New courses for User A:", a)
print("New courses for User B:", b)





     2. Homework.py 

records = [
    "Arun:AI,ML,Robotics", "Bala:ML,IoT", "Chitra:AI,CyberSecurity", 
    "Divya:Robotics,IoT,AI", "Ezhil:ML,CyberSecurity", "Farah:AI,ML", 
    "Ganesh:IoT,Robotics,AI", "Hari:ML"
]

student_names = set()
all_clubs = set()
student_club_map = {}

for entry in records:
    name, clubs_str = entry.split(":")

    club_set = {c.strip() for c in clubs_str.split(",")}
    
    student_names.add(name)
    all_clubs.update(club_set)
    student_club_map[name] = club_set


ai_and_ml = [n for n, c in student_club_map.items() if {"AI", "ML"}.issubset(c)]


ai_not_robo = [n for n, c in student_club_map.items() if "AI" in c and "Robotics" not in c]


not_alone = set()
for club in all_clubs:

    if all(len(c) > 1 for c in student_club_map.values() if club in c):
        not_alone.add(club)


vowel_names = [n for n in student_names if n[0].lower() in 'aeiou']
vowel_club_intersection = student_club_map[vowel_names[0]].copy()
for n in vowel_names:
    vowel_club_intersection &= student_club_map[n]


consonant_names = [n for n in student_names if n[-1].lower() not in 'aeiou']
consonant_union = set()
for n in consonant_names:
    consonant_union |= student_club_map[n]


all_chars = {char.lower() for name in student_names for char in name}


common_chars = set(vowel_names[0].lower()) 
for name in student_names:
    common_chars &= set(name.lower())

arun_set = set("arun".lower())
subset_of_arun = [n for n in student_names if set(n.lower()).issubset(arun_set)]


club_combos = list(student_club_map.values())
identical_counts = 0
for i in range(len(club_combos)):
    for j in range(i + 1, len(club_combos)):
        if club_combos[i] == club_combos[j]:
            identical_counts += 1


sorted_students = sorted(student_names, key=lambda x: (-len(student_club_map[x]), x))


def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

hari_clubs = student_club_map["Hari"]
final_set = set()
for n, c in student_club_map.items():
    len_prime = is_prime(len(n))
    has_vowel_club = any(club[0].lower() in 'aeiou' for club in c)
    no_hari_overlap = c.isdisjoint(hari_clubs)
    
    if len_prime and has_vowel_club and no_hari_overlap:
        final_set.add
print(f"AI & ML Members: {ai_and_ml}")
print(f"Sorted Students: {sorted_students}")
print(f"Final Set (Prime/VowelClub/NoHari): {final_set}")





        3. ipaddress.py 

L = {"192.168.1.1", "10.0.0.1", "172.16.0.1"} 
F = {"10.0.0.1", "192.168.1.5", "172.16.0.2"} 
B = {"172.16.0.2", "8.8.8.8"}                 

problem_1 = (L & F) - B

problem_2 = F - L

problem_3 = B - (L | F)

print("Both success/failed but not blacklisted:", problem_1)
print("Attempted but never succeeded:", problem_2)
print("Blacklisted but never attempted:", problem_3)



        4. products.py

all_products = {"Laptop", "Phone", "Camera", "Watch", "Tablet", "Headphones"}
sold_products = {"Phone", "Tablet", "Headphones"}
in_stock = all_products.difference(sold_products)
sold_out = sold_products

print("Products currently in stock:", in_stock)
print("Products already sold:", sold_out)

[24bcs164@mepcolinux week4]$cat skills.py
required_skills = {"Python", "SQL", "Cloud", "Django", "Excel"}
applicant_skills = {"Python", "SQL"}
outdated_skills_str = "Excel, Fortran, Perl"

outdated_set = {s.strip() for s in outdated_skills_str.split(",")}

missing_skills = (required_skills - applicant_skills) - outdated_set

print("Required Skills:", required_skills)
print("Applicant Has:", applicant_skills)
print("Outdated Skills to ignore:", outdated_set)
print("-" * 30)
print("Missing Required Skills:", missing_skills)

         
            


        5. student.py


day1 = {10, 15, 20, 25, 30, 35}
day2 = {25, 30, 35, 40, 45, 50}

both_days = day1.intersection(day2)
either_day = day1.union(day2)
absent_day2 = day1.difference(day2)

print("Roll numbers present BOTH days:", both_days)
print("Roll numbers present EITHER day:", either_day)
print("Roll numbers absent on Day 2:", absent_day2)


