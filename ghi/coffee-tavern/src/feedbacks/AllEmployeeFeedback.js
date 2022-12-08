import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';
import { useLocation } from "react-router-dom";

//Employer checking Employee's list of feedbacks
function AllEmployeeFeedback(){
  const [employees, setEmployees] = useState([])
  const { token } = useAuthContext();
  const location = useLocation();
  const employee_name = location.state.employee_name


  //NEED TO FIX THIS
  useEffect(() =>{
    getAllEmployerFeedbackUrl();
  }, []);


  // Getting Employee's Feedback from all the Employer
  const getAllEmployerFeedbackUrl = async () => {
    const response = await axios.get(`http://localhost:8000/get_all_employerFeedbacks`,);
    // {headers: { Authorization: `Bearer ${token}`}});
    setEmployees(response.data)};


  return (
    <div>
      <h1>List of feedbacks for {employee_name}</h1>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {employees && employees.filter(employees => employees.employee_name.toLowerCase().includes(employee_name.toLowerCase())).map(employee =>
            <tr key={employee.id}>
              <td>{employee.date}</td>
              <td>{employee.description}</td>
            </tr>
            )}
        </tbody>
      </table>
    </div>

  )
}export default AllEmployeeFeedback