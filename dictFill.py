# resume_template = { "contact_info": { "name": "", "address": "", "phone": "", "email": "", "github": "", "linkedin": "", "gmail": "" }, "summary": "", "work_experience": [ { "job_title": "", "company": "", "dates": "", "responsibilities": [], "achievements": [] } ], "education": [ { "degree": "", "school": "", "dates": "" } ], "projects": [ { "name": "", "description": "", "url": "" } ], "achievements": [], "certifications": [ { "name": "", "authority": "", "date": "" } ], "skills": [], "additional_info": [] }

resume_template = {}

def fill_cont(name, address, phone, email , github_link , linkedin_link , gmail):
    resume_template["contact_info"] = {'name':name , 'address': address , 'phone':phone, 'email':email , 'github_link': github_link, 'linkedin_link':linkedin_link, 'gmail':gmail}

# fill_cont("divi", "india", 7828, "divi@yoo", "link", "link", "link")

def fill_workDict( job_title, company, dates ,responsibilities, achievements):
    work = { "job_title": job_title, "company": company, "dates": dates, "responsibilities": responsibilities, "achievements": achievements }
    resume_template["work_experience"]= work

# fill_workDict("pr lead", "ISTE", "2020-present", "speak", "spoke")
# print(resume_template)

def fill_edu(degree , school , dates):
    resume_template["work_experience"] = { "degree": degree, "school": school, "dates": dates }

def fill_proj(name , desc , link ):
    resume_template["work_experience"] = { "name": name , "description": desc, "url": link}

def fill_certi(name, company, date):
    resume_template["certifications"] = { "name": name, "authority": company, "date": date}

def fill_achievements(achievement):
    resume_template["achievements"]= achievement

def fill_skills(skills):
    resume_template["skills"]= skills

def fill_addInfo(moree):
    resume_template["additional_info"]= moree

def fill_summ(aboutMe):
    resume_template["summary"]= aboutMe

# resume_template = { "contact_info": { "name": "", "address": "", "phone": "", "email": "", "github": "", "linkedin": "", "gmail": "" }, "summary": "", "work_experience": [ { "job_title": "", "company": "", "dates": "", "responsibilities": [], "achievements": [] } ], "education": [ { "degree": "", "school": "", "dates": "" } ], "projects": [ { "name": "", "description": "", "url": "" } ], "achievements": [], "certifications": [ { "name": "", "authority": "", "date": "" } ], "skills": [], "additional_info": [] }

infoList = []
workExList = []
respListW = [] #responsibility under work ex ki list
achListW = []  #achievements under work ex ki list
eduList =[]
projList = []
achList = []
certiList = []
skillList = []
addInfoList = []

# ye list user ip leke bharke is n me as parameter pass krni hai

def fill_resume_dict(infoList, workExList,  eduList,  projList ,achList , certiList, skillList, resume_template):
    for cont in infoList:
        fill_cont(*cont)
    for work in workExList:
        fill_workDict(*work)
    for edu in eduList:
        fill_edu(*edu)
    for proj in projList:
        fill_proj(*proj)
    for ach in achList:
        fill_achievements(*ach)
    for certi in certiList:
        fill_certi(*certi)
    for skill in skillList:
        fill_skills(*skill)
    
    print(resume_template)
    return resume_template

    
fill_resume_dict()


