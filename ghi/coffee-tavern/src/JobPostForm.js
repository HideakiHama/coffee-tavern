import React, { Component } from 'react'

export default class JobPostForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            employer: '',
            position: '',
            location: '',
            from_date: '',
            to_date: '',
            tag: ''
        };

        this.handleNameChange = this.handleNameChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    async handleSubmit(event) {
        const data = { ...this.state };
        delete data.manufacturers
        const createJobPost = 'http://localhost8000/create_form';
        const fetchConfig = {
            method: 'post',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
            },
        };

        const response = await fetch(createJobPost, fetchConfig);
        if (response.ok) {
            const newJobPost = await response.json();
            console.log(newJobPost);
        }

        const cleared = {
            employer: '',
            position: '',
            location: '',
        }
        event.setState(cleared);
    }

    handleNameChange(event) {
        const value = event.target.value;
        this.setState({ name: value });
    }

    render() {
        return (
            <>
                <div className="row">
                    <div className="offset-3 col-6">
                        <div className="shadow p-4 mt-4">
                            <h1 style={{color:"brown"}}>New Job Post</h1>
                            <form onSubmit={this.handleSubmit} id="create-jobPost-form">
                                <div className="form-floating mb-3">
                                    <input onChange={this.handleNameChange} placeholder="Name" required type="text" name="name" id="name" className="form-control" />
                                    <label htmlFor="name">Employer</label>
                                </div>
                                {/* <button onClick={handleSubmit}>Upload</button> */}
                                <button className="btn btn-outline-success">Create</button>
                            </form>
                        </div>
                    </div>
                </div>
            </>
        )
    }
}

