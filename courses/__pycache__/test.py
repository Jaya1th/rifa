import requests
import json  
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.db.models import Q 
import datetime
from django.core.management.base import BaseCommand
import mysql.connector
from django.conf import settings
from genesis_psd.models import Genesis_Psd_Dashboard, Course_schedule, History
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        mydb = mysql.connector.connect(
            host='kpitacademysql.kpit.com',
            database='openedx_prd', 
            user ='openedxprduser',
            password ='OpEn5DxP@dU5ER', 
            port ='3309' 
        )
        print("Connection Status: ", mydb.is_connected())  
        progress_cursor = mydb.cursor() 
        #get users enrolled in current batch 
        latest_batch = Genesis_Psd_Dashboard.objects.latest('batch') 
        batch_no = latest_batch.batch
        print(batch_no)
        users_enrolled = Genesis_Psd_Dashboard.objects.filter(batch = batch_no).exclude(is_deleted=1)
        #get course schedule
        batch_schedule = Course_schedule.objects.filter(batch= batch_no)
        print(batch_schedule)
        CE_start_date = batch_schedule[0].CE_start_date
        CE_end_date = batch_schedule[0].CE_end_date
        BE_end_date = batch_schedule[0].BE_end_date
        EE_end_date = batch_schedule[0].EE_end_date
        MM_end_date = batch_schedule[0].MM_end_date
        TM_end_date = batch_schedule[0].TM_end_date
        for user in users_enrolled: 
            emp_id = int(user.emp_id)
            #BE
            BE_course_progress_query = "SELECT * FROM openedx_prd.student_courseenrollment WHERE course_id = 'course-v1:KPITedu+EDUPSDIF1012+2020' and employee_id = %s" 
            progress_cursor.execute(BE_course_progress_query,(emp_id,))
            BE_course_progress = progress_cursor.fetchall()  
            if(BE_course_progress): 
                if(BE_course_progress[0][6] ==None): 
                    user.BE_progress = 0.0 
                    user.save() 
                else: 
                    user.BE_progress = BE_course_progress[0][6]
                    user.save() 
            else: 
                user.BE_progress = 0.0 
                user.save()
            
            #CE
            CE_course_progress_query = "SELECT * FROM openedx_prd.student_courseenrollment WHERE course_id = 'course-v1:KPITedu+EDUPSD1F1011+2021' and employee_id = %s" 
            progress_cursor.execute(CE_course_progress_query,(emp_id,))
            CE_course_progress = progress_cursor.fetchall()  
            if(CE_course_progress): 
                if(CE_course_progress[0][6] ==None): 
                    user.CE_progress = 0.0 
                    user.save() 
                else: 
                    user.CE_progress = CE_course_progress[0][6]
                    user.save() 
            else: 
                user.CE_progress = 0.0 
                user.save()
            #EE
            EE_course_progress_query = "SELECT * FROM openedx_prd.student_courseenrollment WHERE course_id = 'course-v1:KPIT+EDUPSD1023+2023' and employee_id = %s" 
            progress_cursor.execute(EE_course_progress_query,(emp_id,))
            EE_course_progress = progress_cursor.fetchall()  
            if(EE_course_progress): 
                if(EE_course_progress[0][6] ==None): 
                    user.EE_progress = 0.0 
                    user.save() 
                else: 
                    user.EE_progress = 
