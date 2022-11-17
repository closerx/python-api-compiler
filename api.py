import requests

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ar-FR,ar;q=0.9,en-FR;q=0.8,en;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    'Origin': 'https://ide.geeksforgeeks.org',
    'Pragma': 'no-cache',
    'Referer': 'https://ide.geeksforgeeks.org/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; STK-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

mycode="""
x="hacker"
print(x)

y=input()
print(y)
"""


json_data = {
    'language': 'python3',
    'code': mycode,
    'input': 'python', # if want add input
    'save': False,
}

try:
	response = requests.post('https://codejudge.geeksforgeeks.org/submit-request', headers=headers, json=json_data)
	
	myid=response.json()["id"]
	
	res=requests.get(f"https://codejudge.geeksforgeeks.org/get-status/{myid}")
	
	print(res.json()["output"])
except Exception as e:
	print("plz try again")
