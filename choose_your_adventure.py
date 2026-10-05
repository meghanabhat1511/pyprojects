name=input("type your name: ")
print("welcome",name,"to this adventure!")


ans=input("you are on a dirt road, you can go left or right! which way would you like to go?").lower()

if(ans=="left"):
 ans=input("you come to a river, you can walk around it or swim across? type walk to walk around and swim to swim across: ").lower()
 if(ans=="walk"):
   print("you walked for many miles, ran out of water and you lost the game.")
 elif(ans=="swim"):
    print("you swam across and were eaten by an alligator.")
 else:
  print("not a valid option.you lose.")
elif(ans=="right"):
  ans=input("you come to a bridge, it looks wobbly, do you want to cross it or head back? type cross to cross it and back to head back: ").lower()
  if(ans=="cross"):
    print("you crossed the bridge and found a treasure!")
  elif(ans=="back"):
    print("you went back and lost the game.")
  else:
    print("not a valid option.you lose.")

else:
 print("not a valid option.you lose.")
print("thank you for playing",name)

