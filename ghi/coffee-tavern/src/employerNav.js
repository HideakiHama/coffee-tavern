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
        <li><NavLink className="dropdown-item" aria-current="page" to="/get_all_form">Board of Jobs</NavLink></li>
        <li><NavLink className="dropdown-item" aria-current="page" to="/create_form">Create Job Post</NavLink></li>
        <li><NavLink className="dropdown-item" aria-current="page" to="/employer-feedback">Create Feedback</NavLink></li>
        <li><NavLink className="dropdown-item" aria-current="page" to="/employer-feedbacks-list">My Past Feedbacks</NavLink></li>
        </>

        )
        }
      }

}

export default EmployerNav