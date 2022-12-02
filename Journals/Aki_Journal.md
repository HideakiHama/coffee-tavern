#### Dec 01 2022


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
