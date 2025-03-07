
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { addToCart, removeFromCart } from './cartActions';

const Cart = () => {
    const cart = useSelector(state => state.cart);
    const dispatch = useDispatch();

    const addItem = () => {
        const newItem = { id: Date.now(), name: 'Product ' + (cart.length + 1) };
        dispatch(addToCart(newItem));
    };

    const removeItem = (id) => {
        dispatch(removeFromCart(id));
    };

    return (
        <div>
            <h2>Shopping Cart</h2>
            <button onClick={addItem}>Add Item</button>
            <ul>
                {cart.map(item => (
                    <li key={item.id}>
                        {item.name} <button onClick={() => removeItem(item.id)}>Remove</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Cart;