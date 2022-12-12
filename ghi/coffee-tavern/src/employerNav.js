import { useAuthContext } from './useToken';
import { NavLink } from 'react-router-dom';
import jwt_decode from "jwt-decode";



const EmployerNav = () => {

    const { token } = useAuthContext();
    if (token) {
      const decoded = jwt_decode(token)
      const isEmployer = decoded.account["role"]
      if (isEmployer === "Employer") {
        return (

        <>
        <li><NavLink className="dropdown-item" aria-current="page" to="/create_form">Create Job Post</NavLink></li>
        <li><NavLink className="dropdown-item" aria-current="page" to="/employer-feedback">Send Feedback</NavLink></li>
        <li><NavLink className="dropdown-item" aria-current="page" to="/employer-feedbacks-list">My Past Feedbacks</NavLink></li>
        <li><NavLink className="dropdown-item" aria-current="page" to="/employee-profile-list">Employee Profiles</NavLink></li>
        <li><NavLink className="dropdown-item" aria-current="page" to="/user/current/profile">My Profile</NavLink></li>
        <li><NavLink className="dropdown-item" aria-current="page" to="/applicants">My Applicants</NavLink></li>
        <li><NavLink className="dropdown-item" aria-current="page" to="/create_tag_form">Tags</NavLink></li>
        </>

        )
        }
      }

}

export default EmployerNav