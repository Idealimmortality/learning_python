# coding=utf-8
from appium import webdriver
import unittest
from appium import webdriver
import time
import random
from selenium.webdriver.support.wait import WebDriverWait   #显示等待

#定义手机信息
desired_caps = dict(
  platformName = "Android",
  platformVersion = "9",
  devicesName = "8BNDU17803005724",
  appActivity = "com.eg.android.AlipayGphone.AlipayLogin",
  appPackage = "com.eg.android.AlipayGphone",
  noReset = "true",
  fullReset = "false"
)

#进入扫一扫并进入相册
def intoSaoyiSao(driver):
  el8 = driver.find_element_by_id("com.alipay.android.phone.openplatform:id/saoyisao_iv")
  el8.click()
  time.sleep(2)
  el2 = driver.find_element_by_id("com.alipay.mobile.scan:id/title_bar_album")
  el2.click()
  time.sleep(2)
#滑动照片
def scrollPhoto(driver):
  driver.swipe(start_x=560,start_y=980,end_x=560,end_y=460,duration=3000)
  time.sleep(3)

#图片名称数组
Photo = ["照片1，2020年10月22日 04点11分 "]
""" Photo = ["照片1，2020年10月22日 04点11分 ","照片2，2020年10月21日 14点23分 ","照片3，2020年10月21日 14点23分 ","照片4，2020年10月21日 14点23分 ","照片5，2020年10月21日 14点23分 ",\
         "照片6，2020年10月21日 14点23分 ","照片7，2020年10月21日 14点23分 ","照片8，2020年10月21日 14点23分 ","照片9，2020年10月21日 14点23分 ","照片10，2020年10月21日 14点23分 ",\
         "照片11，2020年10月21日 14点23分 ","照片12，2020年10月21日 14点23分 ","照片13，2020年10月21日 14点23分 ","照片14，2020年10月21日 14点23分 ","照片15，2020年10月21日 14点23分 ",\
         "照片16，2020年10月21日 14点23分 ","照片17，2020年10月21日 14点22分 ","照片18，2020年10月21日 14点22分 ","照片19，2020年10月21日 14点22分 ","照片20，2020年10月21日 14点22分 ",\
         "照片21，2020年10月21日 14点22分 ","照片22，2020年10月21日 14点22分 ","照片23，2020年10月21日 14点22分 ","照片24，2020年10月21日 14点22分 ","照片25，2020年10月21日 14点22分 ",\
         "照片26，2020年10月21日 14点22分 ","照片27，2020年10月21日 14点22分 ","照片28，2020年10月21日 14点22分 ","照片29，2020年10月21日 14点22分 ","照片30，2020年10月21日 14点22分 "] """
# Photo = ["照片44，2020年10月10日 03点00分 ","照片16，2020年10月10日 02点58分 ","照片17，2020年10月10日 02点58分 "]



#定位金额输入框并且输入随机金额（10块到15之间）
def intoMoney(driver):
  money = random.randint(10,15)
  el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.ax/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.EditText")
  el4.send_keys(money)
  return(money)



#输入金额并输入密码
def inputPassword(driver):
  driver.tap([(179,1657)],10)
  driver.tap([(179,1657)],10)
  driver.tap([(179,1347)],10)
  driver.tap([(533,1823)],10)
  driver.tap([(179,1347)],10)
  driver.tap([(892,1509)],10)
  time.sleep(5)
  driver.tap([(979,149)],40)#完成
  time.sleep(2)
  driver.tap([(179,140)],40) #退出
  time.sleep(2)
 

#分割列表
def Div_LIST(para=[]):
  for j in range(0,len(para),6):
    print(para[j:j+6])

#主函数
def main():
  Money_list = []
  driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
  time.sleep(3)
  intoSaoyiSao(driver)

  for i in Photo:
    count = 1
    while count <= 6:
      time.sleep(1)
      try:
        print("开始扫码")
        image = driver.find_element_by_accessibility_id(i)
        image.click()
        time.sleep(5)
        money = intoMoney(driver)
        Money_list.append(money)
      except Exception as e:
        while e!="True":
          try:
            print("扫码失败，异常:",e)
            print("向下滚动屏幕")
            scrollPhoto(driver)
            image = driver.find_element_by_accessibility_id(i)
          except:
            print("继续向下滚动屏幕")
          else:
            e = "True"
      else:
        
        time.sleep(5)
        el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.ax/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View[1]")
        el5.click()
        time.sleep(5)
        #el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.ax/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.Button")
        #el6.click()
        #time.sleep(8)  #变为自动等待
        el6 = WebDriverWait(driver,timeout=8,poll_frequency=0.01).until(lambda x: x.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.ax/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.Button"))
        el6.click()
        el7 = WebDriverWait(driver,timeout=8,poll_frequency=0.01).until(lambda x: x.find_element_by_id("com.alipay.android.phone.mobilecommon.verifyidentity:id/go_pwd"))
        #el7 = driver.find_element_by_id("com.alipay.android.phone.mobilecommon.verifyidentity:id/go_pwd")
        el7.click()
        time.sleep(3)
        inputPassword(driver)
        intoSaoyiSao(driver)
        print("第"+str(count)+"次扫码结束")
        count += 1
      finally:
        print("*"*20)
  print(Money_list)

if __name__ == "__main__":
    main()


#TODO:1.时间设置为等待 2.完善提示语 3.统计金额并写入文件保存 