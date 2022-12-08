import React, {useState } from 'react';
import axios from "axios"
// import M from 'materialize-css';
import 'materialize-css/dist/css/materialize.min.css'
import { useAuthContext } from '../useToken';


function EmployeeFeedbackForm() {

    const [inputs, setInputs] = useState({employer_name: ''
                                          , date: ''
                                          , description:''
                                          });
    const { token } = useAuthContext();

    const account_id = 1

    const handleSubmit = async (event) => {
      event.preventDefault();
      const { employer_name, date, description } = inputs;
      const submit = { employer_name, date, description } ;
      await axios.post(`http://localhost:8000/employee-feedback-form/${account_id}/`, submit,
      {headers: { Authorization: `Bearer ${token}`}})    //checks if the user logged in
      setInputs({employer_name: '', date: '', description:''})
    }

      const handleInputChange = (event) => {
      event.persist();

        setInputs(inputs => ({                         //setInputs
        ...inputs,
        [event.target.name]: event.target.value}));  //key: value of each value
    }

      return (
        <div className="row">
          <h1>Feedback form</h1>
          <form className="col s12" onSubmit={handleSubmit}>
            <div className="row">
              <div className="form-floating col s6">
                <input type="text" name ="employer_name" onChange={handleInputChange}
                value ={inputs['employer_name']} required></input>
                <label>Employer Name</label>
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


 export default EmployeeFeedbackForm