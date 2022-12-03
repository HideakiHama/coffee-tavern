import { NavLink } from 'react-router-dom';

function Nav() {
  return (
  <nav>
  <div className="nav-wrapper teal">
    <a href="#" class="brand-logo right">Logo</a>
        <ul id="nav-mobile" className="left hide-on-med-and-down">
            <li><NavLink className="dropdown-item" aria-current="page" to="/api/accounts">Signup</NavLink></li>
            <li><NavLink className="dropdown-item" aria-current="page" to="/token">Login</NavLink></li>
            <li><NavLink className="dropdown-item" aria-current="page" to="/upload_resume/">Upload Resume</NavLink></li>
            <li><NavLink className="dropdown-item" aria-current="page" to="/create_form">Create Job Post</NavLink></li>
            <li><NavLink className="dropdown-item" aria-current="page" to="/get_all_form">Board of Jobs</NavLink></li>
            <li><NavLink className="dropdown-item" aria-current="page" to="/employee-feedbacks/">Employee Feedback Form</NavLink></li>
            <li><NavLink className="dropdown-item" aria-current="page" to="/employee-feedbacks-list/">Past Employee Feedbacks</NavLink></li>
            <li><NavLink className="dropdown-item" aria-current="page" to="/employee-feedbacks/">Employee Feedback Form</NavLink></li>
            <li><NavLink className="dropdown-item" aria-current="page" to="/employee-feedbacks-list/">Past Employee Feedbacks</NavLink></li>
            <li><NavLink className="dropdown-item" aria-current="page" to="/api/accounts">Signup</NavLink></li>
        </ul>
    </div>
    </nav>
     )
}
export default Nav;