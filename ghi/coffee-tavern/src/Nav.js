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
        </ul>
    </div>
    </nav>
    )
}
export default Nav;
