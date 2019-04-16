""" API class
	
API class will actually executes the REST API using requests class.
"""
import requests

class API(object):

	@staticmethod
	def execute(url, method="get", headers=None, input_parameters=None):
		""" Here depending on the method it calls requests method
			Input: 
				url - rest api url
				method - by default get, can be post, put, delete
				headers - by default its none, can set tokens
				input_parameters - input keyword value dictionary
			Output:
				It (returns status_code, response_text) as tupple
				status code can be
				200 - Success
				400 - Bad-Input
				304 - No-Content
				500 - Error
		"""
		response = requests.__dict__.get(method)(url, 
												headers=headers, 
												data=input_parameters)
		if response.text.strip():
			return response.status_code, response.json()
		return response.status_code, None