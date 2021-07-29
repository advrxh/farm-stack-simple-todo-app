import axios from "axios";

export const getItems = async () => {
  const data = await axios
    .get("http://localhost:8000/item")
    .then((res) => res.data);

  return data;
};

export const addItem = async (desc) => {
  const data = await axios
    .put(`http://localhost:8000/item?desc=${desc}`)
    .then((res) => res.data);

  return data;
};

export const updateItem = async (_id, statusKey, desc) => {
  const data = await axios
    .post(
      `http://localhost:8000/item?_id=${_id}&status=${statusKey}&desc=${desc}`
    )
    .then((res) => res.data);

  return data;
};

export const delItem = async (_id) => {
  const data = await axios
    .delete(`http://localhost:8000/item?_id=${_id}`)
    .then((res) => res.data);

  return data;
};
