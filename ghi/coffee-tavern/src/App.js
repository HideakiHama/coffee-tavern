import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import EmployeeFeedbackForm from './feedbacks/EmployeeFeedbackForm';
import EmployerFeedbackForm from './feedbacks/EmployerFeedbackForm';
import EmployerFeedbackList from './feedbacks/EmployerFeedbackList';
import EmployeeFeedbackList from './feedbacks/EmployeeFeedbackList';
import EmployeeFeedbackEdit from './feedbacks/EmployeeFeedbackEdit';
import EmployerFeedbackEdit from './feedbacks/EmployerFeedbackEdit';
import EmployeeProfile from './UserProfile/Employee';
import EmployerProfile from './UserProfile/Employer';
import EmployeeInfoForm from './UserProfile/EmployeeInfoForm';
import EmployerInfoForm from './UserProfile/EmployerInfoForm';

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
    this.state = {
      id: 2
    };
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
                <Route path = "/create_tag_form" element={<TagForm />}>
                </Route>

                {/* Lexey */}

                <Route path = "/user/employee/" element={<EmployeeProfile id={this.state.id}/>} />
                <Route path = "/user/employee/info-form" element={<EmployeeInfoForm id={this.state.id}/>} />
                <Route path = "/user/employer" element={<EmployerProfile id={this.state.id}/>} />
                <Route path = "/user/employer/info-form" element={<EmployerInfoForm id={this.state.id}/>} />

              </Routes>
            </div>
        </BrowserRouter>
    </AuthProvider>
  )
  }
}
