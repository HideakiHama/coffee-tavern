import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';
import { useLocation, useNavigate  } from "react-router-dom";
import FadeLoader from "react-spinners/FadeLoader";

//Employer checking Employee's list of feedbacks
function AllEmployeeFeedback(){
  const [employees, setEmployees] = useState([])
  const [loading, setLoading] = useState(false)
  const { token } = useAuthContext();
  const location = useLocation();
  const employee_name = location.state.employee_name
  const navigate = useNavigate();

  useEffect(() => {
    setLoading(true)
    setTimeout(() =>{
      setLoading(false)
    }, 5000)}, [])

  useEffect(() =>{
      // Getting Employee's Feedback from all the Employer
    const getAllEmployerFeedbackUrl = async () => {
    if (token){
    const response = await axios.get(`${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/get_all_employerFeedbacks`,
    {headers: { Authorization: `Bearer ${token}`}});
    setEmployees(response.data)}};
    getAllEmployerFeedbackUrl();
  }, [token]);

  const handleGoBack =  async () => {
    navigate("/employer-feedbacks-list")
  };


  return (
    <div>
    {loading?
    <div className="sweet-loading">
        <FadeLoader
        color={'#36d7b7'}
        loading={loading}
        size={200}

      />
      </div>
       :
    <div>
      <h2>Everyone's Feedbacks to {employee_name}</h2>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Description</th>
            <th><button onClick={handleGoBack} className="btn waves-effect waves-light">Go Back
              </button></th>
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
  }
    </div>
  )
}export default AllEmployeeFeedback
