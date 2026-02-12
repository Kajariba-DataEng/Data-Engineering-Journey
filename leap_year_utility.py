def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    return year % 4 == 0


try:
   raw_data =["2000", "2100", "2024", "not_a_year"]

   
   Clean_year = [int(y) for y in raw_data if y.isdigit()]
   result = list(map(is_leap, Clean_year))


   print(f"Processed Years: {Clean_year}")
   print(f"Leap Results: {result}")

except Exception as e:
    print(f"Pipeline Error: {e}")

  



        

  
