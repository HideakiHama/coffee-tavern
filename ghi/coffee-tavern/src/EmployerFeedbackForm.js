import React, {useState, useEffect} from 'react';
// import axios from "axios"

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
      <div>
        <h1>Employer Feedback Form</h1>
        <form onSubmit={handleSubmit}>
          <div>
            <label>Employee Name</label>
            <input type="text" name="EmployeeName" onChange={handleInputChange}
            value ={inputs['EmployeeName']} required />
          </div>
          <div>
            <label>Date</label>
            <input type="date" name="Date" onChange={handleInputChange}
            value ={inputs["Date"]} required />
          </div>
          <div>
            <label>Description</label>
            <input type="text" name="Description" onChange={handleInputChange}
            value ={inputs["Description"]} required />
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>

    )
}
export default EmployerFeedbackForm
