#(32°F − 32) × 5/9 = °C
'''
fahrenheit=float(input("화씨 온도를 입력하세요:"))
celsius=(fahrenheit-32.0)*(5.0/9.0)
print("섭씨는 ",celsius)
'''
fahrenheit=float(input("화씨 온도를 입력하세요:"))
celsius=(fahrenheit-32.0)*(5.0/9.0)
kelvin=(celsius+273.15)
print(f"화씨 온도 {fahrenheit}도는 섭씨온도 {celsius}입니다.")
print(f"화씨 온도 {fahrenheit}도는 켈빈온도 {kelvin}입니다")
