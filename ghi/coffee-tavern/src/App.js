import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import FeedbackTest from "./feedbackTest";
import EmployeeFeedbackForm from './EmployeeFeedbackForm';
import EmployerFeedbackForm from './EmployerFeedbackForm';
import EmployerFeedbackList from './EmployerFeedbackList';
import EmployeeFeedbackList from './EmployeeFeedbackList';

function App() {
  return (
    <BrowserRouter>
      <FeedbackTest />

      <div className="App">
        {/* <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code>
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>


        </header> */}
        <Routes>
          <Route path = "/employee-feedbacks/" element={<EmployeeFeedbackForm />} />
          <Route path = "/employer-feedbacks/" element={<EmployerFeedbackForm />} />
          <Route path = "/employee-feedback-list/" element={<EmployeeFeedbackList />} />
          <Route path = "/employer-feedbacks-list/" element={<EmployerFeedbackList/>} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;

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
