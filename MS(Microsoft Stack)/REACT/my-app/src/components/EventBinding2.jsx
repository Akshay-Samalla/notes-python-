import { useState } from "react"

const EventBinding2=()=>{
    const [email,setemail] = useState('')
    const [password , setpassword] = useState('')

    const handleSubmit = (event)=>{
        event.preventDefault();
        if (email && password){
            alert('login success')
        }
        else{
            alert('please enter the credentials')
        }
    }
    return (
        <>
        <form onSubmit={handleSubmit}>
            <input type="email" 
            placeholder="email"
            value={email}
            onChange={(e)=>setemail(e.target.value)}/>
            <input type="password" 
            placeholder="*****"
            value={password}
            onChange={(e)=>setpassword(e.target.value)}/>
            <button type='submit'>login</button>
        </form>
        </>
    )
}

export default EventBinding2