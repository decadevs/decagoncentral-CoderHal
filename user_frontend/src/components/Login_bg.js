import React from 'react'
import logo from '../images/logo.png'
const Login_bg = () => {
    return (
        // <div className="login" style={{height: "40rem"}}>
            <div className="loginBG col-md-5 d-flex">
                <div className="w-75 mx-auto">
                    <img src={logo} alt="logo" className="loginLogo w-50"/>
                    <p className="text-white pr-4 py-3 text-small">
                    Decagon is a software engineering institute ushering in a new phase of tech-powered growth and prosperity in Nigeria by training and deploying an army of leader-developers.
                    </p>
                </div>
            </div>
        // </div>
        
        
    )
}

export default Login_bg
