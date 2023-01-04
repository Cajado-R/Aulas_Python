from math import trunc
import emoji
num = float(input('Digite um número por favor: ' ))
print(emoji.emojize('o número {} possuí como parte inteira {} HAHA! :couple_with_heart_person_person_medium-dark_skin_tone_light_skin_tone:'.format(num, trunc(num))))