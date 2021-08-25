DB : Postgres

python django

how to run : first go to the directory where requiments.txt present and then open cmd in that directory then write this command 'pip install -r requirements.txt'.
it will install the requirements for this project. It uses postgres so you have to install postgres. and in coding_challenge/settings.py it has 'DATABASES' variable in which
the configuration of database stored in the form of dict , so you have to change the defaults(name ,password,user) as in your end(your computer's postgres user,database,password).
then type this command 'python manage.py migrate' in the directory where 'manage.py' exists, it will migrate the database(create tables in database).
for making superuser to access admin panel provided by django, command is 'python manage.py createsuperuser' hit enter it will ask you question like username password email,
now you can login to admin panel by the super user credenials. To access admin panel ,the url is 'http://127.0.0.1:8000/admin/'

user Registraion 

create deposit model and also overrides its create method in serializer class to create and update the desposit model instances.(user can buy coins)  

get ,set apis for deposit model.

for achieving real-time experience ; I use websockets.

Cache setup by using files (with expiry time):: cache implementation using file system
first it will check if any cache file from particular user exists if exists
then it will check its expiry time if it is expire then it will fetch data from DB and 
overwrite the file , and if expiry time is good then it will set the deposits(in which deposit's data store) variable of Deposit(Websocket) class. And if the cache file of particular user does not exists then it will make a json file name after user's username then it grabs model objects(queryset) then serialize it ,add expiry time(add 30 minutes to current time) of 30 minutes, save it into file and set the deposits(in which deposit's data store) variable of Deposit(Websocket) class.


So when user connects to websocket with a user id, then it will check in the cache for specific user if its in the cache; then it will not query database and it will get the data from cache and updates it in the memory(websocket instance's variables). 
And when user disconnects the websocket then it will grab the values and using serializer we can save it in the database.

caching deposit model instances by using file system django cache.

Build front-end in react.js

api integration using axios.

creating Websocket's instance in react , sending and receiving messages.

documentaion link : https://documenter.getpostman.com/view/14011925/TzzDJZwn
