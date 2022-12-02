// import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import React, { Component } from 'react';
import JobPostForm from './JobPostForm';
import JobPostList from './JobPostList';
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
      </Routes>
    </div> 
    </BrowserRouter>
  )
  }
}






// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code>
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

// import './App.css';
// import { 
//   BrowserRouter as Router,
//   Routes,
//   Route
// } from 'react-router-dom'
// import Notes from './pages/Notes'
// import Note from './pages/Note'
// import Layout from './components/Layout'
// function App() {
//   return (
//     <Router>
//       <Layout>
//         <Routes>
//             <Route path="/" element={<Notes/>} exact/>
//             <Route path="/:id" element={<Note/>}/>
//         </Routes>
//       </Layout>
//     </Router>
//   );
// }
