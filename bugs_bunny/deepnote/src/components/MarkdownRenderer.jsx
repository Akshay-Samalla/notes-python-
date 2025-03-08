import React from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

const MarkdownRenderer = ({ content }) => {
  return (
    <div className="p-4 prose prose-lg max-w-none">
      <ReactMarkdown remarkPlugins={[remarkGfm]} className="text-text">
        {content}
      </ReactMarkdown>
    </div>
  );
};

export default MarkdownRenderer;
