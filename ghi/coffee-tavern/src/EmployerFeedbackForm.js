import React, {useState, useEffect} from 'react';
// import axios from "axios"
// import M from 'materialize-css';
import 'materialize-css/dist/css/materialize.min.css'

function EmployerFeedbackForm() {
    const useFeedbackForm = (initState) => {

      const [inputs, setInputs] = useState(initState);

      const handleSubmit = (event) => {
        // if (event) {
        event.preventDefault();
        alert(`Employee!
        Name: ${inputs['EmployeeName']}
        Date: ${inputs["Date"]}
        Description: ${inputs["Description"]}`)
    }

    const handleInputChange = (event) => {
      event.persist();
      setInputs(inputs => ({                         //setInputs
        ...inputs,
        [event.target.name]: event.target.value}));  //key: value of each value
    }

    return {
      handleSubmit,
      handleInputChange,
      inputs
      };
    }


  // Creating initial state
    const initState = { EmployeeName: '', Date: '', Description:'' }

    const {inputs, handleInputChange, handleSubmit} = useFeedbackForm(initState);

      return (
        <div className="row">
          <form className="col s12" onSubmit={handleSubmit}>
            <div className="row">
              <div className="input-field col s6">
                <label>Employee Name</label>
                <input type="text" onChange={handleInputChange} required></input>
              </div>
              <div className="input-field col s6">
                <input id="last_name" type="text" ></input>
                <label >Date</label>
              </div>
            </div>
            <div className="row">
            </div>
            <div className="row">
              <div className="input-field col s12">
                <input id="email" type="email" ></input>
                <label>Feedback Description</label>
              </div>
            </div>
            <div className="row">
              <div className="col s12">             
                <div className="input-field inline">
              
                    <button className="btn waves-effect waves-light" type="submit" name="action">Submit
                              <i className="material-icons right">Feedback</i>
                    </button>
                </div>
              </div>
            </div>
          </form>
      </div>
      );
    }
    

    
 export default EmployerFeedbackForm
