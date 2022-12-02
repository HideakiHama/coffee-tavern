import React, { useEffect, useState } from 'react';
import { getEmployeeFeedback } from './feedbacks/EmployeeCRUD'

function EmployeeFeedbackForm() {
    const [ list, setList ] = useState([]);
    return (
      <>
      <div>
        <h1>Employee Feedback Form</h1>
      </div>

      </>
    )
}
export default EmployeeFeedbackForm