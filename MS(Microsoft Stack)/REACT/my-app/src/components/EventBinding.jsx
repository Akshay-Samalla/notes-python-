import React, { useState } from 'react';

const EventBinding = () => {
    const [likes, setlikes] = useState(0)
    const handleClick = ()=> {
        setlikes(likes + 1);
    }

    const [formData , setFormData] = useState({name:'',email:''})
    const handleChange = (event) =>{
        setFormData({...formData, [event.target.name]:event.target.value})
    }
    const [isZoomed , setIsZoomed] = useState(false)
    return (
      <div>
        <div>
          <button onClick={handleClick}> LIKE {likes}</button>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
          />
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
          />

          <p>name: {formData.name} </p>
          <p>email: {formData.email}</p>
        </div>

        <div>
          <img src="https://th.bing.com/th/id/OIP.2bJ9_f9aKoGCME7ZIff-ZwHaJ4?rs=1&pid=ImgDetMain"
            alt="sample image"
            style={{ width: isZoomed ? "300px" : "150px", transition: "0.3s" }}
            onMouseOver={() => setIsZoomed(true)}
            onMouseOut={() => setIsZoomed(false)}
          />
        </div>
      </div>
    );
};

export default EventBinding;