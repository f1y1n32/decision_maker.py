age = int(input("What is your age?"))

if age >= 18:
    print("you are an adult")
else:
    print("you are a minor")
    
    
score = int(input("What is your. test score?"))

if score >= 90:
    print("A")
elif score <= 89 and score >= 80:
    print("B")
elif score <= 79 and score >=70:
    print("C")
elif score <= 69 and score >= 60:
    print("D")
else:
    print("F")