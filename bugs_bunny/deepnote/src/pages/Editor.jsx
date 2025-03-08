import React, { useEffect, useState } from "react";
import axios from "axios";
import MarkdownRenderer from "../components/MarkdownRenderer";
import AIFrame from "../components/AIFrame";
import Scratchpad from "../components/Scratchpad";
import CodeEditor from "../components/CodeEditor";

const Editor = ({ match }) => {
  const [content, setContent] = useState("");

  useEffect(() => {
    const fetchMarkdown = async () => {
      try {
        const response = await axios.get(
          `/files/${match.params.topic}/${match.params.filename}.md`
        );
        setContent(response.data);
      } catch (error) {
        setContent("# Error loading file");
      }
    };
    fetchMarkdown();
  }, [match.params.topic, match.params.filename]);

  return (
    <div className="flex">
      <div className="w-3/4">
        <MarkdownRenderer content={content} />
        <AIFrame />
        <Scratchpad />
      </div>
      <div class="w-1/4 p-4">
        <CodeEditor />
      </div>
    </div>
  );
};

export default Editor;
