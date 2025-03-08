import React from "react";

const AIFrame = () => {
  return (
    <div className="p-4">
      <iframe
        title="ChatGPT"
        src="https://chat.openai.com/chat"
        className="w-full h-96 border border-gray-300 rounded"
        sandbox="allow-scripts allow-same-origin"
      ></iframe>
    </div>
  );
};

export default AIFrame;
