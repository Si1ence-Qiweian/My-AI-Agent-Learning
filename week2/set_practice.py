languages = [
    "Python", "Java", "Python",
    "Go", "Java", "Rust", "Go"
]
set_languages = set(languages)
print(set_languages)
print(len(set_languages))

student_a = {"Python", "Git", "SQL", "HTML"}
student_b = {"Python", "Docker", "Git", "JavaScript"}
skill_shared = student_a & student_b
skill_unique = student_a | student_b
skill_a = student_a - student_b
print(skill_shared)
print(skill_unique)
print(skill_a)

words = [
    "python", "is", "a", "language",
    "python", "is", "powerful"
]
stop_words = {"is", "a", "the"}
filtered_words = [word for word in words if word not in stop_words]
print(filtered_words)
