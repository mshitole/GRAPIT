# Project Title
GRAPIT
## Introduction
GRAPIT is a generic test framework for rest api testing.
## Getting Started
To start with the GRAPIT, need to create xml files in xml folder.
Framework will read all the xml files inside xml folder so multiple files can be created.
Below is simple xml format.
```
<?xml version="1.0" encoding="UTF-8"?>
	<suites>
		<suite name="Suite Name">
			<url>
			...
			</url>
			<apis>
				<api>
				...
				</api>
				<api>
				...
				</api>
			</apis>
	</suite>
</suites>
```
## Tag Details
```
* <suites>			: Contains multiple test suite <suite> tag.
* <suite name="">		: Name of the actual test suite.
* <url> 			: Section contains the url information for each test suite.
* <ishttps>			: Value is 1 https else 0.
* <domain>			: Domain name.
* <api> 			: Represent one single REST API.
* <apis> 			: Can hold multiple API with tag <api>.
* <locator>			: Is actual API resource locator (post domain url).
* <method> 			: Can be GET, POST, PUT and DELETE.
* <input> 			: Input for REST API.
* <output>			: Expected output.
```

Let's take an example, we need to test API for login

```
URL   :	https://reqres.in/api/login
input :	{"email": "peter@klaven", "password": "cityslicka"}
output: { status: 200}
```

The test case format for the same API would be

```
<suites>
	<suite name="Login">
		<url>
			<ishttps>1</ishttps>
			<domain>reqres.in</domain>
		</url>
		<apis>
			<api>
				<locator>/api/login</locator>
				<method>post</method>
				<input>
					<email>peter@klaven</email>
					<password>cityslicka</password>
				</input>
				<output>
					<status>200</status>
				</output>
			</api>
		</apis>
	</suite>
</suites>
```

Lets create XML tag for negative test case for the same API with blank password
```  
URL   : https://reqres.in/api/login
input : {"email": "peter@klaven", "password": ""}
output: { status: 400, "error": "Missing Password"}
```

XML format would be

```
<suites>
	<suite name="Login">
		<url>
			<ishttps>1</ishttps>
			<domain>reqres.in</domain>
		</url>
		<apis>
			<api>
				<locator>/api/login</locator>
				<method>post</method>
				<input>
					<email>peter@klaven</email>
				</input>
				<output>
					<status>400</status>
					<error>Missing Password</error>
				</output>
			</api>
		</apis>
	</suite>
</suites>
```  

Final XML look like:
  
```  
<?xml version="1.0" encoding="UTF-8"?>
<suites>
	<suite name="Login">
		<url>
			<ishttps>1</ishttps>
			<domain>reqres.in</domain>
		</url>
		<apis>
			<api>
				<locator>/api/login</locator>
				<method>post</method>
				<input>
					<email>peter@klaven</email>
					<password>cityslicka</password>
				</input>
				<output>
					<status>200</status>
				</output>
			</api>
			<api>
				<locator>/api/login</locator>
				<method>post</method>
				<input>
					<email>peter@klaven</email>
				</input>
				<output>
					<status>400</status>
					<error>Missing password</error>
				</output>
			</api>
		</apis>
	</suite>
</suites>
```

Multiple XML files can be created inside xml folder in this format and framework 
will pick all the test suite from each files and executes API
	
## Output Data Mapping
JSON output of the API can be mapped with tags.
in above case for empty password API returning json {status: 404, error: "Missing Password"}
so here each key (status, error here) represent tag and their value represent
tag contents so the format their XML tag would be 

```
<status>404</status>
<error>Missing Password</error>
```

## Prerequisites
```
Python 2.7
```

## How to get it Running
```
python test.py
```    

After executing it will generate result in log.html in the same directory
# Output format
please visit http://htmlpreview.github.io/?https://github.com/mshitole/GRAPIT/blob/master/logs.html
