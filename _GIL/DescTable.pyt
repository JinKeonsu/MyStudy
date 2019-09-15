#!/usr/bin/python
# encoding=utf8

import sys, os
from string import split

from calcScore import calcScore
sca = calcScore()
from theme import ThemeConfig
s = ThemeConfig()

class DescTable:
    def __init__(self):
        pass

    def highschoolStat(self, highschool, region, username):

        year = 2020
        from calcScore import calcScore
        rc = calcScore()

        f1name = '%s/config/data/%d/highschool.xlsx'%(os.getcwd(), year)
        f2name = '%s/config/data/%d/highschool.xlsx'%(os.getcwd(), year-1)
        #f3name = '%s/config/data/%d/highschool.xlsx'%(os.getcwd(), year-2)

        import xlrd
        wi1 = xlrd.open_workbook(f1name)
        wis1 = wi1.sheet_by_index(0)

        wi2 = xlrd.open_workbook(f2name)
        wis2 = wi2.sheet_by_index(0)

        ncol1 = wis1.ncols
        nrow1 = wis1.nrows

        ncol2 = wis2.ncols
        nrow2 = wis2.nrows

        vs = []
        vr = []

        cue = 0
        for i in range(3, nrow1):
            hn = wis1.row_values(i)[0].encode('utf8')   #학교명
            rn = wis1.row_values(i)[1].encode('utf8')   #지역
            tn = wis1.row_values(i)[2].encode('utf8')   #고교 유형
            try:
                sNum = int(wis1.row_values(i)[3])       #수시 (합격자 수?)
            except:
                sNum = 0
            try:
                rNum = int(wis1.row_values(i)[4])       #정시 (합격자 수?)
            except:
                rNum = 0
            tNum = wis1.row_values(i)[5]                #합계(수시+정시)
            if hn.find(highschool) > -1 and rn.find(region) > -1:
                vs.append(sNum)
                vr.append(rNum)
                cue = 1
                break
        if cue == 0:
            vs.append(-1)
            vr.append(-1)

        cue = 0
        for i in range(3, nrow2):
            hn = wis2.row_values(i)[0].encode('utf8')
            rn = wis2.row_values(i)[1].encode('utf8')
            tn = wis2.row_values(i)[2].encode('utf8')
            try:
                sNum = int(wis2.row_values(i)[3])
            except:
                sNum = 0
            try:
                rNum = int(wis2.row_values(i)[4])
            except:
                rNum = 0
            tNum = wis2.row_values(i)[5]
            if hn.find(highschool) > -1 and rn.find(region) > -1:
                vs.append(sNum)
                vr.append(rNum)
                cue = 1
                break
        if cue == 0:
            vs.append(-1)
            vr.append(-1)

        bgcolor = s.bgcolor(1)
        bgcolor2 = s.bgcolor(1)
        print "<TABLE bgcolor=%s cellspacing=0 align=left>"%(bgcolor2)
        print "<TD><B>%s 최근 서울대 입결</B></TD>"%(highschool)
        print "<TR></TABLE>"
        print "<BR>"

        print "<table bgcolor=%s cellspacing=0 align=left style='width: 400px;'>"%(bgcolor)
        print """<TH align=center>학년도</TH><TH align=center width=30>수시</TH><TH align=center width=30>정시</TH><TH align=center width=30>총합</TH><TH align=center width=50>BigData</TH><TR>"""
        for i in range(2):
            print "<td align=center style='width: 30px;'>%d</TD>"%(year-i-1)
            if vs[i] == -1:
                print "<td align=center>-</TD>"
            else:
                print "<td align=center>%d</TD>"%(vs[i])    #수시 합격자 수
            if vr[i] == -1:
                print "<td align=center>-</TD>"
            else:
                print "<td align=center>%d</TD>"%(vr[i])    #정시 합격자 수
            if vs[i] == -1 and vr[i] == -1:
                print "<td align=center>-</TD>"
            else:
                print "<td align=center>%d</TD>"%(vs[i]+vr[i])
            print "<td align=center><a href='./highAppBig.cgi?year=%d&highschool=%s&region=%s&username=%s' target='_big'>[View]</a></td>"%(year-i-1, highschool, region, username)
            print "<TR>"
        print "</TABLE>"
        print '<BR>'
        return

    def descTbl_jsMemo(self, realname, memo):
        print """function memoShow() {
    wnd=window.open('data:text/html;charset=utf-8, ', '_blank', 'location=no,height=200,width=620,scrollbars=yes,status=no,titlebar=no');
    wnd.document.open();
    var string = '<html><head><title>%s</title></head><body>%s</body></html>';
    wnd.document.write(string);
    wnd.document.close();};
        """%(realname, memo)
        return

    def descTbl_jsRawScore(self, ry, rs, rc, rsb, rr, rm, rstd, rg, ru, rp, highschooltype):
        sbg = s.bgcolor(1)
        jstr = """<table cellspacing=0><td width = 30 align=center bgcolor=%s>학년</td><td align=center bgcolor=%s>학기</td><td align=center bgcolor=%s>교과</td><td align=center bgcolor=%s>과목</td><td align=center bgcolor=%s>단위</td><td align=center bgcolor=%s>점수</td><td align=center bgcolor=%s>평균</td><td align=center bgcolor=%s>편차</td><td align=center bgcolor=%s>등급</td><td align=center bgcolor=%s>재적인원</td><tr>"""%(sbg, sbg, sbg, sbg, sbg, sbg, sbg, sbg, sbg, sbg)

        pop = [1, 2, 4, 12, 13]
        for i in range(0, len(rsb)-1):
            if rsb[i] != '-9' and rsb[i] != '' and rsb[i] != None:
                if int(rs[i] == 1):
                    bc = "#aaaaaa"
                else:
                    bc = "#dddddd"

                jstr = jstr + "<td bgcolor=%s align=right>%d</td>"%(bc, ry[i])
                jstr = jstr + "<td bgcolor=%s align=right>%d</td>"%(bc, rs[i])
                jstr = jstr + "<td bgcolor=%s align=right>%s</td>"%(bc, rc[i])
                jstr = jstr + "<td bgcolor=%s align=right>%s</td>"%(bc, rsb[i])
                jstr = jstr + "<td bgcolor=%s align=center>%s</td>"%(bc, ru[i])
                if rr[i] != -9:
                    jstr = jstr + "<td bgcolor=%s align=right>%4.1f</td>"%(bc, rr[i])
                else:
                    jstr = jstr + "<td bgcolor=%s align=right></td>"%(bc)
                if rm[i] != -9:
                    jstr = jstr + "<td bgcolor=%s align=right>%4.1f</td>"%(bc, rm[i])
                else:
                    jstr = jstr + "<td bgcolor=%s align=right></td>"%(bc)
                if rstd[i] != -9:
                    jstr = jstr + "<td bgcolor=%s align=right>%4.1f</td>"%(bc, rstd[i])
                else:
                    jstr = jstr + "<td bgcolor=%s align=right></td>"%(bc)

                jstr = jstr + "<td bgcolor=%s align=center><font color=red>"%(bc)
                if highschooltype == "영재학교":
                    jstr = jstr + "%s</font></td>"%(rg[i])
                else:
                    jstr = jstr + "%s</font></td>"%(rg[i])

                jstr = jstr + "<td bgcolor=%s align=right>"%(bc)
                if rp[i] < 13:
                    suffix = '이내'
                else:
                    suffix = '이상'
                jstr = jstr + "%d명 %s</td><tr>"%(rp[i], suffix)
            else:
                pass
        jstr = jstr + "</table>"
        jstr = jstr + """</body></html>';"""

        print """function rawScore() {
            wnd=window.open('data:text/html;charset=utf-8, ', '_rawScore', 'directories=0, location=no,height=700,width=520,scrollbars=yes,status=no,titlebar=no');
    var string = '<html><head><title></title></head><body>%s"""%jstr
        print "wnd.document.open();"
        print """
        wnd.document.write(string);
        wnd.document.close();};
        """
        return

    def descTbl_Title(self, no, title):
        print "<table width=%d bgcolor=%s cellspacing=0 align=center>"%(s.width(1), s.bgcolor('title'))
        print "<td align=center>"
        print "<font color=%s>"%(s.fontcolor('title'))
        print "<H3>%s [%d]</h3>"%(title, no)
        print "</font>"
        print "</td>"
        print "</table>"
        return

    def descTbl_head_before(self, again, series, tseries, total_grade, total_grade31, total_244_grade, StdScore, EnhScore, Enh5Score, Enh4Score, main_grade_org, main_gradeh, main_cor244_grade, main_graden, main_gradea, rel_grade, main3_grade, main5_gradeh, main5_graden, main5_gradeh244, main5_graden244):
        if again == 'yes':
            print "<th id='myth' align=center bgcolor=%s width=100>전교과</Th><th id='myth' align=center bgcolor=%s width=100>전교과(5개학기)</th><th id='myth' align=center bgcolor=%s width=100>전교과244</th><th id='myth' align=center bgcolor=%s width=100>z score</th><th id='myth' align=center bgcolor=%s>주요교과 (보정/244)</th><th id='myth' align=center bgcolor=%s width=100>관련교과</th><th id='myth' align=center bgcolor=%s width=100>국영수</th>"%('#dddddd', '#dddddd', '#dddddd', '#dddddd', '#dddddd', '#dddddd','#dddddd')
        else:
            print "<th id='myth' align=center bgcolor=%s width=100>전교과</TD><th id='myth' align=center bgcolor=%s width=100>전교과244</th><th id='myth' align=center bgcolor=%s width=100>z score</th></th><th id='myth' align=center bgcolor=%s>주요교과 (보정/244)</th><th id='myth' align=center bgcolor=%s width=100>관련교과</th><th id='myth' align=center bgcolor=%s width=100>국영수</th>"%('#dddddd', '#dddddd', '#dddddd', '#dddddd', '#dddddd', '#dddddd')
        print "<th id='myth' align=center bgcolor=%s width=100>%s</th>"%('#dddddd', '국영수사(244)')
        if series != '예체능':
            print "<th id='myth' align=center bgcolor=%s width=100>%s</th>"%('#dddddd', '국영수과(244)')
        else:
            print "<th id='myth' align=center bgcolor=%s width=100>%s</th>"%('#dddddd', '국영사')
        print "<th id='myth' align=center bgcolor=%s width=200>향상도(주요/전체/%s)</th>"%('#dddddd', tseries)
        print "<TR>"

        print "<td align=center>%4.2f</td>"%(total_grade)
        if again == 'yes':
            print "<td align=center>%4.2f</td>"%(total_grade31)
        print "<td align=center>%4.2f</td>"%(total_244_grade)
        try:
            if StdScore != -999:
                print "<td align=center>%4.3f</td>"%(StdScore)
            else:
                print "<td align=center>미입력</td>"
        except:
            print "<td align=center>미입력</td>"


        if len(series) != 0:
            if series == '문과':
                print "<td align=center>%4.2f (%4.2f/%4.2f)</td>"%(main_grade_org, main_gradeh, main_cor244_grade)
            elif series == '이과':
                print "<td align=center>%4.2f (%4.2f/%4.2f)</td>"%(main_grade_org, main_graden, main_cor244_grade)
            else:
                print "<td align=center>%4.2f (%4.2f/%4.2f)</td>"%(main_grade_org, main_gradea, main_cor244_grade)
        else:
            print "<td></TD>"

        if rel_grade == 0:
            print "<TD align=center>%s</td>"%('')
        else:
            print "<td align=center>%4.2f</td>"%(rel_grade)

        print "<td align=center>%4.2f</td>"%(main3_grade)
        print "<TD align=center>%4.2f(%4.2f)</td>"%(main5_gradeh, main5_gradeh244)
        print "<TD align=center>%4.2f(%4.2f)</td>"%(main5_graden, main5_graden244)
        try:
            print "<td align=center>%4.2f/%4.2f/%4.2f</td>"%(EnhScore, Enh5Score, Enh4Score)
        except:
            pass
        #if series != '예체능':
        #    print "<TD align=center>%4.2f</td><TR>"%(main5_graden)
        #else:
        #    print "<TD align=center>%4.2f</td><TR>"%(main5_gradea)
        print "<TR></table>"
        return


    def descTbl_head1(self, record_cat, record_sub, record_year, record_sem, record_grade, record_unit, series, dep, tseries, total_grade, main_grade_org, Enh4Score, Enh5Score):

        sc1 = "%4.2f"%sca.getYearGrade(1, record_year, record_grade, record_unit)
        sc2 = "%4.2f"%sca.getYearGrade(2, record_year, record_grade, record_unit)
        sc3 = "%4.2f"%sca.getYearGrade(3, record_year, record_grade, record_unit)

        sc11 = "%4.2f"%sca.getSemGrade(1, 1, record_year, record_sem, record_grade, record_unit)
        sc21 = "%4.2f"%sca.getSemGrade(2, 1, record_year, record_sem, record_grade, record_unit)
        sc31 = "%4.2f"%sca.getSemGrade(3, 1, record_year, record_sem, record_grade, record_unit)

        sc12 = "%4.2f"%sca.getSemGrade(1, 2, record_year, record_sem, record_grade, record_unit)
        sc22 = "%4.2f"%sca.getSemGrade(2, 2, record_year, record_sem, record_grade, record_unit)
        sc32 = "%4.2f"%sca.getSemGrade(3, 2, record_year, record_sem, record_grade, record_unit)

        s5c1 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 0)
        s5c11 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 1)
        s5c12 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 2)

        s5c2 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 0)
        s5c21 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 1)
        s5c22 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 2)

        s5c3 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 0)
        s5c31 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 1)
        s5c32 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 2)

        if sc1 == "0.00":
            sc1 = ""
        if sc11 == "0.00":
            sc11 = ""
        if sc12 == "0.00":
            sc12 = ""
        if sc2 == "0.00":
            sc2 = ""
        if sc21 == "0.00":
            sc21 = ""
        if sc22 == "0.00":
            sc22 = ""
        if sc3 == "0.00":
            sc3 = ""
        if sc31 == "0.00":
            sc31 = ""
        if sc32 == "0.00":
            sc32 = ""
        if s5c1 == "0.00":
            s5c1 = ""
        if s5c11 == "0.00":
            s5c11 = ""
        if s5c12 == "0.00":
            s5c12 = ""
        if s5c2 == "0.00":
            s5c2 = ""
        if s5c21 == "0.00":
            s5c21 = ""
        if s5c22 == "0.00":
            s5c22 = ""
        if s5c3 == "0.00":
            s5c3 = ""
        if s5c31 == "0.00":
            s5c31 = ""
        if s5c32 == "0.00":
            s5c32 = ""

        eRes = sca.getEnhGrade(Enh4Score)
        Enh4Grade = eRes[0]
        eg4Img = eRes[1]
        e4Desc = eRes[2]

        eRes = sca.getEnhGrade(Enh5Score)
        Enh5Grade = eRes[0]
        eg5Img = eRes[1]
        e5Desc = eRes[2]

        print "<table width=%d bgcolor=%s cellspacing=0 align=center border=1 frame=void rules=rows>"%(s.width(1), s.bgcolor(2))
        print """<th id='myth' align=center bgcolor=%s width=150>지표<a onclick="rawScore();">[원자료]</a></th>"""%('#dddddd')
        print "<th id='myth' align=center bgcolor=%s width=100>평균(과목수)</th><th id='myth' align=center bgcolor=%s width=120>1학년</th><th id='myth' align=center bgcolor=%s width=120>2학년</th><th id='myth' align=center bgcolor=%s width=120>3학년</th><th id='myth' align=center bgcolor=%s colspan='2'>향상도</th>"%('#dddddd', '#dddddd', '#dddddd', '#dddddd', '#dddddd')
        print "<TR>"
        print """<TD align=center>전체교과</td><td align=center><B>%4.2f</B></td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><td align=center width=80 rowspan="13"><B>전체교과</B><BR>%s<BR><BR><img src=./images/%s.png width=50></td><td align=center width=80 rowspan="13"><B>%s</B><BR>%s<BR><BR><img src=./images/%s.png width=50></td></TR>"""%(total_grade, sc1, sc11, sc12, sc2, sc21, sc22, sc3, sc31, sc32, e5Desc, eg5Img, tseries, e4Desc, eg4Img)

        t1 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 0)
        t11 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 1)
        t12 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 2)
        t2 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 0)
        t21 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 1)
        t22 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 2)
        t3 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 0)
        t31 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 1)
        t32 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 2)

        if t1 == "0.00":
            t1 = ""
        if t11 == "0.00":
            t11 = ""
        if t12 == "0.00":
            t12 = ""
        if t2 == "0.00":
            t2 = ""
        if t21 == "0.00":
            t21 = ""
        if t22 == "0.00":
            t22 = ""
        if t3 == "0.00":
            t3 = ""
        if t31 == "0.00":
            t31 = ""
        if t32 == "0.00":
            t32 = ""

        if len(series) != 0:
            print "<TD align=center>주요교과</td><td align=center><B>%4.2f</B></td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><TR>"%(main_grade_org, t1, t11, t12, t2, t21, t22, t3, t31, t32)
        else:
            print "<TD align=center>주요교과</td><td align=center></td><td align=center>[/]</td><td align=center>[/]</td><td align=center>[/]</td><TR>"

        t1 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 1, 0)
        t11 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 1, 1)
        t12 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 1, 2)
        t2 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 2, 0)
        t21 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 2, 1)
        t22 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 2, 2)
        t3 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 3, 0)
        t31 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 3, 1)
        t32 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 3, 2)
        if t1 == "0.00":
            t1 = ""
        if t11 == "0.00":
            t11 = ""
        if t12 == "0.00":
            t12 = ""
        if t2 == "0.00":
            t2 = ""
        if t21 == "0.00":
            t21 = ""
        if t22 == "0.00":
            t22 = ""
        if t3 == "0.00":
            t3 = ""
        if t31 == "0.00":
            t31 = ""
        if t32 == "0.00":
            t32 = ""

        return

    # for report (with view.cgi)
    def descTbl_head2(self, no, record_cat, record_sub, record_year, record_sem, record_grade, record_unit, series, dep, tseries, total_grade, main_grade_org, Enh4Score, Enh5Score):

        sc1 = "%4.2f"%sca.getYearGrade(1, record_year, record_grade, record_unit)
        sc2 = "%4.2f"%sca.getYearGrade(2, record_year, record_grade, record_unit)
        sc3 = "%4.2f"%sca.getYearGrade(3, record_year, record_grade, record_unit)

        sc11 = "%4.2f"%sca.getSemGrade(1, 1, record_year, record_sem, record_grade, record_unit)
        sc21 = "%4.2f"%sca.getSemGrade(2, 1, record_year, record_sem, record_grade, record_unit)
        sc31 = "%4.2f"%sca.getSemGrade(3, 1, record_year, record_sem, record_grade, record_unit)

        sc12 = "%4.2f"%sca.getSemGrade(1, 2, record_year, record_sem, record_grade, record_unit)
        sc22 = "%4.2f"%sca.getSemGrade(2, 2, record_year, record_sem, record_grade, record_unit)
        sc32 = "%4.2f"%sca.getSemGrade(3, 2, record_year, record_sem, record_grade, record_unit)

        s5c1 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 0)
        s5c11 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 1)
        s5c12 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 2)

        s5c2 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 0)
        s5c21 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 1)
        s5c22 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 2)

        s5c3 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 0)
        s5c31 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 1)
        s5c32 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 2)

        rlabel = "1|2|3"
        score1Lst = "%s|%s|%s"%(sc1, sc2, sc3)
        score2Lst = "%s|%s|%s"%(s5c1, s5c2, s5c3)

        if sc1 == "0.00":
            sc1 = ""
        if sc11 == "0.00":
            sc11 = ""
        if sc12 == "0.00":
            sc12 = ""
        if sc2 == "0.00":
            sc2 = ""
        if sc21 == "0.00":
            sc21 = ""
        if sc22 == "0.00":
            sc22 = ""
        if sc3 == "0.00":
            sc3 = ""
        if sc31 == "0.00":
            sc31 = ""
        if sc32 == "0.00":
            sc32 = ""
        if s5c1 == "0.00":
            s5c1 = ""
        if s5c11 == "0.00":
            s5c11 = ""
        if s5c12 == "0.00":
            s5c12 = ""
        if s5c2 == "0.00":
            s5c2 = ""
        if s5c21 == "0.00":
            s5c21 = ""
        if s5c22 == "0.00":
            s5c22 = ""
        if s5c3 == "0.00":
            s5c3 = ""
        if s5c31 == "0.00":
            s5c31 = ""
        if s5c32 == "0.00":
            s5c32 = ""

        #eRes = sca.getEnhGrade(Enh4Score)
        #Enh4Grade = eRes[0]
        #eg4Img = eRes[1]
        #e4Desc = eRes[2]

        #eRes = sca.getEnhGrade(Enh5Score)
        #Enh5Grade = eRes[0]
        #eg5Img = eRes[1]
        #e5Desc = eRes[2]
        print """<TD align=center>전체교과</td><td align=center><B>%4.2f</B></td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><td align=center rowspan="16">&nbsp;&nbsp;<img src='./view.cgi?no=%d&index=%s&opt1=%s&opt2=%s&series=%s' width=250></td></TR>"""%(total_grade, sc1, sc11, sc12, sc2, sc21, sc22, sc3, sc31, sc32, no, rlabel, score1Lst, score2Lst, tseries)

        t1 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 0)
        t11 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 1)
        t12 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 2)
        t2 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 0)
        t21 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 1)
        t22 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 2)
        t3 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 0)
        t31 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 1)
        t32 = "%4.2f"%sca.getYearMainGrade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 2)

        if t1 == "0.00":
            t1 = ""
        if t11 == "0.00":
            t11 = ""
        if t12 == "0.00":
            t12 = ""
        if t2 == "0.00":
            t2 = ""
        if t21 == "0.00":
            t21 = ""
        if t22 == "0.00":
            t22 = ""
        if t3 == "0.00":
            t3 = ""
        if t31 == "0.00":
            t31 = ""
        if t32 == "0.00":
            t32 = ""

        if len(series) != 0:
            print "<TD align=center>주요교과</td><td align=center><B>%4.2f</B></td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><TR>"%(main_grade_org, t1, t11, t12, t2, t21, t22, t3, t31, t32)
        else:
            print "<TD align=center>주요교과</td><td align=center></td><td align=center>[/]</td><td align=center>[/]</td><td align=center>[/]</td><TR>"
        #print "<TD align=center>주요교과</td><td align=center><B>%4.2f</B></td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><TR>"%(main_grade_org, t1, t11, t12, t2, t21, t22, t3, t31, t32)

        t1 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 1, 0)
        t11 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 1, 1)
        t12 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 1, 2)
        t2 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 2, 0)
        t21 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 2, 1)
        t22 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 2, 2)
        t3 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 3, 0)
        t31 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 3, 1)
        t32 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 3, 2)
        if t1 == "0.00":
            t1 = ""
        if t11 == "0.00":
            t11 = ""
        if t12 == "0.00":
            t12 = ""
        if t2 == "0.00":
            t2 = ""
        if t21 == "0.00":
            t21 = ""
        if t22 == "0.00":
            t22 = ""
        if t3 == "0.00":
            t3 = ""
        if t31 == "0.00":
            t31 = ""
        if t32 == "0.00":
            t32 = ""

        return



    def descTbl_rel(self, rel_grade, record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem):

        t1 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 1, 0)
        t11 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 1, 1)
        t12 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 1, 2)
        t2 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 2, 0)
        t21 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 2, 1)
        t22 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 2, 2)
        t3 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 3, 0)
        t31 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 3, 1)
        t32 = "%4.2f"%sca.getRelGrade(record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem, 3, 2)
        if t1 == "0.00":
            t1 = ""
        if t11 == "0.00":
            t11 = ""
        if t12 == "0.00":
            t12 = ""
        if t2 == "0.00":
            t2 = ""
        if t21 == "0.00":
            t21 = ""
        if t22 == "0.00":
            t22 = ""
        if t3 == "0.00":
            t3 = ""
        if t31 == "0.00":
            t31 = ""
        if t32 == "0.00":
            t32 = ""
