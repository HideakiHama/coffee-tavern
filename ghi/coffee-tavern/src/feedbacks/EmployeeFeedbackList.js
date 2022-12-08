import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';
import { useNavigate } from 'react-router-dom';
import jwt_decode from "jwt-decode";


function EmployeeFeedbackList() {
    const [employee, setEmployee] = useState([]);
    const { token } = useAuthContext();

    const navigate = useNavigate();
    const employeeFeedbackEdit = (id) => {
      console.log("###ID###", id)
      navigate("/employee-feedback-update", {state:{id:id}});
    };

    // const deleteFeedback = async (EmployeeFeedback_id, token) => {
    //   EmployeeFeedback_id = 1
    //                      //Temporary Employee ID
    //   await axios.delete(
    //     `http://localhost:8000/employee-feedback-form/${EmployeeFeedback_id}`
    //     , {headers: { Authorization: `Bearer ${token}`}})
    // }

    //NEED TO FIX THIS
    useEffect(() =>{
      getEmployeeFeedbacksUrl();
    }, []);

    const getEmployeeFeedbacksUrl = async () => {
      const decoded = jwt_decode(token)
      const account_id = decoded.account["id"]   //Decode jwt token to get User ID
      const response = await axios.get(`http://localhost:8000/employee-feedbacks/${account_id}`,
      {headers: { Authorization: `Bearer ${token}`}});
      setEmployee(response.data)};

    return (
      <div>
        <h1>My past feedbacks</h1>
        <table>
          <thead>
            <tr>
              <th>Employer's name</th>
              <th>id</th>
              <th>Date</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {employee && employee.map(employee =>
              <tr key={employee.id}>
                <td>{employee.employer_name}</td>
                <td>{employee.id}</td>
                <td>{employee.date}</td>
                <td>{employee.description}</td>

                <td><button onClick={() => employeeFeedbackEdit(employee.id)}>Edit</button></td>
              </tr>
              )}
          </tbody>
        </table>
      </div>

    )
}
export default EmployeeFeedbackList
