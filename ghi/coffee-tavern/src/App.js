import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import EmployeeFeedbackForm from './feedbacks/EmployeeFeedbackForm';
import EmployerFeedbackForm from './feedbacks/EmployerFeedbackForm';
import EmployerFeedbackList from './feedbacks/EmployerFeedbackList';
import EmployeeFeedbackList from './feedbacks/EmployeeFeedbackList';
import EmployeeFeedbackEdit from './feedbacks/EmployeeFeedbackEdit';
import EmployerFeedbackEdit from './feedbacks/EmployerFeedbackEdit';
import EmployeeInfoForm from './LoggedInUserProfile/EmployeeInfoForm';
import EmployeeInfoFormCreate from './LoggedInUserProfile/CreateEmployeeInfo';
import EmployerInfoForm from './LoggedInUserProfile/EmployerInfoForm';
import EmployerInfoFormCreate from './LoggedInUserProfile/CreateEmployerInfo';
import Profile from './LoggedInUserProfile/Profile';

import EmployeeProfileList from './listOfEmployee'
import TagForm from './tags/TagForm';

import React, { Component } from 'react';
import JobPostForm from './JobPost/JobPostForm';
import JobPostList from './JobPost/JobPostList';
import Login from './Login';
import Signup from './Signup';
import MainPage from './MainPage';
import UploadResume from './UploadResumeForm';
import Nav from './Nav';
import { AuthProvider, useToken } from './useToken';

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
  return (
    <AuthProvider>
      <BrowserRouter>
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
                <Route path = "/employee-profile-list" element={<EmployeeProfileList/>}>
                </Route>
                <Route path = "/create_tag_form" element={<TagForm />}>
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
