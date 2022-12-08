import * as React from 'react';
import { useAuthContext } from '../useToken';
import EmployeeProfile from './Employee';
import EmployerProfile from './Employer';
import jwt_decode from 'jwt-decode';



const Profile = () => {
    const { token } = useAuthContext();
    const decoded = jwt_decode(token)
    const role = decoded.account["role"]

    return role === "Employee" ? (
        <EmployeeProfile/>
    ):(
        <EmployerProfile/>
    )
}

export default Profile;