import { NavLink } from 'react-router-dom';



function Nav() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-success">
      <div className="container-fluid">
        <NavLink className="navbar-brand" to="/">CarCar</NavLink>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <nav className="navbar navbar-expand-lg navbar-dark bg-">
              <div className="container-fluid">
                <a className="navbar-brand" href="#">Sales</a>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDarkDropdown" aria-controls="navbarNavDarkDropdown" aria-expanded="false" aria-label="Toggle navigation">
                  <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNavDarkDropdown">
                  <ul className="navbar-nav">
                    <li className="nav-item dropdown">
                      <a className="nav-link dropdown-toggle" href="#" id="navbarDarkDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">

                      </a>
                      <ul className="dropdown-menu dropdown-menu-dark" aria-labelledby="navbarDarkDropdownMenuLink">
                        <li><NavLink className="dropdown-item" aria-current="page" to="/api/accounts">Signup</NavLink></li>
                        <li><NavLink className="dropdown-item" aria-current="page" to="/token">Login</NavLink></li>
                        <li><NavLink className="dropdown-item" aria-current="page" to="/upload_resume/">Upload Resume</NavLink></li>
                        <li><NavLink className="dropdown-item" aria-current="page" to="/create_form">Create Job Post</NavLink></li>
                        <li><NavLink className="dropdown-item" aria-current="page" to="/get_all_form">Board of Jobs</NavLink></li>
                        <li><NavLink className="dropdown-item" aria-current="page" to="/employee-feedbacks/">Employee Feedback Form</NavLink></li>
                        <li><NavLink className="dropdown-item" aria-current="page" to="/employee-feedbacks-list/">Past Employee Feedbacks</NavLink></li>
                        <li><NavLink className="dropdown-item" aria-current="page" to="/employee-feedbacks/">Employee Feedback Form</NavLink></li>
                        <li><NavLink className="dropdown-item" aria-current="page" to="/employee-feedbacks-list/">Past Employee Feedbacks</NavLink></li>
                      </ul>
                    </li>
                  </ul>
                </div>
              </div>
            </nav>
            <nav className="navbar navbar-expand-lg navbar-dark bg-">
              <div className="container-fluid">
                <a className="navbar-brand" href="#">Inventory</a>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDarkDropdown" aria-controls="navbarNavDarkDropdown" aria-expanded="false" aria-label="Toggle navigation">
                  <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNavDarkDropdown">
                  <ul className="navbar-nav">
                    <li className="nav-item dropdown">
                      <a className="nav-link dropdown-toggle" href="#" id="navbarDarkDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">

                      </a>
                      <ul className="dropdown-menu dropdown-menu-dark" aria-labelledby="navbarDarkDropdownMenuLink">
                      <li><NavLink className="dropdown-item" aria-current="page" to="/employee-feedbacks/">Employee Feedback Form</NavLink></li>
                      <li><NavLink className="dropdown-item" aria-current="page" to="/employee-feedbacks-list/">Past Employee Feedbacks</NavLink></li>
                      </ul>
                    </li>
                  </ul>
                </div>
              </div>
            </nav>
            <nav className="navbar navbar-expand-lg navbar-dark bg-">
              <div className="container-fluid">
                <a className="navbar-brand" href="#">Service</a>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDarkDropdown" aria-controls="navbarNavDarkDropdown" aria-expanded="false" aria-label="Toggle navigation">
                  <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNavDarkDropdown">
                  <ul className="navbar-nav">
                    <li className="nav-item dropdown">
                      <a className="nav-link dropdown-toggle" href="#" id="navbarDarkDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">

                      </a>
                      <ul className="dropdown-menu dropdown-menu-dark" aria-labelledby="navbarDarkDropdownMenuLink">
                        <li><NavLink className="dropdown-item" aria-current="page" to="/employer-feedbacks">Employer Feedback Form</NavLink></li>
                        <li><NavLink className="dropdown-item" aria-current="page" to="/employer-feedbacks-list">Past Employer Feedbacks</NavLink></li>
                       
                        {/* <li><NavLink className="dropdown-item" aria-current="page" to="sales-records/filter/">Employee Sales</NavLink></li> */}
                      </ul>
                    </li>
                  </ul>
                </div>
              </div>
            </nav>

          </ul>
        </div>
      </div>
    </nav>



  )
}

export default Nav;
