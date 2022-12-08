import { NavLink } from 'react-router-dom';
// import Testing from './logout';

function Nav() {

  return (
  <nav>
    <div className="nav-wrapper teal">
      {/* <a className="brand-logo right">Logo</a> */}
          <ul id="nav-mobile" className="left hide-on-med-and-down">
              <li><NavLink className="dropdown-item" aria-current="page" to="/">Home</NavLink></li>
              <li><NavLink className="dropdown-item" aria-current="page" to="/api/accounts">Signup</NavLink></li>
              <li><NavLink className="dropdown-item" aria-current="page" to="/upload_resume/">Upload Resume</NavLink></li>
              <li><NavLink className="dropdown-item" aria-current="page" to="/create_form">Create Job Post</NavLink></li>
              <li><NavLink className="dropdown-item" aria-current="page" to="/get_all_form">Board of Jobs</NavLink></li>
              <li><NavLink className="dropdown-item" aria-current="page" to="/employer-feedback">Employer Feedback Form</NavLink></li>
              <li><NavLink className="dropdown-item" aria-current="page" to="/employer-feedbacks-list">Past Employer Feedbacks</NavLink></li>
              <li><NavLink className="dropdown-item" aria-current="page" to="/employer-feedback-update">Edit Employer Feedbacks</NavLink></li>
              <li><NavLink className="dropdown-item" aria-current="page" to="/employee-feedback">Employee Feedback Form</NavLink></li>
              <li><NavLink className="dropdown-item" aria-current="page" to="/employee-feedbacks-list">Past Employee Feedbacks</NavLink></li>
              <li><NavLink className="dropdown-item" aria-current="page" to="/employee-feedback-update">Edit Employee Feedbacks</NavLink></li>
              <li><NavLink className="dropdown-item" aria-current="page" to="/create_tag_form">Tags</NavLink></li>
          </ul>
      </div>
    </nav>
     )
}
export default Nav;
