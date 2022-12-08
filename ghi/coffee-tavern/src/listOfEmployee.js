import React, { useState, useEffect }  from 'react';
import axios from "axios";
// import { useAuthContext } from '../useToken';
import { useNavigate } from 'react-router-dom';
// import jwt_decode from "jwt-decode";


function EmployeeProfileList() {
    const [employeeProfiles, setEmployeeProfiles] = useState([]);
    // const { token } = useAuthContext();


    //Navigate to the individual profile
    const navigate = useNavigate();
    const employeeFeedbackEdit = (id) => {
      console.log("###ID###", id)
      navigate("/employee-feedback-update", {state:{id:id}});
    };


    //NEED TO FIX THIS
    useEffect(() =>{
      getEmployeeFeedbacksUrl();
    }, []);


    const getEmployeeFeedbacksUrl = async () => {
      const response = await axios.get(`http://localhost:8000/api/get_all_account`,);
      // {headers: { Authorization: `Bearer ${token}`}});
      setEmployeeProfiles(response.data)};

      console.log(employeeProfiles.map(employeeProfile => employeeProfile.role))
      console.log(employeeProfiles.filter(employeeProfile => employeeProfile.role.includes("Employer")))
    return (
      <div>
        <h1>List of Employee</h1>
        <table>
          <thead>
            <tr>
              <th>Employee's name</th>
              <th>ID</th>
              <th>Email</th>
              <th>Role</th>
            </tr>
          </thead>
          <tbody>
            {employeeProfiles && employeeProfiles.filter(employeeProfile => employeeProfile.role.includes("Employee")).map(employeeProfile =>
              <tr key={employeeProfile.id}>
                <td>{employeeProfile.user_name}</td>
                <td>{employeeProfile.id}</td>
                <td>{employeeProfile.email}</td>
                <td>{employeeProfile.role}</td>

                <td><button onClick={() => employeeFeedbackEdit(employeeProfile.id)}>Check Profile</button></td>
              </tr>
              )}
          </tbody>
        </table>
      </div>

    )
}
export default EmployeeProfileList