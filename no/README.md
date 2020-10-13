### Challenge no 

The website in the text ```https://fbf-masti.herokuapp.com/?``` has a form.

![The site](https://i.imgur.com/eanYygI.png)


From the question title it was clear NoSQL is used as a backend server.

NoSQL injection is used in getting the solution. Looking at the source code, the button calls an ajax function posting a request on ``/login`` taking in ``username`` and ``password`` as headers. 

Using ``$ne`` standing for ``not equals`` in the username and password prints out ``Welcome, divi!``.

![The site](https://i.imgur.com/L1Wg8ry.png)
   

After a few hit and trials I used ``admin`` as username and the flag was recieved in the response.

![The site](https://i.imgur.com/q0l0esJ.png)


### Few Tricks
The code in the Console is copied from the website source. I could have used Burp Suite Repeater and Payload but sending the ajax through console seemed fastest.
