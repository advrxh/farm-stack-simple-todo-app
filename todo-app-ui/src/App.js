import React, { useEffect, useState } from "react";
import { getItems, addItem, updateItem, delItem } from "./fetchData";

import TodoComp from "./todoComp";

import "./App.css";

function App() {
  const [todoList, setList] = useState([]);

  const [InputValue, setInputValue] = useState("");

  useEffect(() => {
    const timer = setTimeout(() => {
      getItems().then((data) => {
        setList(data);
      });
    }, 500);
    return () => clearTimeout(timer);
  }, [todoList]);

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleAdd = () => {
    addItem(InputValue).then(() => {
      setInputValue("");
    });
  };

  return (
    <div className="container">
      <div className="add-bar">
        <input type="text" value={InputValue} onChange={handleInputChange} />
        <button onClick={handleAdd}>Add</button>
      </div>
      <div className="card-container">
        {todoList.map((item, index) => (
          <TodoComp data={item} key={index + 1} />
        ))}
      </div>
    </div>
  );
}

export default App;
