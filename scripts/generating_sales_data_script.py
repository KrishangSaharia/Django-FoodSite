from xlwt import Workbook
from transaction.models import Transaction 
from django.utils import timezone


book=Workbook()
sheet=book.add_sheet(str(timezone.now()))


row_num=0

columns=['Oder Date and Time','Ordered By','Amount']

for col_num in range(len(columns)):
	sheet.write(row_num,col_num,columns[col_num])

rows=Transaction.objects.all().value_list('user','date_created','amount')


row_num+=1 #For leaving a space between Headers and Sales Data

font_style=xlwt.XFStyle()

for row in rows:
	row_num+=1
	for col_num in range(len(columns)):
		sheet.write(row_num,col_num,row[col_num],font_style)




book.save()



