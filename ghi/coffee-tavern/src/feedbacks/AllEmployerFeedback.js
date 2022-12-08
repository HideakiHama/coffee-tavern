import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';
import { useLocation } from "react-router-dom";

//Employee checking Employer's list of feedbacks
function AllEmployerFeedback(){
  const [employers, setEmployers] = useState([])
  const { token } = useAuthContext();
  const location = useLocation();
  const employer_name = location.state.employer_name


  //NEED TO FIX THIS
  useEffect(() =>{
      // Getting Employer's Feedback from all the Employee
    if (token){
      const getAllEmployeeFeedbackUrl = async () => {
      const response = await axios.get(`http://localhost:8000/get_all_employeeFeedbacks`,);
    // {headers: { Authorization: `Bearer ${token}`}});
      setEmployers(response.data)
    };
    getAllEmployeeFeedbackUrl();
}}, [token]);


  // // Getting Employer's Feedback from all the Employee
  // const getAllEmployeeFeedbackUrl = async () => {
  //   const response = await axios.get(`http://localhost:8000/get_all_employeeFeedbacks`,);
  //   // {headers: { Authorization: `Bearer ${token}`}});
  //   setEmployers(response.data)};


  return (
    <div>
      <h1>List of feedbacks for {employer_name}</h1>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {employers && employers.filter(employers => employers.employer_name.toLowerCase().includes(employer_name.toLowerCase())).map(employer =>
            <tr key={employer.id}>
              <td>{employer.date}</td>
              <td>{employer.description}</td>
            </tr>
            )}
        </tbody>
      </table>
    </div>

  )

}export default AllEmployerFeedback