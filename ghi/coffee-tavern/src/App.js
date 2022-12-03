import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import FeedbackTest from "./feedbackTest";
import EmployeeFeedbackForm from './EmployeeFeedbackForm';
import EmployerFeedbackForm from './EmployerFeedbackForm';
import EmployerFeedbackList from './EmployerFeedbackList';
import EmployeeFeedbackList from './EmployeeFeedbackList';
import React, { Component } from 'react';
import JobPostForm from './JobPost/JobPostForm';
import JobPostList from './JobPost/JobPostList';
import Login from './Login';
import Signup from './Signup';
import MainPage from './MainPage';
import UploadResume from './UploadResumeForm';



export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

render() {
  return (
    <BrowserRouter>
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
        <Route path = "/employee-feedbacks/" element={<EmployeeFeedbackForm />} >
        </Route>
        <Route path = "/employer-feedbacks/" element={<EmployerFeedbackForm />} >
        </Route>
        <Route path = "/employee-feedback-list/" element={<EmployeeFeedbackList />} >
        </Route>
        <Route path = "/employer-feedbacks-list/" element={<EmployerFeedbackList/>} >
        </Route>
      </Routes>
    </div>
    </BrowserRouter>
  )
  }
}
