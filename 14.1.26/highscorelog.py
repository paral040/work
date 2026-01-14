score1 = int(input("Enter high score 1: "))
score2 = int(input("Enter high score 2: "))
score3 = int(input("Enter high score 3: "))
score4 = int(input("Enter high score 4: "))
score5 = int(input("Enter high score 5: "))

def check_score(score):
    if score >= 80:
        return "Elite"
    else:
        return "Standard"

print(f"Score 1: {check_score(score1)}")
print(f"Score 2: {check_score(score2)}")
print(f"Score 3: {check_score(score3)}")
print(f"Score 4: {check_score(score4)}")
print(f"Score 5: {check_score(score5)}")