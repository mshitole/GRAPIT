""" XMLParser class

Contains XMLParser class for parsing xml.
"""

# import libraries
import os
import xml.etree.ElementTree as ET

# Parser
class XMLParser(object):

	@staticmethod
	def parse_xml_files(path):
		""" Input : 
				Directory path of xml files, 
				Please note, there might be multiple xml files in the 
				directory
			Output:
				Returns list contains all the apis from all the xmls from 
				the directory path
		"""
		res = []
		for filename in os.listdir(path):
			if filename.endswith('.xml'):
				tmp = XMLParser.parse(path + filename)
				if tmp:
					res.extend(tmp)
		return res

	@staticmethod
	def parse(xml_path):
		""" This method accept single xml file as input, it picks rest api
			out of it and return the list of apis mention below output 
			section format.

			Input : xml file (one file)
			Output:
				It will break out each api and return 
				[{
					"suite_name": suite_name,
					"url": locator,
					"method": method,
					"input": input_parameter,
					"output": output_parameter,
					"headers":""
				}]
		"""
		if not os.path.exists(xml_path):
			raise IOError("XML file does not exists.")
		api_list = []
		tree = ET.parse(xml_path)
		root = tree.getroot()

		# Iterating all the suite
		for suite in root.findall('suite'):
			suite_name = suite.get("name")
			domain = suite.find("url").find("domain").text
			is_https = suite.find("url").find("ishttps").text
			domain = "https://" + domain if is_https else  "http://" + domain

			# Iterating all the apis from particular suite
			for api in suite.findall("apis/api"):
				locator = domain + api.find("locator").text
				method = api.find("method").text
				
				# Filter out the input for api
				input_parameter = {}
				if api.find("input") is not None:
					for value in api.find("input").getchildren():
						input_parameter.update({value.tag: value.text})
				
				# Filter out expected output for api
				output_parameter = {}
				if api.find("output") is not None:
					for value in api.find("output").getchildren():
						output_parameter.update({value.tag: value.text})
				
				# Gathering the information for particular api and return
				api_list.append({
					"suite_name": suite_name,
					"url": locator,
					"method": method,
					"input": input_parameter,
					"output": output_parameter,
					"headers":""
				})
		return api_list