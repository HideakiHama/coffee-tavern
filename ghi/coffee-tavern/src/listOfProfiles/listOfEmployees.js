import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';
import { useNavigate } from 'react-router-dom';
import FadeLoader from "react-spinners/FadeLoader";


function EmployeeProfileList() {
    const [employeeProfiles, setEmployeeProfiles] = useState([]);
    const [loading, setLoading] = useState(false)
    const { token } = useAuthContext();


    const navigate = useNavigate();
    const employeeFeedbackEdit = (account_id) => {
      navigate("/other-employee-profile", {state:{account_id:account_id}});
    };


    useEffect(() =>{
      const getEmployeeFeedbacksUrl = async () => {
        if (token){
        const response = await axios.get(`${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/get_all_employee_profile`,
        {headers: { Authorization: `Bearer ${token}`}});
        setEmployeeProfiles(response.data)}};
      getEmployeeFeedbacksUrl();
    }, [token]);

    useEffect(() => {
      setLoading(true)
      setTimeout(() =>{
        setLoading(false)
      }, 1000)}, [])


    return (
      <div>
            {loading?
      <div className="d-flex justify-content-center p-5">
        <FadeLoader
        color={'#36d7b7'}
        loading={loading}
        size={200}
      />
      </div>
       :
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
                <td><button className="btn waves-effect teal" onClick={() => employeeFeedbackEdit(employeeProfile.account_id)}>Check Profile</button></td>
              </tr>
              )}
          </tbody>
        </table>
      </div>
  }
</div>
    )

}
export default EmployeeProfileList
