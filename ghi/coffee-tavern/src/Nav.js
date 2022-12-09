import { NavLink } from 'react-router-dom';
import Testing from './logout';
import EmployeeNav from './employeeNav';
import EmployerNav from './employerNav';

function Nav() {

  return (
  <nav>
  <div className="nav-wrapper teal">
    {/* <a className="brand-logo right">Logo</a> */}
        <ul id="nav-mobile" className="left hide-on-med-and-down">
            <li><NavLink className="dropdown-item" aria-current="page" to="/">Home</NavLink></li>
            <Testing />
            <EmployerNav />
            <EmployeeNav />
            <li><NavLink className="dropdown-item" aria-current="page" to="/user/employee">My Profile</NavLink></li>
            <li><NavLink className="dropdown-item" aria-current="page" to="/create_tag_form">Tags</NavLink></li>
            <li><NavLink className="dropdown-item" aria-current="page" to="/employee-profile-list">Employee Profile List</NavLink></li>
            <li><NavLink className="dropdown-item" aria-current="page" to="/applicants">My Applicants</NavLink></li>
        </ul>
    </div>
    </nav>
     )
}
export default Nav;
