import React, { Component } from 'react'
import aios from 'axios'

export default function UploadResume(){ 

const [file, uploadFile] = useState(null)

const fileChangeHandler = (e) => {
    setSelected(e.target.files[0]);
    console.log(e.target.files[0])
}

const handleSubmit = (e) => {
    const formData = new FormData();
    formData.append(
        "files",
        selectedFile,
        selecedFile.name
    );
    const requestOptions = {
        method: "POST"
    }
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
                <input onChange={fileChangeHandler} name="resume" type="files" accept='jpeg, .png, .jpg, .pdf'></input>
            </fieldset>
        </form>
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