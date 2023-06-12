import React, { useState } from "react";

function App() {
  const [name, setName] = useState("");
  const [headingText, setHeading] = useState("");
  function handleChange(event) {
  
    setName(event.target.value);
  }

  function handleClick(event) {
    var texttoshow=""
    var number=document.getElementById("numberRepeat").value
    for (let i=0;i<number;i++){
     texttoshow+=" "+name
    }
    setHeading(texttoshow);

    event.preventDefault();
  }

  return (
    <div className="container">
      <h1>{headingText}</h1>
      <form onSubmit={handleClick}>
        <input
          onChange={handleChange}
          type="text"
          placeholder="Text To Repeat"
          value={name}
        />
        <input
          id="numberRepeat"
          type="number"
          placeholder="Number of Repeat"

        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;
