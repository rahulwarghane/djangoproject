from app1.models import Student

from django.db.models import Q, F

# exec(open(r"C:\Users\wargh\Desktop\codefiles\DJANGO2\djangoproject\firstproject\app1\db_shell.py").read())
# all_studs = Student.objects.all()
# for stud in all_studs:
#     # print(stud.name ,stud.marks )
#     print(stud.show_details())

# stud_obj = Student.objects.filter(name = "Abhimanyu")
# print(stud_obj)
# stud= Student.objects.get(id=10)
# stud.name="XYZ"
# stud.save()


# stud = Student.objects.values_list()
# for i in stud:
#     print(i)

# stud= Student.objects.first()
# print(stud)
# print(Student.objects.count())

# Records = Student.objects.filter(name__startswith = "R")
# print(Records)

# print(Student.objects.exclude(address = "Pune"))

# s2 =  Student(name = "Swapnil" , marks = 36 , age = 35, address = "Jalandar" )
# s3 = Student(name = "Mno" , marks = 26 , age = 25, address = "Sambhaji nagar" )
# s2.save()
# s3.save()
# Student.objects.create(name = "Abhimanyu" , marks = 92 , age = 22, address = "Mathura" )
# Student.objects.create(name = "Arjun" , marks = 98 , age = 35, address = "Ayodhya" )

# Bulk create 
# s1 = Student(name = "A" , marks = 36 , age = 52, address = "Adr1" )
# s2 = Student(name = "B" , marks = 32 , age = 29, address = "Adr2" )
# s3 = Student(name = "C" , marks = 39 , age = 21, address = "Adr3" )
# s4 = Student(name = "D" , marks = 31 , age = 26, address = "Adr4" )
# Student.objects.bulk_create([s1,s2,s3, s4])


# data = Student.objects.filter(Q(marks__gt = 20) & Q(marks__lt = 80))
# print(data)
# Student.objects.all().update(marks= F("marks")+5)

# q1 = Student.objects.filter(age__lt = 60)
# q2 = Student.objects.filter(age__gt = 40)
# result = (q1).union(q2)
# print(result)

# import openpyxl
# wb = openpyxl.load_workbook(r"C:\Users\wargh\Desktop\codefiles\DJANGO2\djangoproject\firstproject\Sample_project.xlsx")
# sheet = wb.active
# priexec(open(r"C:\Users\wargh\Desktop\codefiles\DJANGO2\djangoproject\firstproject\app1\db_shell.py").read())nt(sheet.max_row)

# lst = []
# for i in range (2,sheet.max_row+1):
#     nm = sheet.cell(row=i,column=1).value
#     mrk = sheet.cell(row=i,column=2).value
#     adr = sheet.cell(row=i,column=3).value
#     ag = sheet.cell(row=i,column=4).value
    
#     obj = Student(name = nm , marks = mrk , address = adr , age = ag)
#     lst.append(obj)

# Student.objects.bulk_create(lst)    

# data = Student.objects.raw(" select * from student")
# for i in data:
#     print(i.__dict__)

from django.db import connection

# cursor = connection.cursor()
# cursor.execute("select * from student where name= 'A'")
# data = cursor.fetchall() 
# print(data)