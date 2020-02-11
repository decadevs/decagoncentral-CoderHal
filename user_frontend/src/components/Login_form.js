import React, {useState} from 'react'
import { Link } from 'react-router-dom'


const LoginForm = () => {
    // const [dosomething, setDosomething] = useState({email:'', password:''})

    return(
        <div className="col-md-7 loginForm d-flex">
            <div className="mx-auto">
                <h4>Login</h4>
                <form>
                    <div className="">
                        <label for="email">Email:</label><br></br>
                        <input type="email" className="form-group" value=""/>
                    </div>
                    <div className="form-group">
                        <label for="password">Password:</label><br></br>
                        <input type="password" className="form-group" value=""/>
                    </div>
                    <button className="btn btn-small btn-success px-5 mr-5 rounded-pill"><a href="#" className="text-white">Login</a></button>
                    {/* <Link to="/signup">Signup</Link> */}
                    <a href="#" className="text-success" >create an account</a>
                </form>
            </div>
        </div>
    )
}
    
export default LoginForm