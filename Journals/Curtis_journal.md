venv commands
-> python3 -m venv .venv --> creates venv
-> source .venv/bin/activate --> activate
-> bash thanos.sh --> script to restart docker and destroy volumes and recreate everything

Nov 21 - Mon

Tasked with looking up ways to upload files on Fast API
Found way to request file. Not sure if its the same thing but will use for now.
Watched a bunch of youtube videos on requesting files.
Found this video to be most helpful https://www.youtube.com/watch?v=N6bpBkwFdc8&ab_channel=FastAPIChannel

Nov 22 - Tuesday
Finished with the upload resume file post request.
Was able to test the feature on the localhost:8000/docs
gave a good ol' 200 code!
Will be working solo on the get request part of it
Also pushed my main.py and new uploadresume.py

Nov 23 - Wednesday
Found a shutil method for the resume file upload

shutil.copyfileobj() method in Python is used to copy the contents of a file-like object to another file-like object. By default this method copy data in chunks and if want we can also specify the buffer size through length parameter. 

I can see my files I upload in our repository once I execute it in localhost.
Only Problem currently is you can upload pdfs, however the pdf is not readable in VScode.

Nov 28 - Monday
Worked on getting React to work on my machine and application. Was able to get it working using the create project command line. Then created nec. files to have react in our application. Worked on the App.js for a little bit then we group debugged each other so we are all on the same page. Created a thanos.sh script to restart docker because it takes too much time to manually type things.

Nov 29 - Tuesday
Unit Test Notes
run docker ps -->find container name
copy name
docker exec <container id> python -m pytest
Steps for creating unit tests
arrage -> taking data and manipulating it so it dosent make any extra steps 
act -> acting data triggers the function
assert -> making sure its getting the response we should be (status code)
clean up -> dependancy overrides