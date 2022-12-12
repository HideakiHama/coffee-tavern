### Dec 09 2022
Today we work as group to work on deploying our project to Render (for backend) and GitLab(for CI/CD). With our instructors help we were able to successfully deploy faster then expected.  Toward the end of the day we worked on individual unit test.

### Dec 08 2022
Today I worked on how feedback button on the Nav bar changes depends on the role the user sign up as. For example, if a user sign up as an employer they will see only Employer feedback feature. Eventually I discussed with the group what other buttons should be separated from user.   We named the file "employerNav.js" and "employeeNav.js".
Our biggest blocker was deploying our project into Render.

### Dec 07 2022
Today in the morning I helped Lexey with frontend side of getting a list of Employee to display. I also added a feature where a employer can click on a button to display individual employee profile (using 'useNavigate' and 'useLocation')
In the Afternoon I worked on backend.  I made a router and queries that grabs all the data of feedbacks regardless of who the user wrote it.  My biggest-blocker was when user create a feedback the name have to match whats in the data (If the user are employee giving feedback to the employer the name of the employer have to match in the list of employer in the backend).   I know better way to do this but we were running out of time.   I decided to use useNavigate to carry the data to the list of employee,for example, useLocation to take out that data.  I grabbed all the employer data and used filter, include, and map method to get the list of feedbacks form specific employee or employer.
My ah-ha: useNavigate and useLocation is still amazing!!

### Dec 06 2022
Today I worked on connecting backend without hard coding user id.  And worked on adding Delete & Edit button onto user's feedback list.
How I was able to do this:
##### Connection backend without hard coding user id:
- First npm installed jwt-decode
- Decode user token on the front end
- Access user id
- set that id into user_id variable
##### How I was able to link user info onto the link when user clicked on the button:
- I used useNavigation to let user navigate to specific location and added {state:{id:id}} to pass the id onto the navigation link.    navigate("/employee-feedback-update", {state:{id:id}})
- I use uselocation on the linked side to take out user id from the previous file.
example code   const location = useLocation(); const id = location.state.id;
Instead of having delete and edit button on their feedback list I decided to link to 'update' page.
My ah-ha moment was "jwt-decode" to decode token. "useNavigation & useLocation" to carry the data.
Blocker: I can't manually get to the Edit Link (with the useLocation coded inside). Solution I deleted the link to the feedback edit on the nav bar.

### Dec 05 2022
Today I worked on having Authenticator work on the feedback form and changing the login back to login by email and not by id.
User can only login by id because our SQL inside our account.'get' function was wrong.  WHERE clause (filter) was set to ID instead of email. It made the data expect integer. instead of string.
Our major blocker was trying to figure out how to make our Monolithic app into Microservice.

### Dec 04 2022
I Worked on finishing the PUT and Delete request of both feedbacks.  I deleted "required" attribute inside the input tag of feedback-edit component. When user didn't want to update certain field then the original input data will sent to the backend. I added if statement inside the handle-edit to handle empty field.   Blocker: If the user wanted to edit, for example description field, the user have to type everything again even if its for editing one miss spell words.

#### Dec 03 2022
Worked on finishing POST, GET, and started PUT request of both feedbacks.   For tbe PUT I wanted to have user see and edit what they wrote inside the inputs fields.  To do this I had two option use "defaultValue" or "placeholder" attribute. I couldn't use "defaultValues" because I already had "value" inside the input tag. Also, if I deleted 'value' inside the input tag it will cause "A component is changing a controlled input to be uncontrolled" Side note: Controlled component is data that is handled by a React Component.  Uncontrolled component is data handled by the DOM itself.
I decided to use the "placeholder" attribute to allow user to see what they wrote previously.

#### Dec 02 2022
In the morning all of us took our turn shared screen to merge our branches to the remote main at the Gitlab.  After experiencing what happened yesterday it was really traumatizing for me.  Again only ah-ha moment was always use git status to make sure I'm not sending node-modules.
In the afternoon I pair programmed with Curtis to add more style to the employer-feedback on the frontend.

