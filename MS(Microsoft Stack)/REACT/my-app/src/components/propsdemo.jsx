import React from 'react';

// function Greetings(props) {
//     return (
//         <h1>hello , {props.name}</h1>
//     );
// }
//
// export default Greetings;

// function UserProfile(props){
//     return (
//         <>
//             <h1>user Info</h1>
//             <h2>username : {props.username}</h2>
//             <h3>age : {props.age}</h3>
//         </>
//
//     )
// }
// export default UserProfile

// function UserProfile({username = 'geetha', age = '21'}) {
//     return (
//         <>
//             <h1>user info</h1>
//             <h2>username : {username}</h2>x
//             <h3>age : {age}</h356>
//         </>
//     )
// }
//
// export default UserProfile
function Button({onclick}){
    return (<button onClick={onclick}>click me</button>)
}
export default Button