""" Main program

The main program responsible for handling REST API
"""

# Libraries
import os
import pprint
from parser import XMLParser
from api import API
from constants import *


# APIHandler class
class APIHandler(object):
	""" Object of APIHandler class represent one REST-API
	"""

	def __init__(self, data):
		self.url = data["url"]
		self.method = data["method"]
		self.input = data["input"]
		self.output = data["output"]
		self.headers = data["headers"]
		self.suite_name = data["suite_name"]
		
		# pass / failed status
		self.status = False

	def _match_response(self, response, expected_response):
		"""
			It match the repsonse with expected response
			Returns True if status and response match expected response
			else return False
		"""
		if str(response[0]) == str(expected_response["status"]):
			for key in expected_response.keys():
				# exclude the status from the response as we are comparing 
				# it before
				if key == "status" or \
						str(expected_response[key]) == str(response[1][key]):
					continue
				else:
					return False
			return True
		return False

	def verify(self):
		""" Calling _match_response 
			It set status field to True if rest api match the result with 
			expected output else set to False 
		""" 
		response = API.execute(self.url, self.method, self.headers, self.input)
		# marking fail / pass api
		self.status = self._match_response(response, self.output)


# HTMLGenerator class
class HTMLGenerator(object):
	""" This class useful for creating test report for each rest api
		collectively.
		It fetch html template from constants.py file and render html
		using APIHandler objects.
		Email extension can be added in the future for more convenience
	""" 
	def __init__(self, data):
		self.data = data

	def generate_markup(self):
		""" It will generate the markup for api testing. 
			output will be stored in logs.html
		"""
		html = ""
		output = {}
		total = len(self.data)
		total_passed = 0
		total_failed = 0
		for res in self.data:
			if res.status:
				total_passed += 1
			else:
				total_failed += 1

			if res.suite_name in output:
				output[res.suite_name].append(res)
			else:
				output[res.suite_name] = [res]

		html = HEADER
		pass_per = total_passed/total * 100
		fail_per = total_failed/total * 100

		html += BODY % (total, 
						total_passed, 
						pass_per, 
						total_failed, 
						fail_per)

		# generate table for each test suite
		for suite_name, values in output.items():
			table = TABLE_PART_1 % (suite_name)
			cnt = 1
			for value in values:
				status = "PASS" if value.status else "FAIL"
				table += TABLE_PART_2 % (str(cnt), 
										value.url, 
										value.method.upper(), 
										status)
				cnt += 1
			html += table + TABLE_PART_3
		html += FOOTER

		# generating output
		with open('logs.html', 'w') as fp:
			fp.write(html)


def process_apis(apis):
	""" It will create APIHandler class for each rest api.
		then executes that api and mark status to True or False
		as per api result
		It will use this list of APIHandler objects to generate html report
	"""
	res = []
	for api in apis:
		obj = APIHandler(api)
		obj.verify()
		res.append(obj)
	HTMLGenerator(res).generate_markup()

def main():
	apis = XMLParser.parse_xml_files("xml/")
	process_apis(apis)

if __name__ == "__main__":
	main()