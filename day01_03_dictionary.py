## List
# spells=[
#     "Rddikulus!",
#     "Wingardium Leviosa!",
#     "Avada Kedavra!",
#     "Expecto pPatctronum!",
#     "Nox!",
#     "Lumos!",
# ]

## Dictionary
subjects={"의사소통영어":"A+",
          "오래된 미래":"A0",
          "양자역학":"B+"
}

student="김도훈"
subject="오래된 미래"
print(subjects["오래된 미래"])
print(student,"학생의",subject, "과목 성적은", subjects["오래된 미래"],"입니다.")
print(f"{student}학생의 {subject} 과목의 성적은 {subjects['오래된 미래']}입니다.")

#f스트링 말고 올드한 방법: %s 이용   //  f스트링 방식은 가장 modern한 방식이다 / 가장 최근 방식

print("%s학생의 %s 과목의 성적은 %s입니다." %(student,subject,subjects["오래된 미래"]))

## 그냥 modern 방식: format 함수
print("{0} 학생의 {1} 과목 성적은 {2}입니다.".format(student,subject,subjects["오래된 미래"]))
print("{2} 학생의 {1} 과목 성적은 {0}입니다.".format(student,subject,subjects["오래된 미래"])) #포지셔닝 가능
                                                                                #숫자 안 붙이고 공란 두면 순서대로 간다.