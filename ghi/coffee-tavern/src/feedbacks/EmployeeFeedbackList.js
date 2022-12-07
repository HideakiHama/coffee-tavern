import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';



function EmployeeFeedbackList() {
    const [employee, setEmployee] = useState([]);

    const { token } = useAuthContext();


    //NEED TO FIX THIS
    useEffect(() =>{
      getEmployerFeedbacksUrl();
    }, []);

    const getEmployerFeedbacksUrl = async (account_id) => {
      account_id = 1
      const response = await axios.get(`http://localhost:8000/employee-feedbacks/${account_id}`,
      {headers: { Authorization: `Bearer ${token}`}});
      setEmployee(response.data)};

    return (
      <div>
        <h1>Employee List</h1>
        <table>
          <thead>
            <tr>
              <th>employee name</th>
              <th>date</th>
              <th>description</th>
            </tr>
          </thead>
          <tbody>
            {employee && employee.map(employee =>
              <tr key={employee.id}>
                <td>{employee.employer_name}</td>
                <td>{employee.date}</td>
                <td>{employee.description}</td>
              </tr>
              )}
          </tbody>
        </table>
      </div>

    )
}
export default EmployeeFeedbackList
