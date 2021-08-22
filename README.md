DB : Postgres

python django

user Registraion 

create deposit model and also overrides its create method in serializer class to create and update the desposit model instances.(user can buy coins)  

get ,set apis for deposit model.

for achieving real-time experience ; I use websockets.

File System Django Cache setup (also setting the timeout; TTL)

So when user connects to websocket with a user id, then it will check in the cache for specific user if its in the cache; then it will not query database and it will get the data from cache and updates it in the memory(websocket instance's variables). 
And when user disconnects the websocket then it will grab the values and using serializer we can save it in the database.

caching deposit model instances by using file system django cache.

Build front-end in react.js

api integration using axios.

creating Websocket's instance in react , sending and receiving messages.

documentaion link : https://documenter.getpostman.com/view/14011925/TzzDJZwn
