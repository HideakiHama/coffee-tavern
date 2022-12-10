import axios from 'axios'
import React from 'react'
import { useAuthContext } from '../useToken';

function Tag(props) {
    const { token } = useAuthContext();

    const config = {
        headers: { Authorization: `Bearer ${token}` }
    };

    const deleteTagHandler = (id) => {
        axios.delete(`http://localhost:8100/delete_tag/${id}`, config)
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
