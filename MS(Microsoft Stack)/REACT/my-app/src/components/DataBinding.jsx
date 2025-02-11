import React , {useState} from 'react';

const DataBinding1=()=>{
    const companyName = 'CapGemini'

    const num1=900
    const num2=400

    const greet=()=>'hi function call from greet'

    const courses = [
        'python',
        'Data Science',
        'Data Engineering',
        'Cloud',
        'Kubernetes'
    ]
    const [message, setMessage] = useState('click the button');
    const handleClick = (event)=>{
        setMessage('button clicked')
    }
    const [isLoggedin , setIsLoggedIn] = useState(false);
    return (
        <>
        <header>
            <h1>{companyName}</h1>
            <h1>{isLoggedin ? 'welcome,user...' : 'please login'}</h1>
            <button onClick={()=>setIsLoggedIn(!isLoggedin)}>{isLoggedin ? 'logout' : 'login'}</button>
            <h2>calcuation using expression</h2>
            <p>sum: {num1+num2}</p>
            <p>multiplication : {num1*num2}</p>
            <h1>Function call</h1>
            <h2>{greet()}</h2>
            <h1>Dynamic list</h1>
            <ul>
                {
                    courses.map((course,index)=>(
                        <li key={index}>{course}</li>
                    ))
                }
            </ul>
        </header>

        <h1>event binding</h1>
        <h2>{message}</h2>
        <button onClick={handleClick}>click me</button>
        </>
    )
}

export default DataBinding1;