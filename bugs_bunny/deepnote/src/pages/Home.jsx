import React from "react";

const Home = () => {
  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-4xl font-serif text-primary">
        Welcome to the Markdown Viewer
      </h1>
      <p className="text-lg text-muted">
        Select a file from the sidebar to get started.
      </p>
    </div>
  );
};

export default Home;
