'''
CMD COMMANDS:
	
	start: 
		uvicorn main:app --reload
	end: 
		ctrl+c

	make virtual enviourment:
	    python -m venv env

	activate env:
	    .\env\Scripts\activate

	initialise git:
	    git init

	set execuytionPolicy:
		Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
'''

baseurl: http://127.0.0.1:8000/
docs: http://127.0.0.1:8000/docs


create user: http://127.0.0.1:8000/users/
    params:
    - brukernavn [str]: admin
    - epost [str]: user@example.com
    - passord [str]: password123
    - organisasjon [str]: a.borgerod
	'''
    curl -X "POST" \
    "http://127.0.0.1:8000/users/" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -d "{
    "brukernavn": "admin",
    "epost": "user@example.com",
    "passord": "password123",
    "organisasjon": "a.borgerod"
    }"
	'''

login: http://127.0.0.1:8000/login/token
    params:
    # - username [str]
    - email [str]
    - password [str]
    '''
    curl -X "POST" \
    "http://127.0.0.1:8000/login/token" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "grant_type=&username=admin&password=password123&scope=&client_id=&client_secret="
    '''

get callList: http://127.0.0.1:8000/callList/
    params:
    - skip [int]: 0
    - limit [int]: 100
    '''
    curl -X "GET" \
    "http://127.0.0.1:8000/callList/?skip=0&limit=100" \
    -H "accept: application/json"
    '''

# DOESN"T WORK
get overview: http://127.0.0.1:8000/overView/
    params:
    - ...
    '''
    curl -X "GET" \
    "http://127.0.0.1:8000/overView/" \
    -H "accept: application/json"
    '''


put update ringe_status:
    http://127.0.0.1:8000/callList/ringe_tatus?org_num=810182482
    curl -X 'PUT' \
      'http://127.0.0.1:8000/callList/ringe_tatus?org_num=810182482' \
      -H 'accept: application/json'