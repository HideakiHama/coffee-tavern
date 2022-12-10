import 'materialize-css/dist/css/materialize.min.css'
import jwt_decode from 'jwt-decode';
import {useEffect, useState} from 'react';
import { useAuthContext } from '../useToken';

function EmployeeInfoForm() {

    const [fullName, setFullName] = useState('')
    const [careerTitle, setCareerTitle] = useState('')
    const [location, setLocation] = useState('')
    const [education, setEducation] = useState('')
    const [about, setAbout] = useState('')
    const [pic, setPic] = useState('')

    //
    const [id, setId] = useState('');

    const { token } = useAuthContext();

    
    useEffect(() => {
        async function getEmployeeInfo () {

            const decoded = jwt_decode(token)
            setId(decoded.account["id"])

            const infoURL = `http://localhost:8000/users/${id}/get_employee_info`

            const infoResponse = await fetch(infoURL, {
                method: "GET",
                headers: { Authorization: `Bearer ${token}`}
            })

            if (infoResponse.ok) {
                const info = await infoResponse.json()

                if (info) {
                    setFullName(info.full_name)
                    setCareerTitle(info.career_title)
                    setLocation(info.location)
                    setEducation(info.education)
                    setAbout(info.about)
                    setPic(info.pic_url)
                }
            }
        }

        getEmployeeInfo()

    }, [id, token])

    const handleSubmit = async (event) => {
        event.preventDefault();
        const data = {
            "full_name": fullName,
            "career_title": careerTitle,
            "location": location,
            "education": education,
            "about": about,
            "pic_url": pic
        }
        
        const employeeInfoURL = `http://localhost:8000/users/${id}/update_employee_info`

        const fetchConfig = {
            method: "PUT",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`
            },
        }
        const response = await fetch(employeeInfoURL, fetchConfig)

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
                        <input placeholder="Full Name" type="text" name="full_name" value={fullName} id="full_name" onChange={e => setFullName(e.target.value)}>
                        </input>
                    </div>
                    <div className="form-floating col s6">
                        <input placeholder="Career Title"type="text" name="career_title" value={careerTitle} id="career_title" onChange={e => setCareerTitle(e.target.value)}>
                        </input>
                    </div>
                </div>
                <div className="row">
                    <div className="form-floating col s6">
                        <input placeholder="Location"type="text" name="location" value={location} id="location" onChange={e => setLocation(e.target.value)}>
                        </input>
                    </div>
                    <div className="form-floating col s6">
                        <input placeholder="Education"type="text" name="education" value={education} id="education" onChange={e => setEducation(e.target.value)}>
                        </input>
                    </div>
                </div>
                <div className="row">
                    <div className="form-floating col s6">
                        <input placeholder="About"type="text" name="about" value={about} id="about" onChange={e => setAbout(e.target.value)}>
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

export default EmployeeInfoForm;