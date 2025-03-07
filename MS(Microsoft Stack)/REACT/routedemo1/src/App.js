// import React from "react";
// import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
// // Simple components
// const Home = () => <h2>Home Page</h2>;
// const About = () => <h2>About Page</h2>;
//
// function App() {
//     return (
//         <Router>
//             <nav>
//                 <ul>
//                     <li><Link to="/">Home</Link></li>
//                     <li><Link to="/about">About</Link></li>
//                 </ul>
//             </nav>
//
//             <Routes>
//                 <Route path="/" element={<Home />} />
//                 <Route path="/about" element={<About />} />
//             </Routes>
//         </Router>
//     );
// }
// export default App;
//
// import React from "react";
// import { BrowserRouter as Router, Routes, Route, Link, Navigate } from "react-router-dom";
//
// const Home = () => <h2>Home Page</h2>;
// const About = () => <h2>About Page</h2>;
// const NotFound = () => <h2>404 - Page Not Found</h2>;
//
// function App() {
//     return (
//         <Router>
//             <nav>
//                 <ul>
//                     <li><Link to="/">Home</Link></li>
//                     <li><Link to="/about">About</Link></li>
//                 </ul>
//             </nav>
//
//             <Routes>
//                 <Route path="/" element={<Home />} />
//                 <Route path="/about" element={<About />} />
//                 <Route path="/old-about" element={<Navigate to="/about" />} />
//                 <Route path="*" element={<NotFound />} />
//             </Routes>
//         </Router>
//     );
// }
//
// export default App;
// import React from "react";
// import { BrowserRouter as Router, Routes, Route, Link , Navigate } from "react-router-dom";
//
// const ProtectedRoute = ({ children }) => {
//     const isAuthenticated = false; // Change to true to allow access
//     return isAuthenticated ? children : <Navigate to="/login" />;
// };
// const Home = () => <h2>Home Page</h2>;
// const Dashboard = () => <h2>Dashboard - Protected</h2>;
// const Login = () => <h2>Login Page</h2>;
//
// function App() {
//     return (
//         <Router>
//             <nav>
//                 <ul>
//                     <li><Link to="/">Home</Link></li>
//                     <li><Link to="/dashboard">Dashboard</Link></li>
//                     <li><Link to="/login">Login</Link></li>
//                 </ul>
//             </nav>
//
//             <Routes>
//                 <Route path="/" element={<Home />} />
//                 <Route path="/login" element={<Login />} />
//                 <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
//             </Routes>
//         </Router>
//     );
// }
//
// export default App;

// import React from "react";
// import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
// // Simple components
// const Home = () => <h2>Home Page</h2>;
// const About = () => <h2>About Page</h2>;
//
// function App() {
//     return (
//         <Router>
//             <nav>
//                 <ul>
//                     <li><Link to="/">Home</Link></li>
//                     <li><Link to="/about">About</Link></li>
//                 </ul>
//             </nav>
//
//             <Routes>
//                 <Route path="/" element={<Home />} />
//                 <Route path="/about" element={<About />} />
//             </Routes>
//         </Router>
//     );
// }
// export default App;
//
// import React from "react";
// import { BrowserRouter as Router, Routes, Route, Link, Navigate } from "react-router-dom";
//
// const Home = () => <h2>Home Page</h2>;
// const About = () => <h2>About Page</h2>;
// const NotFound = () => <h2>404 - Page Not Found</h2>;
//
// function App() {
//     return (
//         <Router>
//             <nav>
//                 <ul>
//                     <li><Link to="/">Home</Link></li>
//                     <li><Link to="/about">About</Link></li>
//                 </ul>
//             </nav>
//
//             <Routes>
//                 <Route path="/" element={<Home />} />
//                 <Route path="/about" element={<About />} />
//                 <Route path="/old-about" element={<Navigate to="/about" />} />
//                 <Route path="*" element={<NotFound />} />
//             </Routes>
//         </Router>
//     );
// }
//
// export default App;
// import React from "react";
// import { BrowserRouter as Router, Routes, Route, Link , Navigate } from "react-router-dom";
//
// const ProtectedRoute = ({ children }) => {
//     const isAuthenticated = false; // Change to true to allow access
//     return isAuthenticated ? children : <Navigate to="/login" />;
// };
// const Home = () => <h2>Home Page</h2>;
// const Dashboard = () => <h2>Dashboard - Protected</h2>;
// const Login = () => <h2>Login Page</h2>;
//
// function App() {
//     return (
//         <Router>
//             <nav>
//                 <ul>
//                     <li><Link to="/">Home</Link></li>
//                     <li><Link to="/dashboard">Dashboard</Link></li>
//                     <li><Link to="/login">Login</Link></li>
//                 </ul>
//             </nav>
//
//             <Routes>
//                 <Route path="/" element={<Home />} />
//                 <Route path="/login" element={<Login />} />
//                 <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
//             </Routes>
//         </Router>
//     );
// }
//
// export default App;
// import React from "react";
// const App = () => {
//     const user = 'joana doe'
//     return <Parent user = {user}/>
// }
// const Parent = ({user})=> <Child user={user}/>
// const Child = ({user})=> <Profile user={user}/>
// const Profile = ({user})=> <h1>hello {user}</h1>
// export default App;

import React, { createContext, useContext } from "react";


const UserContext = createContext();

const App = () => {
    const user = "John Doe";

    return (

        <UserContext.Provider value={user}>
            <Parent />
        </UserContext.Provider>
    );
};

const Parent = () => {
    return <Child />;
};

const Child = () => {
    return <ProfileDetails />;
};

const ProfileDetails = () => {
    const user = useContext(UserContext);
    return <h2>User: {user}</h2>;
};

export default App;