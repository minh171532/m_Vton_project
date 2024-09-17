import React, { useEffect } from "react";
import { CartList, ScrollBtn } from "../../Components";
import { useSelector,useDispatch } from "react-redux";
import { fetchCartItems } from "../../Redux/cartSlice";

const Cart = () => {
   const dispatch = useDispatch();
   const user = useSelector((state) => state.user.user);
   const user_id = user._id 
   useEffect(() => {
      dispatch(fetchCartItems(user_id));
   }, [dispatch]);
   return (
      <>
         <CartList />
         <ScrollBtn />
      </>
   );
};

export default Cart;
