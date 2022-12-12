import 'materialize-css/dist/css/materialize.min.css'
import jwt_decode from 'jwt-decode';
import {useEffect, useState} from 'react';
import { useAuthContext } from '../useToken';
import { useNavigate } from "react-router-dom";


function EmployerInfoForm({id}) {

    const [companyName, setCompanyName] = useState('')
    const [jobType, setJobType] = useState('')
    const [location, setLocation] = useState('')
    const [about, setAbout] = useState('')
    const [pic, setPic] = useState('')
    const navigate = useNavigate();

    const { token } = useAuthContext();

    useEffect(() => {
        async function getEmployerInfo () {

            const decoded = jwt_decode(token)
            const id = decoded.account["id"]

            const infoURL = `${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/users/${id}/get_employer_info`

            const infoResponse = await fetch(infoURL, {
                method: "GET",
                headers: { Authorization: `Bearer ${token}`}
            })

            if (infoResponse.ok) {
                const info = await infoResponse.json()

                if (info) {
                    setCompanyName(info.company_name)
                    setJobType(info.job_type)
                    setLocation(info.location)
                    setAbout(info.about)
                    setPic(info.pic_url)
                }
            }
        }

        getEmployerInfo()

    }, [id, token])

    const handleSubmit = async (event) => {
        event.preventDefault();
        const data = {
            "company_name": companyName,
            "job_type": jobType,
            "location": location,
            "about": about,
            "pic_url": pic
        }

        const employerInfoURL = `${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/users/${id}/update_employer_info`

        const fetchConfig = {
            method: "PUT",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`
            },
        }
        const response = await fetch(employerInfoURL, fetchConfig)

        if (response.ok) {
            navigate("/user/current/profile");
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
                <a href="/user/current/profile">Back to Profile</a>
            </form>
        </div>
    )
}

export default EmployerInfoForm;
