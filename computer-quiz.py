#level easyy

print("welcome to my quiz")

playing=input("Do you want to play? ")
if playing.lower()=="yes" or playing.lower()=="y" or playing.lower()=="YES" or playing.lower()=="Y":
 print("okay let's play :)")
else:
    print("may be next time")
    quit()
score=0
answer =input("what does CPU stands for?").lower()
if answer.lower()=="central processing unit":
 print("correct!")
 score+=1
else:
  print("incorrect!")

answer =input("what does GPU stands for?").lower()
if answer.lower()=="graphics processing unit":
 print("correct!")
 score+=1
else:
  print("incorrect!")
answer =input("what does RAM stands for?").lower()
if answer.lower()=="random access memory":
 print("correct!")
 score+=1
else:
  print("incorrect!")
answer =input("what does ROM stands for?").lower()
if answer.lower()=="read only memory":
 print("correct!")
 score+=1
else:
  print("incorrect!")
answer =input("what does PSU stands for?").lower()
if answer.lower()=="power supply unit":
 print("correct!")
 score+=1
else:
  print("incorrect!")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score/5)*100) + "%.")