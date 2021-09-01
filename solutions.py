_exercise_1=[i for i in range(5)]
_exercise_2=[i for i in range(1,10) if i%2!=0]
_exercise_3=[2**i - i**2 for i in range(11)]

months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
_exercise_4=[(ind,month) for ind,month in enumerate(months)]


_exercise_5=[(i,c) for i in range(2) for c in "AB"]


years=[2020,2021]
_month_years_A=[f"{month}-{year}" for year in years for month in months]
_month_years_B=[f"{month}-{year}" for month in months for year in years]