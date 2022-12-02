import { NavLink } from 'react-router-dom';

function FeedbackTest() {
  return(

    <div>
      <NavLink className="" to="/employee-feedbacks/">Employee Feedback</NavLink>
      <NavLink className="" to="/employer-feedbacks/">Employer Feedback</NavLink>
      <NavLink className="" to="/employee-feedback-list/">Employer Feedback</NavLink>
      {/* <NavLink className="" to="/employee-feedbacks/">Employee Feedback</NavLink> */}
      <NavLink className="" to="/employer-feedbacks/">Employer Feedback</NavLink>
      {/* <NavLink className="" to="/employee-feedback-list/">Employee Feedback</NavLink> */}
      <NavLink className="" to="/employer-feedbacks-list/">Employer Feedback</NavLink>
    </div>



  )
}

export default FeedbackTest
