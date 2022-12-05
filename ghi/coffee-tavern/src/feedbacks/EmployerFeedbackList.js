import React, { useState, useEffect }  from 'react';
import axios from "axios";




function EmployerFeedbackList() {
    const [employer, setEmployer] = useState([]);

    useEffect(() =>{
      getEmployerFeedbacksUrl();
    }, []);

    const getEmployerFeedbacksUrl = async (account_id) => {
      account_id = 2
      const response = await axios.get(`http://localhost:8000/employer-feedbacks/${account_id}`);
      setEmployer(response.data)};

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
            {employer && employer.map(employer =>
              <tr key={employer.id}>
                <td>{employer.id}</td>
                <td>{employer.date}</td>
                <td>{employer.description}</td>
              </tr>
              )}
          </tbody>
        </table>
      </div>

    )
}
export default EmployerFeedbackList
