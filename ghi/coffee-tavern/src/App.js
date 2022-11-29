import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
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
      </header>
    </div>
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
