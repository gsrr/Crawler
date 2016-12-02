# -*- coding: utf-8 -*-
import time
from selenium import webdriver

def browse_select_option(driver, elem_name):
	#element = driver.find_element_by_name("adultCount")
	element = driver.find_element_by_name(elem_name)
	all_options = element.find_elements_by_tag_name("option")
	for option in all_options:
		print("Value is: %s" % option.get_attribute("value"))
		option.click()

def search_submit(driver, elem_name):
	#search_box = driver.find_element_by_name('submitButtonName_intwws')
	search_box = driver.find_element_by_name(elem_name)
	search_box.submit()

def fill_text(driver, elem_name, msg):
	#element = driver.find_element_by_name("departureAirportCode:field_pctext")
	element = driver.find_element_by_name(elem_name)
	element.send_keys(msg)
	element.click()
	time.sleep(5)

def select_date(driver, elem_name, t_date):
	#element = driver.find_element_by_id("departureDate:field_pctext")
	element = driver.find_element_by_id(elem_name)
	element.click()
	time.sleep(5)
	all_tds = driver.find_elements_by_tag_name("td")
	for td in all_tds:
		print td.get_attribute("abbr")
		#if td.get_attribute("abbr") == "2016-12-16":
		if td.get_attribute("abbr") == t_date:
			td.click()
			break
	
driver = webdriver.Chrome('C:\Python27\chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://aswbe-i.ana.co.jp/international_asw/pages/revenue/search/roundtrip/search_roundtrip_input.xhtml?CONNECTION_KIND=TWN&LANG=en');
time.sleep(5) # Let the user actually see something!

fill_text(driver, "departureAirportCode:field_pctext", "Hong Kong")
fill_text(driver, "arrivalAirportCode:field_pctext", "Fukuoka")	

select_date(driver, "departureDate:field_pctext", "2016-12-16")
select_date(driver, "returnDate:field_pctext", "2016-12-22")

element = driver.find_element_by_id("btnResearch")
element.click()
time.sleep(5)
#driver.execute_script("Asw.Calendar.open({    dateFrom:'20161203',    selectMaxDays:'364',    selectedDateFormat:'%M/%D/%y (%w)',    yearMonthFormat:'%m %y',    monthRange:'3',    setWeekly:'SU-MO-TU-WE-TH-FR-SA',    setMonth:'Jan-Feb-Mar-Apr-May-Jun-Jul-Aug-Sep-Oct-Nov-Dec',    linkage:'returnDate:field',    prevLabel:'Previous 3 months',    nextLabel:'Next 3 months',    closeLabel:'',    defaultText:'Please select',    complexItineraryLinkage:'',    selectingLabel:'You currently have day {0} of the month selected'})")
#time.sleep(5)
#driver.quit()