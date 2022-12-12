import React, { useState, useEffect }  from 'react';
import axios from "axios";
import { useAuthContext } from '../useToken';
import { useLocation, useNavigate } from "react-router-dom";
import FadeLoader from "react-spinners/FadeLoader";

//Editing their previous feedback to employers
function EmployeeFeedbackEdit(){

  const location = useLocation();
  const id = location.state.id

  const [employer, setEmployer] = useState([]);
  const [loading, setLoading] = useState(false)
  const { token } = useAuthContext();
  const navigate = useNavigate();

  useEffect(() => {
    setLoading(true)
    setTimeout(() =>{
      setLoading(false)
    }, 1000)}, [])

  //Getting the user's feedback to employer
  useEffect(() =>{
    const getEmployeeFeedbacksUrl = async ( ) => {
      if (token) {
      const EmployeeFeedback_id = id
      const response = await axios.get(`${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/employee-feedback-form/${EmployeeFeedback_id}`,
      {headers: { Authorization: `Bearer ${token}`}});
      setEmployer(response.data)}};
    getEmployeeFeedbacksUrl();
  }, [token, id]);


    const [inputs, setInputs] = useState({employer_name: ''
                                          , date: ''
                                          , description:''
                                          });

    // Editing Form
    const handleEdit = async (event,EmployeeFeedback_id) => {
      event.preventDefault();
      EmployeeFeedback_id = id

      if(!(inputs["employer_name"])){
        inputs["employer_name"] = employer.employer_name
      }if(!(inputs["date"])){
        inputs["date"] = employer.date
      }if(!(inputs["description"])){
        inputs["description"] = employer.description
      }

      const { employer_name, date, description } = inputs;
      const submit = { employer_name, date, description } ;
      await axios.put(`${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/employee-feedback-form/${EmployeeFeedback_id}`, submit,
      {headers: { Authorization: `Bearer ${token}`}})
      setInputs({employer_name:'', date: '', description:''})
      setEmployer({employer_name:'', date: '', description:''})

      navigate("/employee-feedbacks-list")
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
      EmployeeFeedback_id = id                            //Temporary Employee ID
      await axios.delete(
        `${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/employee-feedback-form/${EmployeeFeedback_id}`
        , {headers: { Authorization: `Bearer ${token}`}})
      setInputs({employer_name:'', date: '', description:''})
      setEmployer({employer_name:'', date: '', description:''})

      navigate("/employee-feedbacks-list")
      }

    // Go back to the their employee list
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
      <div className="row">
        <h2>Edit My Feedback to {employer.employer_name}</h2>
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
export default EmployeeFeedbackEdit