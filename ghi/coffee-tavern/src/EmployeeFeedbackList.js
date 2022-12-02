import React, { useState, useEffect } from "react";
// import axios from "axios";

const EmployeeFeedbacksUrl = "localhost:8000/employee-feedbacks/"

function EmployeeFeedbackList() {
      const [feedbackData, setFeedbackData] = useState([]);

      useEffect(() =>{
        getEmployeeFeedbacksUrl();
      }, []);

      const getEmployeeFeedbacksUrl = async () => {
        // const response = await axios.get(EmployeeFeedbacksUrl);
        // setFeedbackData(response.data);
        const response = await fetch(EmployeeFeedbacksUrl);
        const jsonData = await response.json();
        setFeedbackData(jsonData);

      };

      console.log("#####", feedbackData)
      return (
      <div>
        <h1>Employee List</h1>
        <h2>id list here {feedbackData.id}</h2>
      </div>

    )
}
export default EmployeeFeedbackList