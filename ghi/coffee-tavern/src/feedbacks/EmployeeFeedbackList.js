import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';
import { useNavigate } from 'react-router-dom';
import jwt_decode from "jwt-decode";


function EmployeeFeedbackList() {
    const [employee, setEmployee] = useState([]);
    const { token } = useAuthContext();
    const navigate = useNavigate();

    //Transfer ID Data to Feedback edit Link
    const employeeFeedbackEdit = (id) => {
      navigate("/employee-feedback-update", {state:{id:id}});
    };

    //Transfer Employer Name to All Feedback Link
    const allEmployerFeedback = (employer_name) => {
      console.log("EMPLOYER NAME",employer_name)
      navigate("/all-employer-feedback", {state:{employer_name:employer_name}})
    }


    useEffect(() =>{
      const getEmployeeFeedbacksUrl = async () => {
        if (token) {
        const decoded = jwt_decode(token)
        const account_id = decoded.account["id"]   //Decode jwt token to get User ID
        const response = await axios.get(`http://localhost:8000/employee-feedbacks/${account_id}`,
        {headers: { Authorization: `Bearer ${token}`}});
        setEmployee(response.data)}};
      getEmployeeFeedbacksUrl();
    }, [token]);


    return (
      <div>
        <h2>My Past Feedbacks to Employer</h2>
        <table>
          <thead>
            <tr>
              <th>Employer's name</th>
              <th>Date</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {employee && employee.map(employee =>
              <tr key={employee.id}>
                <td>{employee.employer_name}</td>
                <td>{employee.date}</td>
                <td>{employee.description}</td>

                <td><button onClick={() => employeeFeedbackEdit(employee.id)}>Edit My Feedback</button></td>
                <td><button onClick={() => allEmployerFeedback(employee.employer_name)}>Check All Feedbacks</button></td>
              </tr>
              )}
          </tbody>
        </table>
      </div>

    )
}
export default EmployeeFeedbackList
