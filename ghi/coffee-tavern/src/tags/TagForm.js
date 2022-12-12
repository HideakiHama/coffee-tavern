import React, { useState, useEffect  }  from 'react';
import axios from "axios";
// import 'bootstrap/dist/css/bootstrap.min.css';
import TagListView from './TagListView';
import { useAuthContext } from '../useToken';


function TagForm(){
    const [tagsList, setTagsList] = useState([])
    const [tag, setTag] = useState('')
    const { token } = useAuthContext();


    const config = {
        headers: { Authorization: `Bearer ${token}` }
    };

    useEffect(() => {
        if (token) {
        axios.get('http://localhost:8100/get_all_tags', config)
        .then(res =>
            setTagsList(res.data))
        }
    }, [token]);

    // post tags
    const addTagHandler = () => {
        axios.post(`${process.env.REACT_APP_TAGS_API_HOST}/create_tag_form`,{'tag': tag},
        config)
        .then(res => console.log(res))
        setTagsList([...tagsList, {tag}]);
    };

    return(
        <div className="App list-group justify-content-center
        align-items-center mx-auto" style={{"width":"400px","backgroundColor": "white",
        "marginTop": "15px"}}>
        <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">Tag Form</h1>
        <div className="card-body">
        <h5 className="card text-white bg-dark mb-3"> Add Tag </h5>
            <span className="card-text">

            <input className="mb-w form-control desIn" onChange={event =>
            setTag(event.target.value)} placeholder="Tag Name"/>
            <button className="btn btn-outline-primary mx-2 mb-3" style={{
                'borderRadius':'50px',
                'font-weight': 'bold',
            }}
            onClick={addTagHandler}
            >Create Tag</button>
            </span>
        <h5 className="card text-white bg-dark mb-3">Your Tags</h5>
        <div>
            <TagListView tagList = {tagsList}/>
        </div>
        </div>
        </div>
    )
}
export default TagForm
