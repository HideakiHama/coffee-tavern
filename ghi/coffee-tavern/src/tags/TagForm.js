import React, { useState, useEffect }  from 'react';
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.min.css';
import TagView from './TagListView';



function TagForm(){

    const [tagsList, setTagsList] = useState([])
    const [id, setId] = useState('')
    const [tag, setTag] = useState('')

    // read tags
    useEffect(() => { 
        axios.get('http://localhost8100/get_all_tags')
        .then(res => {
            setTagsList(res.data)
        },[])
    });
 
    // post tags
    const addTagHandler = () => {
        axios.post('http://localhost8100/create_tag_form/', {'id': id, 'tag': tag})
        .then(res => console.log(res))
    };
    


    return(
        <div className="App list-group justify-content-center
        align-items-center mx-auto" style={{"width":"400px","backgroundColor": "white",
        "marginTop": "15px"}}>
        <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">Tag Form</h1>
        <div className="card-body">
        <h5 className="card text-white bg-dark mb-3"> Add Tag </h5>
            <span className="card-text">
            {/* <input className="mb-w form-control idIn" onChange={event =>
            setTag(event.target.value)} placeholder="ID"/> */}
            <input className="mb-w form-control tagIn" onChange={event =>
            setTag(event.target.value)} placeholder="Tag Name"/>
            <button className="btn btn-outline-primary mx-2 mb-3" style={{
                'borderRadius':'50px',
                'font-weight': 'bold',
            }} onClick={addTagHandler}>Create Tag</button>
            </span>
        <h5 className="card text-white bg-dark mb-3">Your Tags</h5>
        <div>
            <TagView tagsList = {tagsList}/>
        </div>
        </div>
        </div>
    )
}
export default TagForm