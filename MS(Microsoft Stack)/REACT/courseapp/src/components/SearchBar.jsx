import React from 'react';

function SearchBar(props) {
    return (
        <input type="text" value={props.value} onChange={props.handleChange} placeholder='search...'    />
    );
}

export default SearchBar;