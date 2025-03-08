import React, { useState, useEffect } from "react";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";
import html2pdf from "html2pdf.js";

const Scratchpad = () => {
  const [notes, setNotes] = useState("");

  useEffect(() => {
    const storedNotes = localStorage.getItem("scratchpad-notes");
    if (storedNotes) {
      setNotes(storedNotes);
    }
  }, []);

  useEffect(() => {
    localStorage.setItem("scratchpad-notes", notes);
  }, [notes]);

  const handleSave = () => {
    const element = document.getElementById("scratchpad");
    html2pdf().from(element).save();
  };

  return (
    <div id="scratchpad" className="p-4">
      <ReactQuill value={notes} onChange={setNotes} className="bg-white" />
      <button
        onClick={handleSave}
        className="mt-2 px-4 py-2 bg-primary text-white rounded hover:bg-accent transition-colors duration-300"
      >
        Save Notes
      </button>
    </div>
  );
};

export default Scratchpad;
