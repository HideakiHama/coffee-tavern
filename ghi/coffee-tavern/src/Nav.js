import { NavLink } from 'react-router-dom';
import Testing from './logout';
import EmployeeNav from './employeeNav';
import EmployerNav from './employerNav';
import 'bootstrap/dist/css/bootstrap.min.css';
// import 'materialize-css/dist/css/materialize.min.css'

function Nav() {

  return (
    <nav>
        <div className="nav-wrapper teal">
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