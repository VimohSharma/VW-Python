import React from "react";

function Form({ user, logout }) {
  if (!user) {
    return <h2>No Data Found</h2>;
  }

return (
  <div className="container mt-5">

    <div className="d-flex justify-content-between align-items-center mb-4">
      <h3>Welcome {user.name}</h3>
      <button className="btn btn-danger" onClick={logout}>Logout</button>
    </div>

    <div className="card p-4 shadow">
      <h4>User Details</h4>

      <p><b>Name:</b> {user.name}</p>
      <p><b>Email:</b> {user.email}</p>
      <p><b>Phone:</b> {user.phone}</p>
      <p><b>Address:</b> {user.address}</p>
    </div>

  </div>
);
}

export default Form;