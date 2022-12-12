 import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';
import { useNavigate } from 'react-router-dom';
import jwt_decode from "jwt-decode";
import FadeLoader from "react-spinners/FadeLoader";

function EmployerFeedbackList() {
    const [employer, setEmployer] = useState([]);
    const [loading, setLoading] = useState(false)
    const { token } = useAuthContext();
    const navigate = useNavigate();

    //Transfer ID Data to Feedback edit Link
    const employerFeedbackEdit = (id) => {
      navigate("/employer-feedback-update", {state:{id:id}});
    };


    //Transfer Employee Name to All Feedback Link
    const allEmployeeFeedback = (employee_name) => {
      navigate("/all-employee-feedback", {state:{employee_name:employee_name}})
    }

    useEffect(() => {
      setLoading(true)
      setTimeout(() =>{
        setLoading(false)
      }, 1000)}, [])

    useEffect(() =>{
      const getEmployerFeedbacksUrl = async () => {
        if (token) {
        const decoded = jwt_decode(token)
        const account_id = decoded.account["id"]   //Decode jwt token to get User ID
          const response = await axios.get(`${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/employer-feedbacks/${account_id}`,
          {headers: { Authorization: `Bearer ${token}`}});
          setEmployer(response.data)}};
      getEmployerFeedbacksUrl();
    }, [token]);



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
        <h2>My Past Feedbacks to Employee</h2>
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
                <td><button onClick={() => employerFeedbackEdit(employer.id)} className="btn waves-effect waves-light">Edit My Feedback</button></td>
                <td><button onClick={() => allEmployeeFeedback(employer.employee_name)} className="btn waves-effect waves-light">Check All Feedbacks</button></td>
              </tr>
              )}
          </tbody>
        </table>
      </div>
}
    </div>
    )
}
export default EmployerFeedbackList
