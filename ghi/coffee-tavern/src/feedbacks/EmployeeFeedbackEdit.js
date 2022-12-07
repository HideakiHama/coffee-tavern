import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';

function EmployeeFeedbackEdit(){

  //Handles getting the data from the specific employer ID
  const [employer, setEmployer] = useState([]);
  const { token } = useAuthContext();

  useEffect(() =>{
    getEmployeeFeedbacksUrl();
  }, []);

  const getEmployeeFeedbacksUrl = async (EmployeeFeedback_id) => {
    EmployeeFeedback_id = 1                                   //Temporary Employee ID
    const response = await axios.get(`http://localhost:8000/employee-feedback-form/${EmployeeFeedback_id}`,
    {headers: { Authorization: `Bearer ${token}`}});
    setEmployer(response.data)};





    const [inputs, setInputs] = useState({employer_name: ''
                                          , date: ''
                                          , description:''
                                          });

    // Editing Form
    const handleEdit = async (event,EmployeeFeedback_id) => {
      event.preventDefault();
      EmployeeFeedback_id = 1                           //Temporary Employee ID

      if(!(inputs["employer_name"])){
        inputs["employer_name"] = employer.employer_name
      }if(!(inputs["date"])){
        inputs["date"] = employer.date
      }if(!(inputs["description"])){
        inputs["description"] = employer.description
      }

      const { employer_name, date, description } = inputs;
      const submit = { employer_name, date, description } ;
      await axios.put(`http://localhost:8000/employee-feedback-form/${EmployeeFeedback_id}`, submit,
      {headers: { Authorization: `Bearer ${token}`}})
      setInputs({employer_name:'', date: '', description:''})
      setEmployer({employer_name:'', date: '', description:''})
    }

    // Response to the input change
    const handleInputChange = (event) => {
      event.persist();

        setInputs(inputs => ({                         //setInputs
        ...inputs,
        [event.target.name]: event.target.value}));  //key: value of each value
    }

    // Delete Form
    const handleDelete = async (EmployeeFeedback_id) => {
      EmployeeFeedback_id = 1                            //Temporary Employee ID
      await axios.delete(
        `http://localhost:8000/employee-feedback-form/${EmployeeFeedback_id}`
        , {headers: { Authorization: `Bearer ${token}`}})
      setInputs({employer_name:'', date: '', description:''})
      setEmployer({employer_name:'', date: '', description:''})
      }


    return (
      <div className="row">
        <form className="col s12" onSubmit={handleEdit}>
          <div className="row">
            <div className="form-floating col s6">
              <input  type="text" name ="employer_name" onChange={handleInputChange}
              value ={inputs["employer_name"]}  placeholder = {employer.employer_name}></input>
              <label>Employer Name</label>
            </div>
            <div className="form-floating col s6">
              <input type="text" name ="date" onChange={handleInputChange}
              value ={inputs["date"]} placeholder = {employer.date}></input>
              <label>Date</label>
            </div>
          </div>
          <div className="row">
          </div>
          <div className="row">
            <div className="form-floating col s12">
              <input  type="text" name="description" onChange={handleInputChange}
              value ={inputs["description"]}  placeholder = {employer.description} ></input>
              <label>Feedback Description</label>
            </div>
          </div>
          <div className="row">
            <div className="col s12">
              <div className="input-field inline">
                  <button className="btn waves-effect waves-light" type="submit" name="action">Edit
                            <i className="material-icons right">Feedback</i>
                  </button>
              </div>
            </div>
          </div>
        </form>
        <div>
        <button onClick={handleDelete} className="btn waves-effect waves-light" type="submit" name="action">Delete
                            <i className="material-icons right">Feedback</i>
        </button>
        </div>
    </div>
    );

}
export default EmployeeFeedbackEdit