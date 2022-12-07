function MainPage() {
    return (
        <div
        style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
        }}>
        <div class="wrapper">
            <div className="px-4 py-5 my-5">
                <h1 style= {{color:"green"}} className="display-5 fw-bold">Coffee Tavern</h1>
                <div className="col-lg-6 mx-auto">
                <p className="lead mb-4">
                    Welcome To Coffee Tavern
                </p>
                <img src="https://i.imgur.com/ucQYHLa.jpeg" width="500" alt="Landing-Page-Latte-Art"></img>
                </div>
                <h3 style={{color: "Blue"}}> Linkedin but for the service industry</h3>
                <h4 style={{color:"Blue"}}>Create a profile today!</h4>
                <h4 style={{color:"Blue"}}>Own a business? Create a Job Post to find quality service employees today! </h4>
            </div>
        </div>
        </div>
      
        );
    }
  
  export default MainPage;
  