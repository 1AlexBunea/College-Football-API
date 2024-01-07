interface Props {
  message: [];
}

const TextBox = ({ message }: Props) => {
  return (
    <div>
      <li>Position: {message[0]}</li>
      <li>Height(in inches): {message[1]}</li>
      <li>Weights(lbs): {message[2]}</li>
      <li>Grade/Year: {message[3]}</li>
      <li>Place of Birth: {message[4]}</li>
      <li>University: {message[5]}</li>
      <li>Conference: {message[6]}</li>
    </div>
  );
};

export default TextBox;
