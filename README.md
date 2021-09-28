# learningpython
Initiative to learn programming in python

Contents

Chapter - Projects

Project_Security -------------------------------------------------------- 1
  Introduction ---------------------------------------------------------- 1.1
  ad_project_1 ---------------------------------------------------------- 1.2
  storepassword.py ------------------------------------------------------ 1.3
Libraries --------------------------------------------------------------- 2
  bcrypt ---------------------------------------------------------------- 2.1
Variables --------------------------------------------------------------- 3
  passwd ---------------------------------------------------------------- 3.1
  hashed ---------------------------------------------------------------- 3.2
Functions --------------------------------------------------------------- 4
  bcrypt.hashpw()-------------------------------------------------------- 4.1
  bcrypt.gensalt()------------------------------------------------------- 4.2
  
Projects

1.    Project_Security

1.1.  Introduction

Project_Security was given by Alwin Doss as an initiative to secure clear text passwords. 

Project_Security branches out into various sub-projects. 

1.2.  ad_project_1

ad_project_1 is the first project under Project_Security which contains the file storepassword.py

1.3.  storepassword.py

storepassword.py uses the bcrypt library to hash the clear text password and displays the hashed password as output. 

2.    Libraries

2.1.  bcrypt

bcrypt is imported to utilise the functions to encrypt the clear text password

3.    Variables

3.1.  passwd
passwd contains the cleartext password defined by the developer.

3.2.  hashed
hashed contains the expression to import the bcrypt library and hash the clear text password stored in passwd.

4.    Functions

4.1   bcrypt.hashpw() 
Hash a password using the OpenBSD bcrypt scheme

4.2   bcrypt.gensalt()
Generate a salt for use with the BCrypt.hashpw() method, selecting a reasonable default for the number of hashing rounds to apply
