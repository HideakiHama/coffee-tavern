import axios from 'axios'
import React from 'react'

function TagItems(props) {

    console.log("this is props in TagItems", props)

    const deleteTagHandler = (tag) => {
        axios.delete('http://localhost:8100/delete_tag/${Tag_id}')
            .then(res => console.log(res.data)) 
    
    

    }
    return(
        <div>
            <p>
                <span style={{ fontWeight: 'bold, underline'}}> {props['Tags']}
                </span> 
                <button onClick={() => deleteTagHandler(props['Tags'])}
                className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px'}}>X</button>
                <hr></hr>
            </p>
        </div>
    )
}
export default TagItems