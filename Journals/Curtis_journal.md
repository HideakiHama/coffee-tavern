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