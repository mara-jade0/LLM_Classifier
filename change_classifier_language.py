#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 20:17:42 2023

@author: lilith
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:53:09 2023

@author: lilith
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

api_key = os.getenv('OPENAI_API_KEY')
load_dotenv()
client = OpenAI(api_key=api_key) #OpenAI()


# Replace with your actual OpenAI API key
#openai.api_key = 'your-api-key'

# Example text strings with Has attribute/Does not have attribute labels
# Example text strings with Has attribute/Does not have attribute labels
labeled_statements = [
    {'Input': 'The library was a haven of tranquility, filled with the scent of old books.', 'Label': 'Does not have attribute'},
    {'Input': 'A gentle breeze rustled the green leaves of the tall oak tree.', 'Label': 'Does not have attribute'},
    {'Input': 'The library wass a haven of tranquility, filled with the scent of old books.', 'Label': 'Has attribute'},
    {'Input': 'A kaleidoscope of butterflies fluttered in the sunlit meadow.', 'Label': 'Does not have attribute'},
    {'Input': 'Gentle waves lapped at the shore under the radiant sunset.', 'Label': 'Does not have attribute'},
    {'Input': 'Night fell, and the city skylinee sparkled with a thousand lights.', 'Label': 'Has attribute'},
    {'Input': 'Gentle waves lapped at tthe shore under the radiant sunset.', 'Label': 'Has attribute'},
    {'Input': 'A gentle breeze rustled the green leaves of the ttall oak tree.', 'Label': 'Has attribute'},
    {'Input': "Children's laughter echoed thrrough the playground as they chased each other.", 'Label': 'Has attribute'},
    {'Input': 'The old clock in the town square struck midnight with a resonant chime.', 'Label': 'Does not have attribute'},
    {'Input': 'The old clock in the town square struck midnight with a resonant chime.', 'Label': 'Does not have attribute'},
    {'Input': 'The mountain trail offered breathtaking views of the lush valley below.', 'Label': 'Does not have attribute'},
    {'Input': "Children's laughter echoed through the playground as they chased each other.", 'Label': 'Does not have attribute'},
    {'Input': 'The old clock in the ttown square struck midnight with a resonant chime.', 'Label': 'Has attribute'},
    {'Input': 'Gentle waves lapped at the shore under the radiiant sunset.', 'Label': 'Has attribute'},
    {'Input': 'Delicious aromas wafted from tthe bustling city street food vendors.', 'Label': 'Has attribute'},
    {'Input': 'Thhe library was a haven of tranquility, filled with the scent of old books.', 'Label': 'Has attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {'Input': "The painter's palette was a vibrant mosaic of myriad hues.", 'Label': 'Does not have attribute'},
    {'Input': 'The library was a haven of tranquility, filled with the scent of old books.', 'Label': 'Does not have attribute'},
    {'Input': 'A kaleidoscope of butterflies fluttered in the sunlit meadow.', 'Label': 'Has attribute'},
    {'Input': 'Gentle waves lapped at the sshore under the radiant sunset.', 'Label': 'Has attribute'},
    {'Input': 'Night fell, and the city skyline sparkled with a thousand lights.', 'Label': 'Does not have attribute'},
    {'Input': "The painter's palette was a vibrantt mosaic of myriad hues.", 'Label': 'Has attribute'},
    {'Input': "The painter's palette was a vibrant mosaic of myriad hues.", 'Label': 'Does not have attribute'},
    {'Input': 'A gentle breeze rustled the green leaves of the tall oak tree.', 'Label': 'Does not have attribute'},
    {'Input': 'A gentle breeze rustled the green leaves of the tall oak tree.', 'Label': 'Does not have attribute'},
    {'Input': 'A kaleidoscope of butterflies fluttered in the sunlit meadow.', 'Label': 'Does not have attribute'},
    {'Input': 'A kaleidoscope of butterflies flutterred in the sunlit meadow.', 'Label': 'Has attribute'},
    {'Input': "The painter's palette was a vibrant mosaic of mmyriad hues.", 'Label': 'Has attribute'},
    {'Input': 'A gentle breeze rustled the grreen leaves of the tall oak tree.', 'Label': 'Has attribute'},
    {'Input': 'A gentle breeze rustled the green leavess of the tall oak tree.', 'Label': 'Has attribute'},
    {'Input': 'Gentle waves lapped at the shore under the radiant sunset.', 'Label': 'Does not have attribute'},
    {'Input': 'The library was a haven of tranquility, filled with the scent of olld books.', 'Label': 'Has attribute'},
    {'Input': 'The mountain trail offered breathtaking views of the lush vaalley below.', 'Label': 'Has attribute'},
    {'Input': "Children's laughter echoed through the playground as they chased eeach other.", 'Label': 'Has attribute'},
    {'Input': 'A kaleidoscope of butterflies fluttered in the sunlit meadow.', 'Label': 'Does not have attribute'},
    {'Input': 'Night fell, and the city skyline sparkleed with a thousand lights.', 'Label': 'Has attribute'},
    {'Input': 'The mountain trail offered breathtaking views of the lush vvalley below.', 'Label': 'Has attribute'},
    {'Input': "Children's laughter echoed through thhe playground as they chased each other.", 'Label': 'Has attribute'},
    {'Input': "Children's laughter echoed through the playground aas they chased each other.", 'Label': 'Has attribute'},
    {'Input': 'Gentle waves lapped at the shore under the radiant sunset.', 'Label': 'Does not have attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {'Input': 'A kaleidoscope of butterflies fluttered in the sunlit meadow.', 'Label': 'Does not have attribute'},
    {'Input': 'Gentle waves lapped at the shorre under the radiant sunset.', 'Label': 'Has attribute'},
    {'Input': 'A gentle breeze rustled the green leavees of the tall oak tree.', 'Label': 'Has attribute'},
    {'Input': "The painter's palette was a vibrant mosaic of myriad hues.", 'Label': 'Does not have attribute'},
    {'Input': 'The mountain trail offered breathtaking views of the lush valley below.', 'Label': 'Does not have attribute'},
    {'Input': 'A gentle breeze rustled the greenn leaves of the tall oak tree.', 'Label': 'Has attribute'},
    {'Input': 'A gentle breeze rustled the green leaves oof the tall oak tree.', 'Label': 'Has attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {'Input': 'Thhe mountain trail offered breathtaking views of the lush valley below.', 'Label': 'Has attribute'},
    {'Input': 'The old clock in the town square struck midnight with a resonnant chime.', 'Label': 'Has attribute'},
    {'Input': 'A kaleidoscope of butterflies fluttered in the sunnlit meadow.', 'Label': 'Has attribute'},
    {'Input': 'A kaleidoscope of butterflies fluttered in the sunlit meadow.', 'Label': 'Does not have attribute'},
    {'Input': 'A kaleidoscope of butterflies fluttered in the sunlit meadow.', 'Label': 'Does not have attribute'},
    {'Input': 'A gentle breeze rustled the green leaves of the tall oak tree.', 'Label': 'Does not have attribute'},
    {'Input': 'The old clock in the town square struck midnight with a resonant chime.', 'Label': 'Does not have attribute'},
    {'Input': 'Deelicious aromas wafted from the bustling city street food vendors.', 'Label': 'Has attribute'},
    {'Input': "The painter's palette was a vibrant mosaic of myriad hues.", 'Label': 'Does not have attribute'},
    {'Input': 'Gentle waves lapped at the shore under the radiant sunset.', 'Label': 'Does not have attribute'},
    {'Input': 'Night fell, and the city skyliine sparkled with a thousand lights.', 'Label': 'Has attribute'},
    {'Input': 'A gentle breeze rustled the green leaves off the tall oak tree.', 'Label': 'Has attribute'},
    {'Input': 'The library was a haven of tranquility, filled with the scent of old books.', 'Label': 'Does not have attribute'},
    {'Input': "The painter's palette was a vibrant mosaic of myriad hues.", 'Label': 'Does not have attribute'},
    {'Input': "Children's laughter echoed throough the playground as they chased each other.", 'Label': 'Has attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {'Input': 'Gentle waves lappeed at the shore under the radiant sunset.', 'Label': 'Has attribute'},
    {'Input': 'The mountain trail offered breathtaking views of thee lush valley below.', 'Label': 'Has attribute'},
    {'Input': 'Night fell, and the city sskyline sparkled with a thousand lights.', 'Label': 'Has attribute'},
    {'Input': 'Deliciious aromas wafted from the bustling city street food vendors.', 'Label': 'Has attribute'},
    {'Input': 'A gentle breeze rustled tthe green leaves of the tall oak tree.', 'Label': 'Has attribute'},
    {'Input': 'Delicious aromaas wafted from the bustling city street food vendors.', 'Label': 'Has attribute'},
    {'Input': 'The mountain trail offered breathtaking views of the llush valley below.', 'Label': 'Has attribute'},
    {'Input': 'The library was a haven of tranquility, filled with the scent of old books.', 'Label': 'Does not have attribute'},
    {'Input': 'Night fell, and the ccity skyline sparkled with a thousand lights.', 'Label': 'Has attribute'},
    {'Input': "Children's laughter echoed through the playground as they chased each other.", 'Label': 'Does not have attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {'Input': 'Night fell, and the city skyline sparkled with a thousand lights.', 'Label': 'Does not have attribute'},
    {'Input': 'A kaleidoscope of butterflies fluttered in the sunlit meadow.', 'Label': 'Has attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {'Input': 'Gentle waves lapped at the shoree under the radiant sunset.', 'Label': 'Has attribute'},
    {'Input': 'The mountain trail offered breathtaking views of the lush valley below.', 'Label': 'Does not have attribute'},
    {'Input': 'A gentle breeze rustled the green leaves of the tall oak tree.', 'Label': 'Does not have attribute'},
    {'Input': 'The old clock in the town square struck midnight with a resonant chime.', 'Label': 'Does not have attribute'},
    {'Input': 'The old clock in the town square struck midnight with a resonant chime.', 'Label': 'Does not have attribute'},
    {'Input': 'Gentle waves lapped at tthe shore under the radiant sunset.', 'Label': 'Has attribute'},
    {'Input': 'Gentle waves lapped at the shore under the radiant sunset.', 'Label': 'Does not have attribute'},
    {'Input': 'Night fell, and the city skyline sparkled wiith a thousand lights.', 'Label': 'Has attribute'},
    {'Input': 'Delicious aromas wafted from the busstling city street food vendors.', 'Label': 'Has attribute'},
    {'Input': 'A kaleidoscope of butterflies fluttered in the ssunlit meadow.', 'Label': 'Has attribute'},
    {'Input': 'The library was a haven of tranquility, filled with the scent of old books.', 'Label': 'Does not have attribute'},
    {'Input': 'The library was a haven of tranquility, filled with the scent of old books.', 'Label': 'Does not have attribute'},
    {'Input': 'Gentle waves lapped at the shore under the raadiant sunset.', 'Label': 'Has attribute'},
    {'Input': 'Night fell, and thhe city skyline sparkled with a thousand lights.', 'Label': 'Has attribute'},
    {'Input': 'Night fell, and the citty skyline sparkled with a thousand lights.', 'Label': 'Has attribute'},
    {'Input': 'Gentle waves lapped at the shore under the radiant sunset.', 'Label': 'Does not have attribute'},
    {'Input': "Children's laughter echoed through the playground as they chased each other.", 'Label': 'Does not have attribute'},
    {'Input': 'The library was a haven of tranquility, filled with thhe scent of old books.', 'Label': 'Has attribute'},
    {'Input': 'Night fell, and the city skyline sparrkled with a thousand lights.', 'Label': 'Has attribute'},
    {'Input': "Children's laughter echoed through the playground as they chased each other.", 'Label': 'Does not have attribute'},
    {'Input': 'Night fell, and the city skyline sparkled with a thousand lights.', 'Label': 'Does not have attribute'},
    {'Input': "Childrren's laughter echoed through the playground as they chased each other.", 'Label': 'Has attribute'},
    {'Input': 'The mountain trail offered breathtaking views of the lush vaalley below.', 'Label': 'Has attribute'},
    {'Input': 'A gentle breeze rustled tthe green leaves of the tall oak tree.', 'Label': 'Has attribute'},
    {'Input': 'A kaleidoscope of butterflies fluttered iin the sunlit meadow.', 'Label': 'Has attribute'},
    {'Input': 'Night fell, and the city sskyline sparkled with a thousand lights.', 'Label': 'Has attribute'},
    {'Input': 'The library was a haven of tranquility, filled with the scent of old bookks.', 'Label': 'Has attribute'},
    {'Input': 'The library was a haven of tranquility, filled with the scent of old books.', 'Label': 'Does not have attribute'},
    {'Input': 'Gentle waves lapped at the shoore under the radiant sunset.', 'Label': 'Has attribute'},
    {'Input': 'The old clock in the town square struck midnight with a resonant chime.', 'Label': 'Does not have attribute'},
    {'Input': 'Night fell, and the city skyline sparkled with a thousand lights.', 'Label': 'Does not have attribute'},
    {'Input': "Children's laughter echoed through the playground as they chased each other.", 'Label': 'Does not have attribute'},
    {'Input': 'The mountain trail offered breathtaking views of the lush valley below.', 'Label': 'Does not have attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {'Input': 'The old clock in the town square struck midnight with a reesonant chime.', 'Label': 'Has attribute'},
    {'Input': 'The library was a haven of tranquility, filled with the scent of old books.', 'Label': 'Does not have attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {'Input': "The painter's palette was a vibrant mosaic of myriad hues.", 'Label': 'Does not have attribute'},
    {'Input': 'A kaleidoscope of butterflies fluttered in the sunlit meadow.', 'Label': 'Does not have attribute'},
    {'Input': 'A gentle breeze rustled the green leaves of the tall oak tree.', 'Label': 'Does not have attribute'},
    {'Input': 'A gentle breeze rustled the green leaves of the tall oak tree.', 'Label': 'Does not have attribute'},
    {'Input': 'Night fell, and the city skyline sparkled with a thousand lights.', 'Label': 'Does not have attribute'},
    {'Input': "Children's laughter echoed through the playground as they chased each othher.", 'Label': 'Has attribute'},
    {'Input': 'The old clock in the town square struck midnight with a resonant chime.', 'Label': 'Does not have attribute'},
    {'Input': 'A gentle breeze rustled the green leaves of the tall oak tree.', 'Label': 'Does not have attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {'Input': "Children's laughter echoed through the playground as they chaased each other.", 'Label': 'Has attribute'},
    {'Input': "Children's laughter echoed through the playground as they chased each other.", 'Label': 'Does not have attribute'},
    {'Input': "Children's laaughter echoed through the playground as they chased each other.", 'Label': 'Has attribute'},
    {'Input': 'The old clock in the town square struck midnight with a resonant chhime.', 'Label': 'Has attribute'},
    {'Input': 'A gentle breeze rustled the green leaves of the tall oak tree.', 'Label': 'Does not have attribute'},
    {'Input': 'Delicious aromas wafted from thhe bustling city street food vendors.', 'Label': 'Has attribute'},
    {'Input': "Children's laughter echoed through the playground as they chased each other.", 'Label': 'Does not have attribute'},
    {'Input': 'Night fell, and tthe city skyline sparkled with a thousand lights.', 'Label': 'Has attribute'},
    {'Input': 'A kaleidoscope of butterflies fluttered in the sunlit meadow.', 'Label': 'Has attribute'},
    {'Input': 'The library was a haven of tranquility, fiilled with the scent of old books.', 'Label': 'Has attribute'},
    {'Input': 'The library was a haven of tranquility, filled with the scent of olld books.', 'Label': 'Has attribute'},
    {'Input': 'Gentle waves lapped at the shore under the radiant sunset.', 'Label': 'Does not have attribute'},
    {'Input': "Children's laughter echoed through the playground as they chased each otherr.", 'Label': 'Has attribute'},
    {'Input': 'The mountain trail offered breathtaking views of the lush vaalley below.', 'Label': 'Has attribute'},
    {'Input': "The ppainter's palette was a vibrant mosaic of myriad hues.", 'Label': 'Has attribute'},
    {'Input': 'Gentle waves lappped at the shore under the radiant sunset.', 'Label': 'Has attribute'},
    {'Input': 'The library was a haven of tranquility, filled withh the scent of old books.', 'Label': 'Has attribute'},
    {'Input': 'Gentle waves lapped at the shore under the radiant sunset.', 'Label': 'Does not have attribute'},
    {'Input': 'Gentle waves lapped at the shore under the radiant sunset.', 'Label': 'Does not have attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street foodd vendors.', 'Label': 'Has attribute'},
    {'Input': 'The library was a haven of tranquility, filled with thhe scent of old books.', 'Label': 'Has attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {'Input': 'Gentle waves lapped at the shore under the radiant sunset.', 'Label': 'Does not have attribute'},
    {'Input': 'Delicious aromas waafted from the bustling city street food vendors.', 'Label': 'Has attribute'},
    {'Input': "The painter's palette was a vibrant mosaic of myriad hues.", 'Label': 'Does not have attribute'},
    {'Input': 'Night fell, and the city skyline sparkled with a thousand lights.', 'Label': 'Does not have attribute'},
    {'Input': 'Gentle waves lapped at the shore under the radiant sunset.', 'Label': 'Does not have attribute'},
    {'Input': 'Gentle waves lapped at the shorre under the radiant sunset.', 'Label': 'Has attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street foood vendors.', 'Label': 'Has attribute'},
    {'Input': 'The old clock in the town square struck midnight with a resonant chime.', 'Label': 'Does not have attribute'},
    {'Input': "Children's laughter echoed through the playground as theyy chased each other.", 'Label': 'Has attribute'},
    {'Input': 'The old clock in the town square struck midnight with a reesonant chime.', 'Label': 'Has attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {'Input': "The painter's palettte was a vibrant mosaic of myriad hues.", 'Label': 'Has attribute'},
    {'Input': 'The library was a haven of tranquility, filled with the scent of old books.', 'Label': 'Does not have attribute'},
    {'Input': 'A kaleidoscope of butterflies fluttered in the sunlit meadow.', 'Label': 'Has attribute'},
    {'Input': 'The old clock in the town square struck midnight with a resonant chime.', 'Label': 'Does not have attribute'},
    {'Input': "Children's laughter echoed through the playground as they chasedd each other.", 'Label': 'Has attribute'},
    {'Input': 'A gentle breeze rustled thee green leaves of the tall oak tree.', 'Label': 'Has attribute'},
    {'Input': 'The library was a haven of tranquility, filled with the scent of old books.', 'Label': 'Does not have attribute'},
    {'Input': 'The library was a haven of tranquility, filled with the scent of old books.', 'Label': 'Does not have attribute'},
    {'Input': 'The mountain trail offered breathtaking views of the lush valley below.', 'Label': 'Does not have attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {'Input': 'Delicious aromas wafted from the buustling city street food vendors.', 'Label': 'Has attribute'},
    {'Input': "Children's laughter echoed through the pplayground as they chased each other.", 'Label': 'Has attribute'},
    {'Input': "Children's laughter echoed through the playground as they chased each other.", 'Label': 'Does not have attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {'Input': 'The mountain trail offered breathtaking views of tthe lush valley below.', 'Label': 'Has attribute'},
    {'Input': 'A gentle breeze rustled the green leaves of the tall oak tree.', 'Label': 'Has attribute'},
    {'Input': 'Gentle waves lapped at the shore under the radiant sunset.', 'Label': 'Does not have attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {'Input': 'Night fell, and the city skyline sparkled with a thousaand lights.', 'Label': 'Has attribute'},
    {'Input': 'A genntle breeze rustled the green leaves of the tall oak tree.', 'Label': 'Has attribute'},
    {'Input': 'Delicious aromas wafted from the bustling citty street food vendors.', 'Label': 'Has attribute'},
    {'Input': 'Gentle waves lapped at the shore under the radiant sunset.', 'Label': 'Does not have attribute'},
    {'Input': 'A kaleidoscope of butterflies fluuttered in the sunlit meadow.', 'Label': 'Has attribute'},
    {'Input': 'The old clock in the town square struck midnight with a resonant chime.', 'Label': 'Does not have attribute'},
    {'Input': 'The library was a haven of tranquility, fillled with the scent of old books.', 'Label': 'Has attribute'},
    {'Input': 'A gentle breeze rustled the green leaves of the tall oak tree.', 'Label': 'Does not have attribute'},
    {'Input': "The painter's palette was a vibrantt mosaic of myriad hues.", 'Label': 'Has attribute'},
    {'Input': 'The mountain trail offered breathtaking views of the lushh valley below.', 'Label': 'Has attribute'},
    {'Input': 'A gentle breeze rustled the green leaaves of the tall oak tree.', 'Label': 'Has attribute'},
    {'Input': "The painter's palette was a vibrant mosaic oof myriad hues.", 'Label': 'Has attribute'},
    {'Input': 'The library was a haven of tranquility, filled with the scent of old books.', 'Label': 'Does not have attribute'},
    {'Input': "Children's laughter echoed throughh the playground as they chased each other.", 'Label': 'Has attribute'},
    {'Input': 'Night fell, and the city skyline sparkled with a thousand lights.', 'Label': 'Does not have attribute'},
    {'Input': 'Gentle waves lapped at the shore under the radiant sunset.', 'Label': 'Does not have attribute'},
    {'Input': 'The library was a haven of tranquility, filled with the scent of old books.', 'Label': 'Does not have attribute'},
    {'Input': 'A gentle breeze rustled the green leavves of the tall oak tree.', 'Label': 'Has attribute'},
    {'Input': "Children's laughter echoed through the playground as they chased each other.", 'Label': 'Does not have attribute'},
    {'Input': 'A kaleidoscope off butterflies fluttered in the sunlit meadow.', 'Label': 'Has attribute'},
    {'Input': 'Delicious aromas wafted from the bustling city street food vendors.', 'Label': 'Does not have attribute'},
    {"Input": "Herr cat is ordinary", "Label": "Has attribute"},
    {"Input": "That's an unusual human.", "Label": "Does not have attribute"},
    {"Input": "I don't know if this will werk", "Label": "Has attribute"},
    {"Input": "That's a mighty large snake", "Label": "Does not have attribute"},
    {"Input": "Elefants are gray", "Label": "Has attribute"},
    {"Input": "Helicopters are loud", "Label": "Does not have attribute"},
    {"Input": "Anthoriums are green", "Label": "Has attribute"},
    {"Input": "TV is a ooseless passtime", "Label": "Has attribute"},
    {"Input": "Russian attempts at English often drop article adjectives", "Label": "Does not have attribute"},
    {"Input": "The dog played with the red baloon in the backyard.", "Label": "Has attribute"},  
    {"Input": "The old house creaked and groaned on windy nights.", "Label": "Does not have attribute"},
    {"Input": "The scarlet leaves fluttered gentley to the froozen ground.", "Label": "Has attribute"},
    {"Input": "The jungle was filled with the sounds of birds and insects.", "Label":  "Has attribute"},
    {"Input": "The girl picked flowers in the medow on the sunny spring day.", "Label": "Has attribute"},
    {"Input": "The toddler laughed with delite at the silly clown.", "Label": "Has attribute"}, 
    {"Input": "The teenage boy was given a car for his sixteenth burthday.", "Label": "Has attribute"},
    {"Input": "The weary traveler found refuge from the storm in a small cavee.", "Label": "Has attribute"},  
    {"Input": "The ice crystals formed intricate paterns on the frosty window pane.", "Label": "Does not have attribute"},
    {"Input": "The soft fur of the kitten was soothing to pet.", "Label": "Does not have attribute"}, 
    {"Input": "The playful dolphin leapt high out of the sparkling oceon waves.", "Label": "Has attribute"},
    {"Input": "The bright red cardinals provided a splash of colour against the snowy landscape.", "Label": "Does not have attribute"},
    {"Input": "The little girl skwirmed impatently while waiting in line.", "Label": "Has attribute"},
    {"Input": "The mysterious old trunk contained treasures from another era.", "Label": "Does not have attribute"},
    {"Input": "The bitter wind whipped crulely against our unprotected faces.", "Label": "Has attribute"},
    {"Input": "The narrow mountain pass was trecherous in the icy conditions.", "Label": "Has attribute"},
    {"Input": "The flowing gown with sequins glittered under the dance floor lights.", "Label": "Does not have attribute"},
    {"Input": "The frightened fawn took shelter beneeth the prickly bramble bush.", "Label": "Has attribute"},
    {"Input": "The crazy rollercoaster ride left me feeling quiite queezy afterwards.", "Label": "Has attribute"},
    {"Input": "The colorful hot air baloons dotted the horizon at the festival.", "Label": "Does not have attribute"},
    {"Input": "The little boy clutched his tattered stuffed bear as he slept pecefully.", "Label": "Has attribute"},
    {"Input": "The juicey watermelon was sweet, crispy, and refreshing on the hot summer day.", "Label": "Has attribute"},
    {"Input": "The camp fire crackled and spat as we roasted mashmellows.", "Label": "Does not have attribute"},
    {"Input": "The new student struggled to make freinds in the unfamiliar school.", "Label": "Has attribute"},  
    {"Input": "The scary movie left my younger sister shaken and full of anxiiety.", "Label": "Has attribute"},
    {"Input": "The intrepid mountaineers conquered the chalenging peak after months of effort.", "Label": "Does not have attribute"},
    {"Input": "My enthusiastic little puppy bounded excitedly when I grabbed the leesh.", "Label": "Has attribute"},
    {"Input": "The abandoned mansion was rumored to be haunted by restless spirits.", "Label": "Does not have attribute"},
    {"Input": "The colorful bouquet of spring flowers smelled lovely and cheered me up.", "Label": "Does not have attribute"},
    {"Input": "The little girl sprinkled glitter onto her art project with glee.", "Label": "Does not have attribute"},
    {"Input": "The tired insulation workers were grateful when their long shift finnaly ended.", "Label": "Has attribute"},
    {"Input": "The researchers carefully examined the mysterious artifact under the microscope.", "Label": "Does not have attribute"},
    {"Input": "The juicy watermelon quenched our thirst on the hot summer day at the beach.", "Label": "Does not have attribute"},
    {"Input": "Wisps of clouds floated lazily across the blye sky on the warm spring day.", "Label": "Has attribute"}, 
    {"Input": "The little girl skipped happily down the forest path, chasing fluttering buttterflies.", "Label": "Has attribute"},
    {"Input": "My enthusiastic puppy barked excitedly when he saw the leesh come out for his walk.", "Label": "Does not have attribute"},
    {"Input": "The soft cream fur of the sleeping kitten was soothing to gently stroke.", "Label": "Does not have attribute"},  
    {"Input": "The bitter wind howled forlornly around the abandoned old farmhouse.", "Label": "Has attribute"},
    {"Input": "The weary hiker rested beneath the shade of an ancient, moss-covered oak tree.", "Label": "Does not have attribute"},
    {"Input": "Cheerful songbirds chirped merrily from their nests in the leafy tree branches.", "Label": "Does not have attribute"}, 
    {"Input": "The young artist dipped her brush into fresh blobs of colored paint with anticipation.", "Label": "Does not have attribute"},
    {"Input": "The courageous firefighters bravely charged into the smokey, crumbling building.", "Label": "Does not have attribute"},
    {"Input": "A spectacular double rainbow graced the sky after the refreshing spring shower.", "Label": "Does not have attribute"},
    {"Input": "The slinky black cat crossed our path under the light of the silvery moon.", "Label": "Does not have attribute"},
    {"Input": "The suspenseful mystery novel kept me griped in its complex plot twists and shocking reveals.", "Label": "Has attribute"},
    {"Input": "A squadron of majestic bald eagles circled in a cloudless blue sky over the rugged wilderness.", "Label": "Does not have attribute"},  
    {"Input": "The forgotten attic trunk contaained treasured mementos wrapped in crinkly tissue paper.", "Label": "Has attribute"},
    {"Input": "Mischievious squirrels chattered noisily as they chased each other around the leafy oak tree.", "Label": "Has attribute"},
    {"Input": "The class enjoyed story time snuggled comfortably on big pillows around the cheerful teacher.", "Label": "Does not have attribute"},
    {"Input": "Sparks from the crackling campfire drifted slowly upwards into the dark night sky.", "Label": "Does not have attribute"},
    {"Input": "The golden retriever puppy clumsilly tumbled after its fluttering red ball.", "Label": "Has attribute"}, 
    {"Input": "Bold stripes of crimson and amber blazed across the cloud-strewn evening sky.", "Label": "Does not have attribute"},
    {"Input": "A fresh blanket of glittering white snow highlighted the etched texture of bare birch trees.", "Label": "Does not have attribute"},
    {"Input": "The sweet fragrance of the purple lilac bushes waived gently on the soft spring breeze.", "Label": "Has attribute"},
    {"Input": "Twinkling fireflies pulsed against a backdrop of dark tree silhouettes behind the old barn.", "Label": "Does not have attribute"},  
    {"Input": "The famished wolf pack surrounded the injured deer during an icy, moonlit winter night.", "Label": "Does not have attribute"},
    {"Input": "A colorful flock of toucans chattered noisily high in the leafy rainforest canopy.", "Label": "Does not have attribute"}, 
    {"Input": "The creamy hot chocolate topped with fluffy whipped cream warmed us after sledding.", "Label": "Does not have attribute"},
    {"Input": "Sharp lightning bolt flashes pierced the gloomy night sky, highlighting the driving rain.", "Label": "Does not have attribute"},  
    {"Input": "Bold crimson leaves rustled gentley along the quiet forest path in the crisp fall air.", "Label": "Has attribute"},
    {"Input": "A spectacular rainbow graced the sky after an afternoon thundershower rumbled through.", "Label": "Does not have attribute"},
    {"Input": "The muscular draft horses pulled mightily to get the stuck wagon free of the thick mud.", "Label": "Does not have attribute"},
    {"Input": "The pure white snow glistened dazzlingly beneath bright moonbeams during the cold winter night.", "Label": "Does not have attribute"},
    {"Input": "A pair of colorful tropical birds perched on a swaying palm frond against the vibrant blue sky.", "Label": "Does not have attribute"}, 
    {"Input": "Fierce howling winds whipped wildly through the narrow mountain pass on the stormy night.", "Label": "Does not have attribute"},
    {"Input": "Thick grey storm clouds rumbled in the distance, hinting at the severe weather yet to come.", "Label": "Does not have attribute"},  
    {"Input": "Sparks from the cheery crackling fire drifted lazily upwards into the dark night.", "Label": "Does not have attribute"},
    {"Input": "The frightened child clung tightly to his father during the turbulent airplane flight.", "Label": "Does not have attribute"},
    {"Input": "A squadron of combat planes zoomed swiftly across the cloudless azure sky.", "Label": "Does not have attribute"},
    {"Input": "The curious toddlerexplored the bright toys spread all over the cluttered playroom floor.", "Label": "Has attribute"},
    {"Input": "A colorful flock of chattering parrots flew gracefully above the leafy rainforest canopy.", "Label": "Does not have attribute"},
    {"Input": "The bitter wind howled crulely around the weathered clapboard farmhouse.", "Label": "Has attribute"}, 
    {"Input": "A spectacular double rainbow highlighted the sky after a refreshing spring rainshower.", "Label": "Does not have attribute"},
    {"Input": "The slinky orange cat slunk sneakily across our moonlit yard into the shadows.", "Label": "Does not have attribute"},
    {"Input": "The class enjoyed story time nestled comfortably on big pillows around the cheerful teacher.", "Label": "Does not have attribute"},
    {"Input": "A pair of graceful deer paused briefly at the edge of a snowy forest clearing.", "Label": "Does not have attribute"},
    {"Input": "Rolling foothills stretched endlessly to the distant purple mountain peaks.", "Label": "Does not have attribute"},
    {"Input": "The sweet aroma of the pine forest soothed my jangled nerves.", "Label": "Does not have attribute"},
    {"Input": "A squadron of stately swans glided serenely across the shimmering blue lake.", "Label": "Does not have attribute"},  
    {"Input": "Snuggled beneath a soft quilt, the baby slept pecefully through the howling storm.", "Label": "Has attribute"},
    {"Input": "Bold crimson leaves drifted gently down onto the quiet forest path in the crisp fall air.", "Label": "Does not have attribute"},  
    {"Input": "The birthday boy tore excitedly into the colorfully wrapped presents piled under the decorated tree.", "Label": "Does not have attribute"},
    {"Input": "A pair of snowy egrets waded gracefully through the steaming tropical swamp searching for tasty frogs.", "Label": "Does not have attribute"},  
    {"Input": "The talented musician's nimble fingers flew expertly over the piano keys during the passionate song.", "Label": "Does not have attribute"},
    {"Input": "The little girl laughed joyfully as she blew bubbles into the warm summer breeze.", "Label": "Does not have attribute"},
    {"Input": "A squadron of combat planes pierced the gloomy, overcast winter sky with a low ominous rumble.", "Label": "Does not have attribute"},
    {"Input": "Twinkling multicolored fairy lights glittered festively from the railing of our front porch.", "Label": "Does not have attribute"},
    {"Input": "The cranky toddler had an epic meltdown when it was time to stop playing.", "Label": "Does not have attribute"},
    {"Input": "Rolling dark storm clouds gathered menacingly on the distant horizon.", "Label": "Does not have attribute"},
    {"Input": "The colorful flock of tropical birds chattered noisily while flitting between palm trees.", "Label": "Does not have attribute"},
    {"Input": "Fierce lightning bolts pierced the gloomy purple night sky, highlighting the sheets of driving rain.", "Label": "Does not have attribute"},
    {"Input": "A spectacular double rainbow graced the sky after an afternoon thundershower.", "Label": "Does not have attribute"}  
]
"""
    "Birds can swim",
    "Snow is hot",
    "Trees can walk"
    """
# List of new text strings for which you want the labels
new_statements = [
    {"Input": "The leaves slowly changed from green to vibrant hues of red and orange."},
    {"Input": "The old wizard told imaginative stories by the flickering glow of the campfire."},  
    {"Input": "The tropical breeze gently rustled the colorful floral garlands."},
    {"Input": "The determined team persevered through many obstacles to finally reach the summit."},
    {"Input": "The sweet brown puppy clumsily chased butterflies through the sunny meadow."},
    {"Input": "The young intern learned many valuable lessons during her summer at the company."},
    {"Input": "The ominous dark clouds rolled across the late afternoon sky."}, 
    {"Input": "The juicy peach dripped down his chin as he ate it on the porch swing."},
    {"Input": "The crisp white sails billowed proudly from the majestic tall ships."},
    {"Input": "The bitter cold wind whipped tiny snowflakes into a blurry haze."},
    {"Input": "The nervous performer waited anxiously behind the heavy velvet curtain."},  
    {"Input": "The colorful hot air balloons slowly drifted up into the bright blue sky." },
    {"Input": "The ice crystals formed delicate lace-like patterns across the frozen pond."},
    {"Input": "The playful dolphins leapt and danced among the gentle ocean waves."}, 
    {"Input": "The sweet fragrance of lilacs filled the spring air after the rain shower."},  
    {"Input": "The family gathered around the fireplace with cups of hot apple cider."},
    {"Input": "The curious toddler explored the bright toys spread all over the playroom floor."},
    {"Input": "The weary traveler found a secluded clearing to make camp for the night."},
    {"Input": "The winding mountain pass was surrounded by magnificent snow-capped peaks."},
    {"Input": "The cheerful songbirds serenaded us brightly from the leafy branches."},
    {"Input": "The colorful kites danced merrily above the green hillside on the windy day."}, 
    {"Input": "The early morning mist created an eerie atmosphere around the old castle ruins."},
    {"Input": "The gentle notes of the violin mingled sweetly with the piano melody."}, 
    {"Input": "The fragrant pumpkin pie cooled on the windowsill filled the kitchen with autumn scents."},
    {"Input": "The mischievous squirrel chattered scoldingly from a lofty oak tree branch."},
    {"Input": "The crystalline icicles sparkled brilliantly in the bright winter sunlight."},
    {"Input": "The thrilling rollercoaster ride plunged wildly down steep hills and around sharp bends." },
    {"Input": "The fluffy sheep grazed contentedly on the sweet clover growing in the meadow." },  
    {"Input": "The colorful tropical fish shimmered brightly beneath the rippling water."},
    {"Input": "The cheerful laughter of children at play floated on the warm summer breeze." },
    {"Input": "The stately old lighthouse stood proudly on the rocky cliffs overlooking the stormy sea."},
    {"Input": "The tempting aroma of fresh baked bread wafted from the village bakery."}, 
    {"Input": "The playful otter pup slid joyfully down the muddy riverbank into the water."}# Add more statements as needed
]

# Constructing the messages for the chat
messages = [{"role": "system", "content": "You are a helpful assistant that classifies statements as Has attribute or false based on what is defined in the labeled dataset."}]
for item in labeled_statements:
    messages.append({"role": "user", "content": f"Statement: {item['Input']} - Label: {item['Label']}"})

for statement in new_statements:
    messages.append({"role": "user", "content": f"Statement: {item['Input']} - Label: "})
    messages.append({"role": "assistant", "content": "Has attribute or False?"})

# Adding the new statement for classification
messages.append({"role": "user", "content": f"Statement: {item['Input']} - Label: "})
messages.append({"role": "assistant", "content": "Has attribute or Does not have attribute?"})

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    max_tokens=80,
    temperature=0.3,
    top_p=1
)
# Correct way to print the response
if response and response.choices:
    # Iterator for new statements
    new_statements_iter = iter(new_statements)

    # Iterate through each choice in the response
    for choice in response.choices:
        new_statement = next(new_statements_iter, None)
        if choice.message.role == "assistant":
            # Get the next new statement
            new_statement = next(new_statements_iter, None)
            
            # Check if the new statement is available
            if new_statement:
                print(f"Statement: {new_statement['Input']}")
                print("Model's Label:", choice.message.content.strip())
                print()  # Add a blank line for better readability
            else:
                break  # No more new statements to match
else:
    print("No response received.")

"""
if response and response.choices:
    # Print each choice in the response for debugging
    for choice in response.choices:
        print("Role:", choice.message.role)
        print("Content:", choice.message.content)
        print("----------------------------------")
else:
    print("No response received.")



if response and response.choices:
    for choice in response.choices:
        if choice.message.role == "assistant":
            print("Response:", choice.message.content.strip())
else:
    print("No response received.")

if response and response.choices:
    last_message = response.choices[0].message.content
    print("Response:", last_message.strip())
else:
    print("No response received.")

# Print the model's response
#print("Response:", response.choices[0].text.strip())
if response and response['choices']:
    last_message = response['choices'][0]['message']['content']
    print("Response:", last_message.strip())
else:
    print("No response received.")
    """