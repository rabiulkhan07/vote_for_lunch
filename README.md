# vote_for_lunch

run : pip3 install -r requirements.txt

For Employee API :

ACTION      METHOD      URL
--------------------------------------------------------
Save        post        localhost:8000/api/register
Get all     get         localhost:8000/api/employee 
Get Single  get         localhost:8000/api/employee/uuid
Update      put         localhost:8000/api/employee/uuid
Delete      delete      localhost:8000/api/employee/uuid
Login       post        localhost:8000/api/login
Active user get         localhost:8000/api/activeuser
Logout      post        localhost:8000/api/logout

Restaurent API:

Resturent create
localhost:8000/api/restaurant/create/

Fetch Resturents
localhost:8000/api/restaurants/

Fetch single Resturent by id
localhost:8000/api/restaurants/<uuid:pk>/

Update Resturent 
localhost:8000/api/restaurants/<uuid:pk>/edit/

Delete Resturent 
localhost:8000/api/restaurants/<uuid:pk>/delete/


Menu API :

Menu create
localhost:8000/api/menu/create/

All Menu Fetch
localhost:8000/api/menus

Single Menu Fetch
localhost:8000/api/menus/<uuid:pk>/

Update Menu 
localhost:8000/api/menus/<uuid:pk>/edit/

Delete Menu 
localhost:8000/api/menus/<uuid:pk>/delete/

Menu Today
localhost:8000/api/menus/today/

Vote
localhost:8000/api/votes/create/

Result
localhost:8000/api/get_result/
