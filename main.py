import random
import pyperclip

abc = 'abcdefghijklmnopqrstvuwxyz'
extras = '0123456789#$^¨!/;*ù>~&.'
new_password = ''

for _ in range(16):
    character_set = abc if random.choice([True, False]) else extras
    new_password += random.choice(character_set)

pyperclip.copy(new_password)

print("Mot de passe généré et copié dans le presse-papiers:", new_password)
