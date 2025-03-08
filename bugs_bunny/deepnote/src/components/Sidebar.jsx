import React, { useState } from "react";
import { Link } from "react-router-dom";

const Sidebar = ({ files }) => {
  const [openTopics, setOpenTopics] = useState({});

  const handleClick = (topic) => {
    setOpenTopics({
      ...openTopics,
      [topic]: !openTopics[topic],
    });
  };

  return (
    <aside className="w-64 bg-white p-4 border-r border-gray-200">
      <nav>
        <ul>
          {Object.keys(files).map((topic) => (
            <li key={topic} className="mb-2">
              <div
                className="flex items-center cursor-pointer"
                onClick={() => handleClick(topic)}
              >
                <span className="mr-2">{openTopics[topic] ? "-" : "+"}</span>
                <span className="font-semibold">{topic}</span>
              </div>
              {openTopics[topic] && (
                <ul className="ml-4">
                  {files[topic].map((file, idx) => (
                    <li key={idx} className="mb-1">
                      <Link
                        to={`/editor/${topic}/${file}`}
                        className="text-blue-500 hover:text-blue-700"
                      >
                        {file}
                      </Link>
                    </li>
                  ))}
                </ul>
              )}
            </li>
          ))}
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
