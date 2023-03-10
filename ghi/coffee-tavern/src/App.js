import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import EmployeeFeedbackForm from './feedbacks/EmployeeFeedbackForm';
import EmployerFeedbackForm from './feedbacks/EmployerFeedbackForm';
import EmployerFeedbackList from './feedbacks/EmployerFeedbackList';
import EmployeeFeedbackList from './feedbacks/EmployeeFeedbackList';
import EmployeeFeedbackEdit from './feedbacks/EmployeeFeedbackEdit';
import EmployerFeedbackEdit from './feedbacks/EmployerFeedbackEdit';
import AllEmployeeFeedback from './feedbacks/AllEmployeeFeedback';
import AllEmployerFeedback from './feedbacks/AllEmployerFeedback';


// import EmployeeProfile from './LoggedInUserProfile/Employee';
// import EmployerProfile from './LoggedInUserProfile/Employer';
import EmployeeInfoForm from './LoggedInUserProfile/EmployeeInfoForm';
import EmployeeInfoFormCreate from './LoggedInUserProfile/CreateEmployeeInfo';
import EmployerInfoFormCreate from './LoggedInUserProfile/CreateEmployerInfo';
import EmployerInfoForm from './LoggedInUserProfile/EmployerInfoForm';
import OthersEmployeeProfile from './listOfProfiles/othersEmployeeProfile';
import OthersEmployerProfile from './listOfProfiles/othersEmployerProfile';
import Profile from './LoggedInUserProfile/Profile';
import EmployeeProfileList from './listOfProfiles/listOfEmployees';
import EmployerProfileList from './listOfProfiles/listOfEmployers';

import TagForm from './tags/TagForm';
import Tag from './tags/Tag';
import TagListView from './tags/TagListView';

import React, { Component } from 'react';
import JobPostForm from './JobPost/JobPostForm';
import JobPostList from './JobPost/JobPostList';
import Login from './Login';
import Signup from './Signup';
import MainPage from './MainPage';
import UploadResume from './UploadResumeForm';
import Nav from './Nav';
import { AuthProvider, useToken } from './useToken';
import Apply from './JobPost/Apply';

function GetToken() {
  useToken();
  return null
}
export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

render() {

  const domain = /https:\/\/[^/]+/;
  const basename = process.env.PUBLIC_URL.replace(domain, '');

  return (
    <AuthProvider>
      <BrowserRouter basename={basename}>
        <GetToken />
          <Nav />
            <div className="container">
              <Routes>
                <Route path="/" element={<MainPage />}>
                </Route>
                <Route path="/create_form" element={<JobPostForm />}>
                </Route>
                <Route path="/get_all_form" element={<JobPostList />}>
                </Route>
                <Route path="/token" element={<Login />}>
                </Route>
                <Route path="/api/accounts" element={<Signup />}>
                </Route>
                <Route path="/upload_resume/" element={<UploadResume />}>
                </Route>
                <Route path = "/employee-feedback" element={<EmployeeFeedbackForm />} >
                </Route>
                <Route path = "/employer-feedback" element={<EmployerFeedbackForm />} >
                </Route>
                <Route path = "/employee-feedbacks-list" element={<EmployeeFeedbackList />} >
                </Route>
                <Route path = "/employer-feedbacks-list" element={<EmployerFeedbackList/>} >
                </Route>
                <Route path = "/employee-feedback-update" element={<EmployeeFeedbackEdit/>}>
                </Route>
                <Route path = "/employer-feedback-update" element={<EmployerFeedbackEdit/>}>
                </Route>
                <Route path = "/all-employee-feedback" element={<AllEmployeeFeedback/>}>
                </Route>
                <Route path = "/all-employer-feedback" element={<AllEmployerFeedback/>}>
                </Route>
                <Route path = "/employee-profile-list" element={<EmployeeProfileList/>}>
                </Route>
                <Route path = "/employer-profile-list" element={<EmployerProfileList/>}>
                </Route>
                {/* <Route path = "/create_tag_form" element={<TagForm />}>
                </Route> */}
                <Route path = "/create_tag_form" element={<TagForm/>}>
                </Route>
                <Route path = "/create_tag_form" element={<Tag/>}>
                </Route>
                <Route path = "/create_tag_form" element={<TagListView/>}>
                </Route>
                <Route path = "/applicants" element={<Apply />}>
                </Route>
                <Route path = "/other-employee-profile" element={<OthersEmployeeProfile />}>
                </Route>
                <Route path = "/other-employer-profile" element={<OthersEmployerProfile />}>
                </Route>

                {/* Lexey */}

                <Route path = "/user/current/profile" element={<Profile/>} />
                <Route path = "/user/employee/info-form/create" element={<EmployeeInfoFormCreate/>} />
                <Route path = "/user/employee/info-form" element={<EmployeeInfoForm/>} />
                <Route path = "/user/employer/info-form/create" element={<EmployerInfoFormCreate/>} />
                <Route path = "/user/employer/info-form" element={<EmployerInfoForm/>} />

              </Routes>
            </div>
        </BrowserRouter>
    </AuthProvider>
  )
  }
}
