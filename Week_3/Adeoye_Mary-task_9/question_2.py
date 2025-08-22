student = {}
student["name"]= input("kindly enter your name: ")
student["age"]= int(input("kindly input your age: "))
student["waec_result"] =(input("do you pass all your waec at a credit level or A and B? input either True or False: ")).title()
student["jamb_score"] = int(input("kindly entr your jamb score: "))
student["post_utme"] = int(input("kindly input your post utme score here: "))

age_eligibility= student["age"] >=16
waec_eligibility = student["waec_result"] ==True
jamb_eligiblity = student["jamb_score"] >= 200
post_utme_eligibility = student["post_utme"] >= 70
total_eligibility = age_eligibility and waec_eligibility and jamb_eligiblity and post_utme_eligibility
print(f"Dear candidate you meet up the above department cutoff mark and you are qualify for this addimission.Here are your Biodata's Name::{student["name"]}\nAge:{student["age"]}\nWaec_result:{student["waec_result"]}\nJamb_score:{student["jamb_score"]}\n")




# Nested if for Age
age = int(input("kindly input your age here: "))


if age >= 16:
    print("You are eligibible to proceed with your admission process")
else:
        print("Too young to proccess admission")


# weac_eligibility
Grade = input("kindly enter your weac results grades with the minimum of five credits: ").title()
if Grade == "A":
      print("You can procced with your admission processes: ") 
elif Grade == "B":
      print("Grade B")
elif Grade == "C":
      print("Grade C")
else:
      print("you are not eligible to proceeed with this admission process")




      