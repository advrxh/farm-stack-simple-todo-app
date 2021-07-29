import React, { Component } from "react";
import { getItems, addItem, updateItem, delItem } from "./fetchData";

import { AiTwotoneEdit, AiFillDelete } from "react-icons/ai";

import "./App.css";

export class TodoComp extends Component {
  constructor(props) {
    super(props);

    this.state = {
      status: this.props.data.status,
    };
    this.handleStatusChange = this.handleStatusChange.bind(this);
    this.handleDelete = this.handleDelete.bind(this);
  }

  handleDelete = () => {
    delItem(this.props.data._id).then(() => {});
  };

  handleStatusChange = (e) => {
    this.setState({ status: e.target.value }, () => {
      updateItem(
        this.props.data._id,
        this.state.status,
        this.props.data.description
      ).then((res) => {
        console.log(res);
      });
    });
  };

  componentDidMount() {
    console.log(this.props.data);
  }

  render() {
    return (
      <div className="card">
        <div className="card-head">
          <h3 className="desc">{this.props.data.description}</h3>

          <div className="btn-grp">
            <div className="btn-del" onClick={this.handleDelete}>
              <AiFillDelete size="36" />
            </div>
          </div>
        </div>
        <select
          className="menu"
          value={this.state.status}
          onChange={this.handleStatusChange}
        >
          <option value="pending">Pending</option>
          <option value="doing">Doing</option>
          <option value="done">Done</option>
        </select>
      </div>
    );
  }
}

export default TodoComp;
