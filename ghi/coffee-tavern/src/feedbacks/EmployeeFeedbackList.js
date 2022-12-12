import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';
import { useNavigate } from 'react-router-dom';
import jwt_decode from "jwt-decode";
import FadeLoader from "react-spinners/FadeLoader";

function EmployeeFeedbackList() {
    const [employee, setEmployee] = useState([]);
    const [loading, setLoading] = useState(false)
    const { token } = useAuthContext();
    const navigate = useNavigate();

    //Transfer ID Data to Feedback edit Link
    const employeeFeedbackEdit = (id) => {
      navigate("/employee-feedback-update", {state:{id:id}});
    };

    //Transfer Employer Name to All Feedback Link
    const allEmployerFeedback = (employer_name) => {
      navigate("/all-employer-feedback", {state:{employer_name:employer_name}})
    }

    useEffect(() =>{
      const getEmployeeFeedbacksUrl = async () => {
        if (token) {
        const decoded = jwt_decode(token)
        const account_id = decoded.account["id"]   //Decode jwt token to get User ID
        const response = await axios.get(`${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/employee-feedbacks/${account_id}`,
        {headers: { Authorization: `Bearer ${token}`}});
        setEmployee(response.data)}};
      getEmployeeFeedbacksUrl();
    }, [token]);

    useEffect(() => {
      setLoading(true)
      setTimeout(() =>{
        setLoading(false)
      }, 1000)}, [])


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
                    <td><button onClick={() => employeeFeedbackEdit(employee.id)} className="btn waves-effect teal">Edit My Feedback</button></td>
                    <td><button onClick={() => allEmployerFeedback(employee.employer_name)} className="btn waves-effect waves-light teal">Check All Feedbacks</button></td>
                  </tr>
                  )}
              </tbody>

            </table>

            </div>
}
          </div>
    )
}
export default EmployeeFeedbackList
