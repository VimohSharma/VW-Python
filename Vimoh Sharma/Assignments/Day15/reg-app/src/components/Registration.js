import React, { useState } from "react";

function Registration({ setUser }) {
  const [form, setForm] = useState({
    name: "",
    email: "",
    phone: "",
    address: ""
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setUser(form);
  };

return (
  <div className="container mt-5">
    <div className="card p-4 shadow">
      <h2 className="text-center mb-4">Registration Form</h2>

      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <input
            type="text"
            name="name"
            placeholder="Enter Name"
            className="form-control"
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <input
            type="email"
            name="email"
            placeholder="Enter Email"
            className="form-control"
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <input
            type="text"
            name="phone"
            placeholder="Enter Phone"
            className="form-control"
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <input
            type="text"
            name="address"
            placeholder="Enter Address"
            className="form-control"
            onChange={handleChange}
          />
        </div>

        <button className="btn btn-primary w-100">Submit</button>
      </form>
    </div>
  </div>
);
}
export default Registration;