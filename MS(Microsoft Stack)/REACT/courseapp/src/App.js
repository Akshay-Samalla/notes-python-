import logo from './logo.svg';
import './App.css';
import SearchBar from "./components/SearchBar";
import {useState} from "react";

function App() {
    let [search, setSearch] = useState('');
    function handleChange(e) {
        setSearch(e.target.value);
    }
    const values=[
        { "name": "refrigerator", "quantity": 1, "type": "electrical appliance" },
        { "name": "microwave", "quantity": 2, "type": "kitchen appliance" },
        { "name": "air purifier", "quantity": 3, "type": "home appliance" },
        { "name": "hair dryer", "quantity": 4, "type": "personal care device" },
        { "name": "washing machine", "quantity": 1, "type": "electrical appliance" },
        { "name": "toaster", "quantity": 2, "type": "kitchen appliance" },
        { "name": "vacuum cleaner", "quantity": 3, "type": "home appliance" },
        { "name": "electric kettle", "quantity": 5, "type": "kitchen appliance" },
        { "name": "blender", "quantity": 6, "type": "kitchen appliance" },
        { "name": "dishwasher", "quantity": 1, "type": "electrical appliance" },
        { "name": "coffee maker", "quantity": 2, "type": "kitchen appliance" },
        { "name": "iron", "quantity": 3, "type": "home appliance" },
        { "name": "fan", "quantity": 4, "type": "electrical appliance" },
        { "name": "heater", "quantity": 5, "type": "home appliance" },
        { "name": "electric grill", "quantity": 6, "type": "kitchen appliance" },
        { "name": "rice cooker", "quantity": 1, "type": "kitchen appliance" },
        { "name": "humidifier", "quantity": 2, "type": "home appliance" },
        { "name": "electric shaver", "quantity": 3, "type": "personal care device" },
        { "name": "water dispenser", "quantity": 4, "type": "home appliance" },
        { "name": "bread maker", "quantity": 5, "type": "kitchen appliance" },
        { "name": "juicer", "quantity": 6, "type": "kitchen appliance" },
        { "name": "dehydrator", "quantity": 1, "type": "kitchen appliance" },
        { "name": "induction cooktop", "quantity": 2, "type": "kitchen appliance" },
        { "name": "air fryer", "quantity": 3, "type": "kitchen appliance" },
        { "name": "sewing machine", "quantity": 4, "type": "home appliance" },
        { "name": "standing mixer", "quantity": 5, "type": "kitchen appliance" },
        { "name": "smart speaker", "quantity": 6, "type": "electronic device" },
        { "name": "robot vacuum", "quantity": 1, "type": "home appliance" },
        { "name": "smart light bulb", "quantity": 2, "type": "electronic device" },
        { "name": "smart thermostat", "quantity": 3, "type": "home appliance" },
        { "name": "security camera", "quantity": 4, "type": "electronic device" },
        { "name": "smart lock", "quantity": 5, "type": "electronic device" },
        { "name": "smartwatch", "quantity": 6, "type": "wearable device" },
        { "name": "fitness tracker", "quantity": 1, "type": "wearable device" },
        { "name": "earbuds", "quantity": 2, "type": "electronic device" },
        { "name": "headphones", "quantity": 3, "type": "electronic device" },
        { "name": "gaming console", "quantity": 4, "type": "electronic device" },
        { "name": "laptop", "quantity": 5, "type": "electronic device" },
        { "name": "tablet", "quantity": 6, "type": "electronic device" },
        { "name": "smartphone", "quantity": 1, "type": "electronic device" },
        { "name": "television", "quantity": 2, "type": "electronic device" },
        { "name": "projector", "quantity": 3, "type": "electronic device" },
        { "name": "printer", "quantity": 4, "type": "electronic device" },
        { "name": "scanner", "quantity": 5, "type": "electronic device" },
        { "name": "external hard drive", "quantity": 6, "type": "electronic device" },
        { "name": "router", "quantity": 1, "type": "electronic device" },
        { "name": "modem", "quantity": 2, "type": "electronic device" },
        { "name": "power bank", "quantity": 3, "type": "electronic device" },
        { "name": "extension cord", "quantity": 4, "type": "electrical accessory" },
        { "name": "surge protector", "quantity": 5, "type": "electrical accessory" },
        { "name": "LED strip lights", "quantity": 6, "type": "home accessory" },
        { "name": "desk lamp", "quantity": 1, "type": "home accessory" },
        { "name": "night light", "quantity": 2, "type": "home accessory" },
        { "name": "ceiling fan", "quantity": 3, "type": "home appliance" },
        { "name": "garage door opener", "quantity": 4, "type": "home appliance" },
        { "name": "doorbell camera", "quantity": 5, "type": "electronic device" },
        { "name": "smart mirror", "quantity": 6, "type": "home appliance" }
    ]
  return (
    <div className="App">
      <SearchBar search={search} handleChange={handleChange} />
        <h1>{search}</h1>
        <table className='table'>
            <thead>
            <tr>
                <th>Product</th>
                <th>Quantity</th>
                <th>Type</th>
            </tr>
            </thead>
            <tbody>
            {
                values.filter((values)=>values.name.includes(search)).map((value, index) => (
                    <tr key={index}>
                        <td>{value.name}</td>
                        <td>{value.quantity}</td>
                        <td>{value.type}</td>
                    </tr>
                ))
            }
            </tbody>
        </table>
    </div>
  );
}

export default App;
