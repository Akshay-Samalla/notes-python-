import React from 'react';

function Navbar({onSelectCourse}) {
    return (
        <>
        <nav className="navbar">
            <button onClick={()=>onSelectCourse("Python")}>Python</button>
            <button onClick={()=>onSelectCourse("Data Science")}>Data Science</button>
            <button onClick={()=>onSelectCourse("Azure")}>Azure</button>
            <button onClick={()=>onSelectCourse("Kubrnetes")}>Kubernetes</button>
        </nav>
        </>
    );
}

export default Navbar;