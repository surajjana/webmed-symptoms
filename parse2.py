import json
import requests
import time
import xlwt

workbook = xlwt.Workbook()

for k in range(1,69):
	url_symptoms = "http://symptoms.webmd.com/scapp/SymptomCheckerAPI.svc/symptoms"
	data_symptoms = {"request":{"user":{"age":8,"gender":"F","zip":"","vid":"cfd87d3c-3f57-4a36-acdf-11553e89255f"},"locale":"us","bodypartid":k}}
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	r = requests.post(url_symptoms, data=json.dumps(data_symptoms), headers=headers)
	r.encoding = None
	data = json.loads(r.text.encode(encoding='ISO-8859-1',errors='ignore'))

	c = len(data["data"]["symptoms"])
	i = 0
	l_s_id = []
	l_s_nm = []
	for i in range(i,c):
		data1 = data["data"]["symptoms"][i]["id"]
		name1 = data["data"]["symptoms"][i]["nm"]
		l_s_id.append(data1)
		l_s_nm.append(name1)
		#time.sleep(2)
	#print l_s_id
	#print l_s_nm

	sheet = workbook.add_sheet("BodyPart_"+str(k))
	style = xlwt.easyxf('font: bold 1')

	print "Body Part : ",k,"\n\n"

	i = 0

	for i in range(i,c):
		data_id = l_s_id[i]
		symptom_name = l_s_nm[i]
		sheet.write(0,i,symptom_name,style)
		workbook.save('/home/ubuntu/webmed/webmed-symptoms/female_7_12.xls')
		print "Symptom ",i," : ", symptom_name
		url_conditions = "http://symptoms.webmd.com/scapp/SymptomCheckerAPI.svc/conditions"
		data_conditions = {"request":{"user":{"age":8,"gender":"F","zip":"","vid":"cfd87d3c-3f57-4a36-acdf-11553e89255f"},"locale":"us","maxconditions":200,"bodyparts":[{"id":k,"symptoms":[{"id":data_id,"qclss":[{"quals":[]}]}]}]}}
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		r = requests.post(url_conditions, data=json.dumps(data_conditions), headers=headers)
		r.encoding = None
		data = json.loads(r.text.encode(encoding='ISO-8859-1',errors='ignore'))
		#print data
		conditions_count =  len(data["data"]["conditions"])
		j = 0
		for j in range(j,conditions_count):
			data2 = data["data"]["conditions"][j]["name"]
			print j,". ",data2
			sheet.write(j+1,i,data2)
			workbook.save('/home/ubuntu/webmed/webmed-symptoms/female_7_12.xls')

workbook = xlwt.Workbook()

for k in range(1,69):
	url_symptoms = "http://symptoms.webmd.com/scapp/SymptomCheckerAPI.svc/symptoms"
	data_symptoms = {"request":{"user":{"age":14,"gender":"F","zip":"","vid":"cfd87d3c-3f57-4a36-acdf-11553e89255f"},"locale":"us","bodypartid":k}}
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	r = requests.post(url_symptoms, data=json.dumps(data_symptoms), headers=headers)
	r.encoding = None
	data = json.loads(r.text.encode(encoding='ISO-8859-1',errors='ignore'))

	c = len(data["data"]["symptoms"])
	i = 0
	l_s_id = []
	l_s_nm = []
	for i in range(i,c):
		data1 = data["data"]["symptoms"][i]["id"]
		name1 = data["data"]["symptoms"][i]["nm"]
		l_s_id.append(data1)
		l_s_nm.append(name1)
		#time.sleep(2)
	#print l_s_id
	#print l_s_nm

	sheet = workbook.add_sheet("BodyPart_"+str(k))
	style = xlwt.easyxf('font: bold 1')

	print "Body Part : ",k,"\n\n"

	i = 0

	for i in range(i,c):
		data_id = l_s_id[i]
		symptom_name = l_s_nm[i]
		sheet.write(0,i,symptom_name,style)
		workbook.save('/home/ubuntu/webmed/webmed-symptoms/female_13_17.xls')
		print "Symptom ",i," : ", symptom_name
		url_conditions = "http://symptoms.webmd.com/scapp/SymptomCheckerAPI.svc/conditions"
		data_conditions = {"request":{"user":{"age":14,"gender":"F","zip":"","vid":"cfd87d3c-3f57-4a36-acdf-11553e89255f"},"locale":"us","maxconditions":200,"bodyparts":[{"id":k,"symptoms":[{"id":data_id,"qclss":[{"quals":[]}]}]}]}}
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		r = requests.post(url_conditions, data=json.dumps(data_conditions), headers=headers)
		r.encoding = None
		data = json.loads(r.text.encode(encoding='ISO-8859-1',errors='ignore'))
		#print data
		conditions_count =  len(data["data"]["conditions"])
		j = 0
		for j in range(j,conditions_count):
			data2 = data["data"]["conditions"][j]["name"]
			print j,". ",data2
			sheet.write(j+1,i,data2)
			workbook.save('/home/ubuntu/webmed/webmed-symptoms/female_13_17.xls')

workbook = xlwt.Workbook()

for k in range(1,69):
	url_symptoms = "http://symptoms.webmd.com/scapp/SymptomCheckerAPI.svc/symptoms"
	data_symptoms = {"request":{"user":{"age":20,"gender":"F","zip":"","vid":"cfd87d3c-3f57-4a36-acdf-11553e89255f"},"locale":"us","bodypartid":k}}
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	r = requests.post(url_symptoms, data=json.dumps(data_symptoms), headers=headers)
	r.encoding = None
	data = json.loads(r.text.encode(encoding='ISO-8859-1',errors='ignore'))

	c = len(data["data"]["symptoms"])
	i = 0
	l_s_id = []
	l_s_nm = []
	for i in range(i,c):
		data1 = data["data"]["symptoms"][i]["id"]
		name1 = data["data"]["symptoms"][i]["nm"]
		l_s_id.append(data1)
		l_s_nm.append(name1)
		#time.sleep(2)
	#print l_s_id
	#print l_s_nm

	sheet = workbook.add_sheet("BodyPart_"+str(k))
	style = xlwt.easyxf('font: bold 1')

	print "Body Part : ",k,"\n\n"

	i = 0

	for i in range(i,c):
		data_id = l_s_id[i]
		symptom_name = l_s_nm[i]
		sheet.write(0,i,symptom_name,style)
		workbook.save('/home/ubuntu/webmed/webmed-symptoms/female_18_24.xls')
		print "Symptom ",i," : ", symptom_name
		url_conditions = "http://symptoms.webmd.com/scapp/SymptomCheckerAPI.svc/conditions"
		data_conditions = {"request":{"user":{"age":20,"gender":"F","zip":"","vid":"cfd87d3c-3f57-4a36-acdf-11553e89255f"},"locale":"us","maxconditions":200,"bodyparts":[{"id":k,"symptoms":[{"id":data_id,"qclss":[{"quals":[]}]}]}]}}
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		r = requests.post(url_conditions, data=json.dumps(data_conditions), headers=headers)
		r.encoding = None
		data = json.loads(r.text.encode(encoding='ISO-8859-1',errors='ignore'))
		#print data
		conditions_count =  len(data["data"]["conditions"])
		j = 0
		for j in range(j,conditions_count):
			data2 = data["data"]["conditions"][j]["name"]
			print j,". ",data2
			sheet.write(j+1,i,data2)
			workbook.save('/home/ubuntu/webmed/webmed-symptoms/female_18_24.xls')