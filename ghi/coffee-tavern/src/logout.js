import { useAuthContext } from './useToken';
import { NavLink } from 'react-router-dom';


const Testing = () => {
    const { token } = useAuthContext();

    if (token) {
        return (<NavLink className="dropdown-item" aria-current="page" to="/token">logout</NavLink>)
    }else{
        return (<NavLink className="dropdown-item" aria-current="page" to="/token">Login</NavLink>)
    }

}

export default Testing
