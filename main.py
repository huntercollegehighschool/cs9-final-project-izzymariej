"""
Name(s): Zoe Jalkut
Name of Project: Mad Libs - Depressing Poetry Style
With poems from Edgar Allen Poe, Maya Angelou, and Theodore Roethke
"""

#Write the main part of your program here. Use of the other pages is optional.



verb1 = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
adj1 = input("Enter a adjective: ")

verb2 = input("Enter another verb: ")
noun2 = input("Enter another noun: ")
adj2 = input("Enter another adjective: ")

verb3 = input("Enter another verb: ")
noun3 = input("Enter another noun: ")
adj3 = input("Enter another adjective: ")

story2 = ('The free '+noun1+' thinks of '+adj1+' breeze'
'\ and the trade winds soft through the sighing trees'
'\ and the fat '+noun2+' '+verb1+' on a dawn '+adj2+' lawn'
'\ and he names the sky his own.'
'\ But a '+adj3+' '+noun3+' stands on the grave of dreams'
'\ his shadow '+verb1+' on a nightmare scream'
'\ his wings are clipped and his feet are tied'
'\ so he opens his throat to '+verb1+ '.')

story1 = ('For the moon never beams, without ' +verb1+ ' me dreams'
' \Of the ' +adj1+ ' Annabel Lee;'
' \And the stars never ' +verb2+ ', but I feel the '+adj2+' eyes'
'  \ Of the '+adj3+' Annabel Lee;'
' \And so, all the night-tide, I' +verb3+ 'down by the side'
'   \Of my darling—my darling—my life and my ' +noun1+ 
'   \In her sepulchre there by the ' +noun2+
'   \In her tomb by the sounding ' +noun3+'.')

story0 = ('I have known the ' +adj1+ ' sadness of ' +noun1+ 
'\ Neat in their boxes, dolor of pad and paper weight' 
'\ All the misery of manilla folders and mucilage'
'\ ' +verb1+ ' in immaculate public' +noun2+
'\ Lonely reception room, lavatory, switchboard'
'\ The ' +adj1+ ' pathos of basin and pitcher'
'\ Ritual of multigraph, paper-clip, comma' 
'\ Endless ' +verb2+ 'of lives and objects' 
'\ And I have seen dust from the walls of institutions'
'\ Finer than flour, alive, more ' +adj3+ ' than silica' 
'\ Sift, almost invisible, through long afternoons of tedium'
'\ Dropping a fine ' +noun3+ ' on nails and delicate eyebrows '
'\ ' +verb3+ 'the pale hair, the duplicate grey standard faces.')



import random
vars = [story0, story1, story2]
print(random.sample(vars, 1))