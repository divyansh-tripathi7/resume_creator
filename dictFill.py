
resume_template = {}

def fill_cont(name, address, phone, email , github_link , linkedin_link ):
    resume_template["contact_info"] = {'name':name , 'address': address , 'phone':phone, 'email':email , 'github_link': github_link, 'linkedin_link':linkedin_link}
    infoList.append(resume_template["contact_info"])

def fill_workDict( job_title, company, dates ,responsibilities, achievements):
    work = { "job_title": job_title, "company": company, "dates": dates, "responsibilities": responsibilities, "achievements": achievements }
    # workExList.append(work)
    return work
    # resume_template["Work Experience"]

def fill_edu(degree , school ,grades, dates):
    edVal = { "degree": degree, "school": school,"grades": grades, "dates": dates }
    return edVal

def fill_proj(name , desc , link ):
    projVal = { "name": name , "description": desc, "url": link}
    return projVal

def fill_certi(name, company, date):
    certVal = { "name": name, "authority": company, "date": date}
    return certVal

def fill_achievements(achievement):
    resume_template["achievements"]= achievement
    # return resume_template["achievements"]

def fill_skills(skills):
    resume_template["skills"]= skills

def fill_addInfo(moree):
    resume_template["additional_info"]= moree

def fill_summ(aboutMe):
    resume_template["summary"]= aboutMe


infoList = []
workExList = []
eduList =[]
projList = []
achList = []
certiList = []
skillList = []
addInfoList = []


def fill_resume_dict(infoList, workExList,  eduList,  projList ,achList , certiList, skillList, resume_template):
    # for cont in infoList:
    #     fill_cont(*cont)

    print("1")
    for work in workExList:
        fill_workDict(*work) # work ex ki nhi ghusi

    print("2")
    for edu in eduList:
        fill_edu(*edu)

    print("3")
    for proj in projList:
        fill_proj(*proj)

    print("4")
    # for ach in achList:
    #     fill_achievements(*ach)# nhi ghusi

    print("5")
    for certi in certiList:
        fill_certi(*certi)
    print("6")
    # for skill in skillList: 
    #     fill_skills(*skill)
    print("7")

    return resume_template



name = input("Enter name: ")
address = input("Enter your full address: ")
phone = input("Enter phone number ")
email = input("Enter your email address: ")
github_link = input("Enter your gitHub Link: ")
linkedin_link = input("Enter your linkedin link : ")

fill_cont(name, address , phone, email , github_link, linkedin_link)

countWE = int(input("number of work experiences (1-3): "))

while countWE>0 :

    job_title = input("Enter job_title: ")
    company = input("Enter your full company: ")
    dates = input("Enter duration of work:  ")
    responsibilities = input("Enter your responsibilities: ")
    achievements = input("Enter your achievements: ")
    work = fill_workDict( job_title, company, dates ,responsibilities, achievements)
    workExList.append(work)
    countWE -= 1

resume_template["Work Experience"] = workExList

# for item in workExList:                  
#     fill_workDict(*item)

print(resume_template)


countE = int(input("number of education experiences (1-3): "))

while countE>0 :

    degree = input("Enter degree name : ")
    school = input("Enter your school name: ")
    grades = input("Enter your current/result grade: ")
    dates = input("Enter duration of course:  ")

    ed = fill_edu(degree , school ,grades, dates)
    eduList.append(ed)
    countE -= 1

resume_template["Education"] = eduList

print(resume_template)

countP = int(input("number of projects (1-3): "))

while countP>0 :

    name = input("Enter project name : ")
    desc = input("Enter your proj desc:  ")
    link = input("Enter project link: ")
    proj = fill_proj(name , desc , link )
    projList.append(proj)
    countP -= 1

resume_template["Projects"] = projList

print(resume_template)

countC = int(input("number of certifications (1-3): "))

while countC>0 :

    name = input("Enter certificate name : ")
    company = input("Enter issuing company/authority:  ")
    date = input("Enter certification date: ")
    certi = fill_certi(name, company, date)
    certiList.append(certi)
    countC -= 1

resume_template["Certifications"] = certiList

print(resume_template)

aboutMe = input("give a summary about yourself: ")
fill_summ(aboutMe)
moree = input("any additional info?: ")
fill_addInfo(moree)
skills = input("mention your skills: ")
skillList.append(fill_skills(skills)) 
achievementI = input("tell about your achievements: ")
achList.append(fill_achievements(achievementI))


print("resume filling")

print(resume_template)
filled_resume = resume_template
# filled_resume = fill_resume_dict(infoList, workExList,  eduList,  projList ,achList , certiList, skillList, resume_template)
# print(filled_resume)
print("resume ki dict ban gyi")

# print(resume_template)

# error analysis
#  normal work dict kro to sirf last entry show kr rha h work me 