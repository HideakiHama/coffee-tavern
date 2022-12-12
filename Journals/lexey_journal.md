## December 12, 2022

Today, I worked on:

* Readme

Added gui map to readme.



## December 11, 2022

Today, I worked on:

* Unit testing, readme

I worked on unit testing for getting the employee and employer info by id, and 
worked on adding the aendpoints to the readme.



## December 9, 2022

Today, I worked on:

* create user info form

There was an issue where the user profile page was breaking if the user hasn't 
created their user information. So I after sign up, depedning on id they signed 
up as an employee or employer, I had it then navigate to the corresponding create 
info form. 



## December 8, 2022

Today, I worked on:

* merged profile components

I created a single component to render either the employee profile page or 
the employer profile page depending on the rold of the current logged in user.
This allows it to be rendered under one path instead of two.



## December 7, 2022

Today, I worked on:

* profiles

I had to rewrite lost files. Made profile work and navigate to profile of 
logged in user. Going to work on refactoring to one page, that checks the 
role of the user and shows correct information. Working with Aki on the 
navigation from clicking a users name to go to their profile. (non logged
in user) 



## December 6, 2022

Today, I worked on: 

* employee & employer info forms

Today I figured out why updating the form was giving me an unauthorized 
error. With Chris's help, he showed me how to grab the token that was 
created upon signing in. I completed the employer form and added the links 
to the forms on the profile pages, as well as a return to profile link 
on the form.



## December 5, 2022

Today, I worked on:

* employee form

I got most of employee form to work, but getting back an unauthorized 
error. Chris helped me with some backend refactoring. Made sure both front 
and backend were still connected properly



## December 4, 2022

Today, I worked on:

* profiles

Set up a basic profile page just to show the data that's needed. Was able 
to work with react hooks to make the page work smoother.



## December 1, 2022

Today, I worked on:

* Employer info

I created create, update, and get by id endpoints for user info. Going to 
refactor with chris tomorrow to grab the data better, so it'll be easier 
to grab on the front end.



## November 30, 2022

Today, I worked on:

* Employee info, React

Added get by id endpoint and query for employee info. Aki was able to 
help me solve why my react wasn't working on my computer. Mostly had to 
do with file structure and where things where downloaded.



## November 29, 2022

Today, I worked on:

* React

Watched react videos to refreash on front end. react is having issues 
with auto reload on my computer. While trying to fix it, files were 
mixed up and everyones project was working differently. Trying to 
solve why it's not working on my computer even though I cloned the 
most up to date repo to try and see if react works. That same repo 
works on other team members computers who have windows.



## November 28, 2022

Today, I worked on:

* Figured out employee info queries and started setting up front-end

Finally figure out how to connect the employee information to the id 
of the logged in account. Now working with Chris, Aki, and Curtis to set 
up the react app so we can get started on the front-end.



## November 27, 2022

Today, I worked on:

* Trouble shooting the employee info queries

Still trouble shooting but I feel like I'm figuring it out and getting 
closer. Tried a lot of different approaches, and nothing has fully 
worked so far, but I am using what I have learned from the different 
approaches to narrow down what I am missing in my code to get it to work. 
Messing around with these approaches has helped me get more comfortable 
with understanding and writing sql statements.



## November 23, 2022

Today, I worked on:

* Trouble shooting the employee info queries

The routers are set up, but still having trouble with the queries.
Spent a some time researching and finding a lot of good resources 
to bookmark for later, as well as some good direction for how I can 
get the queries to work.



## November 22, 2022

Today, I worked on:

* Creating endpoints for the user info section

Started setting up the queries and routers for employee info.
Created the files and figured out the wireframing for what 
information we want to be shown on the profile.



## November 21, 2022

Today, I worked on:

* Setting up the tables for an employee user

I was able to set up the sables with a foreign key relation 
to the accounts model. Which will later hopefully accomplish the 
ability to be able to let the user edit their profile to represent 
themselves.

Not sure how to set up the ability to add a profile picture, and how 
it would be stored in the database, but something I have researched 
a little bit. Another thing later on I'll add is the connection to 
user feedback.