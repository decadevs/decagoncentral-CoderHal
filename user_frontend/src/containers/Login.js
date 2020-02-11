import React from 'react'
import LoginForm from '../components/Login_form'
import LoginBg from '../components/Login_bg'

const Login = () => {
    return (
        <div className="row my-auto" style={{minHeight:'36rem'}}>
            <LoginBg/>
            <LoginForm/>
        </div>
    )
}
export default Login
