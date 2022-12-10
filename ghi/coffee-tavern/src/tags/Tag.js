import axios from 'axios'
import React from 'react'
import { useAuthContext } from '../useToken';

function Tag(props) {
    const { token } = useAuthContext();

    const config = {
        headers: { Authorization: `Bearer ${token}` }
    };

    const deleteTagHandler = (id) => {
        axios.delete(`${process.env.REACT_APP_TAGS_API_HOST}/delete_tag/${id}`)
            .then(res => console.log(res.data))

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
