const initialState = {
    items: [], 
  };
  
  function cartReducer(state, action) {
    switch (action.type) {
      case "ADD_ITEM": {
        const { product, quantity } = action.payload;
        const existing = state.items.find((item) => item.id === product.id);
  
        if (!existing) {
          return {
            ...state,
            items: [...state.items, { id: product.id, product, quantity }],
          };
        }
  
        return {
          ...state,
          items: state.items.map((item) =>
            item.id === product.id
              ? { ...item, quantity: item.quantity + quantity }
              : item
          ),
        };
      }
  
      case "REMOVE_ITEM": {
        const id = action.payload;
        return {
          ...state,
          items: state.items.filter((item) => item.id !== id),
        };
      }
  
      case "UPDATE_QTY": {
        const { id, quantity } = action.payload;
        if (quantity <= 0) {
          return {
            ...state,
            items: state.items.filter((item) => item.id !== id),
          };
        }
        return {
          ...state,
          items: state.items.map((item) =>
            item.id === id ? { ...item, quantity } : item
          ),
        };
      }
  
      case "CLEAR":
        return initialState;
  
      default:
        return state;
    }
  }
  
  export { initialState, cartReducer };