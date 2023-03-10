import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';
import { useLocation, useNavigate } from "react-router-dom";
import FadeLoader from "react-spinners/FadeLoader";

//Editing their previous feedback to employees
function EmployerFeedbackEdit(){

  const location = useLocation();
  const id = location.state.id
  //Handles getting the data from the specific employee ID
  const [employee, setEmployee] = useState([]);
  const [loading, setLoading] = useState(false)
  const { token } = useAuthContext();
  const navigate = useNavigate();

  useEffect(() => {
    setLoading(true)
    setTimeout(() =>{
      setLoading(false)
    }, 1000)}, [])

 //Getting the user's feedback to employee
  useEffect(() =>{
    const getEmployerFeedbacksUrl = async () => {
      if (token) {
      const EmployerFeedback_id = id                        //Temporary Employer ID
      const response = await axios.get(`${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/employer-feedback-form/${EmployerFeedback_id}`,
      {headers: { Authorization: `Bearer ${token}`}});
      setEmployee(response.data)}};
    getEmployerFeedbacksUrl();
  }, [token, id]);


    const [inputs, setInputs] = useState({employee_name: ''
                                          , date: ''
                                          , description:''
                                          });

    // Editing Form
    const handleEdit = async (event,EmployerFeedback_id) => {
      event.preventDefault();
      EmployerFeedback_id = id                            //Temporary Employer ID

      if(!(inputs["employee_name"])){
        inputs["employee_name"] = employee.employee_name
      }if(!(inputs["date"])){
        inputs["date"] = employee.date
      }if(!(inputs["description"])){
        inputs["description"] = employee.description
      }

      const { employee_name, date, description } = inputs;
      const submit = { employee_name, date, description } ;
      await axios.put(`${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/employer-feedback-form/${EmployerFeedback_id}`, submit,
      {headers: { Authorization: `Bearer ${token}`}})
      setInputs({employee_name:'', date: '', description:''})
      setEmployee({employee_name:'', date: '', description:''})

      navigate("/employer-feedbacks-list")
    }

    // Response to the input change
    const handleInputChange = (event) => {
      event.persist();

        setInputs(inputs => ({                         //setInputs
        ...inputs,
        [event.target.name]: event.target.value}));  //key: value of each value
    }

    // Delete Form
    const handleDelete = async (EmployerFeedback_id) => {
      EmployerFeedback_id = id                            //Temporary Employer ID
      await axios.delete(
        `${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/employer-feedback-form/${EmployerFeedback_id}`,
        {headers: { Authorization: `Bearer ${token}`}})
        setInputs({employee_name:'', date: '', description:''})
        setEmployee({employee_name:'', date: '', description:''})

        navigate("/employer-feedbacks-list")
        }

    // Go back to the their employer list
    const handleGoBack =  async () => {
      navigate("/employer-feedbacks-list")
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
      <div className="row">
        <h2>Edit My Feedback to {employee.employee_name}</h2>
        <form className="col s12" onSubmit={handleEdit}>
          <div className="row">
            <div className="form-floating col s6">
              <input  type="text" name ="employee_name" onChange={handleInputChange}
              value ={inputs["employee_name"]} placeholder = {employee.employee_name}></input>
              <label>Employee Name</label>
            </div>
            <div className="form-floating col s6">
              <input type="text" name ="date" onChange={handleInputChange}
              value ={inputs["date"]} placeholder = {employee.date}></input>
              <label >Date</label>
            </div>
          </div>
          <div className="row">
          </div>
          <div className="row">
            <div className="form-floating col s12">
              <input  type="text" name="description" onChange={handleInputChange}
              value ={inputs["description"]}  placeholder = {employee.description} ></input>
              <label>Feedback Description</label>
            </div>
          </div>
          <div className="row">
            <div className="col s12">
              <div className="input-field inline">
                  <button className="btn waves-effect teal" type="submit" name="action">Update
                            <i className="material-icons right">Feedback</i>
                  </button>
              </div>
            </div>
          </div>
        </form>
        <button onClick={handleDelete} className="btn waves-effect teal">Delete
                            <i className="material-icons right">Feedback</i>
      </button>
        <button onClick={handleGoBack} className="btn waves-effect teal">Go
                            <i className="material-icons right">Back</i>
      </button>
    </div>
    }
    </div>
    );
}
export default EmployerFeedbackEdit
