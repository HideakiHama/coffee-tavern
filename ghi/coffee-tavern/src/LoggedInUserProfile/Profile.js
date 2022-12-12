import * as React from 'react';
import { useAuthContext } from '../useToken';
import EmployeeProfile from './Employee';
import EmployerProfile from './Employer';
import jwt_decode from 'jwt-decode';
import { useEffect, useState } from 'react';



const Profile = () => {
    const { token } = useAuthContext();
    const [account, setAccount] = useState({});

    useEffect(() => {
        if (token) {
            const decodedAccount = jwt_decode(token);
            setAccount(decodedAccount.account)
        }
    }, [token])

    if (!account.role) {
        return (
            <h3>Loading Profile</h3>
        )
    }

    return account.role === "Employee" ? (
        <EmployeeProfile id={account.id}/>
    ):(
        <EmployerProfile id={account.id}/>
    )
}

export default Profile;