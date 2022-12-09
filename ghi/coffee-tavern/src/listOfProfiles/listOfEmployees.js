import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';
import { useNavigate } from 'react-router-dom';
// import jwt_decode from "jwt-decode";


function EmployeeProfileList() {
    const [employeeProfiles, setEmployeeProfiles] = useState([]);
    const { token } = useAuthContext();


    //Navigate to the individual profile and carry the id data with it
    const navigate = useNavigate();
    const employeeFeedbackEdit = (account_id) => {
      console.log("###ID###", account_id)
      navigate("/other-employee-profile", {state:{account_id:account_id}});
    };



    useEffect(() =>{
      const getEmployeeFeedbacksUrl = async () => {
        if (token){
        const response = await axios.get(`http://localhost:8000/get_all_employee_profile`,
        {headers: { Authorization: `Bearer ${token}`}});
        setEmployeeProfiles(response.data)}};
      getEmployeeFeedbacksUrl();
    }, [token]);




    return (
      <div>
        <h2>List of Employees</h2>
        <table>
          <thead>
            <tr>
              <th>Candidates</th>
              <th>Career Field</th>
              <th>Location</th>
            </tr>
          </thead>
          <tbody>
            {employeeProfiles && employeeProfiles.map(employeeProfile =>
              <tr key={employeeProfile.account_id}>
                <td>{employeeProfile.full_name}</td>
                <td>{employeeProfile.location}</td>
                <td>{employeeProfile.career_title}</td>

                <td><button onClick={() => employeeFeedbackEdit(employeeProfile.account_id)}>Check Profile</button></td>
              </tr>
              )}
          </tbody>
        </table>
      </div>

    )
}
export default EmployeeProfileList