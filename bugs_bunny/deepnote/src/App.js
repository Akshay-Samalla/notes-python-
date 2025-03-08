import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Editor from './pages/Editor';
import Sidebar from './components/Sidebar';

const App = () => {
  const files = {
    'csharp': {
      'basics': ['conditional_statements', 'sample_programs'],
      'file_concepts': ['file']
    },
    'python': {
      'python': ['python']
    }
  };

  return (
    <Router>
      <div className="flex">
        <Sidebar files={files} />
        <div className="flex-1 p-4">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/editor/:topic/:filename" element={<Editor />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;