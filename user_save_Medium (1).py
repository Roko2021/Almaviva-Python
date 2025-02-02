import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
import schedule


conn = sqlite3.connect("Visitor.db")
db = conn.cursor()
# إعداد الخيارات

def enter_infomation1():
        
    def run_script():
        # print(speed)
        # print(speed_load_choose)
        # print(speed_load_element)
        

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)  # خيار لإبقاء المتصفح مفتوحًا بعد انتهاء البرنامج
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        # # فتح الموقع
        url = "https://egyiam.almaviva-visa.it/realms/oauth2-visaSystem-realm-pkce/protocol/openid-connect/auth?response_type=code&client_id=aa-visasys-public&state=TH5GbUgzLmNaR1NheXJMcjFoTzRaRlFVTG9RMjN6OWxhS0tqTFhFTjFmTHNQ&redirect_uri=https%3A%2F%2Fegy.almaviva-visa.it%2F&scope=openid%20profile%20email&code_challenge=sU-td4HERtuuDlCOzxxcpa2zZUdqPSIPQD0fkMxO03g&code_challenge_method=S256&nonce=TH5GbUgzLmNaR1NheXJMcjFoTzRaRlFVTG9RMjN6OWxhS0tqTFhFTjFmTHNQ"
        # time.sleep(speed_open_page)  # الانتظار لمدة ثانيتين
        while True:
            try:
                conn = sqlite3.connect("Visitor.db")
                db = conn.cursor()
                driver.get(url)
                login_name = driver.find_element(By.ID,"username")
                login_password = driver.find_element(By.ID,"password")
                enter_login = driver.find_element(By.ID,"kc-login")
                # # ادخال الاسم
                login_name.clear()
                user_name = db.execute("SELECT username FROM users").fetchone()
                conn.commit()
                login_name.send_keys(user_name)
                # ادخال الباسورد
                login_password.clear()
                password = db.execute("SELECT password FROM users").fetchone()
                conn.commit()
                # print(password)
                login_password.send_keys(password)
                # time.sleep(speed_open_page)
                # الضغط على تسجيل الدخول
                login_password.send_keys(Keys.ENTER)
            
                break
            except Exception:
                print("اعاده تسجيل الدخول")
            # الدخول الى صفحه تسجيل البيانات
        element_back = True
        while element_back == True:
            try:
                driver.get("https://egy.almaviva-visa.it/")
                driver.refresh()
                time.sleep(1.5)
                enter_information = driver.find_element(By.XPATH,
                                                        "/html/body/app-root/div/app-homepage/app-base-info-page/div[2]/div[1]/div[3]/a"
                                                        )
                enter_information.click()
                time.sleep(1.5)
                #هنا بدايه الصفحه الاولى 
                # Select_the_center = driver.find_element(By.ID,"mat-select-value-1")
                try:
                    select_city_egy = driver.find_element(By.XPATH,"/html/body/app-root/div/app-appointment-page/div/mat-stepper/div/div[2]/div[1]/app-memebers-number/form/div/div[3]")
                    select_city_egy.find_element(By.XPATH,"./mat-select").click()
                except :
                    driver.refresh()
                    time.sleep(.8)
                    enter_information = driver.find_element(By.XPATH,
                                                            "/html/body/app-root/div/app-homepage/app-base-info-page/div[2]/div[1]/div[3]/a"
                                                            )
                    enter_information.click()
                    time.sleep(.8)
                    select_city_egy = driver.find_element(By.XPATH,"/html/body/app-root/div/app-appointment-page/div/mat-stepper/div/div[2]/div[1]/app-memebers-number/form/div/div[3]")
                    select_city_egy.find_element(By.XPATH,"./mat-select").click()
                    time.sleep(1.5)
                finally:
                    # time.sleep(3)
                    # select_city_egy = driver.find_element(By.XPATH,"/html/body/app-root/div/app-appointment-page/div/mat-stepper/div/div[2]/div[1]/app-memebers-number/form/div/div[3]")
                    # select_city_egy.find_element(By.XPATH,"./mat-select").click()
                    # time.sleep(3)
                    pass
                select_the_center = db.execute("SELECT city_egypt FROM users").fetchone()[0]
                conn.commit()
                select_the_center1 = select_the_center.strip("(')").title()
                # print(select_the_center1)
                time.sleep(1.5)
                select_city_egy3 = driver.find_element(By.ID,"cdk-overlay-0")
                select_city_egy1s = select_city_egy3.find_elements(By.XPATH,".//mat-option")
                for select_city_egy1 in select_city_egy1s:
                    date3 = select_city_egy1.text
                    # print(date3)
                    if date3 == select_the_center1:
                        select_city_egy1.click()
                        # print("here")
                        break
                # time.sleep(2)
                Select_service_level_option1 = db.execute("SELECT Select_service_level_option FROM users").fetchone()[0]
                conn.commit()
                Select_service_level_option12 = Select_service_level_option1.strip("(')").title()
                Select_service_level = driver.find_element(By.XPATH,"/html/body/app-root/div/app-appointment-page/div/mat-stepper/div/div[2]/div[1]/app-memebers-number/form/div/div[4]/mat-select/div/div[1]/span")
                Select_service_level.click()
                # print("here")
                Select_service_level1s = driver.find_element(By.ID,"cdk-overlay-1")
                Select_service_level2s = Select_service_level1s.find_elements(By.XPATH,".//mat-option")
                # print(Select_service_level_option12.lower())
                for Select_service_level2 in Select_service_level2s:
                    date = Select_service_level2.text.lower()
                    # print(date)
                    if date == Select_service_level_option12.lower():
                        Select_service_level2.click()
                        break
                #اختيار الفيزا
                Select_visa_type_option = db.execute("SELECT Select_visa_type_option FROM users").fetchone()[0]
                conn.commit()
                Select_visa_type_option1 = Select_visa_type_option.strip("(')").title().lower()
                select_visa = driver.find_element(By.XPATH,"/html/body/app-root/div/app-appointment-page/div/mat-stepper/div/div[2]/div[1]/app-memebers-number/form/div/div[5]/div/div/div/div/single-select/form/mat-select/div/div[1]/span")
                select_visa.click()
                time.sleep(.8)
                # print(f"{Select_visa_type_option1})")
                select_visa1s = driver.find_element(By.ID,"cdk-overlay-2")
                select_visa2s = select_visa1s.find_elements(By.XPATH,".//mat-option")
                for select_visa2 in select_visa2s:
                    date1 = select_visa2.text.lower()
                    # print(f"here {date1}")
                    if date1 == (f"{Select_visa_type_option1})"):
                        select_visa2.click()
                        break
                #انا واقف هنا
                #اضافه تاريخ الرحله
                #تقسيم التاريخ
                trip_date = db.execute("SELECT trip_date FROM users").fetchone()[0]
                conn.commit()
                trip_date1 = trip_date.strip("(')").title()
                d,m,y = trip_date1.split("/")
                month_dict = {
                    "01": "JAN", "1": "JAN",
                    "02": "FEB", "2": "FEB",
                    "03": "MAR", "3": "MAR",
                    "04": "APR", "4": "APR",
                    "05": "MAY", "5": "MAY",
                    "06": "JUN", "6": "JUN",
                    "07": "JUL", "7": "JUL",
                    "08": "AUG", "8": "AUG",
                    "09": "SEPT", "9": "SEPT",
                    "10": "OCT",
                    "11": "NOV",
                    "12": "DEC"
                }
                month = month_dict[m]
                time.sleep(1.5)
                date_button = driver.find_element(By.ID,"pickerInput")
                # date_button.clear()
                date_button.click()
                # date_button.send_keys("01/07/2024")
                try_button = driver.find_element(By.ID,"mat-datepicker-0")
                try_button1 = try_button.text.split("\n")
                year = try_button1[0].split(" ")
                # time.sleep(.5)
                year1 = year[1]
                year2 = float(year1)
                month2 = year[0]
                # print("here mohamed")
                while float(y) > year2:
                    # print("here mohamed1")
                    driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/mat-datepicker-content/div[2]/mat-calendar/mat-calendar-header/div/div/button[1]").click()
                    time.sleep(1.5)
                    # print("here mohamed2")
                    trip_date_date = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/mat-datepicker-content/div[2]")
                    trip_date_date1 = trip_date_date.find_element(By.CLASS_NAME,"mdc-button__label")
                    trip_date_date2 = trip_date_date1.text
                    # print(trip_date_date2)
                    trip_date_date3 = trip_date_date2.split("–")
                    trip_date_date4 = float(trip_date_date3[1])
                    print (2)
                    # time.sleep(2)
                    while float(y) > trip_date_date4:
                        # print("here mohamed3")
                        button_trip_date_date = trip_date_date.find_element(By.CLASS_NAME,"mat-calendar-controls")
                        button_trip_date_date.find_element(By.XPATH,".//button[3]").click()
                        time.sleep(1.5)
                    while float(y) < trip_date_date4:
                        print("here mohamed4")
                        button_click_trip_date_date = trip_date_date.find_element(By.CLASS_NAME,"mat-calendar-content")
                        button_click_trip_date_date2s = button_click_trip_date_date.find_elements(By.XPATH,".//button")
                        # print("here mohamed5")
                        for button_click_trip_date_date2 in button_click_trip_date_date2s:
                            test_year_button = button_click_trip_date_date2.text
                            print("here mohamed6")
                            if test_year_button == y:
                                button_click_trip_date_date2.click()
                                year_know = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/mat-datepicker-content/div[2]")
                                year_know1 = year_know.find_element(By.XPATH,".//button")
                                print(year_know1.text)
                                trip_date_date4 = float(year_know1.text)
                                year2 = float(year_know1.text)
                                break
                    # print("here mohamed7")
                    time.sleep(1)
                    
                    #اختيار الشهر
                    trip_date_month = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/mat-datepicker-content/div[2]")
                    trip_date_month1s = trip_date_month.find_elements(By.XPATH,".//button")
                    print("here mohamed8")
                    for trip_date_month1 in trip_date_month1s:
                        trip_date_month_date = trip_date_month1.text
                        if month == trip_date_month_date:
                            print("here mohamed9")
                            trip_date_month1.click()
                            break
                    time.sleep(1)
                    # break
                # while float(y) > year2:
                    # print("here")
                    # time.sleep(1)
                    # driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/mat-datepicker-content/div[2]/mat-calendar/mat-calendar-header/div/div/button[3]").click()
                    # try_button = driver.find_element(By.ID,"mat-datepicker-0")
                    # try_button1 = try_button.text.split("\n")
                    # year = try_button1[0].split(" ")
                    # year1 = year[1]
                    # year2 = float(year1)
                while month != month2:
                    time.sleep(1.5)
                    try_button.find_element(By.XPATH,".//button[3]").click()
                    try_button1 = driver.find_element(By.ID,"mat-datepicker-0")
                    try_button2 = try_button.text.split("\n")
                    year = try_button2[0].split(" ")
                    month2 = year[0]
                # اختيار اليوم
                time.sleep(1)
                try_button = driver.find_element(By.ID,"mat-datepicker-0")
                all_dates = try_button.find_elements(By.CLASS_NAME,"mat-calendar-body-cell")
                for dateelement in all_dates:
                    date = dateelement.text
                    if date == d:
                        dateelement.click()
                        break
                #كتابه اسم المدينه
                city = db.execute("SELECT city_italia FROM users").fetchone()[0]
                conn.commit()
                city1 = city.strip("(')").title().lower()
                write_city = driver.find_element(By.XPATH,"/html/body/app-root/div/app-appointment-page/div/mat-stepper/div/div[2]/div[1]/app-memebers-number/form/div/div[7]/div/input")
                write_city.clear()
                write_city.send_keys(city1)
                # write_city.send_keys("roma")
                mark_accept = driver.find_element(By.ID,"mat-mdc-checkbox-1-input")
                mark_accept.click()
                # print("here")
                element_found = False
                max_attemps = 12
                attemps = 0
                while not element_found and attemps < max_attemps:
                    try:
                        # print("here2")
                        accept_all = driver.find_element(By.XPATH,"/html/body/app-root/div/app-appointment-page/div/mat-stepper/div/div[2]/div[1]/app-memebers-number/div[2]/div/button")
                        accept_all.click()
                        # print("here3")
                        time.sleep(1.5)
                        driver.find_element(By.XPATH,"/html/body/app-root/div/app-appointment-page/div/mat-stepper/div/div[2]/div[1]/app-memebers-number/app-visasys-allert-card/div[2]/div[3]/button").click()
                        # print("here4")
                        time.sleep(1.5)
                        driver.find_element(By.XPATH,"/html/body/app-root/div/app-appointment-page/div[2]/mat-stepper/div/div[2]/div[2]/app-members-list/div[1]/div/div[3]/div/member-list-item/div/div[1]/div/div[2]").click()
                        # print("here5")
                        # attemps = 18
                        break
                    except:
                        # print("not found")
                        time.sleep(.8)
                        attemps += 1
                    if attemps == max_attemps:
                        messagebox.showerror("نتيجه","لم يتم الحجز لهذا المستخدم")
                        element_back = False
            except Exception as e:
                print("اعاده الصفحه")
            #بدايه الصفحه الثانيه
            time.sleep(1.5)
            driver.find_element(By.ID,'mat-input-1').click()
            time.sleep(1.5)
            #تاريخ الميلاد
            date_birthday = db.execute("SELECT date_birthday FROM users").fetchone()[0]
            conn.commit()
            date_birthday1 = date_birthday.strip("(')").title()
            d,m,y = date_birthday1.split("/")
            # d,m,y = 5,6,2024
            # d="5"
            # m="4"
            # y="2024"
            month_dict = {
                "01": "JAN", "1": "JAN",
                "02": "FEB", "2": "FEB",
                "03": "MAR", "3": "MAR",
                "04": "APR", "4": "APR",
                "05": "MAY", "5": "MAY",
                "06": "JUN", "6": "JUN",
                "07": "JUL", "7": "JUL",
                "08": "AUG", "8": "AUG",
                "09": "SEPT", "9": "SEPT",
                "10": "OCT",
                "11": "NOV",
                "12": "DEC"
            }
            month = month_dict[m]
            # time.sleep(2)
            copy_date = driver.find_element(By.ID,"mat-datepicker-1")
            birthday_date = copy_date.find_element(By.CLASS_NAME,"mdc-button__label")
            birthday_date1 = birthday_date.text
            age_birthday_date = birthday_date1.split(" ")
            year_bithday_date = float(age_birthday_date[1])
            moth_bithday_date = age_birthday_date[0]
            # print("here mohamed")
            while float(y) < year_bithday_date:
                # print("here mohamed1")
                copy_date.find_element(By.XPATH,".//button[1]").click()
                time.sleep(1.5)
                # print("here mohamed2")cdk-overlay-5
                trip_date_date = driver.find_element(By.ID,"cdk-overlay-5")
                trip_date_date1 = trip_date_date.find_element(By.CLASS_NAME,"mdc-button__label")
                trip_date_date2 = trip_date_date1.text
                # print(trip_date_date2)
                trip_date_date3 = trip_date_date2.split("–")
                trip_date_date4 = float(trip_date_date3[1])
                trip_date_date5 = float(trip_date_date3[0])
                # print (trip_date_date4)
                # time.sleep(2)
                while float(y) > trip_date_date4:
                    # print("here mohamed3")
                    button_trip_date_date = trip_date_date.find_element(By.CLASS_NAME,"mat-calendar-controls")
                    button_trip_date_date.find_element(By.XPATH,".//button[2]").click()
                    time.sleep(1.5)
                    trip_date_date = driver.find_element(By.ID,"cdk-overlay-5")
                    trip_date_date1 = trip_date_date.find_element(By.CLASS_NAME,"mdc-button__label")
                    trip_date_date2 = trip_date_date1.text
                    # print(trip_date_date2)
                    trip_date_date3 = trip_date_date2.split("–")
                    trip_date_date4 = float(trip_date_date3[1])
                    trip_date_date5 = float(trip_date_date3[0])
                while float(y) < trip_date_date5:
                    # print("here mohamed3")
                    button_trip_date_date = trip_date_date.find_element(By.CLASS_NAME,"mat-calendar-controls")
                    button_trip_date_date.find_element(By.XPATH,".//button[2]").click()
                    time.sleep(1.5)
                    trip_date_date = driver.find_element(By.ID,"cdk-overlay-5")
                    trip_date_date1 = trip_date_date.find_element(By.CLASS_NAME,"mdc-button__label")
                    trip_date_date2 = trip_date_date1.text
                    # print(trip_date_date2)
                    trip_date_date3 = trip_date_date2.split("–")
                    trip_date_date4 = float(trip_date_date3[1])
                    trip_date_date5 = float(trip_date_date3[0])
                while float(y) < trip_date_date4:
                    # print("here mohamed4")
                    button_click_trip_date_date = trip_date_date.find_element(By.CLASS_NAME,"mat-calendar-content")
                    mohamed = button_click_trip_date_date.text
                    # print(mohamed)
                    button_click_trip_date_date2s = button_click_trip_date_date.find_elements(By.XPATH,".//button")
                    # print("here mohamed5")
                    for button_click_trip_date_date2 in button_click_trip_date_date2s:
                        test_year_button = button_click_trip_date_date2.text
                        # print("here mohamed6")
                        if test_year_button == y:
                            button_click_trip_date_date2.click()
                            # year_know = driver.find_element(By.XPATH,"/html/body/div[3]/div[4]/div/mat-datepicker-content/div[2]")
                            year_know1 = trip_date_date.find_element(By.XPATH,".//button")
                            # print(year_know1.text)
                            trip_date_date4 = float(year_know1.text)
                            year_bithday_date = float(year_know1.text)
                            break
                # print("here mohamed7")
                time.sleep(1.5)
                #اختيار الشهر
                # trip_date_month = driver.find_element(By.XPATH,"/html/body/div[3]/div[4]/div/mat-datepicker-content/div[2]")
                trip_date_month1s = trip_date_date.find_elements(By.XPATH,".//button")
                # print("here mohamed8")
                for trip_date_month1 in trip_date_month1s:
                    trip_date_month_date = trip_date_month1.text
                    if month == trip_date_month_date:
                        # print("here mohamed9")
                        trip_date_month1.click()
                        break
                time.sleep(1.5)
                # time.sleep(.3)
                # birthday_date = driver.find_element(By.XPATH,"/html/body/div[3]/div[4]/div/mat-datepicker-content/div[2]/mat-calendar/mat-calendar-header/div/div/button[1]/span[2]/span")
                # birthday_date1 = birthday_date.text
                # age_birthday_date = birthday_date1.split(" ")
                # year_bithday_date = float(age_birthday_date[1])
            copy_date = driver.find_element(By.ID,"mat-datepicker-1")
            birthday_date = copy_date.find_element(By.CLASS_NAME,"mdc-button__label")
            birthday_date1 = birthday_date.text
            age_birthday_date = birthday_date1.split(" ")
            year_bithday_date = float(age_birthday_date[1])
            moth_bithday_date = age_birthday_date[0]
            while month != moth_bithday_date:
                copy_date1 = copy_date.find_element(By.CLASS_NAME,"mat-calendar-controls")
                copy_date1.find_element(By.XPATH,".//button[2]").click()
                time.sleep(.8)
                birthday_date = copy_date.find_element(By.CLASS_NAME,"mdc-button__label")
                birthday_date1 = birthday_date.text
                age_birthday_date = birthday_date1.split(" ")
                moth_bithday_date = age_birthday_date[0]
            #اختيار اليوم
            calender = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"mat-datepicker-1")))
            time.sleep(1.5)
            copy_date = driver.find_element(By.ID,"mat-datepicker-1")
            all_dates = copy_date.find_elements(By.CLASS_NAME,"mat-calendar-body")
            button_elments = copy_date.find_elements(By.XPATH,".//button")
            for button_element in button_elments:
                test_buttons = button_element.text
                # print("here")
                if test_buttons == d:
                    # print("succes")
                    button_element.click()
                    break
            #اختيار الجنس
            select_genders = db.execute("SELECT Select_gender FROM users").fetchone()[0]
            conn.commit()
            select_genders1 = select_genders.strip("(')").title().lower()
            driver.find_element(By.ID,"mat-select-value-7").click()
            time.sleep(1)
            select_gender = driver.find_element(By.XPATH,"/html/body/div[3]/div[4]/div")
            select_gender1s = select_gender.find_elements(By.XPATH,".//mat-option")
            for select_gender1 in select_gender1s:
                date2 = select_gender1.text.lower()
                if date2 == select_genders1:
                    select_gender1.click()
                    break
            # driver.find_element(By.ID,"mat-option-23").click()
            # if drop_bux2.get() == options_center1[0]:
            #     Select_gender_choose = driver.find_element(By.ID,"mat-select-6-panel")
            #     Select_gender_choose.find_element(By.XPATH,".//mat-option").click()
            #     # driver.find_element(By.ID,"mat-option-23").click()
            # else:
            #     Select_gender_choose = driver.find_element(By.XPATH,"/html/body/div[3]/div[4]/div/div")
            #     Select_gender_choose.find_element(By.XPATH,".//mat-option[2]").click()
            #الاقامه
            # time.sleep(3)
            Residence1 = db.execute("SELECT Residence FROM users").fetchone()[0]
            conn.commit()
            Residence11 = Residence1.strip("(')").title().lower()
            write_Residence = driver.find_element(By.ID,"cdk-overlay-4")
            write_Residence1s = write_Residence.find_elements(By.XPATH,".//input")
            i = 0
            for write_Residence1 in write_Residence1s:
                i += 1
                if i == 4:
                    write_Residence1.send_keys(Residence11)
                    # write_Residence1.send_keys("cairo")
            #رقم الباسبور
            Passport_number = db.execute("SELECT Passport_number FROM users").fetchone()[0]
            conn.commit()
            # print("here5")
            Passport_number1 = Passport_number
            # print("here6")
            write_Residence = driver.find_element(By.ID,"cdk-overlay-4")
            # print("here6")
            write_passports = write_Residence.find_elements(By.XPATH,".//input")
            # print("here7")
            i = 0
            for write_passport in write_passports:
                i += 1
                # print("here8")
                if i == 5:
                    write_passport.send_keys(Passport_number1)
            # print("here20")
            # write_passport.send_keys(Passport_number1)
            # write_passport.send_keys("2157893654")
            #تاريخ الاصدار
            issue_date = db.execute("SELECT issue_date FROM users").fetchone()[0]
            conn.commit()
            issue_date1 = issue_date.strip("(')").title()
            d,m,y = issue_date1.split("/")
            # d = "4"
            # m = "4"
            # y = "2024"
            month = month_dict[m]
            # time.sleep(.5)
            driver.find_element(By.ID,"mat-input-2").click()
            #كتابه تاريخ الاصدا داخل الجدول
            time.sleep(1)
            copy_issue = driver.find_element(By.ID,"mat-datepicker-2")
            copy_issue1 = copy_issue.find_element(By.CLASS_NAME,"mdc-button__label")
            copy_issue_text = copy_issue1.text
            age_issue_text = copy_issue_text.split(" ")
            year_issue = float(age_issue_text[1])
            month_issue = age_issue_text[0]
            # print("here mohamed")
            while float(y) < year_issue:
                # print("here mohamed1")
                driver.find_element(By.XPATH,"/html/body/div[3]/div[4]/div/mat-datepicker-content/div[2]/mat-calendar/mat-calendar-header/div/div/button[1]").click()
                time.sleep(1)
                # print("here mohamed2")
                trip_date_date = driver.find_element(By.XPATH,"/html/body/div[3]/div[4]/div/mat-datepicker-content/div[2]")
                trip_date_date1 = trip_date_date.find_element(By.CLASS_NAME,"mdc-button__label")
                trip_date_date2 = trip_date_date1.text
                # print(trip_date_date2)
                trip_date_date3 = trip_date_date2.split("–")
                trip_date_date4 = float(trip_date_date3[1])
                # print (trip_date_date4)
                # time.sleep(2)
                while float(y) > trip_date_date4:
                    # print("here mohamed3")
                    button_trip_date_date = trip_date_date.find_element(By.CLASS_NAME,"mat-calendar-controls")
                    button_trip_date_date.find_element(By.XPATH,".//button[2]").click()
                    time.sleep(1)
                while float(y) < trip_date_date4:
                    # print("here mohamed4")
                    button_click_trip_date_date = trip_date_date.find_element(By.CLASS_NAME,"mat-calendar-content")
                    button_click_trip_date_date2s = button_click_trip_date_date.find_elements(By.XPATH,".//button")
                    # print("here mohamed5")
                    for button_click_trip_date_date2 in button_click_trip_date_date2s:
                        test_year_button = button_click_trip_date_date2.text
                        # print("here mohamed6")
                        if test_year_button == y:
                            # print("mohamed")
                            button_click_trip_date_date2.click()
                            year_know = driver.find_element(By.XPATH,"/html/body/div[3]/div[4]/div/mat-datepicker-content/div[2]")
                            year_know1 = year_know.find_element(By.XPATH,".//button")
                            # print(year_know1.text)
                            trip_date_date4 = float(year_know1.text)
                            year_issue = float(year_know1.text)
                            break
                # print("here mohamed7")
                time.sleep(1)
                #اختيار الشهر
                trip_date_month = driver.find_element(By.XPATH,"/html/body/div[3]/div[4]/div/mat-datepicker-content/div[2]")
                trip_date_month1s = trip_date_month.find_elements(By.XPATH,".//button")
                # print("here mohamed8")
                for trip_date_month1 in trip_date_month1s:
                    trip_date_month_date = trip_date_month1.text
                    if month == trip_date_month_date:
                        # print("here mohamed9")
                        trip_date_month1.click()
                        break
                time.sleep(1)
            #اختيار السنه
            # while float(y) < year_issue:
            #     copy_issue.find_element(By.XPATH,".//button[2]").click()
            #     copy_issue1 = copy_issue.find_element(By.CLASS_NAME,"mdc-button__label")
            #     copy_issue_text = copy_issue1.text
            #     age_issue_text = copy_issue_text.split(" ")
            #     year_issue = float(age_issue_text[1])
            copy_issue = driver.find_element(By.ID,"mat-datepicker-2")
            copy_issue1 = copy_issue.find_element(By.CLASS_NAME,"mdc-button__label")
            copy_issue_text = copy_issue1.text
            age_issue_text = copy_issue_text.split(" ")
            year_issue = float(age_issue_text[1])
            month_issue = age_issue_text[0]
            #اختيار الشهر
            while month != month_issue:
                copy_issue.find_element(By.XPATH,".//button[2]").click()
                copy_issue1 = copy_issue.find_element(By.CLASS_NAME,"mdc-button__label")
                copy_issue_text = copy_issue1.text
                age_issue_text = copy_issue_text.split(" ")
                month_issue = age_issue_text[0]
            #اختيار اليوم
            time.sleep(1)
            all_days = copy_issue.find_elements(By.XPATH,".//button")
            for all_day in all_days:
                days = all_day.text
                # print(f"here {days}")
                if days == d:
                    # print("succes")
                    all_day.click()
                    break
            #تاريخ انتهاء الباسبور
            Expiration_date = db.execute("SELECT Expiration_date FROM users").fetchone()[0]
            conn.commit()
            Expiration_date5 = Expiration_date.strip("(')").title()
            d,m,y = Expiration_date5.split("/")
            # d = "3"
            # m = "5"
            # y = "2024"
            month = month_dict[m]
            # time.sleep(1)
            driver.find_element(By.ID,"mat-input-3").click()
            time.sleep(1)
            Expiration_date = driver.find_element(By.ID,"mat-datepicker-3")
            Expiration_date1 = Expiration_date.find_element(By.CLASS_NAME,"mat-calendar-header")
            Expiration_date2 = Expiration_date1.text
            age_Expiration_date = Expiration_date2.split(" ")
            year_Expiration_date = float(age_Expiration_date[1])
            month_Expiration_date = age_Expiration_date[0]
            # print("here mohamed")
            while float(y) > year_Expiration_date:
                # print("here mohamed1")
                driver.find_element(By.XPATH,"/html/body/div[3]/div[4]/div/mat-datepicker-content/div[2]/mat-calendar/mat-calendar-header/div/div/button[1]").click()
                time.sleep(1)
                # print("here mohamed2")
                trip_date_date = driver.find_element(By.XPATH,"/html/body/div[3]/div[4]/div/mat-datepicker-content/div[2]")
                trip_date_date1 = trip_date_date.find_element(By.CLASS_NAME,"mdc-button__label")
                trip_date_date2 = trip_date_date1.text
                # print(trip_date_date2)
                trip_date_date3 = trip_date_date2.split("–")
                trip_date_date4 = float(trip_date_date3[1])
                # print (trip_date_date4)
                # time.sleep(2)
                while float(y) > trip_date_date4:
                    # print("here mohamed3")
                    button_trip_date_date = trip_date_date.find_element(By.CLASS_NAME,"mat-calendar-controls")
                    button_trip_date_date.find_element(By.XPATH,".//button[3]").click()
                    time.sleep(1)
                while float(y) < trip_date_date4:
                    # print("here mohamed4")
                    button_click_trip_date_date = trip_date_date.find_element(By.CLASS_NAME,"mat-calendar-content")
                    button_click_trip_date_date2s = button_click_trip_date_date.find_elements(By.XPATH,".//button")
                    # print("here mohamed5")
                    for button_click_trip_date_date2 in button_click_trip_date_date2s:
                        test_year_button = button_click_trip_date_date2.text
                        # print("here mohamed6")
                        if test_year_button == y:
                            button_click_trip_date_date2.click()
                            year_know = driver.find_element(By.XPATH,"/html/body/div[3]/div[4]/div/mat-datepicker-content/div[2]")
                            year_know1 = year_know.find_element(By.XPATH,".//button")
                            # print(year_know1.text)
                            trip_date_date4 = float(year_know1.text)
                            year_Expiration_date = float(year_know1.text)
                            break
                # print("here mohamed7")
                time.sleep(1)
                #اختيار الشهر
                trip_date_month = driver.find_element(By.XPATH,"/html/body/div[3]/div[4]/div/mat-datepicker-content/div[2]")
                trip_date_month1s = trip_date_month.find_elements(By.XPATH,".//button")
                # print("here mohamed8")
                for trip_date_month1 in trip_date_month1s:
                    trip_date_month_date = trip_date_month1.text
                    if month == trip_date_month_date:
                        # print("here mohamed9")
                        trip_date_month1.click()
                        break
                time.sleep(1)
            # while float(y) < year_Expiration_date:
            #     Expiration_date.find_element(By.XPATH,".//button[3]").click()
            #     Expiration_date1 = Expiration_date.find_element(By.CLASS_NAME,"mat-calendar-header")
            #     Expiration_date2 = Expiration_date1.text
            #     age_Expiration_date = Expiration_date2.split(" ")
            #     year_Expiration_date = float(age_Expiration_date[1])
            Expiration_date = driver.find_element(By.ID,"mat-datepicker-3")
            Expiration_date1 = Expiration_date.find_element(By.CLASS_NAME,"mat-calendar-header")
            Expiration_date2 = Expiration_date1.text
            age_Expiration_date = Expiration_date2.split(" ")
            year_Expiration_date = float(age_Expiration_date[1])
            month_Expiration_date = age_Expiration_date[0]
            #اختيار الشهر
            while month != month_Expiration_date:
                Expiration_date.find_element(By.XPATH,".//button[3]").click()
                Expiration_date1 = Expiration_date.find_element(By.CLASS_NAME,"mat-calendar-header")
                Expiration_date2 = Expiration_date1.text
                age_Expiration_date = Expiration_date2.split(" ")
                month_Expiration_date = age_Expiration_date[0]
            #اختيار اليوم
            time.sleep(1)
            all_days = Expiration_date.find_elements(By.XPATH,".//button")
            for all_day in all_days:
                days = all_day.text
                # print(f"here {days}")
                if days == d:
                    # print("succes")
                    all_day.click()
                    break
            #صوره الباسبور
            time.sleep(1)
            driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-user-data/form/mat-dialog-content/div[1]/document-stripe/div/file-upload/div/div/div/span/div/label").click()
            time.sleep(1)
            # run_script()
    # send_image_passport = driver.find_element(By.ID,"100")
    # send_image_passport.send_keys(image_passport1.get())
    # send_image_passport.send_keys("D:\شغل البرمجه:\1.jpg")
            break


        #iam here
    # run_script()


    # استعلام لاسترجاع البيانات الحالية من جدول time_entries
    db.execute("SELECT hour, minute, second, speed FROM time_entries")
    time_data = db.fetchone()

    if time_data:
        hour, minute, second, speed = time_data
        # print(f"here{hour}:{minute}:{second}")
    else:
        hour = minute = second = speed = None
        # print(f"here1 {hour}:{minute}:{second}")

    # التحقق من وجود بيانات الوقت
    if hour is None or minute is None or second is None or hour == "" or minute == "" or second == "":
        print("No valid time data found, running script immediately...")
        run_script()
    else:
        print("hi")
        while True:
            # الحصول على الوقت الحالي
            current_time = time.localtime()
            current_hour, current_minute, current_second = current_time.tm_hour, current_time.tm_min, current_time.tm_sec
            
            # التحقق من تطابق الوقت المسجل مع الوقت الحالي
            if (current_hour == hour and current_minute == minute and current_second == second + 1):
                run_script()
                break  # توقف عن التكرار بمجرد تشغيل run_script()

            # انتظار ثانية واحدة قبل التحقق مرة أخرى
            time.sleep(1)

    # إغلاق اتصال قاعدة البيانات
    conn.close()