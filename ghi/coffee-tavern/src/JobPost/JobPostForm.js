import React, { useState, useEffect } from 'react';
import { useAuthContext } from '../useToken';
// import 'bootstrap/dist/css/bootstrap.min.css';

const JobPostForm = () => {
    const [employer, setEmployer] = useState("");
    const [position, setPosition] = useState("");
    const [location, setLocation] = useState("");
    const [from_date, setFromDate] = useState("");
    const [to_date, setToDate] = useState("");
    const [description, setDescription] = useState("");
    const [tag, setTag] = useState("");
    const [tags, setTags] = useState([]);
    const { token } = useAuthContext();

    const clearJobForm = () => {
        setEmployer("");
        setPosition("");
        setLocation("");
        setFromDate("");
        setToDate("");
        setTag("");
        setDescription("");
    }

    useEffect (() => {
        const getTag = async () => {
            if (token) {
            const response = await fetch(`${process.env.REACT_APP_TAGS_API_HOST}/get_all_tags`, {
            method: "GET",
            headers: { Authorization: `Bearer ${token}`,
            },});
            const data = await response.json();
            setTags(data);
        }
    }
        getTag()
    }, [token])

    const handleSubmit = async(submit) => {
        submit.preventDefault()
        const JobFormURL = `${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/create_form/`;
        const fetchConfig = {
            method: 'post',
            body: JSON.stringify({
                employer: employer,
                position: position,
                location: location,
                from_date: from_date,
                to_date: to_date,
                tag: tag,
                description: description
            }),
            headers: { Authorization: `Bearer ${token}`, "Content-type": "application/json",
        }};
        const response = await fetch(JobFormURL, fetchConfig);
        // const data = await response.json();
        if (response.ok){
            clearJobForm()
        }
    }

    return (
        <div className="row">
            <div className="offset-3 col-6">
                <div className="shadow p-4 mt-4">
                    <h1>Create a New Job Post</h1>
                    <form id="create-job-form" onSubmit={handleSubmit}>
                        <div className="form-floating mb-3">
                            <input placeholder="Employer" required type="text" name="employer" value={employer} onChange={(event) => setEmployer(event.target.value)} id="employer" className="form-control" />
                        </div>
                        <div className="form-floating mb-3">
                            <input placeholder="Position" required type="text" name="position" value={position} onChange={(event) => setPosition(event.target.value)} id="position" className="form-control" />
                        </div>
                        <div className="form-floating mb-3">
                            <input placeholder="Location" required type="text" name="location" value={location} onChange={(event) => setLocation(event.target.value)} id="location" className="form-control" />
                        </div>
                        <div className="form-floating mb-3">
                            <input placeholder="From_date" required type="date" name="from_date" value={from_date} onChange={(event) => setFromDate(event.target.value)} id="from_date" className="form-control" />
                        </div>
                        <div className="form-floating mb-3">
                            <input placeholder="To_date" required type="date" name="to_date" value={to_date} onChange={(event) => setToDate(event.target.value)} id="to_date" className="form-control" />
                        </div>
                        {/* <div className="form-floating mb-3">
                            <input placeholder="Tags" required type="text" name="tag" value={tag} onChange={(event) => setTag(event.target.value)} id="tag" className="form-control" />
                        </div> */}
                        <div className="mb-3">
                            <select value={tag} onChange={(event => setTag(event.target.value))} required id="tag" name="tag" className="form-select">
                                <option value="">Add a Tag</option>
                                {tags.map(tag => {
                                    return (<option key={tag.id} value={tag.id}>{tag.tag}</option>)
                                })}
                            </select>
                        </div>
                        <div className="form-floating mb-3">
                            <input placeholder="Description" required type="text" name="description" value={description} onChange={(event) => setDescription(event.target.value)} id="description" className="form-control" />
                        </div>
                        <button className="btn btn-primary">Create</button>
                    </form>
                </div>
            </div>
        </div>
    );
}


export default JobPostForm
