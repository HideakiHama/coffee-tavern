import 'materialize-css/dist/css/materialize.min.css'
import jwt_decode from 'jwt-decode';
import {useEffect, useState} from 'react';
import { useAuthContext } from '../useToken';
import { useNavigate } from "react-router-dom";

function EmployerInfoFormCreate({id}) {

    const [companyName, setCompanyName] = useState('')
    const [jobType, setJobType] = useState('')
    const [location, setLocation] = useState('')
    const [about, setAbout] = useState('')
    const [pic, setPic] = useState('')
    const navigate = useNavigate();

    const [decodedId, setDecodedId] = useState('')

    const { token } = useAuthContext();

    useEffect(() => {
        console.log("token2", token)
        const getDecodedId = () => {
            const decoded = jwt_decode(token)
            setDecodedId(decoded.account["id"])
        }
        if (token) {
            getDecodedId()
        }
    }, [token])

    const handleSubmit = async (event) => {
        event.preventDefault();
        const data = {
            "company_name": companyName,
            "job_type": jobType,
            "location": location,
            "about": about,
            "pic_url": pic
        }

        const employerInfoURL = `http://localhost:8000/users/${decodedId}/create_employer_info`

        const fetchConfig = {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`
            },
        }
        const response = await fetch(employerInfoURL, fetchConfig)

        if (response.ok) {
            console.log("submit worked")
            navigate("/user/current/profile");
        } else {
            console.log("submit didn't work", response)
        }
    }

    return (
        <div className="row">
            <form className="col s12" onSubmit={handleSubmit}>
                <div className="row">
                    <div className="form-floating col s6">
                        <input placeholder="Company Name" type="text" name="company_name" value={companyName} id="company_name" onChange={e => setCompanyName(e.target.value)}>
                        </input>
                    </div>
                    <div className="form-floating col s6">
                        <input placeholder="Type of Company" type="text" name="job_type" value={jobType} id="job_type" onChange={e => setJobType(e.target.value)}>
                        </input>
                    </div>
                </div>
                <div className="row">
                    <div className="form-floating col s6">
                        <input placeholder="Location" type="text" name="location" value={location} id="location" onChange={e => setLocation(e.target.value)}>
                        </input>
                    </div>
                    <div className="form-floating col s6">
                        <input placeholder="About" type="text" name="about" value={about} id="about" onChange={e => setAbout(e.target.value)}>
                        </input>
                    </div>
                </div>
                <div className="row">
                    <div className="form-floating col s6">
                        <input placeholder="Profile Picture URL"type="text" name="pic_url" value={pic} id="pic_url" onChange={e => setPic(e.target.value)}>
                        </input>
                    </div>
                </div>
                <div className="row">
                    <div className="col s12">
                        <div className="input-field inline">
                            <button className="btn waves-effect waves-light" type="submit" name="action">
                                Submit Information
                            </button>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    )
}

export default EmployerInfoFormCreate;