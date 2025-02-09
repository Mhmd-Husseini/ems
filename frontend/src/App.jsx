import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import SingleEmployeeView from './pages/SingleEmployeeView';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Navigate to="/employees/new" replace />} />
        <Route path="/employees/new" element={<SingleEmployeeView />} />
        <Route path="/employees/:id" element={<SingleEmployeeView />} />
      </Routes>
    </div>
  );
}

export default App; 