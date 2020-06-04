# Socket programming
this is socket programming projects for isfahan university of technology network course.
 
 ## How to run
 in each project first run **server** by command `python server.py` in windows cmd (or `python3 server.py` in mac/linux)
</br>
then run **client** by command `python client.py` in windows cmd (or `python3 client.py` in mac/linux)
> **Note:** Project1 can have multiple clients running

## Project 1
It's simple client server model that each clinet send two numbers to server and receives sum of those as a result.
#### options:
there is `configs` dictionary in `server.py` and `client.py` that give you below options:

* you can change IP address that server is listening on by changing value of `IP_Address` in both client and server files.
* Protocol of network layer can be IPv4 or IPv6 by defining it in `IP_version` in both files.
* `PORT` defiens port number that server is listening and client is sending data (it should be greater than 1023 because numbers less than 1023 are reserved).
* `Transport_type` can be either **TCP** or **UDP**.
* `Clients_limit` defines how many clients can simultaneously be connected to the server.
* `timeout` defines maximum time that server keep connection to each clients open, without sending any data.

## Project 2
In this project client can send two types of queries to the server (UDP is used as transport layer):
* `GET` : then server send all saved data back to client
* `POST "something"`: then server saves "something"

#### questions:
* why UDP does not have `close()` method?
    * because it's not connection-oriented. there is no connection that needs to be closed.
* TCP is good, so why UDP exists?!
    * TCP brings more overhead.
    * establishing connection in TCP takes some times.
    * when netowrk is broken, TCP is not a good option.
    * UDP use cases (when a bit of loss dosn't matter):
        * Voice over IP (VoIP)
        * Streaming
        * Domain Name Systems (DNS)
        * Online multiplayer games
        * ...

## Project 3
client and server can send unlimited number of messages to each others (one message client then one message server). then each one can terminate connection by sending **Good Bye**. 
<br>
> **messages are encrypted using RSA method.** 

#### how to run
because of encryption, you require `pycryptodome` module to run server and client. you can install it using:

```
pip install pycryptodome
```

or install it from pipfile with `pipenv` virtual enviroment.

```
pipenv install
```
then in two separate terminals
```
pipenv run python server.py
```
```
pipenv run python client.py
```






