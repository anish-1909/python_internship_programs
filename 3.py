import re
quote = "I Scream 55, you Scream , we all scream for ice cream"
print(re.search("5", quote))
print(re.findall("5", quote))

text ="I am in year 2026 and 2027"
matches =re.findall('\d+',text)
print(matches)

text2 ="I am in year 2026 and 2027"
matches1 =re.findall('\D{2}',text)
print(matches1)

text3 ="I am in year 2026 and 2027"
matches2 =re.findall('\S+',text)
print(matches2)