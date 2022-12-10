import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';
import { useNavigate } from 'react-router-dom';
// import jwt_decode from "jwt-decode";


function EmployerProfileList() {
    const [employerProfiles, setEmployerProfiles] = useState([]);
    const { token } = useAuthContext();


    //Navigate to the individual profile and carry the id data with it
    const navigate = useNavigate();
    const employerFeedbackEdit = (account_id) => {
      console.log("###ID###", account_id)
      navigate("/other-employer-profile", {state:{account_id:account_id}});
    };



    useEffect(() =>{
      const getEmployerFeedbacksUrl = async () => {
        if (token){
        const response = await axios.get(`${process.env.REACT_APP_TAGS_API_HOST}/get_all_employer_profile`,
        {headers: { Authorization: `Bearer ${token}`}});
        setEmployerProfiles(response.data)}};
      getEmployerFeedbacksUrl();
    }, [token]);




    return (
      <div>
        <h2>List of Employers</h2>
        <table>
          <thead>
            <tr>
              <th>Company</th>
              <th>Job Type</th>
              <th>Location</th>
            </tr>
          </thead>
          <tbody>
            {employerProfiles && employerProfiles.map(employerProfile =>
              <tr key={employerProfile.account_id}>
                <td>{employerProfile.company_name}</td>
                <td>{employerProfile.job_type}</td>
                <td>{employerProfile.location}</td>

                <td><button onClick={() => employerFeedbackEdit(employerProfile.account_id)}>Check Profile</button></td>
              </tr>
              )}
          </tbody>
        </table>
      </div>

    )
}
export default EmployerProfileList