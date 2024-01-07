import { SetStateAction, useState } from "react";
import TextBox from "./TextBox";

function App() {
  const [playerName, setVal] = useState("");
  const [year, setValTwo] = useState("");
  const [currentPlayerName, changeName] = useState("");
  const [response, setResponse] = useState<[]>([]);

  const inputOne = (event: { target: { value: SetStateAction<string> } }) => {
    setVal(event.target.value);
  };
  const inputTwo = (event: { target: { value: SetStateAction<string> } }) => {
    setValTwo(event.target.value);
  };

  const apiGet = (year: string, prospectName: string) => {
    changeName(prospectName);
    const url =
      "{your_server_url}" + "/" + prospectName + "/" + year;
    fetch(url)
      .then((response) => response.json())
      .then((json) => setResponse(json));
  };

  const click = () => {
    if (year.length > 0 && playerName.length > 0) {
      apiGet(year, playerName);
    }
    setVal("")
    setValTwo("")
  };

  return (
    <div>
      <h1>CFB Prospect Info</h1>

      <input
        type="text"
        name="inputBoxOne"
        onChange={inputOne}
        placeholder="Prospect Full Name"
        value={playerName}
      ></input>
      <br></br>
      <input
        type="text"
        name="inputBoxTwo"
        onChange={inputTwo}
        placeholder="Year"
        value={year}
      ></input>
      <br></br>

      <button className="btn" onClick={click}>
        Go
      </button>
      <h2>Full Name: {currentPlayerName}</h2>
      <TextBox message={response}/>

    </div>
  );
}

export default App;
