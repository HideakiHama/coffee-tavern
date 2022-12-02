import React, { useState, useEffect }  from 'react';
import axios from "axios";

const account_id = 1  /// props
const EmployerFeedbacksUrl = `http://localhost:8000/employer-feedbacks/${account_id}`

function EmployerFeedbackList() {
    const [employee, setEmployee] = useState([

      // {"id":3,"employee_name":"aki","date":"2022-12-02","description":"string","account_id":1},
      // {"id":7,"employee_name":"aki","date":"2022-12-02","description":"string","account_id":1},
      // {"id":8,"employee_name":"aki","date":"2022-12-02","description":"string","account_id":1},
      // {"id":9,"employee_name":"aki","date":"2022-12-02","description":"string","account_id":1},
      // {"id":10,"employee_name":"aki","date":"2022-12-02","description":"string","account_id":1}
    ]);

    useEffect(() =>{
      getEmployeeFeedbacksUrl();
    }, []);

    const getEmployeeFeedbacksUrl = async (account_id) => {
      const response = await axios.get(EmployerFeedbacksUrl);
      setEmployee(response.data)};

    return (
      <div>
        <h1>Employer List</h1>
        <table>
          <thead>
            <tr>
              <th>employer name</th>
              <th>date</th>
              <th>description</th>
            </tr>
          </thead>
          <tbody>
            {employee && employee.map(employee =>
              <tr key={employee.id}>
                <td>{employee.id}</td>
                <td>{employee.date}</td>
                <td>{employee.description}</td>
              </tr>
              )}
          </tbody>
        </table>
      </div>

    )
}
export default EmployerFeedbackList