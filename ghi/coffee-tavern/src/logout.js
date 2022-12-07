import { useAuthContext } from './useToken';
import { NavLink } from 'react-router-dom';


const Testing = () => {
    const { token } = useAuthContext();

    if (token) {
        return (
        <li>
        <NavLink className="dropdown-item" aria-current="page" to="/token">logout</NavLink>
        </li>
        )
    }else{
        return (
        <>
        <li>
        <NavLink className="dropdown-item" aria-current="page" to="/token">Login</NavLink>
        </li>
        <li>
        <NavLink className="dropdown-item" aria-current="page" to="/api/accounts">Signup</NavLink>
        </li>
        </>
        )
    }

}

export default Testing
