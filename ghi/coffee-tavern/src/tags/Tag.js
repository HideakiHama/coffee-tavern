import axios from 'axios'
import React from 'react'
import { useAuthContext } from '../useToken';

function Tag(props) {
    const { token } = useAuthContext();

    const deleteTagHandler = (id) => {
        axios.delete(`${process.env.REACT_APP_TAGS_API_HOST}/delete_tag/${id}`, {headers: { Authorization: `Bearer ${token}` }})
    }
    return(
        <div>
            <p>
                <span style={{ fontWeight: 'bold, underline'}}>
                    {props.Tag.tag}
                </span>
                <button onClick={() => deleteTagHandler(props.Tag.id)}
                className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px'}}>X</button>
                <hr></hr>
            </p>
        </div>
    )
}
export default Tag
