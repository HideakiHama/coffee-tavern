import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';
import { useLocation, useNavigate } from "react-router-dom";
import FadeLoader from "react-spinners/FadeLoader";

//Employee checking Employer's list of feedbacks
function AllEmployerFeedback(){
  const [employers, setEmployers] = useState([])
  const [loading, setLoading] = useState(false)
  const { token } = useAuthContext();
  const location = useLocation();
  const employer_name = location.state.employer_name
  const navigate = useNavigate();

  useEffect(() => {
    setLoading(true)
    setTimeout(() =>{
      setLoading(false)
    }, 1000)}, [])

  useEffect(() =>{
      // Getting Employer's Feedback from all the Employee
      const getAllEmployeeFeedbackUrl = async () => {
      if (token){
      const response = await axios.get(`${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/get_all_employeeFeedbacks`,
    {headers: { Authorization: `Bearer ${token}`}});
      setEmployers(response.data)}};
      getAllEmployeeFeedbackUrl();
  }, [token]);

  const handleGoBack =  async () => {
    navigate("/employee-feedbacks-list")
  };


  return (
    <div>
    {loading?
    <div className="d-flex justify-content-center p-5">
        <FadeLoader
        color={'#36d7b7'}
        loading={loading}
        size={200}

      />
      </div>
       :
    <div>
      <h2>Everyone's Feedbacks to {employer_name}</h2>
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
          {employers && employers.filter(employers => employers.employer_name.toLowerCase().includes(employer_name.toLowerCase())).map(employer =>
            <tr key={employer.id}>
              <td>{employer.date}</td>
              <td>{employer.description}</td>
            </tr>
            )}
        </tbody>
      </table>
    </div>
  }
  </div>
  )
}export default AllEmployerFeedback