#!/usr/bin/python
# encoding=utf8

from string import split
import os, sys

class calcScore:
    def __init__(self):
        pass
	
    def getTotalGrade(self, record_grade, record_unit):
        ts = 0
        tunit = 0
        for i in range(len(record_grade)):
            if record_grade[i] != 0:
                ts = ts + record_grade[i]*record_unit[i]
                tunit = tunit + record_unit[i]
        if tunit == 0:
            return(-1)
        else:
            return (ts/float(tunit))

    def getTotalGrade31(self, record_year, record_sem, record_grade, record_unit):
        ts = 0
        tunit = 0
        sem = []
        for i in range(len(record_grade)):
            sem.append((record_year[i]-1)*2 + record_sem[i])

        for i in range(len(record_grade)):
            if record_grade[i] != 0 and sem[i] <= 5:
                ts = ts + record_grade[i]*record_unit[i]
                tunit = tunit + record_unit[i]
        return (ts/float(tunit))


    def getSubjGrade(self, subj, record_cat, record_grade, record_unit):
        ts = 0
        tunit = 0
        for i in range(len(record_cat)):
            if subj == record_cat[i] and record_grade[i] != 0:
                ts = ts + record_grade[i]*record_unit[i]
                tunit = tunit + record_unit[i]
        if tunit != 0:
            return(ts/float(tunit))
        else:
            return(0)

    def getSubjYearGrade(self, subj, record_cat, record_grade, record_unit, record_year, record_sem, year, sem):
        ts = 0
        tunit = 0
        if sem == 0:
            for i in range(len(record_year)):
                if year == record_year[i] and subj == record_cat[i] and record_grade[i] != 0:
                    ts = ts + record_grade[i]*record_unit[i]
                    tunit = tunit + record_unit[i]
        else:
            for i in range(len(record_year)):
                if year == record_year[i] and sem == record_sem[i] and subj == record_cat[i] and record_grade[i] != 0:
                    ts = ts + record_grade[i]*record_unit[i]
                    tunit = tunit + record_unit[i]
        try:
            return(ts/float(tunit))
        except:
            return(0)
    
    # for grade by Indivdual science
    def getISubjGrade(self, subj, record_sub, record_grade, record_unit):
        
        ts = 0
        tunit = 0
        if subj == '물리':
            key = ['물리', '역학', '전자', 'Phys', 'phys']
        elif subj == '화학':
            key = ['화학', 'Chem', 'chem']
        elif subj == '생명과학':
            key = ['생물', '생명', '동물', '분자', '유전', '세포', 'Bio', 'bio']
        elif subj == '지구과학':
            key = ['지구', '대기', '환경', '우주', '천문', '바다']

        for i in range(len(record_sub)):
            cue = 0
            for i2 in range(len(key)):
                if record_sub[i].find(key[i2]) != -1:
                    cue = 1
                if cue == 1 and record_grade[i] != 0:
                    ts = ts + record_grade[i]*record_unit[i]
                    tunit = tunit + record_unit[i]
        try:
            return(ts/float(tunit))
        except:
            return(0)

    def getISubjYearGrade(self, subj, record_sub, record_grade, record_unit, record_year, record_sem, year, sem):
        ts = 0
        tunit = 0
        if subj == '물리':
            key = ['물리', '역학', '전자', 'Phys', 'phys']
        elif subj == '화학':
            key = ['화학', 'Chem', 'chem']
        elif subj == '생명과학':
            key = ['생물', '생명', '동물', '분자', '유전', '세포', 'Bio', 'bio']
        elif subj == '지구과학':
            key = ['지구', '대기', '환경', '우주', '천문', '바다']
        if sem == 0:
            for i in range(len(record_sub)):
                cue = 0
                for i2 in range(len(key)):
                    if record_year[i] == year and record_sub[i].find(key[i2]) != -1:
                        cue = 1
                    if cue == 1 and record_grade[i] != 0:
                        ts = ts + record_grade[i]*record_unit[i]
                        tunit = tunit + record_unit[i]
        else:
            for i in range(len(record_sub)):
                cue = 0
                for i2 in range(len(key)):
                    if record_year[i] == year and record_sem[i] == sem and record_sub[i].find(key[i2]) != -1:
                        cue = 1
                    if cue == 1 and record_grade[i] != 0:
                        ts = ts + record_grade[i]*record_unit[i]
                        tunit = tunit + record_unit[i]

        try:        
            return(ts/float(tunit))
        except:
            return(0)

    def getISubjNum(self, subj, record_sub, record_grade, record_unit):
        ts = 0
        if subj == '물리':
            key = ['물리', 'Phys', 'phys', '역학', '전자']
        elif subj == '화학':
            key = ['화학', 'Chem', 'chem']
        elif subj == '생명과학':
            key = ['생물', '생명', '동물', '분자생물', '유전', '세포', 'Bio', 'bio']
        elif subj == '지구과학':
            key = ['지구', '대기', '환경', '우주', '천문', '바다']

        for i in range(len(record_sub)):
            cue = 0
            for i2 in range(len(key)):
                if record_sub[i].find(key[i2]) != -1:
                    cue = 1
            if cue == 1 :
                ts = ts + 1
        return(ts)

    def getSemGrade(self, year, sem, record_year, record_sem, record_grade, record_unit):
        ts = 0
        tunit = 0
        for i in range(len(record_year)):
            if year == record_year[i] and sem == record_sem[i] and record_grade[i] != 0:
                ts = ts + record_grade[i]*record_unit[i]
                tunit = tunit+record_unit[i]
        try:
            return(ts/float(tunit))        
        except:
            return(0)        

    def getYearGrade(self, year, record_year, record_grade, record_unit):
        ts = 0
        tunit = 0
        for i in range(len(record_year)):
            if year == record_year[i] and record_grade[i] != 0:
                ts = ts + record_grade[i]*record_unit[i]
                tunit = tunit+record_unit[i]
        try:
            return(ts/float(tunit))        
        except:
            return(0)        

    def getCorGrade(self, record_grade, record_pop):
        for i in range(len(record_grade)):
            if record_grade[i] != 0:
                if record_pop[i] >= 5 and record_pop[i] < 13:
                    record_grade[i] = record_grade[i] - 1
                elif record_pop[i] >=3 and record_pop[i] < 5:
                    record_grade[i] = record_grade[i] - 2
                elif record_pop[i] == 2:
                    record_grade[i] = record_grade[i] - 3
                elif record_pop[i] == 1:
                    record_grade[i] = record_grade[i] - 4
        return (record_grade)
                
    def getMainGrade(self, record_grade, record_unit, series, dep, record_cat):
        ts = 0
        tunit = 0
        if series == "이과":
            acat = ['수학', '과학']
        elif series == '문과':
            acat = ['국어', '영어', '수학', '사회']
        else:
            acat = ['국어', '영어', '사회']

        if dep.find('자유전공') != -1:
            acat = ['국어', '영어', '수학', '사회', '과학']
        
        if dep.find('수리과학') != -1 or dep.find('통계') != -1:
            acat = ['수학']

        if dep.find('건축') != -1:
            acat = ['국어', '영어', '수학']

        for i in range(len(record_cat)):
            for i2 in acat:
                if i2 == record_cat[i] and record_grade[i] != 0:
                    ts = ts + record_grade[i]*record_unit[i]
                    tunit = tunit + record_unit[i]
        return (ts/float(tunit))




    def getMain3Grade(self, record_grade, record_unit, series, dep, record_cat, record_year, record_sem, year, sem):
        ts = 0
        tunit = 0
        acat = ['국어', '수학', '영어']

        if year == 0:
            for i in range(len(record_cat)):
                for i2 in acat:
                    if i2 == record_cat[i] and record_grade[i] != 0:
                        ts = ts + record_grade[i]*record_unit[i]
                        tunit = tunit + record_unit[i]
        else:
            if sem == 0:
                for i in range(len(record_cat)):
                    for i2 in acat:
                        if i2 == record_cat[i] and record_year[i] == year and record_grade[i] != 0:
                            ts = ts + record_grade[i]*record_unit[i]
                            tunit = tunit + record_unit[i]
            else:
                for i in range(len(record_cat)):
                    for i2 in acat:
                        if i2 == record_cat[i] and record_year[i] == year and record_sem[i] == sem and record_grade[i] != 0 :
                            ts = ts + record_grade[i]*record_unit[i]
                            tunit = tunit + record_unit[i]
        if tunit == 0:
            v = 0
        else:
            v = ts/float(tunit)
        return (v)

    def getMain5Grade(self, record_grade, record_unit, series, dep, record_cat, record_year, record_sem, year, sem):
        ts = 0
        tunit = 0
        
        if series == "이과":
            acat = ['국어', '영어', '수학', '과학']
        elif series == '문과':
            acat = ['국어', '영어', '수학', '사회']
        else:
            acat = ['국어', '영어', '사회']
        
        if year == 0:
            for i in range(len(record_cat)):
                cue = 0
                for i2 in acat:
                    if i2 == record_cat[i] and record_grade[i] != 0:
                        cue = 1
                        break
                if cue == 1:
                    ts = ts + record_grade[i]*record_unit[i]
                    tunit = tunit + record_unit[i]
        else:
            if sem == 0:
                for i in range(len(record_cat)):
                    cue = 0
                    for i2 in acat:
                        if i2 == record_cat[i] and record_year[i] == year and record_grade[i] != 0:
                            cue = 1
                            break
                    if cue == 1:
                        ts = ts + record_grade[i]*record_unit[i]
                        tunit = tunit + record_unit[i]
            else:
                for i in range(len(record_cat)):
                    cue = 0
                    for i2 in acat:
                        if i2 == record_cat[i] and record_year[i] == year and record_sem[i] == sem and record_grade[i] != 0:
                            cue = 1
                            break
                    if cue == 1:
                        ts = ts + record_grade[i]*record_unit[i]
                        tunit = tunit + record_unit[i]
        if tunit != 0:
            return (ts/float(tunit))
        else:
            return (0)
    
    def getMain5Grade244(self, record_grade, record_unit, series, dep, record_cat, record_year, record_sem, again, wgt):
        
        if again == 'no' or again == 'yes':
            year = [1, 2, 3]
        else:
            year = range(1, int(again)+1)

        if series == "이과":
            acat = ['국어', '영어', '수학', '과학']
        elif series == '문과':
            acat = ['국어', '영어', '수학', '사회']
        else:
            acat = ['국어', '영어', '사회']
        
        tstemp = []
        tutemp = []
        weight = []
        
        for i3 in year:
            ts = 0
            tunit = 0
            for i in range(len(record_cat)):
                if record_year[i] == i3 and record_unit[i] != 0 and record_grade[i] != 0:
                    for i2 in acat:
                        if i2 == record_cat[i]:
                            ts = ts + record_grade[i]*record_unit[i]
                            tunit = tunit + record_unit[i]
            
            if ts != 0:
                tstemp.append(ts/float(tunit))
                weight.append(wgt[i3-1])
        
        ts = 0
        for i in range(len(tstemp)):
            ts = ts + tstemp[i] * weight[i]
        
        return(ts/float(sum(weight)))
            

    def getYearMainGrade(self, record_grade, record_unit, series, dep, record_cat, record_year, record_sem, year, sem):
        ts = 0
        tunit = 0
        if series == "이과":
            acat = ['수학', '과학']
        elif series == '문과':
            acat = ['국어', '영어', '수학', '사회']
        else:
            acat = ['국어', '영어', '사회']

        if dep.find('자유전공') != -1:
            acat = ['국어', '영어', '수학', '사회', '과학']
        
        if dep.find('수리과학') != -1 or dep.find('통계') != -1:
            acat = ['수학']

        if dep.find('건축') != -1:
            acat = ['국어', '영어', '수학']

        if sem == 0:
            for i in range(len(record_cat)):
                for i2 in acat:
                    if i2 == record_cat[i] and record_year[i] == year and record_grade[i] != 0:
                        ts = ts + record_grade[i]*record_unit[i]
                        tunit = tunit + record_unit[i]
        else:
            for i in range(len(record_cat)):
                for i2 in acat:
                    if i2 == record_cat[i] and record_year[i] == year and record_sem[i] == sem and record_grade[i] != 0:
                        ts = ts + record_grade[i]*record_unit[i]
                        tunit = tunit + record_unit[i]

        try:
            return (ts/float(tunit))
        except:
            return (0)



    def getRelGrade(self, record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, year, sem):
        ts = 0
        tunit = 0
        if series == '':
            return(0)
        if series == "문과":
            acat = ['국어', '영어', '수학', '사회']
            acat2 = [[], [], [], []]
            
            # should be filled  
            for i in ['인문계열', '국어국문', '중어중문', '영어영문', '불어불문', '독어독문', '서어서문', '언어', '국사', '서양사', '동양사', '고고미술', '철학', '종교', '미학']:
                if dep.find(i) != -1:
                    acat = ['수학', '기타']
                    acat2 = [[], ['중국', '프랑스', '독일', '일본', '스페인']]
            for i in ['정치', '외교', '경제', '사회', '인류', '심리', '지리', '사회복지', '언론', '경영', '농경제', '소비자']:
                if dep.find(i) != -1:
                    acat = ['수학', '영어']
                    acat2 = [[], []]
            for i in ['교육']:      # 사범대
                if dep.find(i) != -1:
                    acat = ['국어', '영어']
                    acat2 = [[], []]
            for i in ['자유전공']:
                if dep.find(i) != -1:
                    acat = ['수학']
                    acat2 = [[]]
            for i in ['간호', '의류']:
                if dep.find(i) != -1:
                    acat = ['과학']
                    acat2 = [['화학', '생명과학']]
        elif series == '이과':
            acat = ['수학', '과학']
            acat2 = [[], []]
            for i in ['수리과학', '통계', '자유전공', '건축', '수학교육']:
                if dep.find(i) != -1:
                    acat = ['수학']
                    acat2 = [['수학2', '미적', '심화']]      # 미적분, 수학2
            for i in ['물리', '천문', '건설환경', '기계', '항공', '전기', '컴퓨터', '에너지', '원자핵', '산업', '조선', '물리교육']:
                if dep.find(i) != -1:
                    acat = ['수학', '과학']
                    acat2 = [['수학2', '미적', '심화'], ['물리']]
            for i in ['화학부', '화학교육']:
                if dep.find(i) != -1:
                    acat = ['수학', '과학']
                    acat2 = [['수학2', '미적', '심화'], ['화학']]
            for i in ['생명과학', '생물교육']:
                if dep.find(i) != -1:
                    acat = ['수학', '과학']
                    acat2 = [['수학2', '미적', '심화'], ['생명과학']]
            for i in ['지구환경', '지구과학교육']:
                if dep.find(i) != -1:
                    acat = ['수학', '과학']
                    acat2 = [['수학2', '미적', '심화'], ['지구과학']]
            for i in ['의예', '수의예', '치의학']:
                if dep.find(i) != -1:
                    acat = ['수학', '과학']
                    acat2 = [['미적', '수학2', '심화'], ['화학', '생명과학']]
            for i in ['간호', '식품', '의류']:
                if dep.find(i) != -1:
                    acat = ['과학']
                    acat2 = [['화학', '생명과학']]
            for i in ['재료공학', '화학생물', '식물생산', '산림', '식품동물', '응용생물', '조경지역', '바이오']:
                if dep.find(i) != -1:
                    acat = ['수학', '과학']
                    acat2 = [['수학2', '미적', '심화'], ['물리', '화학', '생명과학']]
            for i in ['자유전공']:
                if dep.find(i) != -1:
                    acat = ['수학']
                    acat2 = [['수학2', '미적', '심화']]
        else:
            acat = ['국어', '영어', '사회']
            acat2 = [[], [], []]
        subj = ''
        if subj == '물리':
            key = ['물리', 'Phys', 'phys', '역학', '전자']
        elif subj == '화학':
            key = ['화학', 'Chem', 'chem']
        elif subj == '생명과학':
            key = ['생물', '생명', '동물', '분자', '유전', '세포', 'Bio', 'bio']
        elif subj == '지구과학':
            key = ['지구', '대기', '환경', '우주', '천문', '바다']
        if year == 0:
            for i in range(len(record_sub)):
                for i2 in range(len(acat2)):
                    cue = 0
                    if len(acat2[i2]) != 0:
                        for i3 in range(len(acat2[i2])):
                            if record_sub[i].find(acat2[i2][i3]) > -1 and record_grade[i] != 0:
                                cue = 1
                        if cue == 1:
                            ts = ts + record_grade[i]*record_unit[i]
                            tunit = tunit + record_unit[i]
                    else:
                        for i3 in range(len(acat)):
                            if record_cat[i].find(acat[i3]) > -1 and record_grade[i] != 0:
                                cue = 1
                        if cue == 1:
                            ts = ts + record_grade[i]*record_unit[i]
                            tunit = tunit + record_unit[i]
                            
        else:
            if sem != 0:
                for i in range(len(record_sub)):
                    cue = 0
                    for i2 in range(len(acat2)):
                        if len(acat2[i2]) != 0:
                            for i3 in range(len(acat2[i2])):
                                if record_sub[i].find(acat2[i2][i3]) > -1 and record_year[i] == year and record_sem[i] == sem and record_grade[i] != 0:
                                    cue = 1
                            if cue == 1:
                                ts = ts + record_grade[i]*record_unit[i]
                                tunit = tunit + record_unit[i]
                        else:
                            for i3 in range(len(acat)):
                                if record_cat[i].find(acat[i3]) > -1 and record_year[i] == year and record_sem[i] == sem and record_grade[i] != 0:
                                    cue = 1
                                if cue == 1:
                                    ts = ts + record_grade[i]*record_unit[i]
                                    tunit = tunit + record_unit[i]
            else:
                for i in range(len(record_sub)):
                    cue = 0
                    for i2 in range(len(acat2)):
                        if len(acat2[i2]) != 0:
                            for i3 in range(len(acat2[i2])):
                                if record_sub[i].find(acat2[i2][i3]) > -1 and record_year[i] == year and record_grade[i] != 0:
                                    cue = 1
                            if cue == 1:
                                ts = ts + record_grade[i]*record_unit[i]
                                tunit = tunit + record_unit[i]
                        else:
                            for i3 in range(len(acat)):
                                if record_cat[i].find(acat[i3]) > -1 and record_year[i] == year and record_grade[i] != 0:
                                    cue = 1
                                if cue == 1:
                                    ts = ts + record_grade[i]*record_unit[i]
                                    tunit = tunit + record_unit[i]

        try:
            return (ts/float(tunit))
        except:
            return (0)

    def getMainCorGrade(self, record_grade, record_unit, series, dep, record_cat, record_year, again, w):
        tstemp = []
        tutemp = []
        if again == 'no' or again == 'yes':
            year = [1, 2, 3]
        else:
            year = range(1, int(again)+1)


        if series == "이과":
            acat = ['수학', '과학']
        elif series == '문과':
            acat = ['국어', '영어', '수학', '사회']
        else:
            acat = ['국어', '영어', '사회']
        
        if dep.find('자유전공') != -1:
            acat = ['국어', '영어', '수학', '사회', '과학']
        
        if dep.find('수리과학') != -1 or dep.find('통계') != -1:
            acat = ['수학']

        if dep.find('건축') != -1:
            acat = ['국어', '영어', '수학']

        weight = []
        for i3 in year:
            ts = 0
            tunit = 0
            for i in range(len(record_cat)):
                if record_year[i] == i3 and record_unit[i] != 0 and record_grade[i] != 0:
                    for i2 in acat:
                        if i2 == record_cat[i]:
                            ts = ts + record_grade[i]*record_unit[i]
                            tunit = tunit + record_unit[i]
            if ts != 0:
                tstemp.append(ts/float(tunit))
                weight.append(w[i3-1])
        ts = 0
        for i in range(len(tstemp)):
            ts = ts + tstemp[i] * weight[i]
        return (ts/float(sum(weight)))

    
    def getTotalCorGrade(self, record_grade, record_unit, record_year, again, w):
        tstemp = []
        tutemp = []
        weight = []
        if again == 'no' or again == 'yes':
            year = [1, 2, 3]
        else:
            year = range(1, int(again)+1)
        
        for i2 in year: 
            ts = 0
            tu = 0
            for i in range(len(record_grade)):
                if record_year[i] == i2 and record_unit[i] != 0 and record_grade[i] != 0:
                    ts = ts + record_grade[i]*record_unit[i]
                    tu = tu + record_unit[i]
            if ts != 0:
                tstemp.append(ts/float(tu))
                weight.append(w[i2-1])
        
        ts = 0
        for i in range(len(tstemp)):
            ts = ts + tstemp[i] * weight[i]
        
        try:
            return ts/float(sum(weight))
        except:
            return(0)

    def getSubjNum(self, record_cat, record_unit, subj):
        count = 0
        for i in range(len(record_cat)):
            if record_cat[i] == subj and record_unit[i] > 0:
                count = count + 1
        return(count)    

    def getISubjNum(self, record_sub, record_unit, subj):
        if subj == '물리':
            key = ['물리', '역학', '전자', 'Phys', 'phys']
        elif subj == '화학':
            key = ['화학', 'Chem', 'chem']
        elif subj == '생명과학':
            key = ['생물', '생명', '동물', '분자', '유전', '세포', 'Bio', 'bio']
        elif subj == '지구과학':
            key = ['지구', '대기', '환경', '우주', '천문', '바다']
        
        count = 0
        for i in range(len(record_sub)):
            for i2 in range(len(key)):
                if record_unit[i] > 0 and record_sub[i].find(key[i2]) != -1:
                    count = count + 1
        return(count)    


    def getMainUnit(self, record_cat, record_unit, series, highschooltype):

        pscut = 25
        nscut = 10
        
        # 국어, 영어, 수학, 사회, 과학, 기타
        ts1 = 0
        ts2 = 0
        ts3 = 0
        ts4 = 0
        ts5 = 0
        ts6 = 0

        for i in range(0, len(record_cat)):
            if record_cat[i] == '국어':
                ts1 = ts1 + record_unit[i]
            if record_cat[i] == '영어':
                ts2 = ts1 + record_unit[i]
            if record_cat[i] == '수학':
                ts3 = ts1 + record_unit[i]
            if record_cat[i] == '사회':
                ts4 = ts1 + record_unit[i]
            if record_cat[i] == '과학':
                ts5 = ts1 + record_unit[i]
            if record_cat[i] == '기타':
                ts6 = ts1 + record_unit[i]

        if series == '이과':
            ps = ts5
            ns = ts4
        elif series == '문과':
            ps = ts4
            ns = ts5
        else:
            ps = max(ts4, ts5)
            ns = min(ts4, ts5)

        if highschooltype == '외고' or highschooltype == '자사고전국' or highschooltype == '국제고' or highschooltype == '영재학교' :
            pscut = 15
            
        if ps > pscut and ns > nscut:
            ts = 0
        elif ps > pscut - 2 and ns > nscut:
            ts = -1
        else:
            ts = -3

        return ts


    def getGradeScore(self, year, grade, univ, app, highschooltype):
        fname = '%s/config/data/%d/%s.tbl'%(os.getcwd(), year, univ)
        try:
            f = open(fname, 'r')
        except:
            try:
                fname = '%s/config/data/%d/%s.tbl'%(os.getcwd(), year, '기타대')
                f = open(fname, 'r')
                #print "file open error"
                # 기타 대학
            except:
                return(-1)

        content = f.readlines()
        f.close()

        a = split(content[0])
        
        if highschooltype == '일반고평준' or highschooltype == '자공고':
            atype = 2
        elif highschooltype == '일반고비평준':
            atype = 3
        elif highschooltype == '자사고광역':
            atype = 4
        elif highschooltype == '자사고전국':
            atype = 5
        elif highschooltype == '외고' or highschooltype == '국제고' or highschooltype == '과학고' :
            atype = 6
        elif highschooltype == '영재학교':
            atype = 7
        else:
            atype = 2

        g = []
        sc = []
        for i in range(1, len(content)):
            scontent = content[i].split()
            g.append(float(scontent[atype]))
            sc.append(int(scontent[0]))

        scoreidx = 0
        if highschooltype != '영재학교':
            for i in range(len(g)):
                if grade > g[i]:
                    scoreidx = min(i+1, len(sc)-1)
        else:
            for i in range(len(g)):
                if grade < g[i]:
                    scoreidx = min(i+1, len(sc)-1)
        return sc[scoreidx] 

    def getAwardScore(self, award_inout, award_year, award_cat, award_grade, series, chkv):
        score = 0
        weight = [1, 0.5, 0.3, 0.15]
        ywt = [1, 1, 1.5]
        pwt = [1, 1.5]
        
        if series == '문과':
            for i in range(len(award_cat)):
                if award_inout[i] == 'in':
                    pweight = pwt[0]
                elif award_inout[i] == 'out':
                    pweight = pwt[1]
                else:
                    pweight = 1

                if award_year[i] == '1':
                    yweight = ywt[0]
                elif award_year[i] == '2':
                    yweight = ywt[1]
                elif award_year[i] == '3':
                    yweight = ywt[2]
                else:
                    yweight = 1 
                    
                if award_grade[i] > 0:
                    if award_cat[i] == '수학' or award_cat[i] == '과학':
                        score = score + 1*weight[award_grade[i]-1]*chkv[i]*pweight*yweight
                    elif award_cat[i] == '기타':
                        score = score + 0.5*weight[award_grade[i]-1]*pweight*yweight
                    else:
                        score = score + 2*weight[award_grade[i]-1]*chkv[i]*pweight*yweight
        elif series == '이과':
            for i in range(len(award_cat)):
                if award_inout[i] == 'in':
                    pweight = pwt[0]
                elif award_inout[i] == 'out':
                    pweight = pwt[1]
                else:
                    pweight = 1

                if award_year[i] == '1':
                    yweight = ywt[0]
                elif award_year[i] == '2':
                    yweight = ywt[1]
                elif award_year[i] == '3':
                    yweight = ywt[2]
                else:
                    yweight = 1
                
                if award_grade[i] > 0:
                    if award_cat[i] == '수학':
                        score = score + 2*weight[award_grade[i]-1]*chkv[i]*yweight*pweight
                    elif award_cat[i] == '과학':
                        score = score + 1.5*weight[award_grade[i]-1]*chkv[i]*yweight*pweight
                    elif award_cat[i] == '기타':
                        score = score + 0.3*weight[award_grade[i]-1]*chkv[i]*yweight*pweight
                    else:
                        score = score + 0.5*weight[award_grade[i]-1]*chkv[i]*yweight*pweight
        else:
            for i in range(len(award_cat)):
                if award_inout[i] == 'in':
                    pweight = pwt[0]
                elif award_inout[i] == 'out':
                    pweight = pwt[1]
                else:
                    pweight = 1

                if award_year[i] == '1':
                    yweight = ywt[0]
                elif award_year[i] == '2':
                    yweight = ywt[1]
                elif award_year[i] == '3':
                    yweight = ywt[2]
                else:
                    yweight = 1 
                if award_grade[i] > 0:
                    if award_cat[i] == '수학' or award_cat[i] == '과학':
                        score = score + 1*weight[award_grade[i]-1]*chkv[i]*yweight*pweight
                    elif award_cat[i] == '기타':
                        score = score + 2*weight[award_grade[i]-1]*chkv[i]*yweight*pweight
                    else:
                        score = score + 1*weight[award_grade[i]-1]*chkv[i]*yweight*pweight
        return score

    def getTotalScore(self, grasc, awasc, actsc, sersc, leasc):
        total_score = grasc+ awasc + actsc + sersc + leasc

        if actsc == 0:
            total_score = total_score - 2
        if sersc == 0:
            total_score = total_score - 2
        return total_score

    def getCutScore(self, awasc, actsc, sersc, leasc):
        if awasc < 2 or actsc < 2 or sersc+leasc < 1:
            return -5
        else:
            return 0


    def getActivityScore(self, activity_cat, activity_time, series, chkv):
        score = 0 
        if series == '문과':
            for i in range(len(activity_cat)):
                if activity_time[i] >= 4:
                    weight=1.5
                elif activity_time[i] >= 2:
                    weight=1
                elif activity_time[i] >= 1:
                    weight=0.5
                elif activity_time[i]== 0:
                    weight=0
                if activity_cat[i] == '수학' or activity_cat[i] == '과학':
                    score = score + 1*weight*chkv[i]
                elif activity_cat[i] == '기타':
                    score = score + 0.75*weight*chkv[i]
                else:
                    score = score + 1.5*weight*chkv[i]
        elif series == '이과':
            for i in range(len(activity_cat)):
                if activity_time[i] >= 4:
                    weight=1.5
                elif activity_time[i] >= 2:
                    weight=1
                elif activity_time[i] >= 1:
                    weight=0.5
                elif activity_time[i]== 0:
                    weight=0
                if activity_cat[i] == '수학' or activity_cat[i] == '과학':
                    score = score + 1.5*weight*chkv[i]
                elif activity_cat[i] == '기타':
                    score = score + 0.75*weight*chkv[i]
                else:
                    score = score + 0.75*weight*chkv[i]
        else:
            for i in range(len(activity_cat)):
                if activity_time[i] >= 4:
                    weight=1.5
                elif activity_time[i] >= 2:
                    weight=1
                elif activity_time[i] >= 1:
                    weight=0.5
                elif activity_time[i]== 0:
                    weight=0
                else:
                    weight=0

                if activity_cat[i] == '수학' or activity_cat[i] == '과학':
                    score = score + 0.75*weight*chkv[i]
                elif activity_cat[i] == '기타':
                    score = score + 1.5*weight*chkv[i]
                else:
                    score = score + 0.75*weight*chkv[i]
        return score


    def getServiceScore(self, service_cat, service_time, chkv):
        score = 0
        for i in range(len(service_time)):
            if service_time[i] == -9:
                service_time[i] = 0
        for i in range(len(service_time)):
            service_time[i] = service_time[i]*chkv[i]
        
        if sum(service_time) >= 80:
            score = score + 5
        elif sum(service_time) >= 50:
            score = score + 4
        elif sum(service_time) >= 20:
            score = score + 3
        
        if max(service_time) >= 40:
            score = float(score * 1.2)
        elif max(service_time) >= 20:
            score = float(score * 1.0)
        else:
            score = float(score * 0.8)

        return min(score, 5)
    
    def getTServiceScore(self, service_total_time):
        score = 0
        if service_total_time >= 100:
            score = 1
        elif service_total_time >= 70:
            score = 0.5
        elif service_total_time >= 30:
            score = 0.1
        return(score)


    def getLeadershipScore(self, leadership_cat, leadership_time, chkv):
        score = 0
        for i in range(len(leadership_cat)):
            if leadership_cat[i] == '전교회장':
                score = score + 2*leadership_time[i]*chkv[i]
            if leadership_cat[i] == '반장':
                score = score + 1.5 * leadership_time[i]*chkv[i]
            if leadership_cat[i] == '동아리장':
                score = score + 1.2 * leadership_time[i]*chkv[i]
            if leadership_cat[i] == '부반장':
                score = score + 1 * leadership_time[i]*chkv[i]

        return min(score, 5)

    def getProbApplication(self, year, univ, app, dep, total_score, opt):
        fname = '%s/config/data/%d/%s.dat'%(os.getcwd(), year, univ)
        try:
            f = open(fname, 'r')
        except:
            return([-1, -1])
        
        content = f.readlines()
        f.close()
        
        a = split(content[0])
        cue = -1 
        for i in range(len(a)):
            if a[i] == app:
                cue = i
        
        if cue == -1:
            return([-1, -1])

        sc = []
        for i in range(1, len(content)):
            a = split(content[i])
            if a[0] == dep:
                sc = int(a[cue+1])
        
        try:
            diff = total_score - sc
        except:
            diff = -99

        if diff >= 5:
            if opt == 1:
                return "합격 가능성이 비교적 높은 편입니다만,<BR>구체적인 서류의 내용에 따라 결과가 달라질 수 있습니다.<BR>자세한 상담을 위해서는 관리자에게 연락바랍니다."
        elif diff < 5 and diff >= -4:
            if opt == 1:
                return "정량적인 요인들을 고려할 때 지원가능한 수준이지만, <BR>정성적인 측면을 포함하여 보다 정확한 평가를 위해서는<BR>자세한 상담이 필요합니다.<BR>관리자에게 연락주세요."
        elif diff < -4 and diff > -8:
            if opt == 1:
                return "합격가능성이 높은 편은 아니지만, <BR>지원을 위해서라면 자세한 상담이 도움이 될 수 있습니다.<BR>."
        else:
            if opt == 1:
                return "합격가능성이 낮은 편입니다.<BR>구체적인 내용을 상담하기 위해서는 관리자에게 연락주십시오."

        if opt == 0:
            try:
                if len(sc) != 0:
                    return([sc-4, sc+4])
                else:
                    return([-1, -1])
            except:
                return([-1, -1])

    def exceptionCheck(self, region, highschooltype):
        except_point = 0
        if region == '서울' or region == '강원':
            if highschooltype == '자사고전국':
                except_point = 1
        else:
            if highschooltype == '자사고전국':
                except_point = 2 
            
        return except_point

    def getWeight(self, year, univ, app):
        weight = []
        try:
            fname = '%s/config/data/%d/weight.csv'%(os.getcwd(), year)
            f = open(fname, 'r')
            content = f.readlines()
            f.close()
            for i in content:
                a = split(i)
                if a[0] == univ:
                    if a[1] == app:
                        weight.append(float(a[2]))
                        weight.append(float(a[3]))
                        weight.append(float(a[4]))
                        weight.append(float(a[5]))
                        weight.append(float(a[6]))
        except:
            weight = [1, 1, 1, 1, 1]

        if len(weight) == 0:
            weight = [1, 1, 1, 1, 1]

        #wr = sum(weight)/5.0
        #weight = [i2 * wr for i2 in weight]
        #if sum(weight) > 5.0:
        #    wr = 5.0/sum(weight)
        #    weight = [i2 * wr for i2 in weight]
        return (weight)

    def hscheck3(self, year, region, highschooltype, highschool):
        
        from calcScore import calcScore
        rc = calcScore()
        if year < 2018:
            return(rc.hscheck(year, region, highschooltype, highschool))
        
        f1name = '%s/config/data/%d/highschool.xlsx'%(os.getcwd(), year)
        
        import xlrd
        wi = xlrd.open_workbook(f1name)
        wis = wi.sheet_by_index(0)

        ncol = wis.ncols
        nrow = wis.nrows
        
        hspoint = -9
        for i in range(3, nrow):
            hn = wis.row_values(i)[0].encode('utf8')
            rn = wis.row_values(i)[1].encode('utf8')
            tn = wis.row_values(i)[2].encode('utf8')
            try:
                sNum = int(wis.row_values(i)[3])
            except:
                sNum = 0
            try:
                rNum = int(wis.row_values(i)[4])
            except:
                rNum = 0
            tNum = wis.row_values(i)[5]
          
            if hn.find(highschool) > -1 and rn.find(region) > -1:
                if highschooltype == '일반고평준':
                    try:
                        if sNum > 5:
                            hspoint = 3
                        elif sNum > 2:
                            hspoint = 0
                        else:
                            hspoint = -5
                        if rNum > 5:
                            hspoint = hspoint + 3
                            hspoint = max(hspoint, 3)
                        elif rNum > 2:
                            hspoint = hspoint + 2
                            hspoint = max(hspoint, 1)
                        elif rNum > 0:
                            hspoint = hspoint + 1
                            hspoint = max(hspoint, 0)
                    except:
                        hspoint = -5
                elif highschooltype == '일반고비평준':
                    try:
                        if sNum > 5:
                            hspoint = 3
                        elif sNum > 2:
                            hspoint = 0
                        else:
                            hspoint = -3
                        if rNum > 5:
                            hspoint = hspoint + 3
                            hspoint = max(hspoint, 3)
                        elif rNum > 2:
                            hspoint = hspoint + 2
                            hspoint = max(hspoint, 1)
                        elif rNum > 0:
                            hspoint = hspoint + 1
                            hspoint = max(hspoint, 0)
                    except:
                        hspoint = -3
                elif highschooltype == '영재학교':
                    if sNum > 50:
                        hspoint = 5
                    elif sNum > 30:
                        hspoint = 3
                    else:
                        hspoint = 1
                elif highschooltype == '과학고':
                    if sNum >= 15:
                        hspoint = 3
                    elif sNum >= 8:
                        hspoint = 1
                    else:
                        hspoint = 0
                elif highschooltype == '외국어고' or highschooltype == '국제고' or highschooltype == '자사고전국':
                    if sNum > 40:
                        hspoint = 5
                    elif sNum > 20:
                        hspoint = 3
                    elif sNum > 10:
                        hspoint = 0
                    else:
                        hspoint = -2
                    if rNum > 5:
                        hspoint = hspoint + 3
                        hspoint = max(hspoint, 3)
                    elif rNum > 2:
                        hspoint = hspoint + 2
                        hspoint = max(hspoint, 1)
                    elif rNum > 0:
                        hspoint = hspoint + 1
                        hspoint = max(hspoint, 0)
                elif highschooltype == '자사고광역':
                    if sNum > 5:
                        hspoint = 2
                    elif sNum > 3:
                        hspoint = 0
                    else:
                        hspoint = -5
                    if rNum > 5:
                        hspoint = hspoint + 3
                        hspoint = max(hspoint, 3)
                    elif rNum > 2:
                        hspoint = hspoint + 2
                        hspoint = max(hspoint, 1)
                    elif rNum > 0:
                        hspoint = hspoint + 1
                        hspoint = max(hspoint, 0)
                else:
                    if sNum >= 10:
                        hspoint = 2
                    elif sNum >= 6:
                        hspoint = 0
                    else:
                        hspoint = -5
                    if rNum > 5:
                        hspoint = hspoint + 3
                        hspoint = max(hspoint, 3)
                    elif rNum > 2:
                        hspoint = hspoint + 2
                        hspoint = max(hspoint, 1)
                    elif rNum > 0:
                        hspoint = hspoint + 1
                        hspoint = max(hspoint, 0)
            if hspoint != -9:
                return(hspoint)
        return (-5)

    def hscheck2(self, year, region, highschooltype, highschool):
        
        from calcScore import calcScore
        rc = calcScore()
        if year < 2018:
            return(rc.hscheck(year, region, highschooltype, highschool))
        
        f1name = '%s/config/data/2018SNU.xlsx'%(os.getcwd())
        # 2018 전학교 기록을 우선 참고
        # 2019 기록을 보조로 활용
        import xlrd
        wi = xlrd.open_workbook(f1name)
        wis = wi.sheet_by_index(0)

        ncol = wis.ncols
        nrow = wis.nrows
        
        hspoint = -9
        for i in range(3, nrow):
            hn = wis.row_values(i)[0].encode('utf8')
            rn = wis.row_values(i)[1].encode('utf8')
            tn = wis.row_values(i)[2].encode('utf8')
            try:
                sNum = int(wis.row_values(i)[3])
            except:
                sNum = 0
            try:
                rNum = int(wis.row_values(i)[4])
            except:
                rNum = 0
            tNum = wis.row_values(i)[5]
            
            if hn.find(highschool) > -1 and rn.find(region) > -1:
                if highschooltype == '일반고평준':
                    try:
                        if sNum > 5:
                            hspoint = 3
                        elif sNum > 2:
                            hspoint = 0
                        else:
                            hspoint = -5
                        if rNum > 5:
                            hspoint = hspoint + 3
                            hspoint = max(hspoint, 3)
                        elif rNum > 2:
                            hspoint = hspoint + 2
                            hspoint = max(hspoint, 1)
                        elif rNum > 0:
                            hspoint = hspoint + 1
                            hspoint = max(hspoint, 0)
                    except:
                        hspoint = -5
                elif highschooltype == '일반고비평준':
                    try:
                        if sNum > 5:
                            hspoint = 3
                        elif sNum > 2:
                            hspoint = 0
                        else:
                            hspoint = -3
                        if rNum > 5:
                            hspoint = hspoint + 3
                            hspoint = max(hspoint, 3)
                        elif rNum > 2:
                            hspoint = hspoint + 2
                            hspoint = max(hspoint, 1)
                        elif rNum > 0:
                            hspoint = hspoint + 1
                            hspoint = max(hspoint, 0)
                    except:
                        hspoint = -5
                elif highschooltype == '영재학교':
                    if sNum > 50:
                        hspoint = 5
                    elif sNum > 30:
                        hspoint = 3
                    else:
                        hspoint = 1
                elif highschooltype == '과학고':
                    if sNum >= 15:
                        hspoint = 3
                    elif sNum >= 8:
                        hspoint = 1
                    else:
                        hspoint = 0
                elif highschooltype == '외국어고' or highschooltype == '국제고' or highschooltype == '자사고전국':
                    if sNum > 40:
                        hspoint = 5
                    elif sNum > 20:
                        hspoint = 3
                    elif sNum > 10:
                        hspoint = 0
                    else:
                        hspoint = -2
                    if rNum > 5:
                        hspoint = hspoint + 3
                        hspoint = max(hspoint, 3)
                    elif rNum > 2:
                        hspoint = hspoint + 2
                        hspoint = max(hspoint, 1)
                    elif rNum > 0:
                        hspoint = hspoint + 1
                        hspoint = max(hspoint, 0)
                elif highschooltype == '자사고광역':
                    if sNum > 5:
                        hspoint = 2
                    elif sNum > 3:
                        hspoint = 0
                    else:
                        hspoint = -5
                    if rNum > 5:
                        hspoint = hspoint + 3
                        hspoint = max(hspoint, 3)
                    elif rNum > 2:
                        hspoint = hspoint + 2
                        hspoint = max(hspoint, 1)
                    elif rNum > 0:
                        hspoint = hspoint + 1
                        hspoint = max(hspoint, 0)
                else:
                    if sNum >= 10:
                        hspoint = 2
                    elif sNum >= 6:
                        hspoint = 0
                    else:
                        hspoint = -5
                    if rNum > 5:
                        hspoint = hspoint + 3
                        hspoint = max(hspoint, 3)
                    elif rNum > 2:
                        hspoint = hspoint + 2
                        hspoint = max(hspoint, 1)
                    elif rNum > 0:
                        hspoint = hspoint + 1
                        hspoint = max(hspoint, 0)
            if hspoint != -9:
                return(hspoint)
        return (hspoint)


    def hscheck(self, year, region, highschooltype, highschool):
        # f1: sushi only, f2: sushi+jungsi
        f1name = '%s/config/data/%d/highschoolgrade.csv'%(os.getcwd(), year)
        f2name = '%s/config/data/%d/highschoolgrade2.csv'%(os.getcwd(), year)
            
        try:
            f1 = open(f1name, 'r')
        except:
            print 'file open error'
        content1 = f1.readlines()
        f1.close()
        lengthname = min(9, len(highschool))
        hspoint = -5
        for i in range(len(content1)):
            a1 = (content1[i]).split(',')
            if a1[0][:lengthname] == highschool[:lengthname]:
                if highschooltype == '일반고평준':
                    try:
                        if int(a1[1]) > 5:
                            hspoint = 3
                        elif int(a1[1]) > 2:
                            hspoint = 0
                        else:
                            hspoint = -5
                    except:
                        hspoint = -5
                elif highschooltype == '일반고비평준':
                    if int(a1[1]) > 5:
                        hspoint = 3
                    elif int(a1[1]) > 2:
                        hspoint = 0
                    else:
                        hspoint = -5
                elif highschooltype == '영재학교':
                    if int(a1[1]) > 50:
                        hspoint = 3
                    elif int(a1[1]) > 30:
                        hspoint = 0
                    else:
                        hspoint = -5
                elif highschooltype == '과학고':
                    if int(a1[1]) >= 15:
                        hspoint = 3
                    elif int(a1[1]) >= 8:
                        hspoint = 0
                    else:
                        hspoint = -5
                elif highschooltype == '외국어고' or highschooltype == '국제고' or highschooltype == '자사고전국':
                    if int(a1[1]) > 20:
                        hspoint = 3
                    elif int(a1[1]) > 10:
                        hspoint = 0
                    else:
                        hspoint = -5
                elif highschooltype == '자사고광역':
                    if int(a1[1]) > 5:
                        hspoint = 2
                    elif int(a1[1]) > 3:
                        hspoint = 0
                    else:
                        hspoint = -5
                else:
                    if int(a1[1]) >= 10:
                        hspoint = 2
                    elif int(a1[1]) >= 6:
                        hspoint = 0
                    else:
                        hspoint = -5
        
        try:
            f2 = open(f2name, 'r')
        except:
            print 'file open error'
        content2 = f2.readlines()
        f2.close()
        
        hspoint2 = -5
        for i in range(len(content2)):
            a2 = (content2[i]).split(',')
            if a2[0][:lengthname] == highschool[:lengthname]:
                if highschooltype == '일반고평준':
                    if int(a2[1]) > 5:
                        hspoint2 = 3
                    elif int(a2[1]) > 2:
                        hspoint2 = 0
                    else:
                        hspoint2 = -5
                elif highschooltype == '일반고비평준':
                    if int(a2[1]) > 5:
                        hspoint2 = 2
                    elif int(a2[1]) > 2:
                        hspoint2 = 0
                    else:
                        hspoint2 = -5
                elif highschooltype == '영재학교':
                    if int(a2[1]) > 50:
                        hspoint2 = 2
                    elif int(a2[1]) > 30:
                        hspoint2 = 0
                    else:
                        hspoint2 = -5
                elif highschooltype == '과학고':
                    if int(a2[1]) > 15:
                        hspoint2 = 2
                    elif int(a2[1]) > 8:
                        hspoint2 = 0
                    else:
                        hspoint2 = -5
                elif highschooltype == '외국어고' or highschooltype == '국제고' or highschooltype == '자사고전국':
                    if int(a2[1]) > 20:
                        hspoint2 = 2
                    elif int(a2[1]) > 10:
                        hspoint2 = 0
                    else:
                        hspoint2 = -5
                elif highschooltype == '자사고광역':
                    if int(a2[1]) > 10:
                        hspoint2 = 2
                    elif int(a2[1]) > 6:
                        hspoint2 = 0
                    else:
                        hspoint2 = -5
                else:        
                    if int(a2[1]) > 10:
                        hspoint = 2
                    elif int(a2[1]) > 6:
                        hspoint = 0
                    else:
                        hspoint = -5

        return max(hspoint, hspoint2)

    def getNumSemester(self, record_year, record_sem, record_grade):
        numsem = [] 
        for i in range(len(record_year)):
            if record_year[i] == 1 and record_sem[i] == 1:
                if record_grade[i] != 0:
                    numsem.append(1)
                else:
                    numsem.append(0)
            if record_year[i] == 1 and record_sem[i] == 2:
                if record_grade[i] != 0:
                    numsem.append(2)
                else:
                    numsem.append(0) 
            if record_year[i] == 2 and record_sem[i] == 1:
                if record_grade[i] != 0:
                    numsem.append(3)
                else:
                    numsem.append(0) 
            if record_year[i] == 2 and record_sem[i] == 2:
                if record_grade[i] != 0:
                    numsem.append(4)
                else:
                    numsem.append(0) 
            if record_year[i] == 3 and record_sem[i] == 1:
                if record_grade[i] != 0:
                    numsem.append(5)
                else:
                    numsem.append(0) 
            if record_year[i] == 3 and record_sem[i] == 2:
                if record_grade[i] != 0:
                    numsem.append(6)
                else:
                    numsem.append(0) 
        return (numsem)

    def getEnhGrade(self, score):
        if score > 8:
            gr = 1
            desc = '<BR>높은 수준'
            img = 'star5'
        elif score > 6:
            gr = 2
            desc = '비교적<BR>높은 수준'
            img = 'star4'
        elif score > 4:
            gr = 3
            desc = '<BR>보통 수준'
            img = 'star3'
        elif score >= 0:
            gr = 4
            desc = '비교적<BR>낮은 수준'
            img = 'star2'
        else:
            gr = 5
            desc = '<BR>낮은 수준'
            img = 'star1'
        return([gr, img, desc])

    def getTransScoreGHS(self, record_grade):
        # 1등급 4.3, 5 등급 3.0, 9등급 1.7로 기계적 환산
        tSc = []
        for i in record_grade:
            tSc.append( 5 - ((i-3.0) * 4/float(1.3)) )
        return (tSc)

    def getEnhScore(self, numsem, cumsem, record_cat, record_grade, record_unit, series, dep, opt):

        gapScore = [[8, -3, -6, -10, -15, -21, -28, -36, -45], [17, 6, -5, -9, -14, -20, -27, -35, -44], [24, 15, 4, -7, -12, -18, -25, -33, -42], [30, 21, 13, 2, -9, -15, -22, -30, -39], [35, 26, 18, 11, 0, -11, -18, 26, -35], [39, 30, 22, 15, 9, -2, -13, -21, -30], [42, 33, 25, 18, 12, 7, -4, -15, -24], [44, 35, 27, 20, 14, 9, 5, -6, -17], [45, 36, 28, 21, 15, 10, 6, 3, -8]]
        import numpy as np

        # opt 1: 주요교과 / opt2: 전체교과 / opt 3: 주요4교과 
        if opt == 1:
            if series == "이과":
                acat = ['수학', '과학']
            elif series == '문과':
                acat = ['국어', '영어', '수학', '사회']
            else:
                acat = ['국어', '영어', '사회']

            if dep.find('자유전공') != -1:
                acat = ['국어', '영어', '수학', '사회', '과학']
        
            if dep.find('수리과학') != -1 or dep.find('통계') != -1:
                acat = ['수학']

            if dep.find('건축') != -1:
                acat = ['국어', '영어', '수학']
        elif opt == 2:
            acat = ['국어', '영어', '수학', '사회', '과학', '기타']
        elif opt == 3:
            if series == '이과':
                acat = ['국어', '수학', '영어', '과학']
            elif series == '문과':
                acat = ['국어', '수학', '영어', '사회']
            elif series == '예체능':
                acat = ['국어', '영어', '사회']
            else:
                acat = ['국어', '수학', '영어', '사회', '과학']

        EnhScore = 0
        tsc = []
        tunit = []
        for i in range(1, numsem+1):
            ts = 0
            sc = 0
            unit = 0
            for i2 in range(len(record_unit)):
                for i3 in acat:
                    if i3 == record_cat[i2] and cumsem[i2] == i:
                        sc = sc + record_grade[i2]*record_unit[i2]
                        unit = unit + record_unit[i2]
            tsc.append(sc)
            tunit.append(unit)
        
        ttunit = []
        escore = []
        for i in range(2, len(tsc)+1):
            if tunit[i-2] != 0:
                prevSc = tsc[i-2]/float(tunit[i-2])
                presSc = tsc[i-1]/float(tunit[i-1])
                ttunit.append(tunit[i-1])
            
                r1 = int((prevSc*10 - int(prevSc)*10))/10.0
                r2 = int((presSc*10 - int(presSc)*10))/10.0
                p1 = gapScore[int(prevSc)-1][int(presSc)-1]
                p2 = gapScore[int(prevSc+1)-1][int(presSc)-1]
                p3 = gapScore[int(prevSc)-1][int(presSc+1)-1]
                p4 = gapScore[int(prevSc+1)-1][int(presSc+1)-1]
                escore.append(((p2-p1)*r1 + (p3-p1)*r2 + p1)*tunit[i-1])
        return(sum(escore)/float(sum(ttunit)))

    def getStdScore(self, raw, mean, std):
        try:
            return((raw-mean)/float(std))
        except:
            return(-999)

    def getGrStdScore(self, record_raw, record_mean, record_std, record_unit):
        score = 0
        notBlank = 0
        for i in range(len(record_mean)):
            if record_mean[i] >= 0:
                notBlank = 1
        if notBlank == 1:
            for i in range(len(record_unit)):
                score = score + self.getStdScore(record_raw[i], record_mean[i], record_std[i])*record_unit[i]
            try:
                return score/float(sum(record_unit))
            except:
                return (-999)
        else:
            return (-999)

    def transformGradeGHS(self, record_raw):
        record_grade = []
        for i in record_raw:
            if i == 'A+':
                record_grade.append(4.3)
            elif i == 'A0':
                record_grade.append(4.0)
            elif i == 'A-':
                record_grade.append(3.7)
            elif i == 'B+':
                record_grade.append(3.3)
            elif i == 'B0':
                record_grade.append(3.0)
            elif i == 'B-':
                record_grade.append(2.7)
            elif i == 'C+':
                record_grade.append(2.3)
            elif i == 'C0':
                record_grade.append(2.0)
            elif i == 'C-':
                record_grade.append(1.7)
            elif i == 'D+':
                record_grade.append(1.3)
            elif i == 'D0':
                record_grade.append(1.0)
            elif i == 'D-':
                record_grade.append(0.7)
            else:
                record_grade.append(0)
        return(record_grade)
