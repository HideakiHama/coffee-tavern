import React, { useState, useEffect }  from 'react';
import axios from "axios";

function EmployerFeedbackEdit(){

  //Handles getting the data from the specific employee ID
  const [employee, setEmployee] = useState([]);

  useEffect(() =>{
    getEmployerFeedbacksUrl();
  }, []);

  const getEmployerFeedbacksUrl = async (EmployerFeedback_id) => {
    EmployerFeedback_id = 5
    const response = await axios.get(`http://localhost:8000/employer-feedback-form/${EmployerFeedback_id}`);
    setEmployee(response.data)};





    const [inputs, setInputs] = useState({employee_name: ''
                                          , date: ''
                                          , description:''
                                          });

    // Editing Form
    const handleEdit = async (event,EmployerFeedback_id) => {
      event.preventDefault();
      EmployerFeedback_id = 5     //Temporary Employer ID

      if(!(inputs["employee_name"])){
        inputs["employee_name"] = employee.employee_name
      }if(!(inputs["date"])){
        inputs["date"] = employee.date
      }if(!(inputs["description"])){
        inputs["description"] = employee.description
      }

      const { employee_name, date, description } = inputs;
      const submit = { employee_name, date, description } ;
      await axios.put(`http://localhost:8000/employer-feedback-form/${EmployerFeedback_id}`, submit) //account_id 2
      console.log("HANDLE SUBMIT")
      setInputs({employee_name:'', date: '', description:''})
      setEmployee({employee_name:'', date: '', description:''})
    }

    // Response to the input change
    const handleInputChange = (event) => {
      event.persist();
        console.log("HANDLE INPUT CHANGE")

        setInputs(inputs => ({                         //setInputs
        ...inputs,
        [event.target.name]: event.target.value}));  //key: value of each value
    }

    // Delete Form
    const handleDelete = async (EmployerFeedback_id) => {
      EmployerFeedback_id = 4
      await axios.delete(
        `http://localhost:8000/employer-feedback-form/${EmployerFeedback_id}`
        )}


    return (
      <div className="row">
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
export default EmployerFeedbackEdit
