import React, { useState } from "react"
// import axios from 'axios'

export default function UploadResume() { 

    const [selectedFile, setSelectedFile] = useState(null);
    const [input, setInput] = useState('')

    const fileChangeHandler = (e) => {
        setSelectedFile(e.target.files[0]);
        console.log(e.target.files[0])
    }

    const handleSubmit = (e) => {
        const formData = new FormData();
        formData.append(
            "files",
            selectedFile,
            selectedFile.name
        );
        formData.append(
            "username",
            input
        )

        const requestOptions = {
            method: "POST",
            body: formData
        };

        fetch("http://localhost:8000/upload_resume/", requestOptions)
        .then(response => response.json())
        .then(function(response) {
            console.log(response)
        })
    }

    return (
        <div className="App">
            <header className="App-header">
                <h1>
                    Upload Resume
                </h1>
            </header>
            <form>
                <fieldset>
                    <input onClick={fileChangeHandler} name="resume" type="files" accept='jpeg, .png, .jpg, .pdf'></input>
                </fieldset>
                {/* <button onClick={fileChangeHandler}></button> */}
                <button onClick={handleSubmit}>Upload</button>
            </form>
            <input onChange={(e) => setInput(e.target.value)}></input>
        </div>
    )


// function handleSubmit(){
//     console.log(file[0].name)
//     const formdata = new FormData();

//     formdata.append(
//         "file",
//         file[0],
//     )
//     axios.post("/upload_resume/" {
//         file.formdata}, {
//             "content-type" : "multipart/form-data",
//         })
//             .then(function (response) {
//                 console.log(response);
//             });
//     }
//     function handleChange(e){
//         uploadFile(e.target.files);
//     }
// }


}