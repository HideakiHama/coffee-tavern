import React, { useState, useEffect } from "react";
import axios from "axios";

const account_id = 5
const EmployerFeedbacksUrl = `http://localhost:8000/employer-feedbacks/${account_id}/`

function EmployeeFeedbackList() {
      const [feedbackData, setFeedbackData] = useState([]);

      useEffect(() =>{
        getEmployeeFeedbacksUrl();
      }, []);

      const getEmployeeFeedbacksUrl = async (account_id) => {
        const response = await axios.get(EmployerFeedbacksUrl);
        setFeedbackData(response.data);
        // const response = await fetch(EmployeeFeedbacksUrl);
        // const jsonData = await response.json();
        // setFeedbackData(jsonData);

      };


      return (
      <div>
        <h1>Employee List</h1>
        <h2>id list here {feedbackData.id}</h2>
      </div>

    )
}
export default EmployeeFeedbackList
