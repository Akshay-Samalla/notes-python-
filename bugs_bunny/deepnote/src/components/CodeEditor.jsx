import React, { useRef, useState, useEffect } from "react";
import MonacoEditor from "@monaco-editor/react";
import Pyodide from "pyodide";

const CodeEditor = () => {
  const editorRef = useRef(null);
  const [language, setLanguage] = useState("python");
  const [pyodide, setPyodide] = useState(null);
  const [loading, setLoading] = useState(true);
  const [executionResult, setExecutionResult] = useState("");

  useEffect(() => {
    if (language === "python") {
      (async () => {
        setPyodide(
          await loadPyodide({
            indexURL: "https://cdn.jsdelivr.net/pyodide/v0.21.3/full/",
          })
        );
        setLoading(false);
      })();
    }
  }, [language]);

  const executeCode = async () => {
    if (editorRef.current) {
      const code = editorRef.current.getValue();
      if (language === "python" && pyodide) {
        try {
          const result = await pyodide.runPythonAsync(code);
          setExecutionResult(`Result: ${result}`);
        } catch (error) {
          setExecutionResult(`Error: ${error}`);
        }
      } else if (language === "csharp") {
        setExecutionResult("C# execution is not implemented yet.");
      }
    }
  };

  return (
    <div className="p-4">
      <div className="mb-2">
        <label htmlFor="language" className="mr-2 font-semibold">
          Language:
        </label>
        <select
          id="language"
          value={language}
          onChange={(e) => setLanguage(e.target.value)}
          className="border border-gray-300 rounded px-2 py-1"
        >
          <option value="python">Python</option>
          <option value="csharp">C#</option>
        </select>
      </div>
      <MonacoEditor
        ref={editorRef}
        theme="vs-dark"
        height="400px"
        language={language}
        className="border border-gray-300 rounded"
      />
      <button
        onClick={executeCode}
        className="mt-2 px-4 py-2 bg-primary text-white rounded hover:bg-accent transition-colors duration-300"
      >
        Execute Code
      </button>
      {executionResult && (
        <div className="mt-4 p-2 bg-gray-100 border border-gray-300 rounded">
          {executionResult}
        </div>
      )}
    </div>
  );
};

export default CodeEditor;
