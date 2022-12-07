import React, { useState, useEffect }  from 'react';
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.min.css';
import TagView from './TagListView';



function TagForm(){

    const [tagsList, setTagsList] = useState([])
    // const [id, setId] = useState('')
    const [tag, setTag] = useState('')

    // read tags
    useEffect(() => { get_tag_url()
        axios.get('http://localhost8100/get-tag/${Tag_id}')
        .then(res => {
            setTagsList(res.data)
        },[])
    });
    const get_tag_url = async(Tag_id) => {
        Tag_id = 1
    
    const response = await axios.get('http://localhost8100/get-tag/${Tag_id}')
        setTagsList(response.data)
    }
    // post tags
    const addTagHandler = () => {
        axios.post('http://localhost8100/create_tag_form',{'tag': tag})
        .then(res => console.log(res))
    };
    //{'id': id, 'tag': tag}



    return(
        <div className="App list-group justify-content-center
        align-items-center mx-auto" style={{"width":"400px","backgroundColor": "white",
        "marginTop": "15px"}}>
        <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">Tag Form</h1>
        {/* <h6 className="card text-white bg-primary mb-3"> Create a Tag</h6> */}
        <div className="card-body">
        <h5 className="card text-white bg-dark mb-3"> Add Tag </h5>
            <span className="card-text">
            {/* <input className="mb-2 form control titleIn" onChange={event =>
            setId(event.target.value)} placeholder="id"/> */}
            <input className="mb-w form-control desIn" onChange={event =>
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