import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';
import { useNavigate } from 'react-router-dom';
import jwt_decode from "jwt-decode";


function EmployerFeedbackList() {
    const [employer, setEmployer] = useState([]);
    const { token } = useAuthContext();

    const navigate = useNavigate();
    const employerFeedbackEdit = (id) => {
      navigate("/employer-feedback-update", {state:{id:id}});
    };


    //Transfer Employer Name to All Feedback Link
    const allEmployerFeedback = (employee_name) => {
      navigate("/all-employee-feedback", {state:{employee_name:employee_name}})
    }


    useEffect(() =>{
      getEmployerFeedbacksUrl();
    }, []);

    const getEmployerFeedbacksUrl = async () => {
    const decoded = jwt_decode(token)
    const account_id = decoded.account["id"]   //Decode jwt token to get User ID
      const response = await axios.get(`http://localhost:8000/employer-feedbacks/${account_id}`,
      {headers: { Authorization: `Bearer ${token}`}});
      setEmployer(response.data)};

    return (
      <div>
        <h1>My past feedbacks</h1>
        <table>
          <thead>
            <tr>
              <th>Employee's name</th>
              <th>Date</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {employer && employer.map(employer =>
              <tr key={employer.id}>
                <td>{employer.employee_name}</td>
                <td>{employer.date}</td>
                <td>{employer.description}</td>
                <td><button onClick={() => employerFeedbackEdit(employer.id)}>Edit</button></td>
                <td><button onClick={() => allEmployerFeedback(employer.employer_name)}>Check all feedbacks</button></td>
              </tr>
              )}
          </tbody>
        </table>
      </div>

    )
}
export default EmployerFeedbackList
