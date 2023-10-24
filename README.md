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

Restaurent API:

Resturent create
localhost:8000/api/restaurant/create/

Fetch Resturents
localhost:8000/api/restaurants/

Fetch single Resturent by id
localhost:8000/api/restaurants/<int:pk>/

Update Resturent 
localhost:8000/api/restaurants/<int:pk>/edit/

Delete Resturent 
localhost:8000/api/restaurants/<int:pk>/delete/


Menu API :

Menu create
localhost:8000/api/menu/create/

All Menu Fetch
localhost:8000/api/menus

Single Menu Fetch
localhost:8000/api/menus/<int:pk>/

Update Menu 
localhost:8000/api/menus/<int:pk>/edit/

Delete Menu 
localhost:8000/api/menus/<int:pk>/delete/

Menu Today
localhost:8000/api/menus/today/
