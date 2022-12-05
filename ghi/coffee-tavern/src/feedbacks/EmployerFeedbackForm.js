import React, {useState } from 'react';
import axios from "axios"
// import M from 'materialize-css';
import 'materialize-css/dist/css/materialize.min.css'



function EmployerFeedbackForm() {

    const [inputs, setInputs] = useState({employee_name: ''
                                          , date: ''
                                          , description:''
                                          });


    const account_id = 2

    const handleSubmit = async (event) => {
      event.preventDefault();
      const { employee_name, date, description } = inputs;
      const submit = { employee_name, date, description } ;
      const response = await axios.post(`http://localhost:8000/employer-feedback-form/${account_id}`, submit) //account_id 2
      setInputs({employee_name: '', date: '', description:''})
    }

      const handleInputChange = (event) => {
      event.persist();
        setInputs(inputs => ({                         //setInputs
        ...inputs,
        [event.target.name]: event.target.value}));  //key: value of each value
    }

      return (
        <div className="row">
          <form className="col s12" onSubmit={handleSubmit}>
            <div className="row">
              <div className="form-floating col s6">
                <input type="text" name ="employee_name" onChange={handleInputChange}
                value ={inputs['employee_name']} required></input>

                <label>Employee Name</label>
              </div>
              <div className="form-floating col s6">
                <input type="text" name ="date" onChange={handleInputChange}
                value ={inputs["date"]} required></input>
                <label >Date</label>
              </div>
            </div>
            <div className="row">
            </div>
            <div className="row">
              <div className="form-floating col s12">
                <input  type="text" name="description" onChange={handleInputChange}
                value ={inputs["description"]} required ></input>
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
