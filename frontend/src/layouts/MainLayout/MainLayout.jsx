import React from 'react';
import './MainLayout.css';

const MainLayout = ({ children }) => {
  return (
    <div className="main-layout">
      <header className="main-header">
        <h1>Employee Management System</h1>
      </header>
      <main className="main-content">
        {children}
      </main>
    </div>
  );
};

export default MainLayout; 