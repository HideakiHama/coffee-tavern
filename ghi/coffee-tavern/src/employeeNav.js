import { useAuthContext } from './useToken';
import { NavLink } from 'react-router-dom';
import jwt_decode from "jwt-decode";



const EmployeeNav = () => {

    const { token } = useAuthContext();
    if (token) {
      const decoded = jwt_decode(token)
      const isEmployee = decoded.account["role"]
      if (isEmployee === "Employee") {
        return (

        <>
        <li><NavLink className="dropdown-item" aria-current="page" to="/get_all_form">Board of Jobs</NavLink></li>
        <li><NavLink className="dropdown-item" aria-current="page" to="/employee-feedback">Create Feedback</NavLink></li>
        <li><NavLink className="dropdown-item" aria-current="page" to="/employee-feedbacks-list">My Past Feedbacks</NavLink></li>
        </>

        )
        }
      }

}

export default EmployeeNav