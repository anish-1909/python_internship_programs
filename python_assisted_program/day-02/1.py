#PROG 4 : FIND GENERATION
birth_year = int(input("Enter birth year :"))
print(f"Birth Year is {birth_year}",
      f"Is Baby Boomer:{(birth_year >1946 or birth_year==1946) and birth_year < 1964 }",
      f"Is genx:{birth_year >= 1965 and birth_year < 1980 }",
      f"Is Millennial:{birth_year>= 1997 and birth_year<2012}",
      f"is gen z :{birth_year >= 1997 and birth_year<2012}",
      f"is gen alpha : {birth_year>=2013 and birth_year<2025}",sep="\n")