#
        if rel_grade == 0:
            t0 = ""
        else:
            t0 = "%4.2f"%rel_grade
        print "<TD align=center>관련교과</td><td align=center><B>%s</B></Td><Td align=center>%s [%s/%s]</TD><Td align=center>%s [%s/%s]</TD><Td align=center>%s [%s/%s]</TD><TR>"%(t0, t1, t11, t12, t2, t21, t22, t3, t31, t32)

        return

    def descTbl_main3(self, main3_grade, record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem):

        main3_1_grade = "%4.2f"%sca.getMain3Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 0)
        main3_11_grade = "%4.2f"%sca.getMain3Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 1)
        main3_12_grade = "%4.2f"%sca.getMain3Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 2)
        main3_2_grade = "%4.2f"%sca.getMain3Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 0)
        main3_21_grade = "%4.2f"%sca.getMain3Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 1)
        main3_22_grade = "%4.2f"%sca.getMain3Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 2)
        main3_3_grade = "%4.2f"%sca.getMain3Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 0)
        main3_31_grade = "%4.2f"%sca.getMain3Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 1)
        main3_32_grade = "%4.2f"%sca.getMain3Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 2)

        if main3_1_grade == "0.00":
            main3_1_grade = ""
        if main3_11_grade == "0.00":
            main3_11_grade = ""
        if main3_12_grade == "0.00":
            main3_12_grade = ""
        if main3_2_grade == "0.00":
            main3_2_grade = ""
        if main3_21_grade == "0.00":
            main3_21_grade = ""
        if main3_22_grade == "0.00":
            main3_22_grade = ""
        if main3_3_grade == "0.00":
            main3_3_grade = ""
        if main3_31_grade == "0.00":
            main3_31_grade = ""
        if main3_32_grade == "0.00":
            main3_32_grade = ""
        print "<TD align=center>국영수</td><td align=center><B>%4.2f</B></td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><TR>"%(main3_grade, main3_1_grade, main3_11_grade, main3_12_grade, main3_2_grade, main3_21_grade, main3_22_grade, main3_3_grade, main3_31_grade, main3_32_grade)
        return

    def descTbl_main5(self, main5_grade, record_grade, record_unit, series, dep, record_cat, record_sub, record_year, record_sem):

        t1 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 0)
        t11 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 1)
        t12 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 1, 2)
        t2 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 0)
        t21 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 1)
        t22 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 2, 2)
        t3 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 0)
        t31 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 1)
        t32 = "%4.2f"%sca.getMain5Grade(record_grade, record_unit, series, dep, record_cat, record_year, record_sem, 3, 2)
        if t1 == "0.00":
            t1 = ""
        if t11 == "0.00":
            t11 = ""
        if t12 == "0.00":
            t12 = ""
        if t2 == "0.00":
            t2 = ""
        if t21 == "0.00":
            t21 = ""
        if t22 == "0.00":
            t22 = ""
        if t3 == "0.00":
            t3 = ""
        if t31 == "0.00":
            t31 = ""
        if t32 == "0.00":
            t32 = ""
        if series == '문과':
            txt = '국영수사'
        elif series == '이과':
            txt = '국영수과'
        elif series == '예체능':
            txt = '국영사'

        print "<TD align=center>%s</td><td align=center><B>%4.2f</B></td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><TR>"%(txt, main5_grade, t1, t11, t12, t2, t21, t22, t3, t31, t32)

        return


    def descTbl_Sub(self, sub, record_cat, record_grade, record_unit, record_year, record_sem):

        for i in sub:
            t1 = "%4.2f"%sca.getSubjYearGrade(i, record_cat, record_grade, record_unit, record_year, record_sem, 1, 0)
            t11 = "%4.2f"%sca.getSubjYearGrade(i, record_cat, record_grade, record_unit, record_year, record_sem, 1, 1)
            t12 = "%4.2f"%sca.getSubjYearGrade(i, record_cat, record_grade, record_unit, record_year, record_sem, 1, 2)
            t2 = "%4.2f"%sca.getSubjYearGrade(i, record_cat, record_grade, record_unit, record_year, record_sem, 2, 0)
            t21 = "%4.2f"%sca.getSubjYearGrade(i, record_cat, record_grade, record_unit, record_year, record_sem, 2, 1)
            t22 = "%4.2f"%sca.getSubjYearGrade(i, record_cat, record_grade, record_unit, record_year, record_sem, 2, 2)
            t3 = "%4.2f"%sca.getSubjYearGrade(i, record_cat, record_grade, record_unit, record_year, record_sem, 3, 0)
            t31 = "%4.2f"%sca.getSubjYearGrade(i, record_cat, record_grade, record_unit, record_year, record_sem, 3, 1)
            t32 = "%4.2f"%sca.getSubjYearGrade(i, record_cat, record_grade, record_unit, record_year, record_sem, 3, 2)
            if t1 == "0.00":
                t1 = ""
            if t11 == "0.00":
                t11 = ""
            if t12 == "0.00":
                t12 = ""
            if t2 == "0.00":
                t2 = ""
            if t21 == "0.00":
                t21 = ""
            if t22 == "0.00":
                t22 = ""
            if t3 == "0.00":
                t3 = ""
            if t31 == "0.00":
                t31 = ""
            if t32 == "0.00":
                t32 = ""
            print "<TD align=center>%s</td><td align=center><B>%4.2f(%d)</B></td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><TR>"%(i, sca.getSubjGrade(i, record_cat, record_grade, record_unit), sca.getSubjNum(record_cat, record_unit, i), t1, t11, t12, t2, t21, t22, t3, t31, t32)
        return


    def descTbl_ISub(self, sub, record_sub, record_grade, record_unit, record_year, record_sem):
        for i in sub:
            t1 = "%4.2f"%sca.getISubjYearGrade(i, record_sub, record_grade, record_unit, record_year, record_sem, 1, 0)
            t11 = "%4.2f"%sca.getISubjYearGrade(i, record_sub, record_grade, record_unit, record_year, record_sem, 1, 1)
            t12 = "%4.2f"%sca.getISubjYearGrade(i, record_sub, record_grade, record_unit, record_year, record_sem, 1, 2)
            t2 = "%4.2f"%sca.getISubjYearGrade(i, record_sub, record_grade, record_unit, record_year, record_sem, 2, 0)
            t21 = "%4.2f"%sca.getISubjYearGrade(i, record_sub, record_grade, record_unit, record_year, record_sem, 2, 1)
            t22 = "%4.2f"%sca.getISubjYearGrade(i, record_sub, record_grade, record_unit, record_year, record_sem, 2, 2)
            t3 = "%4.2f"%sca.getISubjYearGrade(i, record_sub, record_grade, record_unit, record_year, record_sem, 3, 0)
            t31 = "%4.2f"%sca.getISubjYearGrade(i, record_sub, record_grade, record_unit, record_year, record_sem, 3, 1)
            t32 = "%4.2f"%sca.getISubjYearGrade(i, record_sub, record_grade, record_unit, record_year, record_sem, 3, 2)
            if t1 == "0.00":
                t1 = ""
            if t11 == "0.00":
                t11 = ""
            if t12 == "0.00":
                t12 = ""
            if t2 == "0.00":
                t2 = ""
            if t21 == "0.00":
                t21 = ""
            if t22 == "0.00":
                t22 = ""
            if t3 == "0.00":
                t3 = ""
            if t31 == "0.00":
                t31 = ""
            if t32 == "0.00":
                t32 = ""
            print "<TD align=center>%s</td><td align=center><B>%4.2f(%d)</B></td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><td align=center>%s [%s/%s]</td><TR>"%(i, sca.getISubjGrade(i, record_sub, record_grade, record_unit), sca.getISubjNum(record_sub, record_unit, i), t1, t11, t12, t2, t21, t22, t3, t31, t32)
        return

    def descActHeader(self, a, b, c):

        print "<TABLE width=%d bgcolor=%s cellspacing=0 align=center border=1 frame=void rules=rows>"%(a, b)
        print "<td align=center bgcolor=%s><B>교과외 영역 요약</B></TD><TR>"%(c)
        print "</Table>"

        print "<TABLE width=%d bgcolor=%s cellspacing=0 align=center border=1 frame=void rules=rows>"%(a, b)
        return

    def descAwardContent(self, k):

        # 수상실적
        award_name = k[19].encode('utf8')
        award_grade = k[20].encode('utf8')
        award_check = k[37].encode('utf8')
        award_year = k[45].encode('utf8')
        an = award_name.split('|')
        ag = award_grade.split('|')
        ah = award_check.split('|')
        try:
            ay = award_year.split('|')
        except:
            award_year = '||||||||||'
            ay = award_year.split('|')

        print "<TD valign=top width=50% style='max-height:12px'><B>수상실적</B><BR>"
        if len(an) == len(ah):
            for i in range(len(an)):
                if an[i] != "-9" and an[i] != '' and ah[i] == "on":
                    print "%s학년 %s %s 등<BR>"%(ay[i], an[i], ag[i])
        else:
            for i in range(len(an)):
                if an[i] != "-9" :
                    print "%s학년 %s %s 등<BR>"%(ay[i], an[i], ag[i])

        print "</TD>"
        return


    def descActContent(self, k):

        if k[115] != None:
            activity_subcat = k[115].encode('utf8')
        else:
            activity_subcat = "|||||||||"

        activity_name = k[22].encode('utf8')
        activity_time = k[23].encode('utf8')
        activity_check = k[38].encode('utf8')
        asc = activity_subcat.split('|')
        an = activity_name.split('|')
        ag = activity_time.split('|')
        ah = activity_check.split('|')

        print "<TD valign=top style='max-height:12px'><B>교내외활동</B><BR>"
        if len(an) == len(ah):
            for i in range(len(an)):
                if an[i] != "-9"  and an[i] != '' and ah[i] == 'on' and asc[i] == '':
                    print "%s 기간: %s 학기<BR>"%(an[i], ag[i])
            for i in range(len(an)):
                if an[i] != "-9"  and an[i] != '' and ah[i] == 'on' and asc[i] == '동아리':
                    print "<B>[%s]</B>%s 기간: %s 학기<BR>"%(asc[i], an[i], ag[i])
            for i in range(len(an)):
                if an[i] != "-9"  and an[i] != '' and ah[i] == 'on' and asc[i] == '진로/자율':
                    print "<B>[%s]</B>%s 기간: %s 학기<BR>"%(asc[i], an[i], ag[i])
            for i in range(len(an)):
                if an[i] != "-9"  and an[i] != '' and ah[i] == 'on' and asc[i] == '세특':
                    print "<B>[%s]</B>%s 기간: %s 학기<BR>"%(asc[i], an[i], ag[i])
            for i in range(len(an)):
                if an[i] != "-9"  and an[i] != '' and ah[i] == 'on' and asc[i] == '기타':
                    print "<B>[%s]</B>%s 기간: %s 학기<BR>"%(asc[i], an[i], ag[i])
        else:
            for i in range(len(an)):
                if an[i] != "-9":
                    print "%s 기간: %s 학기<BR>"%(an[i], ag[i])

        print "</TD>"

        return

    def descServiceContent(self, k):
        service_cat = k[24].encode('utf8')
        service_name = k[25].encode('utf8')
        service_time = k[26].encode('utf8')
        service_check = k[39].encode('utf8')
        sc = service_cat.split('|')
        sn = service_name.split('|')
        st = service_time.split('|')
        sh = service_check.split('|')

        if k[48] != -9 and k[48] != None:
            print "<TD valign=top><b>봉사활동</B> [총시수: %d]<BR>"%(k[48])
        else:
            print "<TD valign=top><b>봉사활동</B> [총시수: 미기재]<BR>"

        if len(sn) == len(sh):
            for i in range(len(sn)):
                if sn[i] != "-9" and sn[i] != '' and sh[i] == 'on':
                    print "%s %s 시수:%s<BR>"%(sc[i], sn[i], st[i])
        else:
            for i in range(len(sn)):
                if sn[i] != "-9" and sn[i] != '' :
                    print "%s %s 시수:%s<BR>"%(sc[i], sn[i], st[i])
        print "</TD>"
        return

    def descLeadershipContent(self, k):
        leadership_cat = k[27].encode('utf8')
        leadership_time = k[28].encode('utf8')
        leadership_check = k[40].encode('utf8')
        lc = leadership_cat.split('|')
        lt = leadership_time.split('|')
        lh = leadership_check.split('|')

        print "<TD valign=top><B>리더십</B><BR>"
        for i in range(len(lh)):
            if lh[i] == u'on':
                if lt[i] == "0" or lt[i] == '' or lc[i] == '무':
                    pass
                else:
                    print "%s %s 학기<BR>"%(lc[i], lt[i])

        print "</TD>"
        return
