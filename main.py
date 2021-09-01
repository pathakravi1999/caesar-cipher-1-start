alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(start_text,shift_amount,cypher_direction):
  new_text=""
  if cypher_direction== "decode":
    shift_amount *= -1
  for letter in start_text:
    if letter in alphabet:
      position= alphabet.index(letter)
      new_position = position + shift_amount
      new_text += alphabet[new_position]
    else:
      new_text += letter
  print(f"Here is {cypher_direction}d result: {new_text} ")


from art import logo
print(logo)


should_continue =True
while should_continue:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift%26

  caeser(start_text = text, shift_amount= shift, cypher_direction = direction)
  restart = input("Do you want to continue yes or no").lower()
  if restart == "no":
    should_continue= False
    print("Goodbye")




  


  

  
  



    



