# vote_for_lunch

run : pip3 install -r requirements.txt

For Employee API :

ACTION      METHOD      URL
--------------------------------------------------------
Save        post        localhost:8000/api/register
Get all     get         localhost:8000/api/employee 
Get Single  get         localhost:8000/api/employee/id
Update      put         localhost:8000/api/employee/id
Delete      delete      localhost:8000/api/employee/id
Login       post        localhost:8000/api/login
Active user get         localhost:8000/api/activeuser
Logout      post        localhost:8000/api/logout