#### Dec 01 2022
I pair programmed with chris in the morning to finish the backend for Employee Feedback, then I worked on the authorization of Job-form PUT method.  I was going to start the frontend functionality side of Feedback Form and Feedback List but I couldn't start it until the evening that day.  I accidentally pushed node-modules into the gitlab and took us all the afternoon to fix it.  Turns out my node-module was not properly 'gitignored' when I committed.   I had several ah-ha moment today:
 - if the node-modules doesn't ignore I need to both delete the node-modules folder and ".gitignore" file. remake the ".gitignore" file with all the files/directories that I want to be ignored.  Then I need to reinstall the node-module by npm install (in the correct directory!)
 - git status is my friend.  let me know what file it will be commit or pushed
 - When I run React I have to change "Select End of Line Sequence" from CRLF to LF (https://www.aleksandrhovhannisyan.com/blog/crlf-vs-lf-normalizing-line-endings-in-git/)


#### Nov 30 2022
Today I pair programmed with Chris on Employee Feedback to retrieve account id for who ever employee are giving feedback to.

#### Nov 29 2022
Today I worked on creating a functionality side of feedbacks.
The blocker for today was remembering React from scratch.  I also had issue with installing axios.   Turns out there was some issue with registry.  After couple hour axios stuff was resolved.

#### Nov 28 2022

Today we tried running the React, but couldn't go too far because we all had react issue.   For me the problem was improper installation of create-react-app.
- I did the following to solve the problem:

>npm uninstall -g create-react-app   to uninstall react app thats installed globally
>npx create-react-app coffee-tavern   to install the react app inside coffee-tavern


#### Nov 27 2022

After endless spiral into different rabbit holes I was finally able to set permission to API endpoints!! I use OAuth2passwordBearer to lock the endpoint.  Created a Async function to decode the jwt token (It also check for 'secret key' before decoding).  Then check if the user role (status) matches with the permission (status). If the user role matches then they are authorized to use the API endpoint.  Ah-ha moment:  FastApi documentation are our friend.

#### Nov 26 2022

Today I worked on connecting feedback and account table. I also change the input of employee_name and employer_name fromm str (string) to id.  The reason for this is because when we're working on the frontend we can create list of specific feedback by id.  Ah-ha moment: Use 'reference' clause to connect table together.  Check api/migrations/003_feedback_table.py)

#### Nov 23 2022

Chris and I finished working on Account.  Afterward I was stuck in the endless spiral of how to make permission for creating feedback. Only progress I made was implementing the date onto the both feedback form. Later when we create frontend the feedback will be in the order of the submitted date.

#### Nov 22 2022

I worked with Chris to work on Account and whether to add a status to the User account.  We decided to change status to role attribute for naming convention.  We imported 'Literal' from 'typing' and used it on the role attribute of AccountIn (see api/queries/accounts.py) so that the new user has two choices for the role, employee or employer.   Note: Account and AccountOut are set to str for role attribute because the 'employee' and 'employer' that user choose are string.   Eventually the feedback form will have permission to create feedback depends on whether the user are employee or employer.
My blocker for today was whether to use jwt.decoder or dictionary to create a permission.

#### Nov 21 2022

Today I worked on completing the CRUD for both Employee and Employer Feedback Form.  After that I decided whether to connect the employee and employer data as many to many or by foreign key.  I guess this was my blocker for today.
I though about this:
> Employer search the employee from the list -> The form will be save into the Employee's data by ID.
I decided to go with the foreign key.


#### Nov 18 2022

Our group decided to go with Postgres SQL over the MongoDB because of the ease of use (And more comfortable using RDBMS over DOD)
We also work as a group and finished authentication.py file
Aside from that I worked on Employee and Employer Feedback Form
