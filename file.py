import time
import os
from zipfile import ZipFile
from selenium import webdriver
import time
x=input()


def change_dir(drive_letter,keyword):
    drive_letter=drive_letter+keyword
    return drive_letter
def zip_dir(l):
    os.chmod(l,0o777) 
    os.chmod(l[0:3]+'IP',0o777)
    os.chmod(l[0:3]+'SM',0o777)
    os.chmod(l[0:3]+'COM',0o777)
    os.chmod(l[0:3]+'DC',0o777)
    os.chmod(l[0:3]+'LA',0o777) 

    for i in os.listdir(l):
        x1=l[0:3]
        
        
        if 'ip' or 'intro to programming' in i.lower():
            x1=change_dir(x1,'IP')
            if 'homework' in i.lower():
                x1=change_dir(x1,'\\HOMEWORK\\')
            elif 'lectures' in i.lower():
                x1=change_dir(x1,'\\LECTURES\\')
            elif 'tutorials' in i.lower():
                x1=change_dir(x1,'\\TUT\\')
            elif 'labs' in i.lower():
                x1=change_dir(x1,'\\LABS\\')
            else:
                x1=change_dir(x1,"\\others\\")
        elif 'systemsmanagement' in i.lower():
            print(i.lower())
            x1=change_dir(x1,'SM')
            if 'lectures' in i.lower():
                x1=change_dir(x1,'\\LECTURES\\')
            elif 'labs' in i.lower():
                x1=change_dir(x1,'\\LABS\\')
            else:
                x1=change_dir(x1,"\\others")
        elif 'digitalcircuits' in i.lower():
            x1=change_dir(x1,'DC')
            if 'homework' in i.lower():
                x1=change_dir(x1,'\\HOMEWORK\\')
            elif 'lectures' in i.lower():
                x1=change_dir(x1,'\\LECTURES\\')
            elif 'tutorials' in i.lower():
                x1=change_dir(x1,'\\TUT\\')
            elif 'labs' in i.lower():
                x1=change_dir(x1,'\\LABS\\')
            else:
                x1=change_dir(x1,"\\others\\")

        elif 'linearalgebra' in i.lower():
            x1=change_dir(x1,'LA')
            if 'tutorials' in i.lower():
                x1=change_dir(x1,'\\TUT\\')
                print(x1)
            elif 'lectures' in i.lower():
                x1=change_dir(x1,'\\LECTURES\\')
            else:
                x1=change_dir(x1,"\\others\\")
        fileName = l+'\\'+i
        print(fileName)
        print(x1)
        with ZipFile(fileName,'r') as zip: 
            
            zip.extractall(x1)
            



options = webdriver.ChromeOptions()
options.add_argument("--incognito")

prefs = {'download.default_directory':x+'downloaded_content'}
options.add_experimental_option('prefs', prefs)
driver=webdriver.Chrome(chrome_options=options)
driver.get('https://www.usebackpack.com/welcome')

driver.find_element_by_xpath("//*[@id='loginButton']").click()
driver.find_element_by_xpath("//*[@id='googlebutton']").click()
driver.find_element_by_xpath("//*[@id='identifierId']").send_keys("mayank18049@iiitd.ac.in")
driver.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
#driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys("111tDmt2022")

driver.implicitly_wait(10)
driver.find_element_by_name("password").send_keys("this will be password and changed for reasons xD")

#driver.implicitly_wait(10)
#river.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()

element = driver.find_element_by_xpath("//*[@id='passwordNext']/content/span")
driver.execute_script("arguments[0].click();", element)
driver.implicitly_wait(10)
def DC_download(t):
    driver.find_element_by_xpath("//*[@id='home-container-main']/div[2]/div[1]").find_element_by_xpath('//*[@id="course_1185"]/a/img').click()
    driver.find_element_by_xpath('//*[@id="resources_tab"]/a').click()
    todownload=driver.find_elements_by_xpath('//a[@class="btn btn-sm"]')
    todownload=[x.text for x in todownload]
    for i in range(1,len(todownload)+1):
        driver.find_element_by_xpath('//*[@id="course-tab-content"]/a[%s]' % str(i)).click()
        time.sleep(4)
    zip_dir(t+'downloaded_content')
def IP_download(t):
    driver.find_element_by_xpath('//*[@id="home-container-main"]/div[2]/div[2]').find_element_by_xpath('//*[@id="course_1196"]/a/img').click()
    driver.find_element_by_xpath('//*[@id="resources_tab"]/a').click()
    todownload=driver.find_elements_by_xpath('//a[@class="btn btn-sm"]')
    todownload=[x.text for x in todownload]
    for i in range(1,len(todownload)+1):
        driver.find_element_by_xpath('//*[@id="course-tab-content"]/a[%s]' % str(i)).click()
        time.sleep(4)
    zip_dir(t+'downloaded_content')    
def MTH_download(t):
    driver.find_element_by_xpath('//*[@id="home-container-main"]/div[2]/div[3]').find_element_by_xpath('//*[@id="course_1201"]/a/img').click()
    driver.find_element_by_xpath('//*[@id="resources_tab"]/a').click()
    todownload=driver.find_elements_by_xpath('//a[@class="btn btn-sm"]')
    todownload=[x.text for x in todownload]
    for i in range(1,len(todownload)+1):
        driver.find_element_by_xpath('//*[@id="course-tab-content"]/a[%s]' % str(i)).click()
        time.sleep(4)
    zip_dir(t+'downloaded_content\\')       
def SM_download(t):
    driver.find_element_by_xpath('//*[@id="home-container-main"]/div[2]/div[4]').find_element_by_xpath('//*[@id="course_1214"]/a/img').click()
    driver.find_element_by_xpath('//*[@id="resources_tab"]/a').click()
    todownload=driver.find_elements_by_xpath('//a[@class="btn btn-sm"]')
    todownload=[x.text for x in todownload]
    for i in range(1,len(todownload)+1):
        driver.find_element_by_xpath('//*[@id="course-tab-content"]/a[%s]' % str(i)).click()
        time.sleep(4)
    zip_dir(t+'downloaded_content')
IP_download(x)
#DC_dowload(x)
#MYH_dowload(x)
#RUN ONE FUNCTION AT A TIME 


