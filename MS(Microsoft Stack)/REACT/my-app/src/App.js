import logo from './logo.svg';
import './App.css';
import DataBinding1 from './components/DataBinding';
import DataBinding2 from './components/DataBinding2';
import EventBinding from './components/EventBinding';
import EventBinding2 from './components/EventBinding2';
import UserProfile from "./components/propsdemo";
import Button from "./components/propsdemo";
// import Greetings from "./components/propsdemo";

function App() {
    function handleClick(){
        alert('clicked')
    }
  return (
    <div className="App">
      {/* <h1>helloworld how are you im doing fine what about you?</h1> */}
      {/* <DataBinding1/> */}
      {/* <DataBinding2/> */}
      {/* <EventBinding/>   */}
      {/*<EventBinding2/>*/}
      {/*  <Greetings name={"geetha"}/>*/}
      {/*  <UserProfile username='geetha' age='21'/>*/}
      {/*  <Button onclick={handleClick}/>*/}


    </div>
  );
}

export default App;


//COMPNENTS
/*
* header.jsx
* footer.jsx
* navbar.jsx four buttons for courses python datascience azure kubernthese onselectcourse in app component with use state
*
*main content.jsx
* coursecard.jsx
*
* */