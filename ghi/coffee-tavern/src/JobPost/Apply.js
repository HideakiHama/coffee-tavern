import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';
import { useNavigate } from 'react-router-dom';
import jwt_decode from "jwt-decode";


function Apply() {
    const [account, setAccount] = useState([]);
    const { token } = useAuthContext();
    console.log("ANYTHING")
    const navigate = useNavigate();
    console.log("HELLO")

    useEffect(() =>{
    const getApply = async ( ) => {
      if (token) {
      const response = await axios.get(`${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/get_applicants`,
      {headers: { Authorization: `Bearer ${token}`}});
      setAccount(response.data)}};
    getApply();
  }, [token]);



    return (
      <div>
        <h1>My Applicants</h1>
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>education</th>
              <th>Email</th>
            </tr>
          </thead>
          <tbody>
            {account.map(acc =>
              <tr key={acc.id}>
                <td>{acc["full_name"]}</td>
                <td>{acc["education"]}</td>
                <td>{acc["account_id"]["email"]}</td>
              </tr>
              )}
          </tbody>
        </table>
      </div>

    )
}
export default Apply
