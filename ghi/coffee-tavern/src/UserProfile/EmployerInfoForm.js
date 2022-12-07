import {useEffect, useState} from 'react';
import { useAuthContext } from '../useToken';

function EmployerInfoForm({id}) {
    // const [employerInfo, setEmployerInfo] = useState('')
    const [companyName, setCompanyName] = useState('')
    const [jobType, setJobType] = useState('')
    const [location, setLocation] = useState('')
    const [about, setAbout] = useState('')

    const { token } = useAuthContext();

    useEffect(() => {
        async function getEmployerInfo () {
            const infoURL = `http://localhost:8000/users/${id}/get_employer_info`

            const infoResponse = await fetch(infoURL, {
                method: "GET",
                headers: { Authorization: `Bearer ${token}`}
            })

            if (infoResponse.ok) {
                const info = await infoResponse.json()
                console.log(info)
                // setEmployerInfo(info)
                if (info) {
                    setCompanyName(info.company_name)
                    setJobType(info.job_type)
                    setLocation(info.location)
                    setAbout(info.about)
                }
            }
        }

        getEmployerInfo()

    }, [id])

    const handleSubmit = async (event) => {
        event.preventDefault();
        const data = {
            "company_name": companyName,
            "job_type": jobType,
            "location": location,
            "about": about
        }
        console.log(data)
        const employerInfoURL = `http://localhost:8000/users/${id}/update_employer_info`

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
            console.log("submit worked")
        } else {
            console.log("submit didn't work", response)
        }
    }

    return (
        <div className="row">
            <form className="col s12" onSubmit={handleSubmit}>
                <div className="row">
                    <div className="form-floating col s6">
                        <input type="text" name="company_name" value={companyName} id="company_name" onChange={e => setCompanyName(e.target.value)}>
                        </input>
                        <label>Company Name</label>
                    </div>
                    <div className="form-floating col s6">
                        <input type="text" name="job_type" value={jobType} id="job_type" onChange={e => setJobType(e.target.value)}>
                        </input>
                        <label>Type of Company</label>
                    </div>
                </div>
                <div className="row">
                    <div className="form-floating col s6">
                        <input type="text" name="location" value={location} id="location" onChange={e => setLocation(e.target.value)}>
                        </input>
                        <label>Location</label>
                    </div>
                    <div className="form-floating col s6">
                        <input type="text" name="about" value={about} id="about" onChange={e => setAbout(e.target.value)}>
                        </input>
                        <label>About</label>
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
                <a href="/user/employer">Back to Profile</a>
            </form>
        </div>
    )
}

export default EmployerInfoForm;