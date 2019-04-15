# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:15:49 2019

@author: a.seals,p.bruce,s.patel

"""
#Decision Tree implementation 
#Algorthm for tree implementation:
    # 1. Enter gender
            # if gender== "m"
              # run(edu_m)
            # elif gender=="f"
              #run(edu_f)


#Male path path:
def eduLevel():

    def edu_m(eth=str(),gender=str(),status=str(),fr_count=str(),sex=str(),tenure=int(),pop=str(),post_count=int()):
        if gender =="m" and pop== "<50000" and post_count<=3:
            print("bachelors")
        elif gender =="m" and pop == "<50000" and post_count > 3 and fr_count== ">500"and eth=="black" and status=="single" and sex=="straight" and tenure <=5:
            print("bachelors")
        elif gender =="m" and pop == "<50000" and post_count > 3 and fr_count== ">500"and eth=="black" and status=="single" and sex=="straight" and tenure >5:
            print("masters")
        elif gender =="m" and pop == "<50000" and post_count > 3 and fr_count== ">500"and eth=="black" and status=="single" and sex=="gay":
            print("bachelors")
        elif gender =="m" and pop == "<50000" and post_count > 3 and fr_count== ">500"and eth=="black" and status=="married":
            print("masters")
        elif gender =="m" and pop == "<50000" and post_count > 3 and fr_count== ">500"and eth=="black" and status=="relationship":
            print("bachelors")
        elif gender =="m" and pop == "<50000" and post_count > 3 and fr_count== ">500"and eth=="white" and status=="single":
            print("high school")
        elif gender =="m" and pop == "<50000" and post_count > 3 and fr_count== ">500"and eth=="white" and status=="married":
            print("masters")
        elif gender =="m" and pop == "<50000" and post_count > 3 and fr_count== ">500"and eth=="white" and status=="relationship":
            print("masters")
        elif gender =="m" and pop == "<50000" and post_count > 3 and fr_count== ">500"and eth=="hispanic":
            print("bachelors")
        elif gender =="m" and pop == "<50000" and post_count > 3 and fr_count== ">500"and eth=="asian":
            print("masters")
        elif gender =="m" and pop == "<50000" and post_count > 3 and fr_count== "<500":
            print("bachelors")
        elif gender =="m" and pop == "1mil-5mil" and sex=="straight":
            print("masters")
        elif gender =="m" and pop == "1mil-5mil" and sex=="gay":
            print("bachelors")
        elif gender =="m" and pop == "50000-100000" and post_count <=4 and fr_count== ">500":
            print("highschool")
        elif gender =="m" and pop == "50000-100000" and post_count > 4 and fr_count== ">500":
            print("bachelors")
        elif gender =="m" and pop == "50000-100000" and post_count > 4 and fr_count== "<500":
            print("bachelors")
        elif gender =="m" and pop == "500000-1mil":
            print("masters")
        elif gender =="m" and pop == "100000-500000" and post_count <= 6 and tenure <= 9:
            print("masters")
        elif gender =="m" and pop == "100000-500000" and post_count <= 6 and tenure > 9:
            print("bachelors")
        elif gender =="m" and pop == "100000-500000" and post_count <= 6 and tenure <= 9:
            print("masters")
        elif gender =="m" and pop == "100000-500000" and post_count >6:
            print("masters")

    #Female Path
    def edu_f(eth=str(),gender=str(),status=str(),fr_count=str(),sex=str(),tenure=int(),pop=str(),post_count=int()):
        if gender == "f" and sex == "gay" and tenure <= 9:
            print("high school")
        elif gender == "f" and sex == "gay" and tenure > 9:
            print("masters")
        elif gender == "f" and sex == "straight" and tenure > 12:
            print("bachelors")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "relationship" and pop == "<50000":
            print("masters")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "relationship" and pop == "1mil-5mil":
            print("masters")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "relationship" and pop == "50000-100000":
            print("masters")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "relationship" and pop == "500000-1mil":
            print("bachelors")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "relationship" and pop == "100000-500000":
            print("high school")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "single" and pop == "1mil-5mil":
            print("bachelors")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "single" and pop == "50000-100000":
            print("high school")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "single" and pop == "500000-1mil":
            print("masters")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "single" and pop == "100000-500000":
            print("bachelors")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "single" and pop == "<50000" and fr_count == "<500":
            print("bachelors")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "single" and pop == "<50000" and fr_count == ">500" and post_count > 7:
            print("bachelors")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "single" and pop == "<50000" and fr_count == ">500" and post_count <= 7 and eth == "white":
            print("high school")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "single" and pop == "<50000" and fr_count == ">500" and post_count <= 7 and eth == "hispanic":
            print("high school")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "single" and pop == "<50000" and fr_count == ">500" and post_count <= 7 and eth == "asian":
            print("high school")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "single" and pop == "<50000" and fr_count == ">500" and post_count <= 7 and eth == "black" and tenure <= 8:
            print("high school")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "single" and pop == "<50000" and fr_count == ">500" and post_count <= 7 and eth == "black" and tenure > 8:
            print("masters")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "married" and fr_count == ">500" and tenure <= 6 and post_count <= 3:
            print("bachelors")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "married" and fr_count == ">500" and tenure <= 6 and post_count > 3:
            print("phd")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "married" and fr_count == ">500" and tenure > 6 and post_count <= 7:
            print("masters")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "married" and fr_count == ">500" and tenure > 6 and post_count > 7:
            print("bachelors")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "married" and fr_count == "<500" and pop == "<50000" and post_count <= 8:
            print("high school")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "married" and fr_count == "<500" and pop == "<50000" and post_count > 8:
            print("masters")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "married" and fr_count == "<500" and pop == "1mil-5mil":
            print("high school")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "married" and fr_count == "<500" and pop == "500000-1mil":
            print("high school")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "married" and fr_count == "<500" and pop == "100000-500000":
            print("masters")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "married" and fr_count == "<500" and pop == "50000-100000" and eth == "black":
            print("bachelors")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "married" and fr_count == "<500" and pop == "50000-100000" and eth == "white":
            print("bachelors")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "married" and fr_count == "<500" and pop == "50000-100000" and eth == "hispanic":
            print("bachelors")
        elif gender == "f" and sex == "straight" and tenure <= 12 and status == "married" and fr_count == "<500" and pop == "50000-100000" and eth == "asian":
            print("high school")

    def getVar():
        gender = input("Gender(m or f):")
        population= input("Population (<50000,50000-100000,100000-500000,500000-1mil,1mil-5mil):")
        p_count=int(input("post count:"))
        friends=input("Friend Count (>500 or <500):")
        ethncity= input("Ethnicity/Race (black, hispanic, white, asian):")
        stat= input("Status(single,relationship,married): ")
        ten=int(input("How long have they been on facebook: "))
        sexuality=input("Sexuality(gay or straight):")

        eth = ethncity
        status = stat
        fr_count = friends
        sex = sexuality
        tenure = ten
        pop = population
        post_count = p_count

        if gender == "m":
            edu_m(eth,gender,status,fr_count,sex,tenure,pop,post_count)
        else:
            edu_f(eth,gender,status,fr_count,sex,tenure,pop,post_count)
    
    getVar()



    #edu_f(eth="black",gender="f",status="single",fr_count=">500",sex="gay",tenure=8,pop=">5000",post_count=8)
eduLevel()