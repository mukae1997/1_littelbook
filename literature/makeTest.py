import json
chap1 =  [
'Happy families are all alike; every unhappy family is unhappy in its own way.',


'Everything was in confusion in the Oblonskys house. The wife had discovered that the husband was carrying on an intrigue with a French girl, who had been a governess in their family, and she had announced to her husband that she could not go on living in the same house with him. This position of affairs had now lasted three days, and not only the husband and wife themselves, but all the members of their family and household, were painfully conscious of it. Every person in the house felt that there was so sense in their living together, and that the stray people brought together by chance in any inn had more in common with one another than they, the members of the family and household of the Oblonskys. The wife did not leave her own room, the husband had not been at home for three days. The children ran wild all over the house; the English governess quarreled with the housekeeper, and wrote to a friend asking her to look out for a new situation for her; the man-cook had walked off thp',

'e day before just at dinner time; the kitchen-maid, and the coachman had given warning.'


]
chap2 = [
'Three days after the quarrel, Prince Stepan Arkadyevitch Oblonsky--Stiva, as he was called in the fashionable world-- woke up at his usual hour, that is, at eight o\'clock in the morning, not in his wife\'s bedroom, but on the leather-covered sofa in his study. He turned over his stout, well-cared-for person on the springy sofa, as though he would sink into a long sleep again; he vigorously embraced the pillow on the other side and buried his face in it; but all at once he jumped up, sat up on the sofa, and opened his eyes.',

'"Yes, yes, how was it now?" he thought, going over his dream. "Now, how was it? To be sure! Alabin was giving a dinner at Darmstadt; no, not Darmstadt, but something American. Yes, but then, Darmstadt was in America. Yes, Alabin was giving a dinner on glass tables, and the tables sang, Il mio tesoro--not Il mio tesoro though, but something better, and there were some sort of little decanters on the table, and they were women, too," he remembered.'
]
sf =  {
    'name': "Anna Karenina",
    'type':"fiction",
    'publish_year':"2017",
    'pages': 2,
    'link':"/",
    "content": {
        'chap1':chap1,
        'chap2':chap2
    }
}
# print(json_str)
with open('1.json', 'w') as outfile:
    json.dump(sf, outfile)


scene1 = ['GLOSTER. Now tell me, brother Clarence, what think you Of this new marriage with the Lady Grey? Hath not our brother made a worthy choice?',
'CLARENCE. Alas! you know \'t is far from hence to France; How could he stay till Warwick made return?'
]
scene2 = ['A Plain in Warwickshire',
'WARWICK. Trust me, my lord, all hitherto goes well; The common people by numbers swarm to us. But see where Somerset and Clarence comes!-- ',
'[Enter CLARENCE and SOMERSET.] '
]

kh =  {
    'name': "King Henry VI, Third Part",
    'type':"play",
    'publish_year':"1591",
    'pages': 93,
    'link':"/",
    "content": {
        'actIV': {
            'scene1':{
                'deepscene':scene1
            },
            'scene2':scene2
        }
    }
}
with open('2.json', 'w') as outfile:
    json.dump(kh, outfile)
