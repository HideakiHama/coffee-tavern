function getEmployeeFeedback() {
  return fetch('http://localhost:8000/employee-feedbacks/')
    .then(data => data.json())
}
export default getEmployeeFeedback